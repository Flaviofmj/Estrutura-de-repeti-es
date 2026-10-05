# QUESTÃO 12 > Leia um número inteiro N e, utilizando um laço for, exiba os N primeiros termos da sequência de 
# Fibonacci. 

# Lê a quantidade de termos da sequência
N = int(input("Digite a quantidade de termos: "))

# Primeiros dois números da sequência de Fibonacci
a = 0
b = 1

# Repete N vezes
for i in range(N):

    # Exibe o termo atual
    print(a)

    # Calcula o próximo termo
    proximo = a + b

    # Atualiza os valores
    a = b
    b = proximo