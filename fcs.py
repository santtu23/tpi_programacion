import csv
import os

def mostrar_pais(pais):
  return f"{pais['nombre']} - Poblacion: {pais['poblacion']} - Superficie: {pais['superficie']} - Continente: {pais['continente']}"

# CARGAR CSV #

def cargar_csv(ruta_archivo):
  paises = []

  if not os.path.exists(ruta_archivo):
    print(f"ERROR el archivo '{ruta_archivo}' no existe")
    return paises
  
  try:
    with open(ruta_archivo, newline="",encoding="utf-8") as archivo:
      lector = csv.DictReader(archivo)

      # VERIFICAMOS EL CSV

      columnas_requeridas = {"nombre", "poblacion", "superficie", "continente"}
      if not columnas_requeridas.issubset(set(lector.fieldnames or [])):
        print(f"ERROR el csv debe tener las columnas {columnas_requeridas}")
        return paises
      
      for numero_fila, fila in enumerate(lector, start=2):
        try:
          nombre = fila["nombre"].strip()
          continente = fila["continente"].strip()
          poblacion = int(fila["poblacion"].strip())
          superficie = float(fila["superficie"].strip())

          if not nombre or not continente:
            print(f"Aviso fila {numero_fila} ignorada: campos vacios")
            continue
          if poblacion < 0 or superficie < 0:
            print(f"Aviso fila{numero_fila} ignorada: valores negativos")
            continue

          paises.append({
              "nombre":     nombre.capitalize(),
              "poblacion":  poblacion,
              "superficie": superficie,
              "continente": continente.capitalize()
          })

        except ValueError:
          print(f"Aviso fila {numero_fila} ignorada: poblacion o superficie incoreccta")
  
  except Exception as e:
    print(f"ERROR no se pudo leer el archivo {e}")

  print(f"{len(paises)} paises cargados correctamente '{ruta_archivo}'")
  return paises

# ---------

def validar_texto(mensaje_1, mensaje_2=None):
    while True:
      try:
        texto = input(mensaje_1).strip()
        # FIX: se permite espacio para nombres como "Nueva Zelanda"
        if texto.replace(" ", "").isalpha():
          if mensaje_2 != None:
            print(mensaje_2)
          return texto
        else:
          print("ERROR... El texto solo puede contener letras.")
      except Exception as e:
        print(f"Hubo un error inesperado... Error: {e}.")

def validar_entero(mensaje_1, mensaje_2=None):
  while True:
    try:
      numero = int(input(mensaje_1))
      if numero < 0:
        print("ERROR... No se permiten números negativos.")
        continue
      if mensaje_2 != None:
        print(mensaje_2)
      return numero
    except ValueError:
      print("ERROR... Por favor ingrese un número entero.")
    except Exception as e:
      print(f"Hubo un error inesperado... Error: {e}.")

def validar_flotante(mensaje_1, mensaje_2=None):
  while True:
    try:
      numero = float(input(mensaje_1))
      if numero < 0:
        print("ERROR... No se permiten números negativos.")
        continue
      if mensaje_2 != None:
        print(mensaje_2)
      return numero
    except ValueError:
      print("ERROR... Por favor ingrese un número válido.")
    except Exception as e:
      print(f"Hubo un error inesperado... Error: {e}.")

# FUNCION DE AGREGAR PAIS #

def agregar_pais(paises):
  nombre = validar_texto("Ingrese el nombre del pais: ")
  # FIX: se capitaliza nombre antes de comparar
  if nombre.capitalize() in [pais["nombre"] for pais in paises]:
    print("El pais ya existe.")
  else:
    print("Nombre del pais ingresado correctamente.")
    poblacion = validar_entero("Ingrese la poblacion del pais: ", "Poblacion del pais ingresada correctamente.")
    superficie = validar_flotante("Ingrese la superficie del pais: ", "Superficie del pais ingresada correctamente.")
    continente = validar_texto("Ingrese el continente del pais: ", "Continente del pais ingresado correctamente.")
    paises.append({
      "nombre": nombre.capitalize(),
      "poblacion": poblacion,
      "superficie": superficie,
      "continente": continente.capitalize()
    })
    print("Pais agregado correctamente.")
  
  return paises

# FUNCION DE LISTAR PAISES #

def listar_paises(paises):
  if not paises:
    print("No hay paises que mostrar.")  
  else:
    print()
    for pais in paises:
      print(mostrar_pais(pais))

# FUNCION DE BUSCAR PAIS #

def buscar_pais(paises):
  if not paises:
    print("No hay paises cargados.")
    return
  
  nombre_buscar = validar_texto("Ingrese el nombre (o parte del nombre): ")
  nombre_buscar = nombre_buscar.lower()

  resultados= [p for p in paises if nombre_buscar in p["nombre"].lower()]

  if resultados:
    print(f"\n{len(resultados)} resultados encontrados: ")
    for pais in resultados:
      print(mostrar_pais(pais))
  else:
    print("No se encontro pais con ese nombre")

# FUNCION DE MODIFICAR PAIS #

def modificar_pais(paises):
  if not paises:
    print("No hay paises cargados.")
  else:
    nombre_pais = validar_texto("Ingrese el pais a modificar: ")
    encontrado = False
    for pais in paises:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"Pais encontrado: {mostrar_pais(pais)}")
        encontrado = True
        while True:
          opcion = input(f""" -- ELIJA UNA OPCIÓN --
1. Modificar población de {nombre_pais}
2. Modificar superficie de {nombre_pais}
3. Salir
- """)
          match opcion:
            case "1":
              pais['poblacion'] = validar_entero(f'Ingrese la nueva poblacion para {nombre_pais}: ', "Población modificada exitosamente.")
              break
            case "2":
              pais['superficie'] = validar_flotante(f'Ingrese la nueva superficie para {nombre_pais}: ', "Superficie modificada exitosamente.")
              break
            case "3":
              print("Volviendo al menú principal...")
              break
            case _:
              print("ERROR... Comando inválido")
    if not encontrado:
      print("Pais no encontrado.")
    return paises

# FUNCION DE ELIMINAR PAIS #

def eliminar_pais(paises):
  if not paises:
    print("No hay paises cargados.")
  else:
    nombre_pais = validar_texto("Ingrese el pais a eliminar: ")
    encontrado = False
    # FIX: se itera sobre una copia para evitar problemas al eliminar
    for pais in paises[:]:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"Pais encontrado: {mostrar_pais(pais)}")
        encontrado = True
        paises.remove(pais)
        print("Pais eliminado")
    if not encontrado:
      print("Pais no encontrado.")
    return paises