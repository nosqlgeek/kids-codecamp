
# Was ist ein Computer?

Ein Computer ist, wie der Name schon sagt, eine Machine welche Berechnungen durchführt. Hier einige Beispielberechnungen:

* Logische Operationen (z.B. A und B ergibt C)
* Einfache Mathe-Aufgaben (z.B., Was ist 5 plus 5?)
* Komplizierte Berechnung von grafischen Objekten (z.B., für 3D-Spiele)


## Wie rechnet ein Computer?

Zum Rechnen benötigt der Computer eine zentrale Recheneinheit, die CPU. CPU-s rechnen üblicherweise mit Zahlen die aus Nullen (0) und Einsen (1) bestehen. Der Grund ist, dass sich solche Schaltungen auf Hardware-Ebene leichter umsetzen lasssen. Ein Schalter ist entweder auf (0) oder zu (1). Wir Menschen nutzen normalerweise nicht das Binäre Zahlensystem. Wir benutzen Dezimalzahlen, welche aus den Ziffern 0 bis 9 bestehen. Grund dafür ist, dass wir 10 Finger haben. Hier einige Bespielzahlen:

|Zahl im Dezimaldarstellung|Zahl in Binärdarstellung|
|--------------------------|------------------------|
|0|0|
|1|1|
|2|10|
|3|11|
|4|100|
|5|101|
|6|110|

Eine einfache Berechnung sieht dann wie folgt aus:

|A|+|B|=|C|
|---|---|---|---|---|
|1|+|1|=|0 Ü1|
||||=|10|

## Wie speichert ein Computer Daten?

Es gibt verschiedene Speicher in einem Computer:

* Flüchtiger Speicher (z.B., RAM), zum schnellen Zugriff bei Berechnungen
* Dauerhafter Speicher (z.B. die Festplatte)

Das Betriebssystem, in unserem Fall Linux, erlaubt es den flüchtigen Speicher über Addressen anzusprechen. Stellt Euch einen Schrank mit mehreren Schubladen vor. Die Schubladen sind durchnummeriert. Sagen wir, wir hätten 32 Schubladen, dann wären unsere Schubladen mit den Zahlen 0 bis 31 beschriftet. Jede Zahl entspricht einer Addresse. Wenn man nun bestimmte Daten ablegen will, dann muss sich zuerst merken in welcher Schublade man die Daten ablegen möchte (z.B., Schublade 5), und dann die Daten dort hinterlegen. Falls man die Addresse (Zahl kennt), dann kann man die Daten auch wieder aus der Schublade herausnehmen.


|Addresse der Schublade|Daten|
|----------------------|-----|
|4|Gelber Zettel|
|2|Roter Zettel|
|31|Grüner Zettel|

Für einen Programmierer ist es recht schwer sich solche Addressen zu merken. Euer Computer hier kann Millionen solcher Addressen verwalten. Daher wäre es gut, wenn man den Addressen Namen geben könnte. Das sehen wir später noch wenn wir Variablen mit Hilfe der Programmiersprache setzen. Hier ein Beispiel für Variablennamen. Es ist wichtig, dass ihr den Variablen eindeutige und sprechende Namen gebt. 

|Addresse der Schublade|Daten|Name|
|----------------------|-----|---|
|4|Gelber Zettel|gelb|
|2|Roter Zettel|rot|
|31|Grüner Zettel|grün|
