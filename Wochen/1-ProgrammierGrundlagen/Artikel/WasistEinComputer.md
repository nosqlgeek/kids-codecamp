
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

Eine Stelle in Binärdarstellung heißt Bit. D.h. die Zahl 110 hat 3 Bits.

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


Das Betriebssystem stellt den persistenten Speicher über Dateisysteme zur Verfügung. Ein Dateisystem hat die Aufgabe Dateien zu verwalten. Dateien können in Ordnern gespeichert werden. Die genaue Umsetzung kann von Dateisystem zu Dateisystem variieren. Eine Datei selbst wird vom Betriebsystem als eine Sequenz von Blöcken (z.B. 4 KB  - 4 Kilobyte = 4096 Bytes = 8*4096 Bit je Block) gesehen. 

|Blöcke|Block_0|Block_1|Block_2|...|Block_n-1|
|------|-------|-------|-------|---|---------|
|Daten|0000110|1111001|0011001|...|0000000|


## Was hat die Datenspeicherung mit der Berechnung zu tun?

Damit der Computer mit Daten (z.B. Zahlen) rechnen kann, passiert folgendes:

1. Ein Teil der Daten wird von der Festplatte in den schnelleren RAM geladen. Meißt gibt es noch einen schneleren Zwischespeicher in der CPU selbst.
2. Im Rahmen der Berechnung werden die Daten in CPU-Registern abgelegt. Ein CPU-Register ist meißt so breit, dass es eine große Zahl aufnehmen kann
3. Das Ergebnis der Berechnung wird wieder in einem Register zwischengespeichert, bevor es in den RAM und dann auf Festplatte geschrieben wird.

|Register|Wert|Operation|
|--------|----|---------|
|R1|0001||
|||+|
|R2|0010||
|R3|0011||

R1 = 1
R2 = 2
R3 = 1+2 = 3