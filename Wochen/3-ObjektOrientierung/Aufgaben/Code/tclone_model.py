# Imports
from datetime import datetime

# Globale Variablen
posts = []

"""
Das TClone Modell hat:

* Benutzer
* Posts
* Kommentare
* Besucherstatistiken
"""

'''
Ein Benutzer hat einen Kurnamem, einen Vornamen und eine
E-Mail-Address
'''
class Benutzer:
    def __init__(self, kurzname, vorname, nachname, email):
        self.kurzname = kurzname
        self.vorname = vorname
        #-  6.a.) Vervollständige:  
        #- < Code hier >

'''
Kommentare und Posts sind sich ziemlich ähnlich, wir starten also mit
einer Basisklasse
'''
class Nachricht:
    def __init__(self, benutzer, zeit, text):
        self.benutzer = benutzer
        self.zeit = zeit
        self.text = text

'''
Ein Kommentar ist eine Nachricht die zu einem Post gehört.
'''
class Kommentar(Nachricht):
     #-  6.b.) Vervollständige:  
     #- < Code hier >


'''
Ein Post ist eine Nachricht.
Ein Post kann mehrere Kommentare haben. Bei Erstellung hat er keine Kommentate (leere Liste von Kommentaren).
In einem Post können andere Nutzer genannt werden. Diese Nennungen werden
hier einfach als Liste der Kurznamen der Nenutzer umgesetzt.
'''
class Post(Nachricht):
    #-  6.b) Vervollständige:  
    #- < Code hier >


'''
Eine Besucherstatistik gehört zu einem Post.
Die Statisitk hat die Egenschaften:

* Anzahl der Besuche
* Anzahl der Besucher (Benutzer die den Post besucht haben)

Um die Anzahl der Besucher zu bestimmen wird eine Menge von Benutzer-Kurznamen verwendet.
'''
#-  6.c.) Schreibe eine Klasse 'Statistik'
#- < Code hier >



#- 6.d.) Übernehme das Hauptprogramm aus der vorherigen Aufgabe und passe es
#        so an, dass es Objekte verwendet.
#- < Code hier >