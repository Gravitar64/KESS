#Aufgabe:
#Ein Theater hat durchschnittlich 200 Besucher, bei einem Eintrittspreis von 8,50€
#Wenn man den Eintrittspreis um 0,50€ senkt, erhöht sich die Besucherzahl um 20
#Bei welchem Eintrittspreis erreicht man das Maximum an Einnahmen?

besucher = 200
eintrittspreis = 8.50

while eintrittspreis > 0:
  einnahmen = besucher * eintrittspreis
  print(besucher, eintrittspreis, einnahmen)
  eintrittspreis -= 0.50
  besucher += 20