# Kontrollstrukturen

## Einführung in die Logik mit binären Zahlen

Computer können nicht nur Daten zwischenspeichern und Berechnungen durchführen, sondern auch logische Operationen durchführen. Folgend siehst Du drei typische Vertreter solcher Operationen:

* NICHT

|a|Ergebnis|
|---|---|
|0|1|
|1|0|

* UND

|a|b|Ergebnis|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0]
|1|1|1|

Nur wenn `a` und `b` auf 1 (wahr) stehen, dann ist das Ergebnis auch 1 (wahr). Ansonsten ist das Ergebnis 0 (falsch).

* ODER

|a|b|Ergebnis|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1]
|1|1|1|

Wenn eines der beiden (`a` oder `b`) auf 1 steht, dann ist das Ergebnis auch 1 (wahr). Wenn beide Eingabewerte auf 0 stehen (falsch), dann ist das Ergebnis auch 0 (falsch). Es ist leicht zu sehen, dass sich ODER genau umgekehrt zu UND verhält. Wir können auch sagen:

* ODER ist gleich NICHT UND
* UND ist gleich NICHT ODER

## Bedingungen

Im vorherigen Abschnitt haben wir bereits mehrfach das Wort 'wenn' verwendet. Unsere erste Kontrollstruktur ist die Bedingung:

* WENN ... DANN ... SONST ...

Hier ist ein Beispiel:

* WENN du eine Aufgabe richtig rechnest, DANN bekommst Du einen Punkt, SONST bekommst Du keinen Punkt

## Schleifen

Eine Schleife bedeutet, dass etwas wiederholt wird. Wir unterscheiden zwischen zwei Arten von Schleifen:

* SOLANGE ... WIEDERHOLE
* WIEDERHOLE BIS ...

Normalerweise sind Schleifen an Bedingungen geknüpft. Hier wieder zwei Beispiele:

* SOLANGE noch nicht alle Aufgaben gerechnet sind, WIEDERHOLE den Ablauf mit der nächsten Aufgabe
* WIEDERHOLE das Lernen aller Vokabeln BIS Du alle Vokabeln richtig auswendig kanntest

Ein besonderer Fall sind Zählschleifen. Dabei ist die Bedingung, dass eine bestimmte Anzahl an Durchläufen (Iterationen) erfolgte:

* VON ... MIT SCHRITTWEITE ... BIS ... WIEDERHOLE

Hier ist ein Beispiel:

* VON 0 MIT SCHRITTWEITE 1 BIS 9 WIEDERHOLE rechne die Aufgabe i