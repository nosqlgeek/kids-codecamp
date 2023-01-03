# Importe
import random

# Globale Variablen
punkte_staende = {}

# Konstanten
## Aufgabenliste - Dazu später mehr
AUFGABEN = [ "4 + 4", "3 * 3", "3 * 7", "42 - 2", "5 * 3", "15 / 3", "33 / 3", "5 * 10", "60 / 6", "7 * 4" ]
NIEMAND = "niemand"

# Hilfsfunktionen 
## Dazu später mehr
def ist_schneller_zufaellig(erster_teilnehmer, zweiter_teilnehmer):
    alle = [ NIEMAND, erster_teilnehmer, zweiter_teilnehmer]
    schnellster = random.randint(0, 2)
    return alle[schnellster]

def notiere_punkt(teilnehmer):
    if not teilnehmer in punkte_staende.keys():
        punkte_staende[teilnehmer] = 0
    
    punkte_staende[teilnehmer] = punkte_staende[teilnehmer] + 1

def rechne_aufgabe(aufgabe):
    return eval(aufgabe)

def ausgabe_punkte():
    print("\n\n---")
    print("Punkte = {}".format(punkte_staende))

## Start des Programms
if __name__ == "__main__":    
    
    print("# Start")
    erster_teilnehmer = "T1"
    zweiter_teilnehmer  = "T2"

    for i in range(0, len(AUFGABEN)-1):

        print("\n## Durchlauf = {}".format(i))

        aktuelle_aufgabe = AUFGABEN[i]
        print("Aufgabe = {}".format(aktuelle_aufgabe))

        schnellster_teilnehmer = NIEMAND
        while schnellster_teilnehmer == NIEMAND:
            schnellster_teilnehmer = ist_schneller_zufaellig(erster_teilnehmer, zweiter_teilnehmer)
            
        print("Schnellster = {}".format(schnellster_teilnehmer))

        richtiges_ergebnis = eval(aktuelle_aufgabe)
        print("Ergebnis = {}".format(richtiges_ergebnis))

        # Der Computer rechnet immer richtig.
        if  richtiges_ergebnis == rechne_aufgabe(aktuelle_aufgabe):
            notiere_punkt(schnellster_teilnehmer)
    
    ausgabe_punkte()