# Übung 1 - Von der Festplatte zur CPU

Auf der Festplatte befindet sich eine Datei mit einer Blockgröße von 8 Bit. Hier der Inhalt der Datei `zahlen.dat`:


```
10000001 00000010 00000001 00000010 000001010 000001010 00000010 00000001 00000001 00000010
01000001 00000010 00000001 00000010 000001010 000001010 00000010 00000001 00000001 00000010
00100001 00000010 00000001 00000010 000001010 000001010 00000010 00000001 00000001 00000010
00010001 00000010 00000001 00000010 000001010 000001010 00000010 00000001 00000001 00000010
00001001 00000010 00000001 00000010 000001010 000001010 00000010 00000001 00000001 00000010
```

Die ersten ersten 5 Zahlen sollen von der Festplatte in den RAM geladen werden. Welche der folgenden Adressen kann dafür verwendet werden?

|Adresse|Wert|Frei|
|0|00000000|1|
|7|11111111|0|
|15|00000000|1|
|23|00000000|1|
|31|00000000|1|
|39|10000000|0|
|47|00000000|1|
|55|00000000|1|

Speichere die Werte der Reihe nach unter den freien Adressen und gib den Adressen sprechende Namen.


Lege die ersten 2 Zahlen jeweils in ein CPU-Register und führe eine Addition (`+`) durch. Das Ergebnis soll in Register `R3` zwischengespeichert werden.

|Register|Wert|
|--------|----|
|R1||
|R2||
|R3||

Speichere den Wert unter R3 unter einer freien Speicheradresse und merke Dir die Adresse in dem Du ihr einen Namen gibst.

Wie würdest Du die Daten zurück auf die Festplatte schreiben?