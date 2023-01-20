# Imports
from datetime import datetime

# Globale Variablen
posts = []

# Klassen
"""
Das TClone Modell hat:

* Benutzer
* Posts
* Kommentare
* Besucherstatistiken
"""

'''
Alle weiteren Klassen beschreiben Objekte
deren Daten wir abrufen oder speichern wollen
'''
class Daten:
    def __init__(self, typ):
        self.typ = typ

    def abrufen(self):
        pass

    def speichern(self):
        pass

    def daten(self):
        return self.__dict__

'''
Ein Benutzer hat einen Kurnamem, einen Vornamen und eine
E-Mail-Address
'''
class Benutzer(Daten):
    def __init__(self, kurzname, vorname, nachname, email):
        super().__init__('nutzer')
        self.kurzname = kurzname
        self.vorname = vorname
        self.nachname = nachname
        self.email = email

'''
Kommentare und Posts sind sich ziemlich ähnlich, wir starten also mit
einer Basisklasse
'''
class Nachricht(Daten):
    def __init__(self, benutzer, zeit, text):
        super().__init__('nachricht')
        self.benutzer = benutzer
        self.zeit = zeit
        self.text = text

'''
Ein Kommentar ist eine Nachricht die zu einem Post gehört.
'''
class Kommentar(Nachricht):
    def __init__(self, benutzer, zeit, text, post):
        super().__init__(benutzer, zeit, text)
        self.typ = 'kommentar'
        self.post  = post


'''
Ein Post ist eine Nachricht.
Ein Post kann mehrere Kommentare haben. Bei Erstellung hat er keine Kommentate (leere Liste von Kommentaren).
In einem Post können andere Nutzer genannt werden. Diese Nennungen werden
hier einfach als Liste der Kurznamen der Nenutzer umgesetzt.
'''
class Post(Nachricht):
    def __init__(self, benutzer, zeit, text, kommentare = [] , nennugen = []):
        super().__init__(benutzer, zeit, text)
        self.typ = 'post'
        self.kommentare = kommentare
        self.nennungen = nennugen
        self.statistik = Statistik(self)
    
    # Überschreiben der Methode 'Speichern'
    def speichern(self):
        posts.append(self)
    
    # Überschreiben der Methode 'Abrufen'
    def abrufen(self):
        print(self.daten())


'''
Eine Besucherstatistik gehört zu einem Post

Um die Anzahl der Besucher zu bestimmen wird eine Menge von Benutzer-Kurznamen verwendet
'''
class Statistik(Daten):
    def __init__(self, post, anzahl_besuche = 0, anzahl_besucher = 0):
        self.post = post
        self.anzahl_besuche = anzahl_besuche
        self.anzahl_besucher = anzahl_besucher
        self.besucher = set()

    def besuche(self, nutzer_kurzname):
        self.besucher.add(nutzer_kurzname)
        self.anzahl_besuche = self.anzahl_besuche + 1
        self.anzahl_besucher = len(self.besucher)

    def abrufen(self):
        print('anzahl_besuche = {}, anzahl_besucher = {}'.format(self.anzahl_besuche, self.anzahl_besucher))

# Hauptprogramm
if __name__ == '__main__':
    
    # Wer bist Du?
    vorname = input('Vorname? Eingbae: ')
    nachname = input('Nachname? Eingabe ')
    kurzname = input('Kurzname? Eingabe: ')
    email = input('E-Mail-Addresse? Eingabe: ')
    
    benutzer = Benutzer(kurzname, vorname, nachname, email)

    # Was willst Du tun?
    aktion = None
    while aktion != 'Q':
        aktion = input('Was möchtest Du tun? \n [P - Post erstellen, R - Posts lesen, Q - Beenden, S - Besucherstatistik] \n Eingabe: ')

        if aktion == 'P':
            text = input('Text: ')

            # Es ist besser die Zeit als Zahl abzuspeichern, da sich später mit 
            # Zahlen besser arbeiten lässt
            post = Post(benutzer, int(datetime.now().timestamp()), text)
            post.speichern()
        elif aktion == 'R':
            for post in posts: 
                post.statistik.besuche(benutzer.kurzname)
                post.abrufen()
        elif aktion == 'S':
            for post in posts:
                post.statistik.abrufen()
        elif aktion == 'Q':
            print('Tschüs!')
        else:
            print('Aktion ist nicht erlaubt')



