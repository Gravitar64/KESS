import random

anz_sechser = 0
for i in range(100):
  würfel = random.randint(1,6)
  if würfel == 6:
    anz_sechser += 1
print(anz_sechser)    