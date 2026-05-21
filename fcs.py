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