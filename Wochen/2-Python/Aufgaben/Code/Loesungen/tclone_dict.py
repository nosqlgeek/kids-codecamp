# Imports
from datetime import datetime

# Globale Variablen
posts = {}
anzahl_besuche = 0

# Start
if __name__ == '__main__':
    # "None" bedeutet "Nicht gesetzt, aber bekannt"
    aktion = None

    while aktion != 'Q':
        # Die Input-Funtion liest Tastatureingaben
        # \n seht für 'Neue Zeile auf der ausgabe'
        aktion = input('Was möchtest Du tun? \n [P - Post erstellen, R - Posts lesen, Q - Beenden, S - Besucherstatistik] \n Eingabe: ')

        if aktion == 'P':
            post_text = input('Text: ')
            zeit = str(datetime.now())
            posts[zeit] = post_text
        elif aktion == 'R':
            for zeit in posts: 
                print('{}: {}'.format(zeit, posts[zeit]))
            anzahl_besuche = anzahl_besuche + 1
        elif aktion == 'S':
            print('Anzahl Besucher: {}'.format(anzahl_besuche))
        elif aktion == 'Q':
            print('Tschüs!')
        else:
            print('Aktion ist nicht erlaubt')