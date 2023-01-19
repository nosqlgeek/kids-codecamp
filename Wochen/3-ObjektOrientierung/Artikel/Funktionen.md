# Funktionen

Bevor wir mehr über Objekte sprechen, sollten wir verstehen was eine Funktion ist.

## Was ist eine Funktion?

Wahrscheinlich kennst du Funktionen schon aus dem Mathe-Untericht (z.B.: `y=f(x)=3*x+1`. In Python können Funktionen nicht nur mit Zahlen arbeiten. Wie wir bereits besprochen haben, sieht der Computer Zahlen, Zeichenketten (Strings) oder Bilder nur als Seqzenz von nullen und einsen. Es ist dem Computer also eigentlich egal ob die Funktion mit Zahlen arbeitet, oder mit Zeichenketten.

Eine Funktion im allgemeinen hat einen oder mehrere Eingabewerte. Diese Eingabewerte werden auf einen oder mehrere Ausgabewerte abgebildet. In Python kann eine Funktion auch auf einen leeren Ausgabewert `None` abbilden.

> Eventuell fragst Du dich jetzt was der Unterschied zwischen einer Funktion und einer Abbildung ist. Bei der Abbildung von letztem mal, haben wir die Eingabewerte direkt auf die Ausgabewerte abgebildet (z.B. `dog` gehört zu `Hund`). Eine Funktion verarbeitet die Eingabewerte um auf die Ausgabewerte abzubilden (z.B., `1+1` ergibt `2`)

Im allgemeinen sieht eine Funktion also so aus:

```
              +-----------+ 
Eingabewerte  |           | Ausgabewerte
------------> |  Funktion | ------------>
              |           |
              +-----------+ 
```

## Warum benutzt man Funktionen?

Wir haben uns bisher nur kleine Programme angeschaut. Sobald Euer Programm eine bestimmte Größe hat, werdet ihr feststellen, dass es ein wenig schwierig wird tausende Zeilen hintereinanderweg zu lesen um zu verstehen was der Programmcode tut. Es ist also besser den Code in funktional Blöcke aufzuteilen, z.B.:

1. Globale Variablen
2. Hilfsfunktionen
3. Hauptprogramm

Wenn ihr den Variablen und Funktionen gute sprechende Namen gebt, könnt ihr das Hauptprogramm verstehen ohne, dass ihr jede einzelne Funktion verstehen müsst. Anders herum, könnt ihr Funktionen verstehen und untersuchen ohne Code den gesamten Code des Hautprogramms durchgehen zu müssen.

Neben besserer Aufteilung des Codes, gibt es einen weiteren wichtigen Grund:

* D(on't) R(epeat) Y(ourself): Versuche so wenig wie möglich Quelltext zu wiederholen! Stattdessen versuche, so viel Quelltext wiederzuverwenden wie möglich.

Wenn Du ein riesig langes Programm hast, dann ist es recht wahrscheinlich, dass bestimmte Teile Deines Programms ähnlich aussehen. An dieser Stelle solltest Du überlegen, ob es nicht besser wäre eine Funktion zu schreiben um diesen Quelltext nur einer Stelle pflegen zu müssen. Pflegen? Ja, Quellcode ist selten komplett fertig. Oft kommt es vor, dass er später angepasst werden muß. Dann ist es viel mehr Aufwand eine Änderung an 20 Stellen vornehmen zu müssen statt innerhalb einer Funktion.


## Funktionen in Python

Erinnerst Du Dich noch an unser erstes Programm? Zwei Teilnehmer sollten um die Wette rechnen. Evtl. sah der Quellcode damals noch sehr unklar für Dich aus. Er enthielt bereits folgende Funktionen:

```
def ist_schneller_zufaellig(erster_teilnehmer, zweiter_teilnehmer):
    alle = [ NIEMAND, erster_teilnehmer, zweiter_teilnehmer]
    schnellster = random.randint(0, 2)
    return alle[schnellster]
```

Die Funktion ermittelt aus allen Teilnehmern zufällig den Teilnehner indem sie eine andere Funktion verwendet, welche zufällig eine Zahl zwischen 0 und 2 'würfelt'. Diese andere Funktion ist bereits Bestandteil von Python. Unsere Funktion bildet also den ersten und den zweiten Teilnehmer auf den schnellsten Teilnehmer ab.

```
erster_teilnehmer  +----------------+ 
zweiter_teilnehmer |                | schnellster_teilnehmer
-----------------> |  ist_schneller | ---------------------->
                   |  _zufaellig    |
                   +----------------+ 
```

Funktionen werden mithilfe von `def` definiert. Dann kommt

* der eindeutige Name der Funktion
* die Eingabewerte der Funktion


Die Rückgabe des Ausgabewertes erfolgt mit Hilfe des Wortes `return`. Eine Funktion, die kein `return` enthält läuft einfach bis zum Ende durch und gibt dann den Ausgabewert `None` zurück.

Mehr zu Funktionen könnt ihr [hier](https://www.w3schools.com/python/python_functions.asp) lesen.

## Funktionen Anderer

Du mußt nicht alle Funktionen immer selber schreiben. Python kommt bereits mit einer Menge wiederverwendbarer Funktionen. Außerdem gibt es Millionen von Softwareentwicklern da draußen, die ihren Quellcode frei veröffentliche (z.B. auf Github). Du mußt Python allerdings sagen wenn Du weitere nicht-standard Funktionen verwenden möchtest. Das tust Du über `import`. Das Einbinden von Funktionen erfolgt normalerweise ganz am Anfang des Programms. Unser erstes Beispiel nutzte den folgenden Import:

```
import random
```

`random` ist in diesem Fall keine Funktion, sondern eine sogannte Bibiliothek. 

> In Python wird eine solche Bibliothek auch Modul genannt.

Diese Bibliothek enthält mehrere Funktionen:

* **randint(a, b)**: Gannzahlige Zufallszahl zwischen a und b (a und b sind inklusive)
* **random.randrange(start, stop, step)**: Zufallsnummer aus einem Wertebereich
* **random.shuffle(seq)**: Zufälliges durchmischen einer Liste

Eine komplette Liste der Funktionen gibt es [hier](https://docs.python.org/3/library/random.html).

> Funktionen können auf mehrere Arten importiert werden. Nähere Information sind [hier](https://www.w3schools.com/python/ref_keyword_import.asp) zu finden.