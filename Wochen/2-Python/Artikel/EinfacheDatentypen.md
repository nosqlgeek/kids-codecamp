# Einfache Datentypen

## Einführung

Wir haben ja letzte Woche gesehen wie Computer Daten speichern und verarbeiten. Um Daten abspeichern zu können, muß der Computer wissen wieviel Speicher er für bestimmte Werte verwenden kann. Ein großes Bild braucht mehr Speicher als eine einzelne Zahl. Anders als bei anderen Programmiersprachen ist Python in der Lage den Datentypen bei Zuweisung des Werts selbst herauszufinden:

```
<variable> = <wert>
```

Manchmal kann es nützlich sein den Typ der Variable zu erzwingen:

```
<variable> = <typ>(<wert>)
```

Die Funktion `type` erlaubt es Euch zu überprüfen, ob eine Variable einen bestimmten Typ hat. Hier ein Beispiel:

```
type(<variable>)
```

Eingebaute Typen unterstützen Operationen. Zahlen, zum Beispiel, kann man addieren. Wir schauen uns folgend einige einfache Datentypen an.

## Wahrheitswerte

Wir hatten uns letzte Woche ja schon mit den Bedingungen beschäftigt. Eine Aussage kann entweder wahr oder falsch (unwahr) sein. Das Ergebnis der Auswertung einer Aussage kann in einer Variable vom Typ `bool` gespeichert werden. Hier nochmal ein Beispiel:

```
ist_rot = True
ist_rund = True

ist_roter_kreis = ist_rot and ist_rund
print(type(ist_roter_kreis))
print(ist_roter_kreis)
```

## Zahlen

Python kennt die folgenden numerischen Datentypen:

* `int`: Integer Zahlen sind ganze Zahlen, z.B. 42
* `float`: Fließkommazahlen sind Kommazahlen, z.B. 1.34

Python unterstützt die folgenden Operationen auf Zahlen:

* `+`: Plus / Addition
* `-`: Minus / Subtraktion
* `*`: Mal / Multiplikation
* `/`: Geteilt durch / Division

Eine vollständige Liste findet ihr [hier](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp).

Das folgende Beispiel zeigt die Division (geteilt durch) zweier Zahlen:

```
a = 12
b = 3
c = a / b
print(type(c))
print(c)
```

Das Ergebnis von `a / b` ist zwar eigentlich die ganze Zahl `4`, allerdings wird die Kommazahl `4.0` zurückgegeben. Du kannst die Kommazahl wieder in eine Ganzzahl umwandeln:

```
c = int(c)
print(type(c))
```

## Text

Python kann auch Texte verarbeiten. Textwerte werden mit Hilfe sogenannter Zeichenketten (auf Englisch `Strings`) gespeichert:

* `str`: Zeichenketten, z.B. `'Hallo Welt!'` oder `"Hallo Welt!"`

Hier einige Beispieloperationen auf Zeichenketten:

* `+`: Aneinanderhängen von Zeichenketten
* `upper`: In Großbuchstaben
* `lower`: In Kleinbuchstaben
* `stip`: Leerzeichen am Anfang und am Ende entfernen
* `len`: Länge des Strings
* `format`: Formatieren indem man innerhalb der Zeichenkette ersetzt

> Nebenbei: Statt Zeichenketten mit `+` zu verketten ist es oft besser lesbar eine Zeichkette zu formattieren. Statt `'Hallo Welt' + ', oder ' + 'Hi' + '!'` nimmt man besser `'{}, oder {}!'.format('Hallo Welt, 'Hi')'`.

Eine vollständige Liste dessen, was ihr mit Strings alles machen könnt, findet sich [hier](https://www.w3schools.com/python/python_strings_methods.asp).

Hier noch ein Beispiel:

```
hello_welt = 'Hello' + ' ' + 'Welt' + '!'
print(hello_welt)
```

## Beliebige andere Daten als Bytes

Manchmal gibt es keinen einfachen, eingebauten, und passenden Datentyp in Python. Python kennt z.B. keinen einfachen Datentyp für Bilder (später mehr zu komplexen Datentypen und Klassen). Ihr könnt die Daten dann direkt als Bytes speichern:

* `bytes`: Aneinanderreihung von aufeinanderfolgenden Bits, Byte-weise gruppiert

Ein Byte sind 8 Bits. Die Bits waren die Nullen und Einsen, die wir letzte Woche besprochen haben. Euer Programm muss dann eben wissen, wie es mit den Bytes umgehen soll.

```
byte_haufen = b'Hallo Welt!'
print(byte_haufen.hex())
48616c6c6f2057656c7421
```

Sicher ist Dir oben die Funktion `hex` aufgefallen. Außerdem fragst Du Dich vielleicht was die Zeichenfolge `48616c6c6f2057656c7421` zu bedeuten hat. Hexadezimalzahlen werden hier nicht im Detail behandelt. Nur soviel: Stell Dir vor, Du hättest 16 Finger (0,..,9, A,..,F). Das praktische an Hex-Zahlen ist, dass eine Hex-Zahl durch 4 Bits ausgedrückt werden kann. Sie stellt also ein Halb-Byte dar. Das heißt, dass zwei Hex-Zahlen ein Byte ergeben. Die ersten Zahlen in unserem Beispiel (4 und 8) entsprechen somit der Bitfolge `0100 1000`. Diese Bitfolge kann Python auch als den Buchstaben `H` sehen. Das heißt, Hex-Zahlen sind praktisch, um:

* Lange Binärzahlen kürzer darzustellen
* Nicht als Text vorliegende Daten als String auszugeben