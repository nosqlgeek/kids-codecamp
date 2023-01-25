import sys
sys.path.append('..')

import pytest
import requests
from datetime import datetime
import server.datenbank as datenbank


@pytest.fixture(autouse=True, scope='module')
def setup():
    #Am Anfang
    print('Einrichten der Testsuite ...')
    datenbank.loeschen()
    datenbank.indizes_erstellen()
    yield
    #Am Ende

def test_benutzer_erstellen():
    print('Erstelle Nutzer ...')
    daten = {'email': 'alexg@nosqlgeeks.de', 'nachname': 'G.', 'vorname': 'Alex'}
    antwort = requests.put('http://localhost:5000/benutzer/alexg', json=daten)
    print(antwort.content)
    assert antwort.status_code == 200

def test_benutzer_abrufen():
    print('Rufe Nutzer ab ...')
    antwort = requests.get('http://localhost:5000/benutzer/alexg')
    print(antwort.content)
    assert antwort.status_code == 200

def test_post_erstellen():
    print('Erstelle Post ...')
    daten = {'benutzer': 'alexg', 'zeit': int(datetime.now().timestamp()), 'text' : 'Hallo @nosqlgeek!'}
    antwort = requests.post('http://localhost:5000/post', json=daten)
    print(antwort.content)
    assert antwort.status_code == 200

def test_posts_abrufen():
    print('Rufe alle Posts ab ...')
    antwort = requests.get('http://localhost:5000/posts')
    print(antwort.content)
    assert antwort.status_code == 200

def test_kommentar_erstellen():
    print("Hänge Kommentar an Post an ...")
    nutzer_daten = { 'nosqlgeek': {'email': 'david@nosqlgeeks.de', 'nachname': 'Maier', 'vorname': 'David'},
                     'alexg': {'email': 'alexg@nosqlgeeks.de', 'nachname': 'G.', 'vorname': 'Alex'}}
    
    for n in nutzer_daten:
        requests.put('http://localhost:5000/benutzer/{}'.format(n), json=nutzer_daten[n])
    
    post_zeit = int(datetime.now().timestamp())
    post_daten = {'benutzer': 'alexg', 'zeit': post_zeit, 'text' : 'Hallo @nosqlgeek!'}
    requests.post('http://localhost:5000/post', json=post_daten)

    #def __init__(self, benutzer, zeit, post, text=""):
    kommentar_daten = {'benutzer': 'nosqlgeek', 'zeit': int(datetime.now().timestamp()), 'text' : 'Hi @alexg, wie geht es Dir?', 'post': 'alexg:{}'.format(post_zeit)}
    antwort = requests.post('http://localhost:5000/kommentar', json=kommentar_daten)
    print(antwort.content)
    assert antwort.status_code == 200
