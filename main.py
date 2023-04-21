from spotipy.oauth2 import SpotifyOAuth
from settings import Settings

import spotipy
import typing
import vk_api
import time

vk = vk_api.VkApi(token = Settings.VK_TOKEN).get_api()
spotify = spotipy.Spotify(
    language = Settings.LANGUAGE,
    auth_manager = SpotifyOAuth(
        scope = Settings.SCOPE,
        client_id = Settings.CLIENT_ID,
        client_secret = Settings.CLIENT_SECRET,
        redirect_uri = Settings.REDIRECT_URI,
        username = Settings.USERNAME,
    ),
)

current_playing = typing.List[typing.Union[str, str, str]]

def update_status_to_standard():

    if vk.users.get(fields="status")[0]["status"] != Settings.MAIN_STATUS:
        vk.status.set(text=Settings.MAIN_STATUS)
    print("Тишина")

def update_status(_current_playing: typing.List[typing.Union[str, str, str]]) -> typing.List[typing.Union[str, str, str]]:
    
    current = spotify.current_user_playing_track()
    track, album, artist = current["item"]["name"], \
                           current["item"]["album"]["name"], \
                           current["item"]["artists"][0]["name"]
    if _current_playing != [track, album, artist]:
        search_result = vk.audio.search(q=f"{artist} {track}")
        if search_result["count"] == 0:
            vk.status.set(text=Settings.STATUS.format(track=track, album=album, artist=artist))
        else:
            vk.audio.setBroadcast(audio=f"{search_result['items'][0]['owner_id']}_{search_result['items'][0]['id']}")
        print("Играет:", track, "-", artist)
    
    if _current_playing is None:
        raise
    return [track, album, artist]

while True:
    try:
        current_playing = update_status(current_playing)
    except (KeyboardInterrupt, SystemExit, Exception):
        update_status_to_standard()
        time.sleep(30)
        pass
