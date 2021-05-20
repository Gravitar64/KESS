import random as rnd 

geheimeZahl = rnd.randrange(1,101)

for n in range(1,11):
  versuch = int(input("Ihre Zahl? "))
  if versuch > geheimeZahl:
    print('zu groß!')
  elif versuch < geheimeZahl:
    print('zu klein!')
  else:
    print(f'Richtig nach nur {n} Versuchen!')
    break
  
