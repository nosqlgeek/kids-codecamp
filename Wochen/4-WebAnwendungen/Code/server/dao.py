import server.datenbank as datenbank

'''
Daten beschreibt eine Datenklasse. Die Klasse beschreibt wie Daten in die
Datenbank geschrieben bzw. aus der Datenbank abgerufen werden. Dieses Muster
wird auch 'Data Access Object' genannt. 
'''
class Daten:
    def __init__(self, typ, id):
        self.typ = typ
        self.id = id


    '''
    Ermittle den Datenbakschlüssel für das Objekt
    '''
    def schluessel_in_db(self):
        return '{}:{}'.format(self.typ, self.id)

    '''
    Rufe ein Objekt anhand seines Typs und seiner ID ab
    '''
    def abrufen(self):
        schluessel = self.schluessel_in_db()
        print('Rufe Daten mit Schlüssel {} ab.'.format(schluessel))
        return datenbank.verbinden().hgetall(schluessel)

    '''
    Speichere die Daten eines Objekts anhand des Typs und der ID
    '''
    def speichern(self):
        schluessel = self.schluessel_in_db()
        print('Wird unter Schlüssel {} gespeichert.'.format(schluessel))
        return datenbank.verbinden().hset(schluessel, mapping=self.daten())

    '''
    Gib die reinen Daten des Objekts zurück 
    '''
    def daten(self):
        # Interessant: Was auch immer ihr im original __dict__ ändert, wird auch am Objekt geändert.
        # Daher ist es besser hier mit einer Kopie zu arbeiten.
        return self.__dict__.copy()

    '''
    Frage nach Objekten des gleichen Typs
    '''
    def abfragen(self, abfrage='*'):
        return datenbank.abfragen(self.typ, abfrage)

    '''
    Prüfe ob das Objekt bereits in der Datenbank existiert
    '''
    def existiert_schon(self):
        schluessel = self.schluessel_in_db()
        return int(datenbank.verbinden().exists(schluessel)) == 1
