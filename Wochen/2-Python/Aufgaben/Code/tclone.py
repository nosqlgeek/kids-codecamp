# Imports
from datetime import datetime

# Globale Variablen  
posts = {}

# Start
if __name__ == '__main__':
    # "None" bedeutet "Nicht gesetzt, aber bekannt"
    aktion = None

    #-  4.a.) Vervollständige: Solange die Aktion nicht 'Q' ist,  
    #- < Code hier >
        # Die Input-Funtion liest Tastatureingaben. \n seht für 'Neue Zeile auf der Ausgabe'
        aktion = input('Was möchtest Du tun? \n [P - Post erstellen, R - Posts lesen, Q - Beenden] \n Eingabe: ')

        # - 4.b.1.) Prüfe ob die Eingabe 'P' ist
        #- < Code hier >
            post_text = input('Text: ')
            zeit = str(datetime.now())
            print('{}: {}'.format(zeit, post_text))
            #- 5.a.) Füge den Post dem Dictionary `posts` hinzu
            #- < Code hier >
        #- 4.b.2.) Prüfe ob die Eingabe 'R' ist 
        #- < Code hier >
            print('Posts:')
            #- 5.b.) Gebe alle Posts aus. Hier eine Beispielzeile: `2023-01-13 10:24:46.832755: Hello`.
            #- < Code hier >

            #- 5.c.) Zähle wie oft die Posts ausgegeben wurden! Erweitere das Programm um eine Aktion zur Ausgabe der Anzahl der Besuche. 
            #- < Code hier >
        #- 4.b.3.) Prüfe ob die Eingabe 'Q' ist 
        #- < Code hier >
            print('Tschüs!')
        else:
            print('Aktion ist nicht erlaubt')