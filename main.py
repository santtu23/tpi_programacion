from fcs import *

#Carga del csv

paises = cargar_csv("paises.csv")

# Si no hay csv o esta vacio
if not paises:
  paises = [
    {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "America"},
    {"nombre": "Japon", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
    {"nombre": "Brasil",    "poblacion": 213993437, "superficie": 8515767.0, "continente": "America"},
    {"nombre": "Alemania",  "poblacion": 83149300,  "superficie": 357022.0,  "continente": "Europa"},
  ]