meine_lottozahlen = [1,12,15,19,23]
print(meine_lottozahlen)

for zahl in meine_lottozahlen:
  print(zahl)

summe = 0
for zahl in meine_lottozahlen:
  print(zahl)
  summe = summe + zahl

print(summe)

print(sum(meine_lottozahlen))
print(max(meine_lottozahlen))
print(min(meine_lottozahlen))

meine_lottozahlen.append(13)
print(meine_lottozahlen)

print(sorted(meine_lottozahlen))