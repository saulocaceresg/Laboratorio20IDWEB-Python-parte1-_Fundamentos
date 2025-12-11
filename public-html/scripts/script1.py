# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
3.	Dada la siguiente fórmula:
salario_neto = salario_base + (horas_extras * pago_hora_extra) + bono - (salario_base * afp/100) - (salario_base * salud/100)
Mostrar salario bruto (sin descuentos), descuentos totales y salario neto.

"""
print("==================== EJERCICIO 1 (3.) ====================")

# Entrada de datos. Con ciclos while para condicionar los datos
salario_base = float(input("Ingrese salario base: "))
while salario_base <= 0:
    print("Salario no válido. INGRESE DE NUEVO.")
    salario_base = float(input("Ingrese salario base: "))

horas_extras = float(input("Ingrese horas extras: "))
while horas_extras < 0:
    print("DATO NO VÁLIDO. INGRESE DE NUEVO.")
    horas_extras = float(input("Ingrese horas extras: "))

if horas_extras > 0:
    pago_hora_extra = float(input("Ingrese el pago por horas extras: "))
    while pago_hora_extra <= 0:
        print("DATO NO VÁLIDO. INGRESE DE NUEVO.")
        pago_hora_extra = float(input("Ingrese el pago por horas extras: "))

bono = float(input("Ingrese el bono: "))
while bono < 0:
    print("DATO NO VÁLIDO. INGRESE DE NUEVO.")
    bono = float(input("Ingrese el bono: "))

afp = float(input("Ingrese el porcentaje AFP (10% - 13%): "))
while afp < 10 or afp > 13:
    print("AFP no válido. INGRESE DE NUEVO.")
    afp = float(input("Ingrese el porcentaje AFP (10% - 13%): "))

salud = float(input("Ingrese seguro de salud (7% - 10%): "))
while salud < 7 or salud > 10:
    print("Porcentaje de salud no válido. INGRESE DE NUEVO.")
    salud = float(input("Ingrese seguro de salud (7% - 10%): "))

# Cálculo del salario y descuentos
salario_neto = salario_base + (horas_extras * pago_hora_extra) + bono - (salario_base * afp/100) - (salario_base * salud/100)

descuentos = (salario_base * afp/100) - (salario_base * salud/100)

salario_bruto = salario_neto - descuentos

print("\nResultados:\nSalario bruto:", salario_bruto, "\nDescuentos totales:", descuentos, "\nSalario neto:", salario_neto)

print("==========================================================")
