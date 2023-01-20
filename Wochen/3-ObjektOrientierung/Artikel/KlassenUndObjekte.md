# Klassen und Objekte

Unser Fokus letzte Woche war auf Kontrollstrukturen. Diese Woche wollen wir uns näher mit Objektorientierung beschäftigen. Am Ende der letzten Stunde haben wir uns auch schon angeschaut, was Objektorientierte Analyse ist und wie sie grundlegend funktioniert.

## Was ist ein Objekt?

Du fragst Dich sicher, was wir mit Objekt meinen. Letztendlich helfen uns Computer, echte Probleme aus der realen Welt zu lösen. Du kannst dir ein Objekt also als einen Gegenstand der realen Welt vorstellen. Mein Auto ist zum Beispiel ein Objekt. Hier eine Beschreibung meines Autos:

* **Marke**: Citroen
* **Modell:**: C4 Spacetourer
* **Anzahl Sitze**: 7
* **Anzahl Räder**: 4
* **Schaltung**: Manuell
* **Anzahl der Gänge**: 6
* **Kraftstoff**: Benzin

Ein Objekt kann außerdem Funktionen haben. Hier einige Beispiele:

* Lenken
* Bremsen
* Beschleunigen
* Blinken

Wenn eine Funktion einem Objekt zugeordnet ist, nennen wir sie auch 'Methode'.

## Was ist eine Klasse?

Ich könnte jetzt die gleichen Eigenschaften verwenden um ein anderes Auto zu beschreiben, z.B.:

* VW Passat, 5 Sitze, Automatik, 5 Gänge, Diesel

Die Vorlage (z.B., Auto: Marke, Modell, Anzahl Sitze, usw.), welche ich verwende, um die Eigenschaften und Funktionen eines Objekts zu beschreiben, nennt man auch Objektklasse (kurz Klasse) oder Objekttyp.

## Beziehungen zwischen Objekten

### Direkte Beziehung

Ein Auto ist kein einzelner Gegenstand, sondern es ist eine Ansammlung von Objekten, die zusammen arbeiten. Mein Auto hat z.B.:

* Lenkrad, dass sich drehen lässt
* Getriebe, dass sich schalten lässt
* Räder, die sich drehen

Wir sollten außerdem nachdenken, wie viel von etwas mit etwas anderem in Beziehung steht. Hier einige Beispiele:

* Ein Auto hat genau ein Lenkrad. Ein Lenkrad gehört genau zu einem Auto.
* Mein Auto hat vier Räder montiert. Jedes Rad ist genau an einem Auto montiert.
* Eine Person kann mehrere Autos besitzen, aber ein Auto hat genau einen Besitzer.


> Wir fassen direkte Beziehungen zwischen Objekttypen hier vereinfacht zusammen. Wenn Du mehr über direkte Beziehungen wissen möchtest, kannst Du Dir die Unterschiede zwischen Assoziation (kennt), Aggregation (ist Teil von), und Komposition (existiert nicht ohne) anschauen.


### Spezialisierung

Es gibt natürlich nicht nur eine Art von Auto. In gewisser Weise ist PKW (Personenkraftwagen = normales Auto) bereits eine Spezialform des Kraftwagens. Eine andere Spezialisierung ist ein LKW (Lastkraftwagen). Wir könnten also folgende Spezialisierungen als Beispiele notieren:

```
+- Kraftwagen
+--- Personenkraftwagen
+------ Van
+------ Geländewagen
+------ Sportwagen
+--- Lastkraftwagen
+------ Kleintransporter
+------ Kipplaster
```

Im Allgemeinen hat ein Kraftwagen natürlich Räder, Sitze und so weiter. Es wäre also sinnvoll eine Klasse Kraftwagen zu definieren und alle anderen Klassen auf dieser Klasse basieren zu lassen.


* Kraftwagen

|Eigenschaft|Typ|Standardwert|
|---|---|---|
|Modell|String|?|
|Anz. Sitze|Zahl|?|
|Anz. Räder|Zahl|?|
|Schaltung|String|?|
|Anz. Gänge|Zahl|?|
|Kraftstoff|String|?|

Wir sagen auch: Die Klasse 'Auto' erbt die Eigenschaften der Klassen 'Kraftwagen':

* Auto

|Eigenschaft|Typ|Standardwert|
|---|---|---|
|Modell|String|?|
|Anz. Sitze|Zahl|5|
|Anz. Räder|Zahl|4|
|Schaltung|String|Manuell|
|Anz. Gänge|Zahl|5|
|Kraftstoff|String|Benzin|

Spezialisierungen können außerdem neue Eigenschaften bekommen. Wir könnten der Klasse 'LKW' (Lastkraftwagen) z.B. ein Ladevolumen hinzufügen:

* LKW

|Eigenschaft|Typ|Standardwert|
|---|---|---|
|Modell|String|?|
|Anz. Sitze|Zahl|3|
|Anz. Räder|Zahl|4|
|Schaltung|String|?|
|Anz. Gänge|Zahl|?|
|Kraftstoff|String|Diesel|
|Ladevolumen|Zahl|?|

## Zusammenfassung

Klassen beschreiben Objekte. Objektklassen können Eigenschaften und Methoden (Funktion haben). Wir können außerdem die Beziehungen zwischen Objekten beschreiben.