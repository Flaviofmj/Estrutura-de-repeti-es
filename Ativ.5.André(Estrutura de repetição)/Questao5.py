# QUESTÃO 5 > Leia N números digitados pelo usuário (N informado previamente) e calcule a média aritmética entre eles, 
# utilizando um laço for.

# Lê a quantidade de números que serão informados
n = int(input("Digite a quantidade de números: "))

# Inicializa a variável soma com 0
soma = 0

# Repete o laço de acordo com a quantidade de números informada
for i in range(1, n + 1):

    # Lê um número informado pelo usuário
    numero = float(input("Digite um número: "))

    # Adiciona o número digitado à variável soma
    soma += numero

# Calcula a média dividindo a soma pela quantidade de números
media = soma / n

# Exibe a média com duas casas decimais
print(f"A média aritmética é: {media:.2f}")