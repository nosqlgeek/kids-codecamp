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