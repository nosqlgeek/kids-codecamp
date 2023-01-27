# Client und Server

Bisher haben wir unsere Anwendung nur lokal laufen lassen. In der Realität bestehen Anwendungen aber oft aus mehreren Diensten (Services). Diese Dienste werden von sogenannten Servern bereitgestellt. Ein Client kann über das Netzwerk (z.B., das Internet) mit dem Server kommunizieren, wenn beide das gleiche Protokoll beherrschen.

```
+---------+           +---------+
| Client  |   <--->   |  Server |
+---------+           +---------+
```


## Was ist ein Protokoll?
Stell Dir vor, Du gehst in ein Restaurant, um etwas zu essen. In diesem Beispiel bist Du der Client und der Kellner ist der Server. Das Protokoll ist in etwa:

1. Du und der Kellner müsst Euch gegenseitig sprachlich verstehen.
2. Du setzt Dich an den Tisch.
3. Der Kellner kommt zu Dir und reicht Dir eine Speisekarte.
4. Du wirst gefragt, ob Du etwas trinken möchtest
5. Das Getränk wird gebracht.
6. Der Kellner fragt Dich, ob Du etwas essen möchtest.
7. Das Essen wird zubereitet und anschließend an Deinen Tisch gebracht.
8. Du zahlst, bevor Du gehst.

Genauso ist das auch bei Computern. Dabei gibt es verschiedene Ebenen der Kommunikation, aber wir wollen das hier nicht allzu kompliziert darstellen:

1. Der Server hat eine Adresse (z.B. 192.168.0.3).
2. Der Server lauscht auf einem Port (z.B. 80). Einen Port kannst Du Dir wie eine Tür vorstellen. Ist die Tür geöffnet, können Daten übertragen werden.
3. Der Client kann eine Verbindung zum Server unter der Adresse und dem Port aufbauen
4. Der Client kann Daten über diese Verbindung zum Server senden.
5. Der Server verarbeitet die Daten und antwortet dem Client.
6. Der Client wird die Antwort verarbeiten und dann entscheiden, wie es weiter geht.

## Welche Protokolle verwendet man?

Die meisten Dienste verwenden heutzutage TCP/IP (Transmission Control Protocol / Internet Protocol) als das grundlegende Kommunikationsprotokoll. Ein Web-Server nutzt zusätzlich das HTTP (Hyper Text Transfer Protocol). Das ist ein Protokoll, das beschreibt, welche Kommandos zur Datenübertragung verwendet werden. Es beschreibt Methoden wie PUT (Aktualisieren oder Erstellen), POST (Erstellen), GET (Abrufen) und DEL (Löschen). Im nächsten Schritt müssen die übertragenen Daten auch einem Protokoll folgen, also vom Server verstanden werden. Zur Darstellung von Inhalten wird oft HTML (Hyper Text Markup Language) und bei strukturierten Daten JSON (Java Script Object Notation) verwendet.

Hier ein Web-Server-Beispiel:

```
+---------+           +-------------+
| Browser |   <--->   |  Web-Server |
+---------+   TCP/IP  +-------------+
              HTTP
```


## Beispiel 1 - 3-Schichten Architektur

Die typische 3-Schichten-Architektur besteht aus:

1. Einer Web-Oberfläche
2. Dem Dienst der die Geschäftslogik beinhaltet
3. Der Datenbank in der die Daten der Anwendung gespeichert werden

```
+-------------+
|   Web-Anw.  |
|  im Browser |
+-------------+
     ^
     |
     v
+-------------+
|   Dienst    |
|im Web-Server|
+-------------+
     ^
     |
     v
+-------------+
|  Datenbank  |
|             |
+-------------+
```

Unsere Python-Beispielanwendung verwendet:

1. HTML und JavaScript für die Web-Anwendung
2. Redis Stack als NoSQL Datenbank
3. Flask zur Realisierung des Web-Servers


## Beispiel 2 - Microservices Architektur

Hier unten siehst Du einmal wie komplex eine Anwendung hinter den Kulissen sein kann:

![Netflix Microservices Architektur](./Bilder/netflix.png)





