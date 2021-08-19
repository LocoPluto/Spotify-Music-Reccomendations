import base64
import requests
import json

class get_access_token():
    access_token = None
    client_id = None
    client_secret = None
    refresh_token = None
    user_id = None
    url = 'https://accounts.spotify.com/api/token'

    def __init__(self):
        with open('credentials.json', 'r') as f:
            creds = json.load(f)
            self.client_id = creds['client_id']
            self.client_secret = creds['client_secret']
            self.refresh_token = creds['refresh_token']
            self.user_id = creds['user_id']
            self.get_access_token()
    
    def b64_encode(self, id, secret):
        b64encoded = base64.b64encode(f'{id}:{secret}'.encode()).decode()
        return b64encoded
    
    def body_parameter(self):
        body_parameter = {'grant_type': 'refresh_token', 'refresh_token': self.refresh_token}
        return body_parameter

    def header(self):
        header = {'Authorization': f'Basic {self.b64_encode(self.client_id, self.client_secret)}'}
        return header

    def get_access_token(self):
        try:
            r = requests.post(self.url, headers=self.header(), data=self.body_parameter())
            self.access_token = r.json()['access_token']
        except Exception:   
            pass

class search_song():
    url = 'https://api.spotify.com/v1/search'
    song_names = []
    artist_names = []
    song_ids = []

    def __init__(self, song):
        self.song = song
        self.song_names.clear()
        self.artist_names.clear()
        self.song_ids.clear()
        r = requests.get(self.url, headers=self.header(), params=self.parameters())
        raw_search = r.json()
        for num in range(5):
            self.song_names.append(raw_search['tracks']['items'][num]['name'])
        for num in range(5):
            self.artist_names.append(raw_search['tracks']['items'][num]['artists'][0]['name'])
        for num in range(5):
            self.song_ids.append(raw_search['tracks']['items'][num]['id'])

    def header(self):
        header = {'Authorization': f'Bearer {client.access_token}'}
        return header
    
    def parameters(self):
        parameters = {'q': self.song, 'type': 'track', 'limit': 5}
        return parameters

class search_artist():
    url = 'https://api.spotify.com/v1/search'
    artist_names = []
    artist_ids = []

    def __init__(self, artist):
        self.artist = artist
        self.artist_names.clear()
        self.artist_ids.clear()
        r = requests.get(self.url, headers=self.header(), params=self.parameters())
        raw_search = r.json()
        for num in range(5):
            try:
                self.artist_names.append(raw_search['artists']['items'][num]['name'])
            except Exception:
                pass
        for num in range(5):
            try:
                self.artist_ids.append(raw_search['artists']['items'][num]['id'])
            except Exception:
                pass

    def header(self):
        header = {'Authorization': f'Bearer {client.access_token}'}
        return header
    
    def parameters(self):
        parameters = {'q': self.artist, 'type': 'artist', 'limit': 5}
        return parameters

class search_genres():
    url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
    genre_names = []

    def __init__(self):
        self.genre_names.clear()
        r = requests.get(self.url, headers=self.header())
        raw_search = r.json()
        self.genre_names = raw_search['genres']

    def header(self):
        header = {'Authorization': f'Bearer {client.access_token}'}
        return header

class tag_list():
    songs = {}
    artists = {}
    genres = []

    def add_song(self, id, name):
        if len(self.songs) + len(self.artists) + len(self.genres) == 5:
            return 'already at max amount of 5 items'
        elif id in self.songs:
            return 'this song is already in the list'
        else:
            self.songs[id] = name
            return 'song added successfully'

    def add_artist(self, id, name):
        if len(self.songs) + len(self.artists) + len(self.genres) == 5:
            return 'already at max amount of 5 items'
        elif id in self.artists:
            return 'this artist is already in the list'
        else:
            self.artists[id] = name
            return 'artist added successfully'

    def add_genre(self, genre):
        if len(self.songs) + len(self.artists) + len(self.genres) == 5:
            return 'already at max amount of 5 items'
        elif genre in self.genres:
            return 'this genre is already in the list'
        else:
            self.genres.append(genre)
            return 'genre added successfully'
    
    def get_song_names(self):
        list = []
        for item in self.songs.values():
            list.append(item)
        return list

    def get_artist_names(self):
        list = []
        for item in self.artists.values():
            list.append(item)
        return list

    def get_song_uris(self):
        list = []
        for item in self.songs.keys():
            list.append(item)
        return list

    def get_artist_uris(self):
        list = []
        for item in self.artists.keys():
            list.append(item)
        return list
    
class get_reccommendations():
    url = 'https://api.spotify.com/v1/recommendations'
    rec_list = None

    def __init__(self, length, tracks, artists, genres, attributes):
        self.length = length
        self.tracks = list(tracks.keys())
        self.artists = list(artists.keys())
        self.genres = genres
        self.attributes = attributes
        self.get_rec_list()

    def header(self):
        header = {'Authorization': f'Bearer {client.access_token}'}
        return header

    def query_params(self):
        dict = {'limit': self.length, 'seed_artists': self.artists, 'seed_genres': self.genres, 'seed_tracks': self.tracks}
        dict.update(self.attributes)
        return dict

    def get_rec_list(self):
        r = requests.get(self.url, headers=self.header(), params=self.query_params())
        self.rec_list = r.json()

    def get_rec_names(self):
        list = []
        raw_search = self.rec_list
        for num in range(self.length):
            list.append(raw_search['tracks'][num]['name'])
        return list
    
    def get_rec_uris(self):
        list = []
        raw_search = self.rec_list
        for num in range(self.length):
            list.append(raw_search['tracks'][num]['uri'])
        return list

class add_to_playlist():
    create_url = None
    add_url = None

    def __init__(self, uri_list, name):
        self.uri_list = uri_list
        self.name = name
        self.create_url = f'https://api.spotify.com/v1/users/{client.user_id}/playlists'
        self.create_playlist()

    def header(self):
        header = {'Authorization': f'Bearer {client.access_token}'}
        return header

    def params(self):
        param_dict = {'name': self.name, 'description': 'Playlist generated using Spotify\'s algorithm'}
        return param_dict

    def create_playlist(self):
        r = requests.post(self.create_url, headers=self.header(), json=self.params())
        raw = r.json()
        id = raw['id']
        self.add_url = f'https://api.spotify.com/v1/playlists/{id}/tracks'
        self.add_to_playlist()

#FIXME I believe not all songs are being added to playlist because some uris are invalid for adding
    def add_to_playlist(self):
        r = requests.post(self.add_url, headers=self.header(), json={'uris': self.uri_list})

#generate the access token at the beginning of the session
client = get_access_token()
