from fcs import *

#Carga del csv

ARCHIVO_CSV ="paises.csv"
paises =[]
paises = cargar_csv(ARCHIVO_CSV, paises)

# Si no hay csv o esta vacio
if not paises:
    paises = [
    {"nombre": "Argentina",      "poblacion": 45376763,    "superficie": 2780400.0,  "continente": "America"},
    {"nombre": "Japon",          "poblacion": 125800000,   "superficie": 377975.0,   "continente": "Asia"},
    {"nombre": "Brasil",         "poblacion": 213993437,   "superficie": 8515767.0,  "continente": "America"},
    {"nombre": "Alemania",       "poblacion": 83149300,    "superficie": 357022.0,   "continente": "Europa"},
    {"nombre": "Mexico",         "poblacion": 126014024,   "superficie": 1964375.0,  "continente": "America"},
    {"nombre": "Francia",        "poblacion": 67897000,    "superficie": 551695.0,   "continente": "Europa"},
    {"nombre": "Nigeria",        "poblacion": 223804632,   "superficie": 923768.0,   "continente": "Africa"},
    {"nombre": "China",          "poblacion": 1412600000,  "superficie": 9596960.0,  "continente": "Asia"},
    {"nombre": "Australia",      "poblacion": 26473055,    "superficie": 7692024.0,  "continente": "Oceania"},
    {"nombre": "Canada",         "poblacion": 38781292,    "superficie": 9984670.0,  "continente": "America"},
    {"nombre": "Egipto",         "poblacion": 105914499,   "superficie": 1002450.0,  "continente": "Africa"},
    {"nombre": "India",          "poblacion": 1428627663,  "superficie": 3287263.0,  "continente": "Asia"},
    {"nombre": "Italia",         "poblacion": 58940000,    "superficie": 301340.0,   "continente": "Europa"},
    {"nombre": "Nueva Zelanda",  "poblacion": 5123000,     "superficie": 270467.0,   "continente": "Oceania"},
]

#Menu principal

while True:
    print(f"""
{NEGRITA}{CIAN}=======Menu principal======{RESET}
{CIAN}1.{RESET}Agregar pais
{CIAN}2.{RESET}Listar paises
{CIAN}3.{RESET}Buscar pais
{CIAN}4.{RESET}Modificar pais
{CIAN}5.{RESET}Eliminar pais
{CIAN}6.{RESET}Filtrar pais
{CIAN}7.{RESET}Ordenar paises
{CIAN}8.{RESET}Estadisticas
{ROJO}9.{RESET}Salir
{NEGRITA}{CIAN}==============================={RESET}""")

    opcion = input("Ingrese una opcion: ").strip()

    match opcion:
        case "1":
            paises = agregar_pais(paises) or paises
        case "2":
            listar_paises(paises) or paises
        case "3":
            buscar_pais(paises) or paises
        case "4":
            paises = modificar_pais(paises) or paises
        case "5":
            paises = eliminar_pais(paises) or paises
        case "6":
            filtrar_paises(paises) or paises
        case "7":
            ordena_paises(paises) or paises
        case "8":
            mostrar_estadisticas(paises) or paises
        case "9":
            print(f"{VERDE}Saliendo del programa...{RESET}")
            guardar_csv(paises, ARCHIVO_CSV)
            break
        case _:
            print(f"{ROJO}Opcion no valida{RESET}")