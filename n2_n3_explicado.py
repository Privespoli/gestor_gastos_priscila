# 1. Define uma lista contendo cinco valores numéricos de gastos
gastos = [15.50, 22.00, 45.30, 10.00, 38.20]

# 2. Cria uma função chamada 'calcular_total' que recebe uma lista como parâmetro
def calcular_total(lista):
    total = 0                    # Inicializa o acumulador em zero
    for gasto in lista:          # Percorre cada elemento (gasto) dentro da lista
        total += gasto           # Soma o gasto atual ao total acumulado
    return total                 # Devolve o valor final da soma

# 3. Executa a função passando a lista de gastos e guarda o resultado na variável
total_gastos = calcular_total(gastos)

# 4. Calcula a média dividindo o total pela quantidade de itens da lista (len)
media_gastos = total_gastos / len(gastos)

# 5. Exibe os resultados gerais formatados no console
print("Gastos:")
print(f"Lista de gastos: {gastos}")
print(f"Gasto total: {total_gastos:.2f} €")       # O ':.2f' formata para mostrar 2 casas decimais
print(f"Gasto medio: {media_gastos:.2f} €")
print("-" * 27)                                  # Imprime 27 traços para criar uma linha divisória

# 6. Pede para o usuário digitar um valor limite (com proteção contra erros)
try:
    limite = float(input("Introduce una cantidad límite para filtrar los gastos: "))
except ValueError:                               # Se o usuário digitar texto em vez de número
    limite = 20.00                               # Define um valor padrão de segurança
    print("Valor no válido. Se usará por defecto el límite de 20.00 €.")

# 7. Usa uma condição (if) para filtrar e mostrar apenas os gastos acima do limite
print(f"Gastos superiores a {limite:.2f} €:")
encontrado = False                               # Variável de controle (flag) para saber se achou algum
for gasto in gastos:                             # Percorre a lista de gastos de novo
    if gasto > limite:                           # Condição: se o gasto for maior que o limite inserido
        print(f"  • {gasto:.2f} €")              # Mostra o gasto correspondente
        encontrado = True                        # Atualiza a flag indicando que encontrou pelo menos um

if not encontrado:                               # Se a flag continuar falsa após o loop
    print(f"  Ningún gasto supera los {limite:.2f} €.")

print("-" * 27)                                  # Outro separador visual

# 8. Compara o total gasto com o orçamento fixo de 100 €
presupuesto = 100.00
if total_gastos > presupuesto:                   # Se os gastos forem maiores que o orçamento
    exceso = total_gastos - presupuesto          # Calcula o valor que passou do limite
    print(f"Has superado el presupuesto de {presupuesto} € por {exceso:.2f} €.")
else:                                            # Caso contrário (se estiver dentro do orçamento)
    restante = presupuesto - total_gastos        # Calcula quanto dinheiro sobrou
    print(f"Estás dentro del presupuesto. Te quedan {restante:.2f} € disponibles.")