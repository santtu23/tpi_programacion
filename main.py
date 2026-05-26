from fcs import *

#Carga del csv

ARCHIVO_CSV ="paises.csv"
paises = cargar_csv(ARCHIVO_CSV)

# Si no hay csv o esta vacio
if not paises:
    paises = [
        {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "America"},
        {"nombre": "Japon", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
        {"nombre": "Brasil",    "poblacion": 213993437, "superficie": 8515767.0, "continente": "America"},
        {"nombre": "Alemania",  "poblacion": 83149300,  "superficie": 357022.0,  "continente": "Europa"},
]

guardar_csv(paises, ARCHIVO_CSV)

#Menu principal

while True:
    print("""\n=======Menu principal======
1.Agregar pais
2.Listar paises
3.Buscar pais
4.Modificar pais
5.Eliminar pais
6.Filtar pais
7.Ordenar paises
8.Estadisticas
9.Salir
===============================""")

    opcion = input("Ingrese una opcion: ").strip()

    match opcion:
        case "1":
            paises = agregar_pais(paises)
        case "2":
            listar_paises(paises)
        case "3":
            buscar_pais(paises)
        case "4":
            paises = modificar_pais(paises)
        case "5":
            paises = eliminar_pais(paises)
        case "6":
            filtrar_paises(paises)
        case "7":
            ordena_paises(paises)
        case "8":
            mostrar_estadisticas(paises)
        case "9":
            print("Saliendo del programa")
            guardar_csv(paises, ARCHIVO_CSV)
            break
        case _:
            print("Opcion no valida")