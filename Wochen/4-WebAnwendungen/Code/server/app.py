import json
from server.model import Post, Benutzer, Kommentar
import server.datenbank as datenbank
from flask import Flask, jsonify, request, abort
import re

app = Flask(__name__)


'''
Die Datenbank speichert unsere Listen als Komma-seperarierte Tags
'''
def tags_zu_list(tags):
    if tags != '':
        return tags.split(',')
    else:
        return []

'''
Wandle den Post in ein Dict, dass JSON entspricht
'''
def post_zu_json(post):
     d = post.daten()
     d['nennungen'] = tags_zu_list(d['nennungen'])
     d['kommentare'] = tags_zu_list(d['kommentare'])
     return d


#-- Fehlerausgaben

@app.errorhandler(404)
def nicht_gefunden(error):
    return {'error': 'Existiert nicht'}, 404

@app.errorhandler(405)
def nicht_erlaubt(error):
    return {'error': 'Die Operation ist nicht erlaubt.'}, 405

@app.errorhandler(500)
def interner_fehler(error):
    return {'error': 'Interner Fehler - {}'.format(error)}, 500

#-- Posts
'''
Posts aller Nutzer abrufen
'''
@app.route('/posts', methods=['GET'])
def posts():
    posts = Post(Benutzer('_jeder_'),-1).abfragen()
    antwort = []
    for post in posts:
        antwort.append(post_zu_json(post))
    return antwort

'''
Posts eines Nutzers abrufen
'''
@app.route('/benutzer/<kurzname>/posts', methods=['GET'])
def benutzer_posts(kurzname):
    posts = Post(Benutzer(kurzname),-1).abfragen()
    antwort = []
    for post in posts:
        antwort.append(post_zu_json(post))
    return antwort

'''
Post erstellen
'''
@app.route('/post', methods=['POST'])
def post_post():
    d = request.json
    text = d['text']
    benutzer = Benutzer(d['benutzer'])
    post = Post(benutzer, d['zeit'], d['text'])

    # Wenn der Post schon existiert, dann wollen wir ihn nicht anlegen
    if post.existiert_schon():
        abort(405)
    # Nur existierende Benutzer dürfen posten
    elif not benutzer.existiert_schon():
        abort(500)
    else:
        if '@' in text:
            nennungen = []
            # Konvertiere alle Wörter im Text die mit '@' beginnen zu einer Liste von Nennungen
            alle_worter = text.split()
            for wort in alle_worter:
                if wort.startswith('@'):
                    zeichen = [' ', '!', '?', '.', ':', ',']
                    genannter_nutzer = wort.split('@')[1]
                    for z in zeichen:
                        genannter_nutzer = genannter_nutzer.strip(z)
                    nennungen.append(genannter_nutzer)
            post.nennungen = nennungen
        post.speichern()
        return post.daten()

#-- Kommentare
'''
Kommentar erstellen
'''
@app.route('/kommentar', methods=['POST'])
def kommentar_post():
    #def __init__(self, benutzer, zeit, post, text=""):
    d = request.json
    benutzer = Benutzer(d['benutzer'])
    zeit = int(d['zeit'])
    text = d['text']
    post_id_als_liste = d['post'].split(':')
    post_benutzer=Benutzer(post_id_als_liste[0])
    post_zeit=int(post_id_als_liste[1])
    post = Post(post_benutzer,post_zeit)

    # Kommentare dürfen nur von existierenden Benutzern an existierende Posts gehangen werden
    if  not (post.existiert_schon() and benutzer.existiert_schon()):
        abort(500)
    else:
        post.abrufen()
        benutzer.abrufen()
        kommentar = Kommentar(benutzer,zeit,post,text)
        kommentar.speichern()
        post.kommentare.append(kommentar)
        post.speichern()
        return kommentar.daten()

'''
Kommentare eines Posts abrufen
'''
@app.route('/post/<post_id>/kommentare')
def post_kommentare():
    print("TODO")

#-- Benutzer
'''
Alle Benutzer abrufen
'''
@app.route('/benutzer', methods=['GET'])
def benutzer_alle():
    benutzer = Benutzer('_jeder_').abfragen()
    antwort = []
    for b in benutzer:
        antwort.append(b)

    return antwort

'''
Details eines Nutzers abrufen
'''
@app.route('/benutzer/<kurzname>', methods=['GET'])
def benutzer_get(kurzname):
    try:
        nutzer = Benutzer(kurzname).abrufen()
        return nutzer.daten()
    except Exception:
        abort(404)

'''
Nutzer erstellen oder aktualisieren
'''
@app.route('/benutzer/<kurzname>', methods=['PUT'])
def benutzer_put(kurzname):
    d = request.json
    print(str(d))
    nutzer = Benutzer(kurzname, d['vorname'], d['nachname'], d['email'])
    nutzer.speichern()
    return nutzer.daten()
