# QUESTÃO 4 > Utilizando um laço for, conte e exiba quantos números pares existem no intervalo de 1 a 100.

# Inicializa o contador de números pares
contador = 0

# Percorre os números de 1 até 100
for numero in range(1, 101):

    # Verifica se o número é par
    if numero % 2 == 0:

        # Adiciona 1 ao contador
        contador += 1

# Exibe a quantidade de números pares
print("Quantidade de números pares:", contador)