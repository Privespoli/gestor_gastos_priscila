gastos = [12, 8, 25, 15, 30]
presupuesto_semanal = 100
limite_gasto_alto = 20

print("Gastos de la semana:", gastos)

# Calcular el total de los gastos:
total = 0
for valor in gastos:
    total = total + valor  
print("Total gastado:", total, "€")

# Calcular el gasto medio:
media = total / len(gastos)
print("Gasto medio:", round(media, 2), "€")

# Gastos que superan los 20€:
print("Gastos mayores de", limite_gasto_alto, "€:")
for gasto in gastos:
    if gasto > limite_gasto_alto:
        print(" -", gasto, "€")

# Comprobar si el total supera el presupuesto semanal:
if total > presupuesto_semanal:
    print("Has superado el presupuesto semanal de", presupuesto_semanal, "€!")
else:
    print("Estás dentro del presupuesto semanal de", presupuesto_semanal, "€!!")