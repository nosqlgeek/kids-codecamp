# Kontrollstrukturen in Python

Wir haben uns die Kontrollstrukturen ja letzte Woche etwas genauer angeschaut. Dieser Artikel wiederholt nochmal das Wichtigste. Statt die Strukturen selbst zu erklären, schauen wir uns einfach nochmal ein Beispiel in der Programmiersprache Python an.

## If

Wenn eine Bedingung erfüllt ist, führe aus:

```
if aufgabe_richtig:
   punkte = punkte + 1
elif aufgabe_teilweise_richtig:
   punkte = punkte + 0.5
else:
   punkte = punkte - 1
```

Bedingungen können mit Hilfe von Vergleichsoperatoren ausgewertet werden. Welche Operatoren erlaubt sind und wie die Operation im Hintergrund funktioniert, hängt vom jeweiligen Datentyp ab. Dazu lernst Du bald mehr. Hier sind einige Beispiele:

* `==`: Gleich
* `!=`: Ungleich
* `>`: Größer als
* `<`: Kleiner als
* `>=`: Größer als, oder gleich
* `<=`: Kleiner als, oder gleich

Das `if aufgabe_richtig:` im obigen Beispiel ist die Kurzform für `if aufgabe_richtig == True`.

Außerdem kannst du mehrere Bedingungen zu einer neuen Bedingung verketten, zum Beispiel:

* `or`: Oder
* `and`: Und
* `not`: Nicht

## Match

> Match ist erst ab Python 3.10 verfügbar

Manchmal hat man sehr viele Bedingungen zu überprüfen. In diesem Falle kann `match ... case ... other ...` besser lesbar sein als `if ... elif ... else`.

```
match grusswort:
   case: 'Hallo!':
       print('Hallo!')
   case: 'Grüß Gott!':
       print('Grüß Dich!')
   case other:
       print('Guten Tag!')
```

## While

Solange eine Bedingung erfüllt ist, wiederhole:

```
while not alle_aufgaben_gerechnet:
   print("Nächste Aufgabe")
```

## For

Wiederhole für eine Anzahl an Werten:

```
for i in range(0, 9):
  print("Rechne Aufgabe {}".format(i))
```

