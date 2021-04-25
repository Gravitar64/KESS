def print_feld(feld):
  for i, inhalt in enumerate(feld):
    print(f' {inhalt} |',end='')
    if (i+1) % 3 == 0: 
      print()
      print('------------')

feld = [" "]*9
spieler = True

while True:
  print_feld(feld)
  zug = input(f"Dein Zug Spieler {'X' if spieler else 'O'} (0-8): ")
  feld[int(zug)] = "X" if spieler else "O"
  spieler = not spieler


