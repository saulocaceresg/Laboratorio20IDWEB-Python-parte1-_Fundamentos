# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0305, C0301, C0200
"""
5.	Programa iterativo y sin confiar en el usuario. Pedir un número N mayor o igual a 3.
Generar una matriz NxN llena con números desde 1 hasta N², ordenados en forma de espiral, por ejemplo:
 
Puedes usar cualquier estructura de datos 

"""
print("==================== EJERCICIO 3 (5.) ====================")

while True:
    # Entrada de datos
    entrada = input("Ingrese un número mayor o igual a 3 ('q' para salir): ")

    # Ciclo while para verificar la validez del dato
    while (not entrada.isdigit() or int(entrada) < 3) and entrada.lower() != "q":
        print("* DATO NO VÁLIDO. INGRESE DE NUEVO. *")
        entrada = input("Ingrese un número mayor o igual a 3 ('q' para salir): ")
        if entrada == 'q':
            break
    
    if entrada.lower() == 'q':
        print("Saliendo...")
        break
    
    # Convierte a entero
    entrada = int(entrada)

    # Lista para llenar con los números desde 1 hasta n^2
    lista = []
    for i in range(entrada ** 2):
        lista.append(i + 1)

    # Se crea una matriz de ceros inicial según el número ingresado
    matriz = [[0 for _ in range(entrada)] for _ in range(entrada)]

    # Variables para manejar el llenado
    indice = 0
    fila_inicio = 0
    fila_final = entrada - 1
    col_inicio = 0
    col_final = entrada - 1
    
    while fila_inicio <= fila_final and col_inicio <= col_final:
        # izquierda a derecha
        for i in range(col_inicio, col_final + 1):
            matriz[fila_inicio][i] = lista[indice]
            indice += 1
        fila_inicio += 1

        # arriba a abajo
        for j in range(fila_inicio, fila_final + 1):
            matriz[j][col_final] = lista[indice]
            indice += 1
        col_final -= 1

        # derecha a izquierda
        if fila_inicio <= fila_final:
            for t in range(col_final, col_inicio - 1, -1):
                matriz[fila_final][t] = lista[indice]
                indice += 1
            fila_final -= 1
        
        # abajo a arriba
        if col_inicio <= col_final:
            for x in range(fila_final, fila_inicio - 1, -1):
                matriz[x][col_inicio] = lista[indice]
                indice += 1
            col_inicio += 1

    print(lista)

    for fila in matriz:
        print(fila)

print("==========================================================")
