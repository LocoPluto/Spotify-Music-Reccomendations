import webbrowser
import json

with open('credentials.json', 'r+') as file:
    data = json.load(file)
    id = data['client_id']
    secret = data['client_secret']
#FIXME opens 2 identical pages
webbrowser.open('http://127.0.0.1:5000/')