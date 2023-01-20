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