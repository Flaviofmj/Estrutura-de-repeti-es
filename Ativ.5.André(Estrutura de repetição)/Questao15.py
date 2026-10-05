# Inicializa a soma dos números
soma = 0

# Inicializa o contador de números informados
quantidade = 0

# Lê o primeiro número
numero = int(input("Digite um número (-1 para encerrar): "))

# Repete enquanto o número for diferente de -1
while numero != -1:

    # Adiciona o número à soma
    soma += numero

    # Conta a quantidade de números informados
    quantidade += 1

    # Solicita o próximo número
    numero = int(input("Digite um número (-1 para encerrar): "))

# Verifica se pelo menos um número foi informado
if quantidade > 0:

    # Calcula a média
    media = soma / quantidade

    # Exibe a soma e a média
    print("Soma:", soma)
    print(f"Média: {media:.2f}")

else:
    # Caso o usuário digite -1 logo no início
    print("Nenhum número foi informado.")