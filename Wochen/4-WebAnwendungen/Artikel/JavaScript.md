# Einführung in Java Script

Wir können Dir hier leider keine zweite Programmiersprache beibringen, aber sobald Du die Grundlagen verstanden hast, ist es nicht mehr so schwer eine ähnliche Sprache zu lernen.

Java Script ist die Programmiersprache, die ein Browser (z.B., Firefox) versteht. Im Wesentlichen erklärt man dem Browser mit Hilfe eines JavaScript-Programms, wie er das HTML der Web-Seite manipulieren soll, wenn ein bestimmtes Ereignis eintritt. Beispielereignisse sind:

* Jemand hat einen Knopf (Button gedrückt)
* Es erfolgte eine Eingabe in ein Feld
* Die Seite wurde geöffnet

Man kann mit Java Script auch mit anderen HTTP-Diensten sprechen. Der übliche Ablauf ist:

1. Rufe über HTTP Daten von einem Server ab
2. Diese Daten werden z.B. als JSON ausgeliefert
3. Manipuliere das HTML der Web-Seite anhand der erhaltenen Daten

Ich verwende wenn möglich ein Rahmenwerk, welches bestimmte Aufgaben bereits vereinfacht. In unserem Beispiel-Code verwende ich `jQuery`.

In der Datei ‘web/index.html’ findet man z.B. folgenden Code-Block:

```
$.get(path, function(daten) {
               daten.forEach(p => {
                   var zeit = new Date(p.zeit * 1000).toLocaleString();
                   var text = p.text;
                   var benutzer = p.benutzer;
                   console.log(p.text);
                  
                   var post_html = post_template.replace("${user}", "@" + benutzer + " " + zeit);
                   var post_html = post_html.replace("${text}", text);
                  
                   $("#posts").append(post_html);
               });
           }) 
```

