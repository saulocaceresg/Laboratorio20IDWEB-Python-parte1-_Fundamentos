# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0305, C0301, C0200
"""
7.	Registro de estudiantes
Crear un programa que permita:
•	Registrar estudiantes (nombre, edad, promedio)
•	Guardar cada estudiante como un diccionario
•	Almacenar todos los estudiantes en una lista 
Menú de opciones:
•	Agregar estudiante
•	mostrar estudiantes
•	mostrar estudiante con mejor promedio
•	buscar por nombre
•	eliminar por nombre
•	salir

"""
print("==================== EJERCICIO 4 (6.) ====================")
def agregar(lista):
    """
    Función para agregar estudiante
    """
    print("\n--- AGREGAR ESTUDIANTE ---")
    nuevo = {}

    nombre = input("-> Ingrese nombre: ")
    nuevo["nombre"] = nombre

    edad = input("-> Ingrese edad: ")
    while not edad.isdigit() or int(edad) <= 0:
        print("* DATO NO VÁLIDO *")
        edad = input("-> Ingrese edad: ")
    nuevo["edad"] = edad
    
    promedio = input("-> Ingrese promedio: ")
    while not promedio.isdigit() or not 0 <= int(promedio) <= 20:
        print("* DATO NO VÁLIDO *")
        promedio = input("-> Ingrese promedio: ")
    nuevo["promedio"] = promedio

    lista.append(nuevo)

def mostrar(lista):
    """
    Función para mostrar estudiantes
    """
    print("\n--- LISTA DE ESTUDIANTES ESTUDIANTE ---")
    for i in lista:
        print(i)

def mejor_promedio(lista):
    """
    Función para el mayor promedio
    """
    print("\n--- MEJOR PROMEDIO ---")
    
    promedios = []
    for i in lista:
        promedios.append(i["promedio"])
    # print(promedios)
    
    mayor = max(promedios)

    mejor_estudiante = ""

    for j in range(len(lista)):
        if lista[j]["promedio"] == mayor:
            mejor_estudiante = f"{lista[j]["nombre"]} => {mayor}"
            break
    
    return mejor_estudiante

def buscar_por_nombre(nombre_ingresado, lista):
    """
    Función para buscar por nombre
    """
    print("\n--- BUSCAR POR NOMBRE ---")

    estudiante = ""
    for i in lista:
        if i["nombre"] == nombre_ingresado:
            estudiante = i
            break
    return estudiante

def eliminar_por_nombre(nombre_ingresado, lista):
    """
    Función para eliminar por nombre
    """
    print("\n--- ELIMINAR POR NOMBRE ---")

    # estudiante_eliminado = None
    for i in lista:
        if i["nombre"] == nombre_ingresado:
            # estudiante = i
            lista.remove(i)
            break

# ========================= PARTE PRINCIPAL ==================================

lista_estudiantes = [
    {"nombre": "Luis", "edad": 18, "promedio": 13},
    {"nombre": "Mateo", "edad": 22, "promedio": 11},
    {"nombre": "Jocinero", "edad": 20, "promedio": 18},
    {"nombre": "Crisanta", "edad": 21, "promedio": 14}
]

while True:
    print("---- MENÚ DE OPCIONES ----\n" \
        "(a) Agregar estudiantes\n" \
        "(b) Mostrar estudiantes\n" \
        "(c) Mostrar estudiante con mejor promedio\n" \
        "(d) Buscar por nombre\n" \
        "(e) eliminar por nombre\n" \
        "(f) salir")
    opcion = input("-> ").lower()

    while opcion not in ('a', 'b', 'c', 'd', 'e', 'f'):
        print("* OPCIÓN NO VÁLIDA. INGRESE DE NUEVO* ")
        opcion = input("-> ").lower()


    match opcion:
        case 'a':
            agregar(lista_estudiantes)
        case 'b':
            mostrar(lista_estudiantes)
        case 'c':
            print(mejor_promedio(lista_estudiantes))
        case 'd':
            nombre_buscar = input("-> Ingrese nombre a buscar: ")
            buscar_por_nombre(nombre_buscar, lista_estudiantes)
        case 'e':
            nombre_eliminar = input("-> Ingrese el nombre del estudiante a eliminar: ")
            eliminar_por_nombre(nombre_eliminar, lista_estudiantes)
        case 'f':
            print("Saliendo...")
    
    opcion = input("¿Desea cotinuar? Sí(S) / No(N)\n-> ")

    while opcion.lower() not in ('s', 'n'):
        print("* OPCIÓN NO VÁLIDA. INGRESE DE NUEVO. *")
        opcion = input("-> ")
    
    if opcion == 'n':
        print("Saliendo...")
        break


print("==========================================================")
