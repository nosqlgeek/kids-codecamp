# Komplexe Datentypen

Es kommt oft vor, dass die einfachen Datentypen nicht ausreichen, um die Anforderung an das Programm oder den Algorithmus abzudecken. Dann helfen die folgenden komplexen Datentypen:

* Listen
* Mengen
* Abbildungen
* Tupel

## Listen

Sicher weißt Du, was eine Einkaufsliste ist. Bei einer Einkaufsliste schreibst Du die zu kaufenden Dinge in der Reihenfolge auf, in der sie im Laden zu finden sind. Bei Listen ist die Reihenfolge also wichtig.

In Python kann eine Liste wie folgt erstellt werden:

```
einkaufsliste = ['Bananen', 'Äpfel', 'Brot', 'Butter', 'Schinken', 'Käse', 'Spülmittel']
```

Eine leere Liste kannst du wie folgt erstellen:

```
leer = []
```

Auf die Werte der Liste kann wie folgt zugegriffen werden:

```
bananen = einkaufsliste[0]
aepfel = einkaufsliste[1]
```

Außerdem kannst Du Listen direkt mit Schleifen verwenden.

```
for zu_kaufen in einkaufsliste:
  print(zu_kaufen)
```

Es gibt einige eingebaute Operationen, die Du auf Listen ausführen kannst:

* `len`: Die Länge der Liste, also die Anzahl der Werte in der Liste, z.B. `einkaufsliste.append('Tücher'`)
* `append`: Hinzufügen am Ende der Liste, z.B. `einkaufsliste.insert(1, 'Birnen')`
* `insert`: Einfügen an einer bestimmten Stelle
* `remove`: Entfernen eines Wertes, z.B. `einkaufsliste.remove('Birnen')`
* `sort`: Sortieren der Liste, z.B. `einkaufsliste.sort()`

Eine vollständige Auflistung der Operationen ist [hier](https://www.w3schools.com/python/python_lists_methods.asp) zu finden.

## Mengen

Anders als bei Listen spielt die Reihenfolge bei Mengen keine Rolle. Es ist sozusagen egal, an welcher Stelle ein Wert steht. Stattdessen ist nur wichtig, ob der Wert in der Menge enthalten ist oder nicht. Hier ein Beispiel für die Teilnehmer dieses Kurses:

```
teilnehmer = {'Julia', 'Alexander', 'Alex', 'Arin'}
```

Eine leere Menge kannst Du wie folgt erstellen:

```
leer = set()
```

Auch Mengen kannst du Wert für Wert mit Hilfe einer Schleife durchgehen:

```
for t in teilnehmer:
  print(t)
```

Mit Mengen kannst Du das folgende anstellen:

* `in`: Überprüfen ob ein Wert in der Menge vorkommt, z.B. `'Alex' in teilnehmer`)
* `add`: Hinzufügen eines Wertes
* `remove`: Entfernen eines Wertes
* `union`: Vereinigen zweier Mengen zu einer neuen Menge, z.B. `alle_teilnehmer=teilnehmer.union({'Samuel'})`

Auch hier gibt es noch viele weitere Operationen. Mehr dazu kannst Du [hier](https://www.w3schools.com/python/python_sets_methods.asp) finden.

## Abbildungen

Wenn wir von Abbildungen sprechen, dann meinen wir keine Bilder, sondern die Abbildung aus dem Mathe-Unterricht. Stellt Euch einmal ein zweidimensionales Koordinatensystem vor. Dort gibt es Punkte. Ein Punkt hat einen x-Wert und einen y-Wert.

|x|y|
|---|---|
|0|0|
|1|3|
|3|9|

Die Tabelle oben ist eine Abbildung von `x` auf `y`.

Der einzige Unterschied in den meisten Programmiersprachen ist, dass Abbildungen nicht nur mit Zahlen, sondern mit beliebigen Werten erstellt werden können. Am Ende handelt es sich ja so oder so um eine Folge von Nullen und Einsen. Ein gutes Beispiel für eine Abbildung ist Euer Vokabelheft aus dem Englischunterricht. Das Vokabelheft bildet zum Beispiel deutsche Wörter auf englische Wörter ab. Python nennt Abbildungen sogar 'Dictionaries', also Wörterbücher.

|Deutsch|Englisch|
|-------|--------|
|'Hund'|'dog'|
|'Katze'|'cat'|
|'Maus'|'mouse'|

Die Tabelle zeigt eine Abbildung von Deutsch auf Englisch.

Abbildungen werden in Python wie folgt geschrieben:

```
punkte = {0: 0, 1: 3, 3: 9}
vokabeln = {'Hund': 'dog', 'Katze': 'cat', 'Maus': 'mouse'}
```

Eine leere Abbildung kann wie folgt erstellt werden:

```
leer = {}
```

Der 'von'-Wert einer Abbildung heißt Schlüssel. Den 'zu'-Wert der Abbildung nennen wir einfach Wert.

Wir können den Wert anhand des Schlüssels wie folgt zugreifen:

```
ubersetzt = vokabeln['Hund']
print(ubersetzt)
```

Hier wieder einige Beispieloperationen:

* `[]`: Lesen, ersetzen, oder hinzufügen von Werten, z.B. `vokabeln['Pferd']='horse'`
* `pop`: Entfernen eines Wertes mit einem bestimmten Schlüssel, z.B. `vokabeln.pop('Pferd')`
* `keys`: Liste aller Schlüssel
* `values`: Liste aller Werte

Eine Übersicht findet ihr [hier](https://www.w3schools.com/python/python_dictionaries_methods.asp).

## Tupel

Ein Tupel ist ähnlich wie eine Liste. Tupel werden verwendet, wenn die Anzahl der Werte bereits vorab feststeht. Wenn ihr ein Tupel einmal gesetzt habt, könnt ihr es nicht mehr verändern.

Im Hintergrund werden die verschiedenen komplexen Datentypen unterschiedlich gespeichert und verwaltet. Tupel sind einfacher aufgebaut und brauchen etwas weniger Speicher als Listen.

Hier zwei Beispiele:

* In einem zweidimensionalen Koordinatensystem besteht ein Punkt immer aus zwei Werten.
* Ein 'normales' Auto (PKW) hat vier Räder. Jeder Reifen hat einen bestimmten Luftdruck.

```
punkt = (1.0, 3.3)
auto_reifendruck = (2.3, 2.4, 2.35, 2.4)
```

Tupel bieten eine überschaubare Anzahl an Operationen an:

* `count`: Anzahl des Vorkommens eines bestimmten Wertes, z.B. `auto_reifendruck.count(2.4)`
* `index`: Position eines bestimmten Wertes im Tupel, z.B. `auto_reifendruck.index(2.3)`