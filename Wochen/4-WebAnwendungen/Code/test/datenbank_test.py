# Include Python modules from the parent folder
import sys
sys.path.append('..')

# Imports
import server.datenbank as datenbank

# Tests
def test_verbinden():
    datenbank.loeschen()
    db = datenbank.verbinden()
    # Überprüfe ob eine Bedingung wahr ist
    assert db.set('test', 'success') == True
    assert db.get('test') == 'success'

def test_abfragen():
    datenbank.loeschen()
    datenbank.verbinden()
    datenbank.indizes_erstellen()
    assert datenbank.abfragen('post','*') == []