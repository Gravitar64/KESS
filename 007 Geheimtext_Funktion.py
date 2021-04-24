def caesar_chiffre(text,schlüssel):
  neuer_text = ""
  for buchstabe in text:
    neuer_text += chr(ord(buchstabe)+schlüssel)
  return neuer_text  

nachricht = input("Bitte Text eingeben: ")
schlüssel = input("Bitte Schlüssel eingeben (- für Entschlüsselung): ")
print(caesar_chiffre(nachricht, int(schlüssel)))
