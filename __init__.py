import datetime
import time

import requests


class BuddylistClient:
    def __init__(self, sp_dc_cookie: str):
        self.sp_dc_cookie = sp_dc_cookie
        self.get_web_access_token_endpoint = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"
        self.get_buddylist_endpoint = (
            "https://guc-spclient.spotify.com/presence-view/v1/buddylist"
        )

    def _get_web_access_token(self)->str:
        headers = {"Cookie": "sp_dc=" + self.sp_dc_cookie}
        response = requests.get(self.get_web_access_token_endpoint, headers=headers)
        return response.json()["accessToken"]

    def get_friend_activity(self) -> dict:
        headers = {
            "Authorization": "Bearer " + self._get_web_access_token(),
        }
        response = requests.get(self.get_buddylist_endpoint, headers=headers)
        return response.json()

    def stream_friend_activity(self)-> None:
        """
        A print stream of new friend activity.
        """
        friend_activity = self.get_friend_activity()
        last_entry = None
        while True:
            friend_activity = self.get_friend_activity()
            if last_entry is None:
                last_entry = friend_activity
            else:
                for entry in friend_activity["friends"]:
                    if entry not in last_entry["friends"]:
                        timestamp_to_datetime = datetime.datetime.fromtimestamp(
                            entry["timestamp"] / 1000
                        )
                        print(
                            f"{entry['user']['name']} is now playing {entry['track']['name']} by {entry['track']['artist']['name']} at {timestamp_to_datetime.strftime('%Y-%m-%d %H:%M:%S')}"
                        )
                last_entry = friend_activity
            time.sleep(60)
