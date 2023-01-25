# Include Python modules from the parent folder
import sys
import time
import pytest
sys.path.append('..')
from datetime import datetime

# Imports
import server.datenbank as datenbank
from server.model import Benutzer, Post, Kommentar, Statistik

# Eine Sekunde schlafen und dann die aktuelle Zeit geben
def aktuelle_zeit():
    time.sleep(1)
    return int(datetime.now().timestamp())

# Einige Tests benötigen einen Benutzer
def benutzer_erstellen():
    benutzer = Benutzer('nosqlgeek', 'David', 'Maier', 'david@nosqlgeeks.de')
    benutzer.speichern()
    return benutzer

@pytest.fixture(autouse=True, scope='function')
def setup():
    #Am Anfang
    print('Einrichten des Tests ...')
    datenbank.loeschen()
    datenbank.indizes_erstellen()
    yield
    #Am Ende

def test_benutzer():
    nutzer_zu_db = Benutzer('nosqlgeek', 'David', 'Maier', 'david@nosqlgeeks.de')
    nutzer_zu_db.speichern()
    nutzer_von_db = Benutzer('nosqlgeek').abrufen()
    assert str(nutzer_von_db.daten()) == "{'typ': 'nutzer', 'id': 'nosqlgeek', 'kurzname': 'nosqlgeek', 'vorname': 'David', 'nachname': 'Maier', 'email': 'david@nosqlgeeks.de'}"

def test_post():
    benutzer = benutzer_erstellen()
    zeit = aktuelle_zeit()
    post_zu_db = Post(benutzer, zeit, 'Hello @julia!', nennugen=['julia'])
    post_zu_db.speichern()
    post_von_db = Post(benutzer, zeit).abrufen()
    
    assert post_von_db.zeit == zeit
    assert post_von_db.benutzer.kurzname == benutzer.kurzname
    assert post_von_db.text == 'Hello @julia!'
    assert 'julia' in post_von_db.nennungen

def test_post_statistik():
    benutzer = benutzer_erstellen()
    zeit = aktuelle_zeit()
    post_zu_db = Post(benutzer, zeit, 'Hello @alex!', nennugen=['alex'])
    post_zu_db.statistik.besuche('nosqlgeek')
    post_zu_db.statistik.besuche('julia')
    post_zu_db.statistik.besuche('julia')
    post_zu_db.speichern()
    post_von_db = Post(benutzer, zeit).abrufen()

    assert post_von_db.statistik.anzahl_besuche == 3
    assert post_von_db.statistik.anzahl_besucher == 2

def test_post_abfrage():
    benutzer = benutzer_erstellen()
    post = Post(benutzer, aktuelle_zeit(), 'Hi everyone!')
    post.speichern()
    assert 0 != len(post.abfragen())

def test_post_kommentare():
    benutzer = benutzer_erstellen()
    zeit1 = aktuelle_zeit()
    zeit2 = aktuelle_zeit()
    post_zu_db = Post(benutzer, zeit1, 'Hallo Welt!')
    kommentar = Kommentar(benutzer, zeit2, post_zu_db, 'Netter post!')
    post_zu_db.kommentare.append(kommentar)
    post_zu_db.speichern()
    post_von_db = Post(benutzer, zeit1).abrufen()
    
    assert len(post_von_db.kommentare) == 1
    kommentar_von_db = post_von_db.kommentare[0] 
    
    assert kommentar_von_db.text == 'Netter post!'
    assert kommentar_von_db.benutzer.id == benutzer.id

    abgefragter_post_kommentar = post_von_db.abfragen()[0].kommentare[0]
    assert abgefragter_post_kommentar.benutzer.id == benutzer.id