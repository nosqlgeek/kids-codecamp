# Imports
from server.dao import Daten
from datetime import datetime


'''
Ein Benutzer hat einen Kurnamem, einen Vornamen und eine
E-Mail-Address
'''
class Benutzer(Daten):
    def __init__(self, kurzname, vorname='', nachname='', email=''):
        super().__init__('nutzer', kurzname)
        self.kurzname = kurzname
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
    
    def abrufen(self):
        daten = super().abrufen()
        return Benutzer(daten['kurzname'],daten['vorname'], daten['nachname'], daten['email'])

        

'''
Kommentare und Posts sind sich ziemlich ähnlich, wir starten also mit
einer Basisklasse
'''
class Nachricht(Daten):
    def __init__(self, benutzer, zeit, text):
        super().__init__('nachricht', '{}:{}'.format(benutzer.kurzname, zeit))
        self.benutzer = benutzer
        self.zeit = zeit
        self.text = text

'''
Ein Kommentar ist eine Nachricht die zu einem Post gehört.
'''
class Kommentar(Nachricht):
    def __init__(self, benutzer, zeit, post, text=""):
        super().__init__(benutzer, zeit, text)
        self.typ = 'kommentar'
        self.id = '{}:{}'.format(post.id, self.id)
        self.post = post
    
    def daten(self):
        d = super().daten()
        d['benutzer'] = self.benutzer.id
        d['post'] = self.post.id
        return d
    
    def abrufen(self):
        d = super().abrufen()
        benutzer = Benutzer(d['benutzer']).abrufen()
        return Kommentar(benutzer, int(d['zeit']), self.post, d['text'])
        



'''
Ein Post ist eine Nachricht.
Ein Post kann mehrere Kommentare haben. Bei Erstellung hat er keine Kommentate.
In einem Post können andere Nutzer genannt werden. Diese Nennungen werden
hier einfach als Liste der Kurznamen der Nenutzer umgesetzt.
'''
class Post(Nachricht):
    def __init__(self, benutzer, zeit, text='', kommentare = [] , nennugen = []):
        super().__init__(benutzer, zeit, text)
        self.typ = 'post'
        self.kommentare = kommentare
        self.nennungen = nennugen
        self.statistik = Statistik(self)
    
    '''
    Der Einfachheit halber (d.h. zur Speicherung und Übertragung, wollen wir die reinen Daten 'flach' 
    (d.h. ohne direkte Beziehungen zu Objekten) handhaben.

    Um das zu erreichen, überschreiben wir hier die daten()-Methode der Eltern-Klasse 'Daten'.
    '''
    def daten(self):
        d = super().daten()
        d['benutzer'] = self.benutzer.id
        d['statistik'] = self.statistik.id
        
        kommentar_ids= []
        for k in self.kommentare:
            kommentar_ids.append(k.id)
        
        #Es gibt mehrere Möglichkeiten Listen in Redis zu speichern. Redis Stack kann mit kommaseparierten Tag-Listen arbeiten
        #z.B. tag1,tag2,tag3
        d['kommentare'] = ','.join(kommentar_ids)
        d['nennungen'] = ','.join(self.nennungen)
        return d
    
    '''
    Wir speichern nicht nur die Daten des Posts, sondern auch die Kommentare
    '''
    def speichern(self):
        # Anzahl der gespeicherten Datensätze
        result = 0
        result = result + super().speichern()
        for k in self.kommentare:
            result = result + k.speichern()
        result = result + self.statistik.speichern()
        return result
    
    '''
    Beim Abrufen müssen wir die flachen Daten wieder in Objekte wandeln
    '''
    def abrufen(self):
        d = super().abrufen()
        benutzer = Benutzer(d['benutzer']).abrufen()
        statistik = Statistik(self).abrufen()
        nennungen = d['nennungen'].split(',')
        
        kommentare = []
        kommentar_ids = []
        
        if d['kommentare'] != '':
            kommentar_ids = d['kommentare'].split(',')
        
        for k in kommentar_ids:
            id_as_list = k.split(':')
            kommentator = Benutzer(id_as_list[2]).abrufen()
            kommentar_zeit = int(id_as_list[3])
            kommentare.append(Kommentar(kommentator, kommentar_zeit, post=self).abrufen())
        
        post = Post(benutzer, int(d['zeit']), d['text'], kommentare, nennungen)
        post.statistik = statistik
        return post
    

'''
Eine Besucherstatistik gehört zu einem Post. 
Um die Anzahl der Besucher zu bestimmen wird eine Menge von Benutzer-Kurznamen verwendet
'''
class Statistik(Daten):
    def __init__(self, post, anzahl_besuche = 0, besucher=set()):
        super().__init__('statistik', post.id)
        self.post = post
        self.anzahl_besuche = anzahl_besuche
        self.anzahl_besucher = len(besucher)
        self.besucher = besucher

    def besuche(self, nutzer_kurzname):
        self.besucher.add(nutzer_kurzname)
        self.anzahl_besuche = self.anzahl_besuche + 1
        self.anzahl_besucher = len(self.besucher)

    def daten(self):
        d = super().daten()
        d['post'] = self.post.id
        d['besucher'] = ','.join(self.besucher)
        return d
    
    def abrufen(self):
        d = super().abrufen()
        anzahl_besuche = int(d['anzahl_besuche'])
        besucher = set()
        for b in d['besucher'].split(','):
            besucher.add(b)
        return Statistik(self.post, anzahl_besuche, besucher)
        