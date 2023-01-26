import sys
sys.path.append('..')

import pytest
import requests
import time
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
    antwort = requests.put('http://localhost:5000/api/benutzer/alexg', json=daten)
    print(antwort.content)
    assert antwort.status_code == 200

def test_benutzer_abrufen():
    print('Rufe Nutzer ab ...')
    antwort = requests.get('http://localhost:5000/api/benutzer/alexg')
    print(antwort.content)
    assert antwort.status_code == 200

def erstelle_post(benutzer, text, zeit=int(datetime.now().timestamp())):
    daten = {'benutzer': benutzer, 'zeit':zeit, 'text': text}
    antwort = requests.post('http://localhost:5000/api/post', json=daten)
    return antwort

def test_post_erstellen():
    print('Erstelle Post ...')
    antwort = erstelle_post('alexg', 'Hallo @nosqlgeek!')
    print(antwort.content)
    assert antwort.status_code == 200

def test_posts_abrufen():
    print('Rufe alle Posts ab ...')
    antwort = requests.get('http://localhost:5000/api/posts')
    print(antwort.content)
    assert antwort.status_code == 200

def test_kommentar_erstellen():
    print("Hänge Kommentar an Post an ...")
    nutzer_daten = { 'nosqlgeek': {'email': 'david@nosqlgeeks.de', 'nachname': 'Maier', 'vorname': 'David'},
                     'juliaf': {'email': 'julia@nosqlgeeks.de', 'nachname': 'F.', 'vorname': 'Julia'}}
    
    for n in nutzer_daten:
        requests.put('http://localhost:5000/api/benutzer/{}'.format(n), json=nutzer_daten[n])
    
    #TODO: Warum ist hier der text leer?
    zeit = int(datetime.now().timestamp())
    antwort = erstelle_post('juliaf', 'Hallo nochmal!', zeit)
    print(antwort.content)

    kommentar_daten = {'benutzer': 'nosqlgeek', 'zeit': int(datetime.now().timestamp()), 'text' : 'Hi @juliaf, wie geht es Dir?', 'post': 'juliaf:{}'.format(zeit)}
    antwort = requests.post('http://localhost:5000/api/kommentar', json=kommentar_daten)
    print(antwort.content)
    assert antwort.status_code == 200

    kommentare_antwort = requests.get('http://localhost:5000/api/post/{}/kommentare'.format(kommentar_daten['post']))
    print(kommentare_antwort.content)
    assert kommentare_antwort.status_code == 200

