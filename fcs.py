import csv
import os

# COLORES ANSI #
ROJO     = "\033[91m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
CIAN     = "\033[96m"
BLANCO   = "\033[97m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"

def mostrar_pais(pais):
  return (f"{NEGRITA}{CIAN}{pais['nombre']}{RESET} - "
          f"Poblacion: {BLANCO}{pais['poblacion']}{RESET} - "
          f"Superficie: {BLANCO}{pais['superficie']}{RESET} - "
          f"Continente: {AMARILLO}{pais['continente']}{RESET}")

# CARGAR CSV #

def cargar_csv(ruta_archivo, paises):

  if not os.path.exists(ruta_archivo):
    print(f"{AMARILLO}Archivo '{ruta_archivo}' no encontrado, se usaran datos por defecto.{RESET}")
    return paises
  
  try:
    with open(ruta_archivo, newline="",encoding="utf-8") as archivo:
      lector = csv.DictReader(archivo)

      # VERIFICAMOS EL CSV

      columnas_requeridas = {"nombre", "poblacion", "superficie", "continente"}
      if not columnas_requeridas.issubset(set(lector.fieldnames or [])):
        print(f"{ROJO}ERROR el csv debe tener las columnas {columnas_requeridas}{RESET}")
        return paises
      
      for numero_fila, fila in enumerate(lector, start=2):
        try:
          nombre = fila["nombre"].strip()
          continente = fila["continente"].strip()
          poblacion = int(fila["poblacion"].strip())
          superficie = float(fila["superficie"].strip())

          if not nombre or not continente:
            print(f"{AMARILLO}Aviso fila {numero_fila} ignorada: campos vacios{RESET}")
            continue
          if poblacion < 0 or superficie < 0:
            print(f"{AMARILLO}Aviso fila{numero_fila} ignorada: valores negativos{RESET}")
            continue

          paises.append({
              "nombre":     nombre.capitalize(),
              "poblacion":  poblacion,
              "superficie": superficie,
              "continente": continente.capitalize()
          })

        except ValueError:
          print(f"{AMARILLO}Aviso fila {numero_fila} ignorada: poblacion o superficie incoreccta{RESET}")
  
  except Exception as e:
    print(f"{ROJO}ERROR no se pudo leer el archivo {e}{RESET}")

  print(f"{VERDE}{len(paises)} paises cargados correctamente '{ruta_archivo}'{RESET}")
  return paises

# GUARDAR CSV #

def guardar_csv(paises, ruta_archivo):
  try:
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
      campos = ["nombre", "poblacion", "superficie", "continente"]

      # Calculamos el ancho máximo de cada columna
      anchos = {campo: len(campo) for campo in campos}
      for pais in paises:
        anchos["nombre"]     = max(anchos["nombre"],     len(str(pais["nombre"])))
        anchos["poblacion"]  = max(anchos["poblacion"],  len(str(pais["poblacion"])))
        anchos["superficie"] = max(anchos["superficie"], len(str(pais["superficie"])))
        anchos["continente"] = max(anchos["continente"], len(str(pais["continente"])))

      def formatear_fila(nombre, poblacion, superficie, continente):
        return (
          f"{nombre:<{anchos['nombre']}} , "
          f"{poblacion:<{anchos['poblacion']}} , "
          f"{superficie:<{anchos['superficie']}} , "
          f"{continente:<{anchos['continente']}}\n"
        )

      archivo.write(formatear_fila("nombre", "poblacion", "superficie", "continente"))

      separador = "-" * (sum(anchos.values()) + 9) + "\n"
      archivo.write(separador)

      for pais in paises:
        archivo.write(formatear_fila(
          str(pais["nombre"]),
          str(pais["poblacion"]),
          str(pais["superficie"]),
          str(pais["continente"])
        ))

    print(f"{VERDE}Datos guardados correctamente en '{ruta_archivo}'{RESET}")
  except Exception as e:
    print(f"{ROJO}ERROR no se pudo guardar el archivo: {e}{RESET}")

