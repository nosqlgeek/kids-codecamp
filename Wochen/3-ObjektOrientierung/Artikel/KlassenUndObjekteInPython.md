# Klassen und Objekte in Python

## Klassen

Eine Klasse wird in Python wie folgt beschrieben:

```
class Kraftwagen:
  def __init__(self, marke, modell, anz_sitze, anz_raeder, schaltung, anz_gaenge, kraftstoff):
     self.marke = marke
     self.modell = modell
     self.anz_sitze = anz_sitze
     self.anz_raeder = anz_raeder
     self.schaltung = schaltung
     self.anz_gaenge = anz_gaenge
     self.kraftstoff = kraftstoff
 
  def lenken(self, richtung):
     pass



k = Kraftwagen('Citroen', 'C4 Spacetourer', 7, 4, 'Manuell', 6, 'Benzin')
print(k.__dict__)
```

Wir leiten die Definition also mit `class` (Klasse) ein. Die Funktion `__init__` ist eine spezielle Funktion (oder besser: Methode). Sie ist der sogenannte Constructor (Konstrukteur). Der Constructor erlaubt uns, Objekte der Klasse mit bestimmten Eigenschaften zu erstellen. Er wird verwendet, um die initialen (anfänglichen) Eigenschaften eines Objekts zu setzen.

> Es gibt auch noch den Destructor `__del__`. Der Destructor wird ausgeführt, wenn ein Objekt nicht länger benötigt, also weggeräumt wird.

Die Funktion `lenken` ist eine Methode der Klasse. Man kann das daran erkennen, dass sie als ersten Eingabewert den Wert `self` hat. `self` bezieht sich auf das Objekt das anhand der Klasse erstellt wurde selbst. Das heißt, wenn ich auf Eigenschaften eines Objekts innerhalb der Klasse zugreifen möchte, dann kan ich das über `self` tun (z.B. `self.marke`)

Ein solches Objekt wird dann mit `<Klassenname>(<Initiale Eigenschaften>)` erstellt. Jedes Objekt hat automatisch die Eigenschaft `__dict__`. Diese eingebaute Eigenschaft erlaubt uns die anderen Eigenschaften eines Objekts einfacher zu untersuchen.

## Direkte Beziehungen

Es gibt mehrere Möglichkeiten direkte Beziehungen umzusetzen. Letztendlich wird dabei eine Klasse von einer anderen als Eigenschaft verwendet.

```
class Rad:
  def __init__(self, druck):
     self.druck = druck

class Kraftwagen:
  def __init__(self, marke, modell, anz_sitze, raeder, schaltung, anz_gaenge, kraftstoff):
     self.marke = marke
     self.modell = modell
     self.anz_sitze = anz_sitze
    
     # Verweis auf eine Liste von Rädern
     self.raeder = raeder
     # Die Anzahl leitet sich von der Länge der Liste ab
     self.anz_raeder = len(raeder)
    
     self.schaltung = schaltung
     self.anz_gaenge = anz_gaenge
     self.kraftstoff = kraftstoff
 
  def lenken(self, richtung):
     pass

# Räder mit Luftdruck
raeder = [Rad(2.5), Rad(2.4), Rad(2.3), Rad(2.2)]
k = Kraftwagen('Citroen', 'C4 Spacetourer', 7, raeder, 'Manuell', 6, 'Benzin')
r = k.raeder
print(k.__dict__)
print(r[0].__dict__)
```

## Spezialisierung / Vererbung

Wir eine Klasse von einer anderen Klasse wie folgt ableiten:

```
class Kraftwagen:
  def __init__(self, marke, modell, anz_sitze, anz_raeder, schaltung, anz_gaenge, kraftstoff):
     self.marke = marke
     self.modell = modell
     self.anz_sitze = anz_sitze
     self.anz_raeder = anz_raeder
     self.schaltung = schaltung
     self.anz_gaenge = anz_gaenge
     self.kraftstoff = kraftstoff
 
  def lenken(self, richtung):
     pass

class PKW(Kraftwagen):
  def __init__(self, marke, modell, schaltung, dach_form, anz_raeder = 4, anz_sitze = 5, anz_gaenge = 5, kraftstoff = 'Benzin'):
     super().__init__(marke, modell, anz_sitze, anz_raeder, schaltung, anz_gaenge, kraftstoff)
     self.dach_form = dach_form

pkw = PKW('Citroen', 'C4 Spacetourer', 'Manuell', 'Panorama', anz_sitze = 7, anz_gaenge = 6 )
print(pkw.__dict__)
```

Die eingebaute Funktion `super` ermittelt die Elternklasse. Das Erlaubt uns den Constructor der Elternklasse aufzurufen. Wir verwenden an dieser Stelle außerdem Standardwerte. Das sind Werte, die bereits im Constructor gesetzt werden. Falls nicht anders angegeben, hat ein PKW also 4 Räder, 5 Sitze, und tankt Benzin.