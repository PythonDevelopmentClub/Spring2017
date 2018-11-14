#  Client Keys
CLIENT_ID = "96sdfsdfsdfsdb570sdfsc0c8ae57004e"
CLIENT_SECRET = "19acbsdfsdf72bsdfsd2a7dfff7"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)


# Server-side Parameters

#OLD CALLBACK   http://127.0.0.1:8000/app/#
# http://127.0.0.1:5001
CLIENT_SIDE_URL = "http://127.0.0.1:5001"
PORT = 5001
# REDIRECT_URI = "{}:{}/callback".format(CLIENT_SIDE_URL, PORT)
REDIRECT_URI = "{}/callback".format(CLIENT_SIDE_URL)

SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}
