# 1. Define uma lista com cinco valores fixos de gastos semanais
gastos = [12, 8, 25, 15, 30]

# Define variáveis para o orçamento limite e o valor para considerar um gasto como "alto"
presupuesto_semanal = 100
limite_gasto_alto = 20

# Exibe a lista completa de gastos no console
print("Gastos de la semana:", gastos)

# 2. Inicia o cálculo do total acumulado dos gastos
total = 0
for valor in gastos:             # Percorre cada elemento (valor) dentro da lista 'gastos'
    total = total + valor        # Soma o valor atual ao acumulador 'total'
print("Total gastado:", total, "€")

# 3. Calcula o gasto médio dividindo o total pelo número de itens da lista (len)
media = total / len(gastos)
print("Gasto medio:", round(media, 2), "€")  # O 'round(..., 2)' arredonda o resultado para 2 casas decimais

# 4. Usa uma condição (if) para filtrar e mostrar apenas os gastos superiores a 20 €
print("Gastos mayores de", limite_gasto_alto, "€:")
for gasto in gastos:             # Percorre a lista de gastos novamente
    if gasto > limite_gasto_alto: # Condição: se o gasto for maior que 20
        print(" -", gasto, "€")  # Mostra o gasto correspondente no console

# 5. Compara o total gasto com o orçamento semanal estipulado de 100 €
if total > presupuesto_semanal:  # Se o total for maior que o orçamento
    print("Has superado el presupuesto semanal de", presupuesto_semanal, "€!")
else:                            # Caso contrário (se estiver dentro do limite)
    print("Estás dentro del presupuesto semanal de", presupuesto_semanal, "€!!")