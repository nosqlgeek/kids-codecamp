import sys
import requests

def test_benutzer_erstellen():
    daten = {'email': 'alexg@nosqlgeeks.de', 'nachname': 'G.', 'vorname': 'Alex'}
    antwort = requests.put('http://localhost:5000/benutzer/alexg', json=daten)
    print(antwort.content)
    assert antwort.status_code == 200


def test_benutzer_abrufen():
    antwort = requests.get('http://localhost:5000/benutzer/nosqlgeek')
    print(antwort.content)
    assert antwort.status_code == 200