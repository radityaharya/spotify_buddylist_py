
# spotify_buddylist_py

A python implementation of [spotify-buddylist](https://github.com/valeriangalliat/spotify-buddylist).

For instructions on how to get the required cookie, please read the original repository's README.

## Installation

```bash
  git clone https://github.com/radityaharya/spotify_buddylist_py
```

## Usage

```python
  from spotify_buddylist_py import BuddylistClient
  
  buddy_list = BuddylistClient("SP_DC_COOKIE")
  friend_activity = buddy_list.get_friend_activity()
  print(friend_activity)
```
