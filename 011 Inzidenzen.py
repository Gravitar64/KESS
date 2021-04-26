import requests

URL = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=GEN%20%3D%20'REGION%20HANNOVER'%20OR%20GEN%20%3D%20'FLENSBURG'%20OR%20GEN%20%3D%20'NORDFRIESLAND'%20OR%20GEN%20%3D%20'CELLE'&outFields=GEN,cases7_per_100k_txt,last_update&returnGeometry=false&outSR=&f=json"

inzidenzen = requests.get(URL).json()

for inzidenz in inzidenzen['features']:
  stand = inzidenz['attributes']['last_update']
  landkreis = inzidenz['attributes']['GEN']
  inz = inzidenz['attributes']['cases7_per_100k_txt']
  print(f'{stand} {landkreis} {inz}')