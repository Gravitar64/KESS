#Aufgabe:
#Ein Theater hat durchschnittlich 200 Besucher, bei einem Eintrittspreis von 8,50€
#Wenn man den Eintrittspreis um 0,50€ senkt, erhöht sich die Besucherzahl um 20
#Bei welchem Eintrittspreis erreicht man das Maximum an Einnahmen?

besucher = 200
eintrittspreis = 8.50
max_einnahmen = besucher * eintrittspreis

while eintrittspreis > 0:
  eintrittspreis -= 0.50
  besucher += 20
  einnahmen = besucher * eintrittspreis
  if einnahmen > max_einnahmen:
    max_einnahmen = einnahmen
    best_preis = eintrittspreis
    best_besucher = besucher
print(f'Bei {best_besucher} Besucher mit {best_preis} Eintrittspreis werden {max_einnahmen} erziehlt')