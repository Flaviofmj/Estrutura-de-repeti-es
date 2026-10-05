# QUESTÃO >  Leia um número inteiro positivo e, utilizando um laço while, calcule a soma dos seus dígitos.

# Lê um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa a soma dos dígitos
soma = 0

# Repete enquanto ainda houver dígitos no número
while numero > 0:

    # Pega o último dígito do número
    digito = numero % 10

    # Adiciona o dígito à soma
    soma += digito

    # Remove o último dígito do número
    numero //= 10

# Exibe o resultado
print("A soma dos dígitos é:", soma)