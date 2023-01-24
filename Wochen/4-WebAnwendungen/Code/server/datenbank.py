# Wir verwenden die Datenbank 'Redis' (also 'Redis Stack')
import redis
from redis.commands.search.query import Query
from redis.commands.search.field import NumericField, TextField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

# Konstanten
DB_HOST='127.0.0.1' 
DB_PORT=6379
DB_PASSWORD=''

# Variablen
verbindung = None


'''
Erstelle einen Datenbankindex: Ein Index wird benötigt um Daten in der Datenbank
effizienter (schneller) zu finden.
'''
def index_erstellen(typ, schema):
    erfolg=False
    
    # Das hier ist neu für Dich. Dabei handelt es sich um ein Beispiel der Fehlerhandhabung:
    # Versuche etwas auszuführen und handhabe den Fehler wenn es nicht klappt.
    try:
        # Wir verwenden HASHes (Abbildungen/Dictionaries) zum abspeichern der Daten
        index_def = IndexDefinition(index_type=IndexType.HASH, prefix=['{}:'.format(typ)])
        index_name = 'index:{}'.format(typ)
        verbindung.ft(index_name).create_index(schema, definition=index_def)
        erfolg=True
    except Exception as err:
            print('WARNUNG: Der Suchindex für den Typ {} kann nicht erstellt werden. - {}'.format(typ, err))

    return erfolg


'''
Die Datenbank will wissen was indiziert werden soll und welchen Datentyp die Eigenschaften haben
'''
def indizes_erstellen():
    post_schema = (TagField('kurzname'),TextField('text'), NumericField('zeit'))
    nutzer_schema = (TagField('kurzname'), TextField('vorname'), TextField('nachname'), TagField('email'))
    index_erstellen('post', post_schema)
    index_erstellen('nutzer', nutzer_schema)

def verbinden():
    # Die Globale Variable ist noch nicht gesetzt, wir teilen Python also mit, dass es nicht nach einer ungesetzten
    # lokalen Variable suchen sol
    global verbindung

    if not verbindung:
        verbindung = redis.Redis(DB_HOST, DB_PORT, decode_responses=True)
        indizes_erstellen()

    return verbindung

'''
Die gesamte Datenbank löschen
'''
def loeschen():
    return verbinden().flushall()


'''
Sende eine Abfrage an die Datenbank
'''
def abfragen(typ, abfrage):
    r = verbinden()
    index_name = 'index:{}'.format(typ)    
    docs = r.ft(index_name).search(Query(abfrage).no_content()).docs

    # Ein wenig Funktionale Programmierung
    # 
    # Die Funktion map bildet jedes Element einer Kollektion
    # von Elementen auf ein anderes Element ab. Das `lambda` bedeutet, dass wir hier eine Funktion zur
    # Abbildung benutzen, welche wir vorher nicht definiert haben. Die Funktion bildet das Ergebnisdokument 
    # zur ID Ergebnisdokuments ab. Wir erhalten also eine Liste von ID-s.
    return list(map(lambda d: d.id, docs))

