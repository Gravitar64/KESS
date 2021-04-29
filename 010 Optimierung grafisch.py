from matplotlib import pyplot as plt 

#Aufgabe:
#Ein Theater hat durchschnittlich 200 Besucher, bei einem Eintrittspreis von 8,50€
#Wenn man den Eintrittspreis um 0,50€ senkt, erhöht sich die Besucherzahl um 20
#Bei welchem Eintrittspreis erreicht man das Maximum an Einnahmen?

besucher = 200
eintrittspreis = 8.50
erg_x, erg_y = [], []

while eintrittspreis > 0:
  einnahmen = besucher * eintrittspreis
  erg_x.append(eintrittspreis)
  erg_y.append(einnahmen)
  eintrittspreis -= 0.50
  besucher += 20

plt.scatter(erg_x, erg_y)
plt.show()


