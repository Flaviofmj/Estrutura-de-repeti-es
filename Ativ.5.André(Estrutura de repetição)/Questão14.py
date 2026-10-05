# Lê um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa o número invertido
invertido = 0

# Repete enquanto ainda houver dígitos
while numero > 0:

    # Pega o último dígito
    digito = numero % 10

    # Adiciona o dígito ao número invertido
    invertido = invertido * 10 + digito

    # Remove o último dígito do número original
    numero //= 10

# Exibe o número invertido
print("Número invertido:", invertido)