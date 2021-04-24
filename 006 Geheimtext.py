nachricht = "wenn etwas Geheimes zu überbringen war, schrieb er in Zeichen, das heißt, er ordnete die Buchstaben so, dass kein Wort gelesen werden konnte: Um diese zu lesen, tauscht man den vierten Buchstaben, also D für A aus und ebenso mit den restlichen."


geheimtext = ""
for buchstabe in nachricht:
  zeichencode = ord(buchstabe)
  zeichencode += 4
  neues_zeichen = chr(zeichencode)
  geheimtext += neues_zeichen
print(geheimtext)

entschlüsselt = ""
for buchstabe in geheimtext:
  zeichencode = ord(buchstabe)
  zeichencode -= 4
  neues_zeichen = chr(zeichencode)
  entschlüsselt += neues_zeichen
print(entschlüsselt)  
