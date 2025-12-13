# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0305, C0301
"""
4.	Programa iterativo. Calculadora de impuestos progresivos
Ingresar el ingreso mensual. El ingreso anual es 12 ingresos mensuales mas 2 aguinaldos que son un sueldo completo.
Calcular el impuesto aplicando tramos progresivos, por ejemplo: 
Rango Tasa 
[0 – 20000] 0% 
<20000 – 50000] 10% 
<50000 – 100000] 20% 
Mayor a 100000 30% 
El impuesto se calcula por tramo, no tomando la tasa completa sobre el total. 
Ejemplo con sueldo mensual de 5000 (anual sería 70000) 
[0 – 20000] → 0 
<20000 – 50000] → 30,000 × 10% = 3000 
<50000 - 70000 → 20,000 × 20% = 4000 
Total impuesto = 7,000 
El programa debe mostrar: 
•	Impuesto por tramo 
•	Total de impuestos
•	Tasa efectiva real (impuesto / ingreso) × 100 en % 

"""
print("==================== EJERCICIO 2 (4.) ====================")

while True:
    print("(Escriba 'q' para salir)")
    entrada = input("Ingreso mensual: ")
    if entrada.lower() == 'q':
        print("Saliendo...")
        break
    
    while float(entrada) <= 0:
        print("DATO NO VÁLIDO. INGRESE DE NUEVO.")
        entrada = input("Ingreso mensual: ")
        if entrada.lower() == 'q':
            print("Saliendo...")
            break

    ingreso_anual = int(entrada) * 14
    impuesto_total = 0
    primer_tramo = 0
    segundo_tramo = 0
    tercer_tramo = 0
    impuesto_total = 0
    tasa_efectiva_real = 0

    if 100000 >= ingreso_anual >= 50000:
        segundo_tramo = 30000 * (10 / 100)
        tercer_tramo = (ingreso_anual - 50000) * (20 / 100)
        impuesto_total = primer_tramo + segundo_tramo + tercer_tramo
        tasa_efectiva_real = (impuesto_total / ingreso_anual) * 10
        # impuesto_total = (ingreso_anual - 50000 * (20 / 100)) + (30000 * (10 / 100))
    elif 50000 > ingreso_anual >= 20000:
        segundo_tramo = 30000 * (10 / 100)
        impuesto_total = primer_tramo + segundo_tramo
        tasa_efectiva_real = (impuesto_total / ingreso_anual) * 100
    else:
        impuesto_total = 0
    
    print("------- RESULTADO ------")
    print(f"Ingreso anual: {ingreso_anual}")
    print(f"-> Impuestos:\n    Primer tramo: {primer_tramo}\n    Segundo tramo: {segundo_tramo}\n    Tercer tramo: {tercer_tramo}")
    print(f"-> Total de impuestos: {impuesto_total}")
    print(f"-> Tasa efectiva real: {tasa_efectiva_real}%")
    print("------------------------\n")


print("==========================================================")
