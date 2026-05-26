import csv
import os

def mostrar_pais(pais):
  return f"{pais['nombre']} - Poblacion: {pais['poblacion']} - Superficie: {pais['superficie']} - Continente: {pais['continente']}"

# CARGAR CSV #

def cargar_csv(ruta_archivo, paises):

  if not os.path.exists(ruta_archivo):
    print(f"Archivo '{ruta_archivo}' no encontrado, se usaran datos por defecto.")
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

    print(f"Datos guardados correctamente en '{ruta_archivo}'")
  except Exception as e:
    print(f"ERROR no se pudo guardar el archivo: {e}")


# --------- #

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

# FUNCION DE VALIDAR CONTINENTES #

def validar_continente(mensaje1, mensaje2 = None):
    continentes_validos = ["america", "asia", "europa", "africa", "oceania"]
    while True:
        try:
            continente = validar_texto(mensaje1).lower()
            if continente not in continentes_validos:
                print(f"ERROR! Continente no válido. Los continentes válidos son: {', '.join(continentes_validos)}")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return continente.capitalize()
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

# FUNCION DE AGREGAR PAIS #

def agregar_pais(paises):
  while True:

    nombre = validar_texto("Ingrese el nombre del pais: ")
    if len(nombre) < 4:
      print("ERROR... El nombre debe tener al menos 4 letras")
    elif nombre.capitalize() in [pais["nombre"] for pais in paises]:
      print("El pais ya existe.")
      return paises
    else:
      print("Nombre del pais ingresado correctamente.")
      break

  while True:
    poblacion = validar_entero("Ingrese la poblacion del pais: ")
    if poblacion <= 500:
      print("ERROR... La poblacion debe ser mayor a 500.")
    else:
      print("Poblacion del pais ingresada correctamente")
      break

  while True:
    superficie = validar_flotante("Ingrese la superficie del pais (km²): ")
    if superficie < 0.44:
      print("ERROR... La superficie debe ser mayor a 0.44km².")
    else:
      print("Superficie ingresada correctamente")
      break

  continente = validar_continente("Ingrese el continente del pais:", "Continente ingresado correctamente")

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
  
# FUNCION DE FILTRAR PAIS #

def filtrar_paises(paises):
  if not paises:
    print("No hay paises cargados")
    return
  
  print("""\n FILTRAR PAISES
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
      print("Opcion no valida")

def filtar_continente(paises):
  continente = validar_texto("Ingrese el continente: ")
  resultados = [p for p in paises if p["continente"].lower() == continente.lower()]

  if resultados:
    print(f"\nPaises en {continente.capitalize()} ({len(resultados)}): ")
    for pais in resultados:
      print(mostrar_pais(pais))
  else: 
    print(f"No se encontraron paises en el continente '{continente.capitalize()}'")

def filtrar_poblacion(paises):
  print("Ingrese la poblacion del pais: ")
  minimo = validar_entero("Minimo: ")
  maximo = validar_entero("Maximo: ")

  if minimo > maximo:
    print("ERROR el minimo no puede ser mayor al maximo")
    return
  
  resultado = [p for p in paises if minimo <= p["poblacion"] <= maximo]

  if resultado:
    print(f"\nPaises con poblacion entre {minimo:,} y {maximo:,} ({len(resultado)}):")
    for pais in resultado:
      print(mostrar_pais(pais))
  else:
    print("No se encontraron paises en ese rango de poblacion")

def filtrar_superficie(paises):
  print("Ingrese el continente del pais en km^2: ")
  minimo = validar_flotante("Minimo: ")
  maximo = validar_flotante("Maximo: ")

  if minimo > maximo:
    print("ERROR el minimo no puede ser mayor que el maximo")
    return
  
  resultado = [p for p in paises if minimo <= p["superficie"] <= maximo]

  if resultado:
    print(f"\nPaíses con superficie entre {minimo:,} y {maximo:,} km^2 ({len(resultado)}):")
    for pais in resultado:
          print(mostrar_pais(pais))
  else:
      print("No se encontraron países en ese rango de superficie.")

# FUNCION DE ORDENAMIENTO #

def ordena_paises(paises):
  orden = input("""Ingrese como desea ver los paises: 
              1 - Nombre
              2 - Poblacion
              3 - Superficie
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
        print("Opcion incorrecta...")
        return
      
    case _:
      print("Opcion incorrecta...")

# FUNCION DE MOSTRAR ESTADISTICAS

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay paises cargados.")
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

    print(f"\nPais con mayor poblacion: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"Pais con menor poblacion: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"Promedio de poblacion: {promedio_poblacion:,.2f}")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km^2")
    print("\nCantidad de paises por continente:")
    for continente, cantidad in continentes.items():
        print(f"  {continente}: {cantidad}")