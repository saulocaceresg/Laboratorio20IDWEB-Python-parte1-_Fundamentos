# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0305, C0301, C0200
"""
6.	Programa iterativo. Normalizador de datos con funciones creadas
    Crea una función llamada normalizar(lista, modo) que reciba:
    •	Una lista de números reales
    •	Un modo de normalización: "minmax", "zscore" o "unit" 
    La función debe devolver una nueva lista sin modificar la original. 
    Modos: 
        "minmax" 
        x' = (x - min) / (max - min) 
        "zscore" 
        x' = (x - media) / desviación estandar 
        "unit" (vector unitario) 
        x' = x / ||vector|| norma del vector 
    Reglas:
        •	Debe validar el modo
        •	Debe manejar división por cero 
    Dados:
        valores = [10, 20, 30] 
    Salida: 
        [0.0, 0.5, 1.0] 
        [-1.224744871391589, 0.0, 1.224744871391589] 
        [0.2672612419124244, 0.5345224838248488, 0.8017837257372732] 
        Original: [10, 20, 30] 
    2 versiones: una con Python puro (sin librerías externas) y otra con librería NumPy

"""
print("==================== EJERCICIO 4 (6.) ====================")

def normalizar(lista, modo):
    """
    Función para normalizar una lista    
    :param lista: Lista con números para normalizar
    :param modo: Modo de normalización
    """
    nueva_lista = []
    
    match modo:
        case "minmax":
            # se usa método max y min para sacar el valor máximo y mínimo de la lista
            maximo = max(lista)
            minimo = min(lista)
            for i in lista:
                resultado = (i - minimo) / (maximo - minimo)
                nueva_lista.append(resultado)

        case "zscore":
            suma = 0
            for i in lista:
                suma += i
            media = suma / len(lista)
            
            suma_desviacion = 0
            for j in lista:
                suma_desviacion += (j - media) ** 2
            
            desviacion_estandar = (suma_desviacion / len(lista)) ** (0.5)

            for x in lista:
                resultado = (x - media) / desviacion_estandar
                nueva_lista.append(resultado)
        
        case "unit":
            suma_cuadrado = 0
            for i in lista:
                suma_cuadrado += i ** 2
            
            vector = suma_cuadrado ** (0.5)

            for x in lista:
                resultado = x / vector
                nueva_lista.append(resultado)
    
    return nueva_lista

# Ciclo while para iteraciones ilimitadas (hasta qye ingrese 'n')
while True:
    # Se crea una nueva lista por cada iteración
    lista_numeros = []
    while True:
        entrada = input("-> Ingrese números ('q' para terminar): ")

        if entrada.lower() == 'q':
            break
        
        entrada = int(entrada)
        lista_numeros.append(entrada)
    
    # Procederá a la normalización si hay más de un solo elemento en la lista
    if len(lista_numeros) > 1:
        lista_nueva = []
        opcion_normalizacion = input(
            "\n---- Elija modo de normalización ----\n"
            "(a) Min-Máx\n"
            "(b) Zscore\n"
            "(c) Unit\n" \
            "-> ").lower()
        
        # Ciclo while para verificar la opción
        while opcion_normalizacion not in ('a', 'b', 'c'):
            print("* OPCIÓN NO VÁLIDA. INGRESE DE NUEVO. *")
            opcion_normalizacion = input("-> ").lower()
        
        match opcion_normalizacion:
            case 'a':
                lista_nueva = normalizar(lista_numeros, "minmax")
                print(f"  Lista original: {lista_numeros}\n  Lista normalizada: {lista_nueva}")
            case 'b':
                lista_nueva = normalizar(lista_numeros, "zscore")
                print(f"  Lista original: {lista_numeros}\n  Lista normalizada: {lista_nueva}")
            case 'c':
                lista_nueva = normalizar(lista_numeros, "unit")
                print(f"  Lista original: {lista_numeros}\n  Lista normalizada: {lista_nueva}")
        
        continuar = input("\n¿Desea continuar? Sí(S) / No (N)\n-> ")
        while continuar.lower() not in ('s', 'n') :
            print("* OPCIÓN NO VÁLIDA. INGRESE DE NUEVO. *")
            continuar = input("-> ")
        
        if continuar.lower() == 'n':
            print("Saliendo...")
            break
    else:
        print("* LISTA VACÍA *")
        print("Saliendo...")
        break

print("==========================================================")
