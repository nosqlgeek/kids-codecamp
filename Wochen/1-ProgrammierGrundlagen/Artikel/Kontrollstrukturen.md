# Kontrollstrukturen
 
## Einführung in die Logik mit binären Zahlen
 
Computer können nicht nur Daten zwischenspeichern und Berechnungen durchführen, sondern auch logische Operationen durchführen. Folgend siehst Du drei typische Vertreter solcher Operationen:
 
* NICHT
 
|A|Ergebnis|
|---|---|
|0|1|
|1|0|
 
Das Ergebnis ist das Gegenteil der Eingabe. Wenn die Eingabe 0 (falsch) ist, dann ist das Ergebnis 1 (wahr).
 
* UND
 
|A|B|Ergebnis|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|
 
Nur wenn `A` und `B` auf 1 (wahr) stehen, dann ist das Ergebnis auch 1 (wahr). Ansonsten ist das Ergebnis 0 (falsch).
 
* ODER
 
|A|B|Ergebnis|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|
 
Wenn eines der beiden (`A` oder `B`) auf 1 steht, dann ist das Ergebnis auch 1 (wahr). Wenn beide Eingabewerte auf 0 stehen (falsch), dann ist das Ergebnis auch 0 (falsch). Es ist leicht zu sehen, dass sich ODER genau umgekehrt zu UND verhält. Wir können auch sagen:
 
* ODER ist gleich NICHT UND
* UND ist gleich NICHT ODER
 
## Bedingungen
 
Im vorherigen Abschnitt haben wir bereits mehrfach das Wort 'wenn' verwendet. Unsere erste Kontrollstruktur ist die Bedingung:
 
* WENN ... DANN ... SONST ...
 
Hier ist ein Beispiel:
 
* WENN du eine Aufgabe richtig rechnest, DANN bekommst Du einen Punkt, SONST bekommst Du keinen Punkt

```
if aufgabe_richtig:
   punkte = punkte + 1
```
 
 
Mit Hilfe der oben genannten Logik können komplexere Bedingungen formuliert werden, z.B.:
 
* WENN (es regnet ODER schneit) UND die Sonne scheint
 
 ```
if (es_regnet or es_schneit) and sonne_scheint:
    print("Wahr")
else:
    print("Falsch") 
 ```

 
## Schleifen
 
Eine Schleife bedeutet, dass etwas wiederholt wird. Wir unterscheiden zwischen zwei Arten von Schleifen:
 
* SOLANGE ... WIEDERHOLE
* WIEDERHOLE BIS ...
 
Normalerweise sind Schleifen an Bedingungen geknüpft. Hier wieder zwei Beispiele:
 
* SOLANGE noch nicht alle Aufgaben gerechnet sind, WIEDERHOLE den Ablauf mit der nächsten Aufgabe

```
while not alle_aufgaben_gerechnet:
   print("Nächste Aufgabe")
```

* WIEDERHOLE das Lernen aller Vokabeln BIS Du alle Vokabeln richtig auswendig kanntest

> Python kennt keine 'repeat until'-Schleife. Allerdings kann sie auch mit Hilfe von while-Schleifen ausgedrückt werden.

```
alle_vokabeln_richtig = False
while True:
   print("Lernen ...")
   alle_vokabeln_richtig = True
   if alle_vokabeln_richtig:
      break
```

Das Unterbrechen von Kontrollstrukturen via `break` wird als 'schmutzige Praxis' bezeichnet. Daher würde man den obigen Code besser so schreiben:

```
alle_vokabeln_richtig = False
while not alle_vokabeln_richtig:
   print("Lernen ...")
   alle_vokabeln_richtig = True
```

Ein besonderer Fall sind Zählschleifen. Dabei ist die Bedingung, dass eine bestimmte Anzahl an Durchläufen (Iterationen) erfolgt:
 
* VON ... MIT SCHRITTWEITE ... BIS ... WIEDERHOLE
 
Hier ist ein Beispiel:
 
* VON 0 MIT SCHRITTWEITE 1 WIEDERHOLE rechne die Aufgabe 9 mal

```
for i in range(0, 9):
  print("Rechne Aufgabe {}".format(i))
```
