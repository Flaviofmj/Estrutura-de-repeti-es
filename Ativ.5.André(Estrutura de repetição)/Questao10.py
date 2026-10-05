# QUESTAO 10 >  Leia uma frase digitada pelo usuário e, utilizando um laço for que percorra caractere a caractere, conte e 
# exiba quantas vogais ela contém.

# Lê uma frase e transforma todas as letras em minúsculas
frase = input("Digite uma frase: ").lower()

# Define as vogais
vogais = "aeiou"

# Contador de vogais
contador = 0

# Cria uma lista para armazenar as vogais encontradas
letras = []

# Percorre a frase caractere por caractere
for letra in frase:

    # Verifica se o caractere é uma vogal
    if letra in vogais:

        # Aumenta o contador em 1
        contador += 1

        # Adiciona a vogal na lista
        letras.append(letra)

# Exibe as vogais encontradas e a quantidade
print(f"Vogais na mensagem: {letras}")
print(f"Quantidade de vogais: {contador}")