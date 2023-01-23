from datetime import datetime
import time

# Imports
import server.dao as dao
from server.model import Benutzer, Post, Kommentar, Statistik


# Sleep one second and return the time
def aktuelle_zeit():
    time.sleep(1)
    return int(datetime.now().timestamp())
    
def test_benutzer():
    nutzer_zu_db = Benutzer('@nosqlgeek', 'David', 'Maier', 'david@nosqlgeeks.de')
    nutzer_zu_db.speichern()
    nutzer_von_db = Benutzer('@nosqlgeek').abrufen()
    assert str(nutzer_von_db.daten()) == "{'typ': 'nutzer', 'id': '@nosqlgeek', 'kurzname': '@nosqlgeek', 'vorname': 'David', 'nachname': 'Maier', 'email': 'david@nosqlgeeks.de'}"
    return nutzer_von_db

def test_post():
    benutzer = test_benutzer()
    zeit = aktuelle_zeit()
    post_zu_db = Post(benutzer, zeit, 'Hello @julia!', nennugen=['@julia'])
    post_zu_db.speichern()
    post_von_db = Post(benutzer, zeit).abrufen()
    
    assert post_von_db.zeit == zeit
    assert post_von_db.benutzer.kurzname == benutzer.kurzname
    assert post_von_db.text == 'Hello @julia!'
    assert '@julia' in post_von_db.nennungen

def test_post_statistik():
    
    benutzer = test_benutzer()
    zeit = aktuelle_zeit()
    post_zu_db = Post(benutzer, zeit, 'Hello @alex!', nennugen=['@alex'])
    post_zu_db.statistik.besuche('@nosqlgeek')
    post_zu_db.statistik.besuche('@julia')
    post_zu_db.statistik.besuche('@julia')
    post_zu_db.speichern()
    post_von_db = Post(benutzer, zeit).abrufen()

    assert post_von_db.statistik.anzahl_besuche == 3
    assert post_von_db.statistik.anzahl_besucher == 2


def test_post_kommentare():
    benutzer = test_benutzer()
    zeit1 = aktuelle_zeit()
    zeit2 = aktuelle_zeit()
    post_zu_db = Post(benutzer, zeit1, 'Hallo Welt!')
    kommentar = Kommentar(benutzer, zeit2, 'Netter post!', post_zu_db)
    post_zu_db.kommentare.append(kommentar)
    post_zu_db.speichern()

if __name__ == '__main__':
    test_post()