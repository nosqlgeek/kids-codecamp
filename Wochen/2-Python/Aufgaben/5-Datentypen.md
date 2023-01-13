# 5.) Datentypen

## Anforderungen

Dein Programm erfüllt also nun die folgenden Anforderungen:

* Es soll möglich sein Posts einzugeben
* Die Zeit der Eingabe muss erfasst werden

Bisher ist führt die Eingabe von `R` (Posts lesen) aber nur zu der Augabe 'Posts:'. Wir müssen unsere Anforderungen also dementsprechend erweitern:

* Alle Posts sollen angezeigt werden können
* Die Anzahl der Besuche (lesen aller Posts) muß erfasst werden

Welche Aktionen müssem wir umsetzen?

* Posts anzeigen
* Anzahl der Besuche anzeigen


## Aufgabe

### a.) Setzen von Werten in Abbildungen

Erweitere das Programm `tclone.py` um das speichern der Posts in einer Abbildung (Dictionary), wobei der Post-Text anhand der Zeit abgelegt wird.

### b.) Iterieren über Abbildungen

Iteriere über das Dictionary und gib alle Werte im Format `Zeit: Text` (z.B. `2023-01-13 10:24:46.832755: Hello`) aus!

### c.) Zahlen

Erweitere das Programm um eine Variable `anzahl_besuche` und zähle wie oft die Posts gelesen wurden! Füge außerdem eine neue Aktion `S - Besucherstatistik` hinzu um den Wert der Variable `anzahl_besuche` zugänglich zu machen.

### d.) Listen

Bei Abbildungen ist die Reihenfolge der Ausgabe nicht unbedingt identisch zur Reihenfolge des Erstellens des Posts. Ändere das Programm und verwende den Typ 'Liste' statt 'Dictionary' für die Variable `posts`!


## Test

Teste Dein Programm indem Du die folgenden Schritte durchführst:

1. Führe das Programm in VSCode aus!
2. Füge einige Posts über 'P' (Post erstellen) hinzu!
3. Gib 'R' (Posts lesen) ein und bestätige mit der Eingabetaste!
4. Du solltest alle eingegebenen Posts sehen.
5. Wiederhole den Schritt 3 einige male
6. Gib 'S' (Besucherstatistik) ein und überprüfe den Wert! 