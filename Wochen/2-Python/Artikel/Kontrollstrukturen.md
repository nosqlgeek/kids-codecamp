# Kontrollstrukturen in Python

Wir haben uns die Kontrollstrukturen ja letzte Woche etwas genauer angeschaut. Dieser Artikel wiederholt nochmal das Wichtigste. Statt die Strukturen selbst zu erklären, schauen wir uns einfach nochmal ein Beispiel in der Programmiersprache Python an.

## If

Wenn eine Bedingung erfüllt ist, führe aus:

```
if aufgabe_richtig:
   punkte = punkte + 1
else:
   punkte = punkte - 1
```

## While

Solange eine Bedingung erfüllt ist, wiederhole:

```
while not alle_aufgaben_gerechnet:
   print("Nächste Aufgabe")
```

## For

```
for i in range(0, 9):
  print("Rechne Aufgabe {}".format(i))
```

