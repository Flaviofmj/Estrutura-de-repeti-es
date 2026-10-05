# QUESTÃO 7 >  Leia um número inteiro não negativo e calcule o seu fatorial, utilizando um laço for.

# Lê um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Inicializa o fatorial com 1
fatorial = 1

# Percorre os números de 1 até o número informado
for i in range(1, numero + 1):

    # Multiplica o fatorial pelo número atual
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é: {fatorial}")