# QUESTÃO 3 > Leia um número inteiro e exiba sua tabuada completa (de 1 a 10), utilizando um laço for.

# Lê um número inteiro informado pelo usuário
numero = int(input("Digite um número inteiro: "))

# Laço for que vai de 1 até 10
for n in range(1, 11):

    # Calcula e exibe a multiplicação
    resultado = numero * n

    print(numero, "x", n, "=", resultado)