# --------- #

def validar_texto(mensaje_1, mensaje_2=None):
    while True:
      try:
        texto = input(mensaje_1).strip()
        # FIX: se permite espacio para nombres como "Nueva Zelanda"
        if texto.replace(" ", "").isalpha():
          if mensaje_2 != None:
            print(f"{VERDE}{mensaje_2}{RESET}")
          return texto
        else:
          print(f"{ROJO}ERROR... El texto solo puede contener letras.{RESET}")
      except Exception as e:
        print(f"{ROJO}Hubo un error inesperado... Error: {e}.{RESET}")

def validar_entero(mensaje_1, mensaje_2=None):
  while True:
    try:
      numero = int(input(mensaje_1))
      if numero < 0:
        print(f"{ROJO}ERROR... No se permiten números negativos.{RESET}")
        continue
      if mensaje_2 != None:
        print(f"{VERDE}{mensaje_2}{RESET}")
      return numero
    except ValueError:
      print(f"{ROJO}ERROR... Por favor ingrese un número entero.{RESET}")
    except Exception as e:
      print(f"{ROJO}Hubo un error inesperado... Error: {e}.{RESET}")

def validar_flotante(mensaje_1, mensaje_2=None):
  while True:
    try:
      numero = float(input(mensaje_1))
      if numero < 0:
        print(f"{ROJO}ERROR... No se permiten números negativos.{RESET}")
        continue
      if mensaje_2 != None:
        print(f"{VERDE}{mensaje_2}{RESET}")
      return numero
    except ValueError:
      print(f"{ROJO}ERROR... Por favor ingrese un número válido.{RESET}")
    except Exception as e:
      print(f"{ROJO}Hubo un error inesperado... Error: {e}.{RESET}")

# FUNCION DE VALIDAR CONTINENTES #

def validar_continente(mensaje1, mensaje2 = None):
    continentes_validos = ["america", "asia", "europa", "africa", "oceania"]
    while True:
        try:
            continente = validar_texto(mensaje1).lower()
            if continente not in continentes_validos:
                print(f"{ROJO}ERROR! Continente no válido. Los continentes válidos son: {', '.join(continentes_validos)}{RESET}")
                continue
            if mensaje2 != None:
                print(f"{VERDE}{mensaje2}{RESET}")
            return continente.capitalize()
        except Exception as e:
            print(f"{ROJO}Ha ocurrido un error inesperado: {e}{RESET}")

# FUNCION DE AGREGAR PAIS #

def agregar_pais(paises):
  while True:

    nombre = validar_texto("Ingrese el nombre del pais: ")
    if len(nombre) < 4:
      print(f"{ROJO}ERROR... El nombre debe tener al menos 4 letras{RESET}")
    elif nombre.capitalize() in [pais["nombre"] for pais in paises]:
      print(f"{AMARILLO}El pais ya existe.{RESET}")
      return paises
    else:
      print(f"{VERDE}Nombre del pais ingresado correctamente.{RESET}")
      break

  while True:
    poblacion = validar_entero("Ingrese la poblacion del pais: ")
    if poblacion <= 500:
      print(f"{ROJO}ERROR... La poblacion debe ser mayor a 500.{RESET}")
    else:
      print(f"{VERDE}Poblacion del pais ingresada correctamente{RESET}")
      break

  while True:
    superficie = validar_flotante("Ingrese la superficie del pais (km²): ")
    if superficie < 0.44:
      print(f"{ROJO}ERROR... La superficie debe ser mayor a 0.44km².{RESET}")
    else:
      print(f"{VERDE}Superficie ingresada correctamente{RESET}")
      break

  continente = validar_continente("Ingrese el continente del pais:", "Continente ingresado correctamente")

  paises.append({
      "nombre": nombre.capitalize(),
      "poblacion": poblacion,
      "superficie": superficie,
      "continente": continente.capitalize()
    })
  print(f"{VERDE}Pais agregado correctamente.{RESET}")
  return paises

