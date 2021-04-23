import random as rnd 

lostrommel = list(range(1,50))
meine_lottozahlen = [1, 12, 49, 32, 16, 48]
jahre = 1

for n in range(jahre * 52 * 2):
  anz_richtige = 0
  rnd.shuffle(lostrommel)
  ziehung = lostrommel[:6]
  for zahl in ziehung:
    if zahl in meine_lottozahlen:
      anz_richtige = anz_richtige + 1
  if anz_richtige > 4:
    print(f"{anz_richtige} Richtige nach {n} Ziehungen (= {n//52//2} Jahre)")
    print(meine_lottozahlen, ziehung)
    print()



