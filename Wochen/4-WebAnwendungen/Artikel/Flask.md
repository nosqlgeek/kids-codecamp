# Web-Server mit Flask

Flask ist ein Rahmenwerk, das es Dir erlaubt, Python-basierte Web-Dienste zu erstellen. Dabei stellt eine laufende Flask-Anwendung selbst einen Web-Server dar. Der Code der Anwendung bestimmt, welche Inhalte dieser Web-Server bereitstellt. Das können einfach statische HTML-Seiten sein, oder eben auch die reinen Daten selbst als JSON.

## Flask und HTTP

Da die Flask-Anwendung HTTP spricht, kannst Du sie ganz einfach mit einem Browser ansprechen. Browser arbeiten mit URL-s (Uniform Resource Locator). Hier einige Beispiele:

* https://www.google.de
* https://www.nosqlgeeks.com/de/

Eine solche URL hat den folgenden Aufbau:

1. Protokoll: z.B. `https`
2. Domäne oder Adresse: z.B. `www.nosqlgeeks.com`
3. Pfad: z.B. `/de`

## Pfade und Routen

Die Ausführung von Funktionen kann in Flask an bestimmte Pfade gebunden werden. Das nennt man dann eine Route. Die folgende Route wird ausgeführt, wenn jemand den Wurzelpfad `/` öffnet. Der Browser würde dann das HTML `<p>Hello, World!</p>` anzeigen.

```
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   return "<p>Hello, World!</p>"
```

## Statische Inhalte

Eine Flask-Anwendung kann auch einfach Inhalte von Dateien eines Unterordners über HTTP bereitstellen. Hier ein Beispiel:

```
@app.route('/<path:path>', methods=['GET'])
def web(path):
   return send_from_directory('web', path)
```
Die Funktion `web` gibt Inhalte innerhalb des Unterordners `web` zurück, wobei der Pfad der Datei als Parameter übergeben wird.