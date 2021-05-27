#Mengenlehre in Python (oder, der Datentyp Set)

#Ein Set ist eine Menge
set1 = {1,2,3,4,5}
print(set1)

#jedes Element kann nur 1x im Set vorkommen
m1 = [1,2,3,4,5,1,2]
m2 = {1,2,3,4,5,1,2}
print(m1)
print(m2)

#die Elemente eines Sets können int, float, str, tuple sein
wort = 'hallo'
set3 = {wort,'Andreas', 'Selma', 'Christian', 'hallo'}
print(set3)

#oder auch die Buchstaben eines wortes
set4 = set()
for b in wort:
  set4.add(b)
print(set4)

set5 = set()
while True:
  a = input('Ihr Buchstabe? ')
  if a:
    set5.add(a)
  else:
    break
print(set5)

print(f'Ist das Set der Buchstaben identisch zum Set der Eingabe? {set5 == set4}')
print(f'Ist das Set der Buchstaben eine Teilmenge des Sets der Eingabe? {set4.issubset(set5)}')
print(f'Welche Buchstaben waren falsch? {set5 - set4}')

