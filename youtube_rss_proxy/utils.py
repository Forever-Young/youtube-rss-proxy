from urllib.parse import urlencode
import requests

from django.conf import settings


class InvalidToken(Exception):
    pass


class OAuth(requests.auth.AuthBase):
    def __init__(self, access_token):
        self.access_token  = access_token

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer {}".format(self.access_token)
        return r


def get_auth_url(state):
    return "https://accounts.google.com/o/oauth2/auth?{}".format(urlencode({
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "scope": "https://www.googleapis.com/auth/youtube",
        "response_type": "code",
        "access_type": "offline",
        "approval_prompt": "force",
        "state": state,
    }))


def get_tokens(code):
    r = requests.post("https://accounts.google.com/o/oauth2/token", {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }).json()
    return r["access_token"], r.get("refresh_token", "")


def refresh_token(refr_token):
    r = requests.post("https://accounts.google.com/o/oauth2/token", {
        "refresh_token": refr_token,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "grant_type": "refresh_token",
    }).json()
    try:
        return r["access_token"]
    except KeyError:
        raise InvalidToken


def get_username(access_token):
    r = requests.get("https://gdata.youtube.com/feeds/api/users/default?alt=json", auth=OAuth(access_token))
    if r.status_code == 401:
        return None
    return r.json()["entry"]["yt$username"]["$t"]


def get_rss(access_token):
    r = requests.get("https://gdata.youtube.com/feeds/api/users/default/newsubscriptionvideos", auth=OAuth(access_token))
    if r.status_code == 401:
        raise InvalidToken
    return r.text, r.headers["Content-Type"]
