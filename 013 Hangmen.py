import random as rnd

with open("wörter.txt") as f:
  wörter = []
  for wort in f:
    wort = wort.strip()
    wort = wort.upper()
    wörter.append(wort)

wort = rnd.choice(wörter)
versuche = 8
gesuchte_buchstaben = set(buchstabe for buchstabe in wort)
geratene_buchstaben = set()


while versuche > 0:
  print(f"Noch {versuche:>2} Versuche: ", end="")
  for buchstabe in wort:
    if buchstabe in geratene_buchstaben:
      print(f'{buchstabe} ', end="")
    else:
      print("_ ", end="")
  versuch = input("Ihr Buchstabe? ").upper()
  geratene_buchstaben.add(versuch)
  if versuch not in gesuchte_buchstaben:
    versuche -= 1
  if gesuchte_buchstaben.issubset(geratene_buchstaben): 
    break  
  
if versuche > 0:
  print(f"GEWONNEN! Das gesuchte Wort war {wort}")
else:
  print(f"VERLOREN! Das gesuchte Wort war {wort}")