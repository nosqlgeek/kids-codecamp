import json
from server.model import Post, Benutzer
import server.datenbank as datenbank
from flask import Flask, jsonify, request, abort

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
def page_not_found(error):
    return {}, 404

@app.errorhandler(500)
def server_error(error):
    return {'error':str(error)}, 500

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


#-- Benutzer
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
Nurtwe erstellen oder aktualisieren
'''
@app.route('/benutzer/<kurzname>', methods=['PUT'])
def benutzer_put(kurzname):
    d = request.json
    print(str(d))
    nutzer = Benutzer(kurzname, d['vorname'], d['nachname'], d['email'])
    nutzer.speichern()
    return nutzer.daten()
