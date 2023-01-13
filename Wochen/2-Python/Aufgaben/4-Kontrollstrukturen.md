# 4.) Kontrollstrukturen

## Anforderungen

Stell Dir vor, jemand fragt Dich: "Kannst Du mir ein Programm schreiben, dass es erlaubt, Nachrichten (Posts) einzugeben? Ich möchte Posts zu einer bestimmten Zeit eingeben können.” Diesen Sätzen entnehmen wir bereits die folgenden Anforderungen:

1. Es soll möglich sein Posts einzugeben
2. Die Zeit der Eingabe muss erfasst werden

Welche Daten müssen wir also erfassen?

* Den Text des Posts
* Die Zeit der Eingabe des Posts

Welche Aktionen müssen wir umsetzen?

* Post erstellen

## Aufgabe

Schreibe ein Kommandozeilenprogramm, das die Anforderungen oben erfüllt. Die folgenden Kontrollstrukturen sollen in Deinem Programm vorkommen:

* `if ... elif ... else`
* `while`

Öffne die Quellcodedatei `tclone.py`. Die Datei ist momentan ein “Lückentext”. Die folgenden Teilaufgaben helfen Dir die Lücken zu füllen:

### a.) Schleifen

Solange die Aktion nicht 'Q' (Beenden) ist, soll das Programm wiederholt werden

### b.) Bedingungen

Wenn die Eingaben 'P' (Post erstellen), 'R' (Posts lesen), oder 'Q' (Beenden) sind, dann sollen die entsprechenden Codeblöcke ausgeführt werden. Falls eine ungültige Eingabe getätigt wird, dann soll die Ausgabe "Aktion ist nicht erlaubt" erfolgen.


## Test

Teste Dein Programm indem Du die folgenden Schritte durchgeführst:

1. Führe das Programm in VSCode aus!
2. Gib 'Bla' ein und bestätige mit der Eingabetaste!
3. Die Ausgabe sollte "Aktion ist nicht erlaubt" sein.
2. Gib 'P' (Groß geschrieben!) ein und bestätige mit der Eingabetaste!
3. Gib einen Text ein!
4. Die Ausgabe sollte die Zeit der Eingabe gefolgt vom Post-Text sein.