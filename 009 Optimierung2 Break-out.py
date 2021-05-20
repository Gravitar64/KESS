# Aufgabe:
# Wir haben einen 18cm langen Draht, den wir zu einem Rechteck biegen können.
# Bei welchen Maßen (Breite x Höhe) haben wir den größten Flacheninhalt?

b = 9
h = 0

while b > 0:
  f = b * h
  u = b*2 + h*2
  print(f'{b} cm x {h} cm = {f} cm²')
  b -= 0.5
  h += 0.5
