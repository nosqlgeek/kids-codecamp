# Imports
from datetime import datetime

# Globale Variablen
posts = []
anzahl_besuche = 0

# Start
if __name__ == '__main__':
    aktion = None

    while aktion != 'Q':
        aktion = input('Was möchtest Du tun? \n [P - Post erstellen, R - Posts lesen, Q - Beenden, S - Besucherstatistik] \n Eingabe: ')

        if aktion == 'P':
            post_text = input('Text: ')
            zeit = str(datetime.now())
            post = {'zeit': zeit, 'text': post_text}
            posts.append(post)
        elif aktion == 'R':
            for post in posts: 
                print('{}: {}'.format(post['zeit'], post['text']))
            anzahl_besuche = anzahl_besuche + 1
        elif aktion == 'S':
            print('Anzahl Besucher: {}'.format(anzahl_besuche))
        elif aktion == 'Q':
            print('Tschüs!')
        else:
            print('Aktion ist nicht erlaubt')