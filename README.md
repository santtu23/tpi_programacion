👨‍💻 Gestión de Países

Sistema CRUD de consola desarrollado en Python para gestionar información de países, con persistencia de datos en archivos CSV.

Trabajo Práctico Integrador — Programación I
Tecnicatura Universitaria en Programación a Distancia — UTN
Integrantes: Santiago Jalil · Uriel Boratti

👨‍💻 Descripción

Aplicacion de lineas de comandos que nos permiten administrar un registro de paises con sus datos principales como nombre, población, superficie y contiente. Los datos se cargan en un archivo csv al iniciar el programa y se guardan al momento de salir.

👨‍💻 Requisitos

-Usar Python 3.10.
-Se usan modulos estándar de bibliotecas.

👨‍💻 Instalacion y Ejecucion

1. Clonar el repositorio (bash).
git clone https://github.com/santtu23/tpi_programacion.git
cd tpi_programacion
2. Ejecutar el programa (bash).
python main.py.
En caso que no exista el archivo csv (paises.csv) se crea uno al momento de iniciar el programa.

👨‍💻 Estructura del proyecto

tpi_programacion/

main.py          # Punto de entrada: carga de datos y menú principa
fcs.py           # Todas las funciones del sistema
paises.csv       # Archivo de datos (se genera al salir)
README.md

Responsabilidad de cada archivo

ARCHIVO
main.py (Inicializa los datos, muestra el menú y carga las diferente funciones).
fcs.py (Contiene toda la lógica: CRUD, validaciones, filtros, ordenamiento, estadisticas y manejo del csv).

👨‍💻 Funcionalidades

=======Menu principal======
1. Agregar país
2. Listar países
3. Buscar país
4. Modificar país
5. Eliminar país
6. Filtrar países
7. Ordenar países
8. Estadísticas
9. Salir
===============================

Detalle de cada opción
1. Agregar país

- Solicita nombre (mínimo 4 letras, sin duplicados), población (> 500), superficie (> 0.44 km²) y continente.
- Valida cada campo antes de agregar.

2. Listar países

- Muestra todos los países cargados con nombre, población, superficie y continente.

3. Buscar país

- Búsqueda parcial e insensible a mayúsculas/minúsculas.
- Muestra todos los resultados que coincidan.

4. Modificar país

- Permite editar la población o la superficie de un país existente.

5. Eliminar país

- Elimina un país por nombre con confirmación visual.

6. Filtrar países

- Por continente: muestra todos los países de un continente.
- Por rango de población: filtra entre un mínimo y máximo.
- Por rango de superficie: filtra entre un mínimo y máximo en km².

7. Ordenar países

- Por nombre, población o superficie.
- Superficie permite elegir orden ascendente o descendente.

8. Estadísticas

- País con mayor y menor población.
- Promedio de población y superficie.
- Cantidad de países por continente.

9. Salir

- Guarda todos los datos en paises.csv antes de cerrar.

👨‍💻 Formato del CSV

El archivo paises.csv tiene la siguiente estructura:

nombre,poblacion,superficie,continente
Argentina,45376763,2780400.0,America
Japon,125800000,377975.0,Asia
Brasil,213993437,8515767.0,America
Alemania,83149300,357022.0,Europa

👨‍💻 Validaciones implementadas

FUNCIÓN 

validar_texto(): Solo letras y espacios (permite nombres como "Nueva Zelanda")
validar_entero(): Entero no negativo
validar_flotante(): Número decimal no negativo
validar_continente(): Solo acepta: America, Asia, Europa, Africa, Oceania

Todas las funciones usan while True + try/except para repetir la solicitud hasta obtener un valor válido.

👨‍💻 Bugs resueltos durante el desarrollo

- return paises faltante en agregar_pais() — la lista quedaba como None después de agregar.

- Iteración sobre lista al eliminar — se resolvió iterando sobre una copia paises[:].

- Nombres con espacios — isalpha() no acepta espacios; se corrigió con texto.replace(' ', '').isalpha().

- Protección ante None — se aplicó el patrón paises = funcion(paises) or paises en el menú principal.

👨‍💻 Video explicativo
(FALTA EL LINK)