# FUNCION DE LISTAR PAISES #

def listar_paises(paises):
  if not paises:
    print(f"{AMARILLO}No hay paises que mostrar.{RESET}")  
  else:
    print()
    for pais in paises:
      print(mostrar_pais(pais))

# FUNCION DE BUSCAR PAIS #

def buscar_pais(paises):
  if not paises:
    print(f"{AMARILLO}No hay paises cargados.{RESET}")
    return
  
  nombre_buscar = validar_texto("Ingrese el nombre (o parte del nombre): ")
  nombre_buscar = nombre_buscar.lower()

  resultados= [p for p in paises if nombre_buscar in p["nombre"].lower()]

  if resultados:
    print(f"\n{VERDE}{len(resultados)} resultados encontrados: {RESET}")
    for pais in resultados:
      print(mostrar_pais(pais))
  else:
    print(f"{AMARILLO}No se encontro pais con ese nombre{RESET}")

# FUNCION DE MODIFICAR PAIS #

def modificar_pais(paises):
  if not paises:
    print(f"{AMARILLO}No hay paises cargados.{RESET}")
  else:
    nombre_pais = validar_texto("Ingrese el pais a modificar: ")
    encontrado = False
    for pais in paises:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"{VERDE}Pais encontrado:{RESET} {mostrar_pais(pais)}")
        encontrado = True
        while True:
          opcion = input(f"""{CIAN} -- ELIJA UNA OPCIÓN --{RESET}
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
              print(f"{CIAN}Volviendo al menú principal...{RESET}")
              break
            case _:
              print(f"{ROJO}ERROR... Comando inválido{RESET}")
    if not encontrado:
      print(f"{AMARILLO}Pais no encontrado.{RESET}")
    return paises

# FUNCION DE ELIMINAR PAIS #

def eliminar_pais(paises):
  if not paises:
    print(f"{AMARILLO}No hay paises cargados.{RESET}")
  else:
    nombre_pais = validar_texto("Ingrese el pais a eliminar: ")
    encontrado = False
    # FIX: se itera sobre una copia para evitar problemas al eliminar
    for pais in paises[:]:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"{VERDE}Pais encontrado:{RESET} {mostrar_pais(pais)}")
        encontrado = True
        paises.remove(pais)
        print(f"{VERDE}Pais eliminado{RESET}")
    if not encontrado:
      print(f"{AMARILLO}Pais no encontrado.{RESET}")
    return paises
  
# FUNCION DE FILTRAR PAIS #

def filtrar_paises(paises):
  if not paises:
    print(f"{AMARILLO}No hay paises cargados{RESET}")
    return
  
  print(f"""\n{NEGRITA}{CIAN} FILTRAR PAISES{RESET}
1.Por continente
2.Por rango de poblacion
3.por rango de superficie""")
  
  opcion = input("Elija una opcion: ").strip()

  match opcion:
    case "1":
      filtar_continente(paises)
    case "2":
      filtrar_poblacion(paises)
    case "3":
      filtrar_superficie(paises)
    case _:
      print(f"{ROJO}Opcion no valida{RESET}")

def filtar_continente(paises):
  continente = validar_texto("Ingrese el continente: ")
  resultados = [p for p in paises if p["continente"].lower() == continente.lower()]

  if resultados:
    print(f"\n{VERDE}Paises en {continente.capitalize()} ({len(resultados)}): {RESET}")
    for pais in resultados:
      print(mostrar_pais(pais))
  else: 
    print(f"{AMARILLO}No se encontraron paises en el continente '{continente.capitalize()}'{RESET}")

def filtrar_poblacion(paises):
  print("Ingrese la poblacion del pais: ")
  minimo = validar_entero("Minimo: ")
  maximo = validar_entero("Maximo: ")

  if minimo > maximo:
    print(f"{ROJO}ERROR el minimo no puede ser mayor al maximo{RESET}")
    return
  
  resultado = [p for p in paises if minimo <= p["poblacion"] <= maximo]

  if resultado:
    print(f"\n{VERDE}Paises con poblacion entre {minimo:,} y {maximo:,} ({len(resultado)}):{RESET}")
    for pais in resultado:
      print(mostrar_pais(pais))
  else:
    print(f"{AMARILLO}No se encontraron paises en ese rango de poblacion{RESET}")

def filtrar_superficie(paises):
  print("Ingrese el continente del pais en km^2: ")
  minimo = validar_flotante("Minimo: ")
  maximo = validar_flotante("Maximo: ")

  if minimo > maximo:
    print(f"{ROJO}ERROR el minimo no puede ser mayor que el maximo{RESET}")
    return
  
  resultado = [p for p in paises if minimo <= p["superficie"] <= maximo]

  if resultado:
    print(f"\n{VERDE}Países con superficie entre {minimo:,} y {maximo:,} km^2 ({len(resultado)}):{RESET}")
    for pais in resultado:
          print(mostrar_pais(pais))
  else:
      print(f"{AMARILLO}No se encontraron países en ese rango de superficie.{RESET}")

# FUNCION DE ORDENAMIENTO #

def ordena_paises(paises):
  orden = input(f"""Ingrese como desea ver los paises: 
              {CIAN}1{RESET} - Nombre
              {CIAN}2{RESET} - Poblacion
              {CIAN}3{RESET} - Superficie
              """).strip().lower()
  match orden:

    case "1" | "nombre":
      nombres = sorted([pais["nombre"] for pais in paises])
      for nombre in nombres:
        print(nombre)

    case "2" | "poblacion":
      poblaciones = sorted([pais["poblacion"] for pais in paises])
      for poblacion in poblaciones:
        print(poblacion)

    case "3" | "superficie":

      orden_dir = input("Ascendente o Descendente (a/d): ").strip().lower()

      if orden_dir == "a" or orden_dir == "ascendente":
        superficies = sorted([pais["superficie"] for pais in paises])
        for superficie in superficies:
          print(superficie)

      elif orden_dir == "d" or orden_dir == "descendente":
        superficies = sorted([pais["superficie"] for pais in paises],reverse=True)
        for superficiee in superficies:
          print(superficiee)

      else:
        print(f"{ROJO}Opcion incorrecta...{RESET}")
        return
      
    case _:
      print(f"{ROJO}Opcion incorrecta...{RESET}")

# FUNCION DE MOSTRAR ESTADISTICAS

def mostrar_estadisticas(paises):
    if not paises:
        print(f"{AMARILLO}No hay paises cargados.{RESET}")
        return

    mayor_pob = paises[0]
    menor_pob = paises[0]
    for pais in paises:
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais

    total_poblacion = 0
    total_superficie = 0
    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]
    
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print(f"\n{NEGRITA}Pais con mayor poblacion:{RESET} {CIAN}{mayor_pob['nombre']}{RESET} ({BLANCO}{mayor_pob['poblacion']:,}{RESET})")
    print(f"{NEGRITA}Pais con menor poblacion:{RESET} {CIAN}{menor_pob['nombre']}{RESET} ({BLANCO}{menor_pob['poblacion']:,}{RESET})")
    print(f"{NEGRITA}Promedio de poblacion:{RESET} {BLANCO}{promedio_poblacion:,.2f}{RESET}")
    print(f"{NEGRITA}Promedio de superficie:{RESET} {BLANCO}{promedio_superficie:,.2f} km^2{RESET}")
    print(f"\n{NEGRITA}Cantidad de paises por continente:{RESET}")
    for continente, cantidad in continentes.items():
        print(f"  {AMARILLO}{continente}{RESET}: {cantidad}")