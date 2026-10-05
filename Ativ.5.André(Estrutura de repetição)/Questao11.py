# QUESTÃO 11 >  Leia um número inteiro positivo e, utilizando um laço while, calcule a soma dos seus dígitos.

# Lê um número inteiro maior que 1
numero = int(input("Digite um número inteiro maior que 1: "))

# Começa o contador de divisores em zero
divisores = 0

# Percorre os números de 1 até o número informado
for i in range(1, numero + 1):

    # Verifica se o número é divisível por i
    if numero % i == 0:

        # Conta o divisor
        divisores += 1

# Um número primo possui exatamente 2 divisores
if divisores == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")