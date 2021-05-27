import random as rnd

with open("wörter.txt") as f:
  wörter = [w.strip().upper() for w in f]

wort = rnd.choice(wörter)
versuche = 8
gesucht = set(c for c in wort)
geraten = set()


while versuche > 0:
  print(f"Noch {versuche:>2} Versuche: ", end="")
  for buchstabe in wort:
    if buchstabe in geraten:
      print(f'{buchstabe} ', end="")
    else:
      print("_ ", end="")
  versuch = input("Ihr Buchstabe? ").upper()
  geraten.add(versuch)
  if versuch not in wort:
    versuche -= 1
  if gesucht.issubset(geraten): 
    break  
  
if versuche > 0:
  print(f"GEWONNEN! Das gesuchte Wort war {wort}")
else:
  print(f"VERLOREN! Das gesuchte Wort war {wort}")