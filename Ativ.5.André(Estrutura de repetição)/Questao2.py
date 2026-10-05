# QUESTÃO 2 > Leia um número inteiro N e calcule a soma de todos os inteiros de 1 até N, utilizando um laço while.

# Lê um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa a soma com zero
soma = 0

# Começa a contagem em 1
n = 1

# Enquanto n for menor ou igual ao número informado
while n <= numero:

    # Adiciona n à soma
    soma += n

    # Incrementa n em 1
    n += 1

# Exibe o resultado
print("A soma de 1 até", numero, "é:", soma)