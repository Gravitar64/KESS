import random as rnd

with open("wörter.txt") as f:
  wörter = [wort.strip().upper() for wort in f]  

gesuchtes_wort = rnd.choice(wörter)
gesuchte_buchstaben = set(buchstabe for buchstabe in gesuchtes_wort)
geratene_buchstaben = set(gesuchtes_wort[0])
anz_versuche = 8

while anz_versuche > 0:
  print(f'Noch {anz_versuche} Versuche! ',end='')
  for buchstabe in gesuchtes_wort:
    if buchstabe in geratene_buchstaben:
      print(f'{buchstabe} ',end='')
    else:
      print('_ ',end='')  
  geraten = input('Welcher Buchstabe? ').upper()
  geratene_buchstaben.add(geraten)
  if geraten not in gesuchte_buchstaben or geraten in 'AEIOU':
    anz_versuche -= 1
  if gesuchte_buchstaben.issubset(geratene_buchstaben):
    break

if anz_versuche > 0:
  print(f'GEWONNEN!')
else:
  print(f'VERLOREN! Das gesuchte Wort war {gesuchtes_wort}')      





