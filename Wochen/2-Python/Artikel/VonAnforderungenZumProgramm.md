# Von Anforderungen zum Programm

## Anforderungen

Während der Übungsaufgabe hast du bereits etwas Wichtiges gelernt. Eine Software-Anwendung sollte immer die Anforderungen (Wünsche) der Benutzer erfüllen. Es ist also ganz wichtig, dass man sich vorab mit Benutzern unterhält und genau aufschreibt, was benötigt wird. Am besten macht man das, indem man ganze Sätze aufschreibt. Hier ein Beispiel:

* Als ... möchte ich in der Lage sein ... mit Hilfe von ... das folgende zu tun ... damit ... .

Einen solchen Satz, bzw. Paragraphen kann man auch Benutzergeschichte (User Story) nennen.

Aus solchen Anforderungen (bzw. Geschichten) kann man folgendes herauslesen:

* Wer hat die Anforderung?
* Was soll erreicht werden?
* Warum soll es umgesetzt werden?
* Welche Funktionen werden benötigt?
* Welche Dinge stehen zur Verfügung oder müssen bereitgestellt werden?
* Wie dringlich ist die Anforderung (z.B. `ich möchte` vs. `es muss`)


## Analyse

Es gibt verschiedene Analyseverfahren, um aus Anforderungen Anwendungen zu erstellen. Ich finde es am einfachsten, Dinge (Objekte) und deren Funktionen aus den Anforderungen herauszulesen.


## 1.) Objekte

In unserer Übungsaufgabe haben wir das schon begonnen. Wenn wir über weiteren Anforderungen unserer TClone-Anwendung nachdenken, dann können wir die folgenden Objekttypen identifizieren:

* Benutzer
* Posts
* Kommentare
* Besucherstatistiken


## 2.) Objektbeziehungen

Wir wollen außerdem wissen wir die Objekte zueinander in Beziehung stehen:

* Ein Benutzer erstellt Posts.
* Ein Benutzer kann anderen Nutzern folgen.
* Ein Post kann mehrere Kommentare haben.
* Statistiken können sowohl je Post oder je Benutzer erfasst werden.

Normalerweise überlege ich hier auch schon wieviel mit wieviel in Beziehung steht. Wie viele Posts hat ein Nutzer (viele, wenig, genau einen)?

## 3.) Objekteigenschaften

Im nächsten Schritt denken wir darüber nach, welche Eigenschaften die Objekte haben sollen. Hier einige Beispiele:

* Benutzer haben z.B. einen Namen und eine E-Mail-Addresse
* Posts haben eine Text und eine Zeit
* Kommentare haben auch einen Text und eine Zeit
* Statistiken haben Zählwerte

Es macht auch Sinn sich zu überlegen, welche Eigenschaften ein solches Objekt eigentlich einmalig machen. Es gibt z.B. viele Leute mit dem gleichen Namen, aber nur eine Person hat genau diese E-Mail-Addresse.

## 4.) Funktionen

Was sollen die Objekte tun können? Hier wieder Beispiele:

* Ein Benutzer meldet sich an
* Ein Post wird kommentiert
* Ein Kommentar wird erstellt

Das hier grob umrissene Verfahren nennt man auch ‘Objektorientierte Analyse’. Wir schauen uns das Ganze nächste Woche nochmal genauer an, wenn wir über objektorientierte Programmierung sprechen.