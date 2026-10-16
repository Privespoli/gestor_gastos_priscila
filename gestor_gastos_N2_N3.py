
gastos = [15.50, 22.00, 45.30, 10.00, 38.20]

# Calcula el total con un bucle
def calcular_total(lista):

    total = 0
    for gasto in lista: 
        total += gasto
    return total

# Ejecución de la función para obtener el total:
total_gastos = calcular_total(gastos)

# Calcular la media:
media_gastos = total_gastos / len(gastos)

# Resultados:
print("Gastos:")
print(f"Lista de gastos: {gastos}")
print(f"Gasto total: {total_gastos:.2f} €")
print(f"Gasto medio: {media_gastos:.2f} €")
print("---------")


# Permite que la persona introduzca un límite para filtrar los gastos
try:
    limite = float(input("Introduce una cantidad límite para filtrar los gastos: "))
except ValueError:
    limite = 20.00
    print("Valor no válido. Se usará por defecto el límite de 20.00 €.")

#  Utiliza una condición para mostrar los gastos superiores al límite introducido
print(f"Gastos superiores a {limite:.2f} €:")
encontrado = False
for gasto in gastos:
    if gasto > limite:
        print(f"  • {gasto:.2f} €")
        encontrado = True

if not encontrado:
    print(f"  Ningún gasto supera los {limite:.2f} €.")

print("---------")

# Compara el total con el presupuesto de 100 €
presupuesto = 100.00
if total_gastos > presupuesto:
    exceso = total_gastos - presupuesto
    print(f"Has superado el presupuesto de {presupuesto} € por {exceso:.2f} €.")
else:
    restante = presupuesto - total_gastos
    print(f"Estás dentro del presupuesto. Te quedan {restante:.2f} € disponibles.")