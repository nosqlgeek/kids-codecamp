# Testen und Debuggen

Eine Web-Anwendung besitzt in der Regel bereits eine gewisse Komplexität. Es ist recht unwahrscheinlich, dass sich in 1000 Code-Zeilen keine Fehler einschleichen. Falls Du einen solchen Fehler siehst, ist folgende Vorgehensweise hilfreich:

0. Finde Fehler möglichst schnell, indem Du parallel zum Quellcode der Anwendung auch Testfälle entwickelst! Da sich solche Tests oft auf Klassen oder Funktionen beziehen, nennt man sie auch Unit-Tests (Bauelement-Tests).
1. Untersuche den Fehler mit Hilfe eines Debuggers!
2. Schreibe einen Test-Fall, der überprüft, ob der Fehler immer noch vorhanden ist!
3. Führe regelmäßig alle Tests aus, um zu prüfen, ob sich nicht neue Fehler eingeschlichen haben.

## Wie schreibt man einen Testfall?

Es gibt verschiedene Bibliotheken zum Testen in Python. Ich verwende hier `pytest`. Der folgende Test prüft ob eine Verbindung zur Datenbank hergestellt werden kann:

```
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
```

Die Funktion `assert` überprüft, ob eine Bedingung erfüllt ist. Nur wenn alle Bedingungen mit `assert` erfüllt sind, ist der Test erfolgreich.

## Wie führt man Tests aus?

Pytest kommt mit einem gleichnamigen Programm:

```
pytest -s datenbank_test.py
```

## Was gibt ein Testlauf aus?

Im allgemeinen sind folgende Informationen zu entnehmen:

* Erfolg/Mißerfolg bestimmter Tests
* Fehlerausgaben
* Log-Ausgaben
* Stacktraces

## Wie kann ich mit VSCode debuggen?

Ich empfehle einen Programmhaupteinstiegspunkt den Du variabel an Deine Bedürfnisse anpassen kannst. Meine Python-Datei hierfür heißt `debug.py`. Hier eine Beispielvorgehensweise:

1. Importiere das Modul, das den Testfall oder das Problem enthält.
2. Setze 'Breakpoints' an Stellen, die Du untersuchen möchtest.
3. Rufe die zu debuggende Funktion im Hauptprogramm von `debug.py` auf!
4. Gehe den Quellcode Schritt für Schritt durch und überprüfe den Inhalt der Variablen!

> Falls du ein Programm zur Laufzeit debuggen musst, gibt es auch die Möglichkeit einen Debugger an ein laufendes Programm anzuhängen.

