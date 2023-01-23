# Include Python modules from the parent folder
import sys
sys.path.append('..')

# Imports
import server.datenbank as datenbank

# Tests
def test_verbinden():
    db = datenbank.verbinden()
    # Überprüfe ob eine Bedingung wahr ist
    assert db.set('test', 'success') == True
    assert db.get('test') == 'success'

def test_abfragen():
    assert str(datenbank.abfragen('post','*')) == "Result{0 total, docs: []}"
    
