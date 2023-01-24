'''
Diese Datei verwende ich als Haupteinstiegspunkt zum Debuggen. 

Meistens ist es Sinnvoll einen Testfall zu schreiben, der einen bestimmten
Fehler auslöst.

1. Verweise auf den Testfall den Du debuggen willst
2. Setze Punkte an denen Du das Programm unterbrechen möchtest (Breakpoints)
3. Starte diese Datei mit 'F5 - Debuggen ausführen'
4. Gehe das Programm Schritt für Schritt durch und prüfe ob die Variablen Deinen
   Vorstellungen entsprechen
'''
import test.dao_test as dao_test


if __name__ == '__main__':
    print("START: Debug-Sitzung")
    
    # Testfall
    dao_test.test_post_abfrage()