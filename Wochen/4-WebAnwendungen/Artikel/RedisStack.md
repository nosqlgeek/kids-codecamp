# Redis Stack

Ein Datenbanksystem stellt den Dienst bereit Daten dauerhaft zu speichern. Kommuniziert wird auch über TCP/IP, allerdings werden andere Protokolle als HTTP zwischen Datenbank-Clients und Datenbankservern verwendet.

Redis ist ein sehr beliebtes NoSQL Datenbanksystem. Daten werden unter einem Schlüssel (eindeutiges Kriterium) abgelegt und zugegriffen.

Redis Stack erweitert die Datenstrukturen, die von Redis unterstützt werden, um zusätzliche Datenstrukturen und Funktionen. Diese sind zum Beispiel:

* Indizieren und abfragen anhand eines Datenbankschemas
* Volltextsuche
* Verwalten von JSON-Dokumenten
* Umgang mit Zeitreihen und Graphen (z.B. Netzwerke)


## Speichern von Daten

Redis Stack ist somit ein sogenanntes Multi-Modell Datenbanksystem und kann Daten in verschiedenen komplexen Datentypen speichern (z.B., Listen, Mengen, Abbildungen/Dictionaries/Hashes, oder JSON).

Wir verwenden für unsere Daten Hashes. Ein Hash ist nichts anderes als eine Abbildung (siehe Woche 2). Es ist also einfach eine Python-Abbildung (Dictionary) zu Redis zu senden. Die Client-Bibliothek wandelt diese Python-Abbildung dann zu einem Redis-Hash. Die Funktion dafür heißt `hset` (Setze Hash).

```
def speichern(self):
       schluessel = self.schluessel_in_db()
       print('Wird unter Schlüssel {} gespeichert.'.format(schluessel))
       print('daten = {}'.format(self.daten()))
       return datenbank.verbinden().hset(schluessel, mapping=self.daten())
```

## Abrufen von Daten

Zum Abrufen verwenden wir einfach die Funktion `hget` (Hole Eigenschaft des Hashes) oder `hgetall` (Hole den gesamten Hash):

```
   def abrufen(self):
       schluessel = self.schluessel_in_db()
       print('Rufe Daten mit Schlüssel {} ab.'.format(schluessel))
       return datenbank.verbinden().hgetall(schluessel)
```

## Abfragen von Daten

Es gibt mehrere Arten, wie man Daten in Redis abfragen kann. Der eleganteste Weg ist die Verwendung der Erweiterung 'RediSearch' (bereits in Redis Stack enthalten).

Dazu muss vorab ein Index erstellt werden, der beschreibt, wie die Daten aussehen. Ein Index erlaubt dabei das leichtere Auffinden von Daten. Statt also alle Daten durchzugehen, wird der Index verwendet, um die Daten schneller zu finden. Ein gutes Beispiel ist der Index in einem Lehrbuch. Wenn Du weißt, mit welchem Anfangsbuchstaben ein Thema anfängt, kannst Du im Index nach dem Thema schauen und die Buchseite schneller finden, ohne das gesamte Buch durchblättern zu  müssen. Das folgende Beispiel zeigt die Erstellung der drei Indizes ‘index:post’, ‘index:kommentar’, und ‘index:nutzer’.

```
'''
Erstelle einen Datenbankindex: Ein Index wird benötigt, um Daten in der Datenbank effizienter (schneller) zu finden.
'''
def index_erstellen(typ, schema):
   erfolg=False
  
   # Das hier ist neu für Dich. Dabei handelt es sich um ein Beispiel der Fehlerhandhabung:
   # Versuche etwas auszuführen und handhabe den Fehler, wenn es nicht klappt.
   try:
       # Wir verwenden HASHes (Abbildungen/Dictionaries) zum abspeichern der Daten
       index_def = IndexDefinition(index_type=IndexType.HASH, prefix=['{}:'.format(typ)])
       index_name = 'index:{}'.format(typ)
       verbindung.ft(index_name).create_index(schema, definition=index_def)
       erfolg=True
   except Exception as err:
           print('WARNUNG: Der Suchindex für den Typ {} kann nicht erstellt werden. - {}'.format(typ, err))

   return erfolg


'''
Die Datenbank will wissen was indiziert werden soll und welchen Datentyp die Eigenschaften haben
'''
def indizes_erstellen():
   post_schema = (TagField('benutzer'),TextField('text'), NumericField('zeit'))
   kommentar_schema = (TagField('benutzer'),TextField('text'), NumericField('zeit'), TagField('post'))
   nutzer_schema = (TagField('kurzname'), TextField('vorname'), TextField('nachname'), TagField('email'))
   index_erstellen('post', post_schema)
   index_erstellen('kommentar', kommentar_schema)
   index_erstellen('nutzer', nutzer_schema)
```

Das Abfragen funktioniert dann so:

```
def abfragen(typ, abfrage):
   r = verbinden()
   index_name = 'index:{}'.format(typ)   
   docs = r.ft(index_name).search(Query(abfrage)).docs
```

Nähere Informationen zur Redis und Redis Stack findest Du [hier](https://www.redis.io).