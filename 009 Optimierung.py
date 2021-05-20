# Aufgabe:
# Ein Theater hat durchschnittlich 200 Besucher, bei einem Eintrittspreis von 8,50€
# Wenn man den Eintrittspreis um 0,50€ senkt, erhöht sich die Besucherzahl um 20
# Bei welchem Eintrittspreis erreicht man das Maximum an Einnahmen?

besucher = 200
ticket = 8.50
for lauf in range(17):
  besucher = besucher + 20
  ticket = ticket -0.5
  einnahmen = besucher * ticket
  print(besucher, ticket, einnahmen)
