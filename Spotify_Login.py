from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

app = Flask(__name__)

app.secret_key = ''
TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    try:
        with open('credentials.json', 'r+') as file:
            data = json.load(file)
            data['refresh_token'] = token_info['refresh_token']
            file.seek(0)
            json.dump(data, file, indent=1)
        return 'Success! You may exit this webpage'
    except Exception:
        return 'Error: failure obtaining refresh token or credential file missing or corrupt'

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = Login_actions.id,
        client_secret = Login_actions.secret,
        redirect_uri=url_for('redirectPage', _external=True),
        scope='user-read-private,playlist-modify-public')

import Login_actions
app.run()
