# QUESTÃO 8 >  Utilizando um laço do-while, solicite repetidamente que o usuário digite uma senha, encerrando apenas 
# quando a senha correta ("1234") for informada. 

# Solicita a senha pelo menos uma vez
while True:

    # Lê a senha informada pelo usuário
    senha = input("Digite a senha: ")

    # Verifica se a senha está correta
    if senha == "1234":

        # Encerra o laço
        break

    # Informa que a senha está incorreta
    print("Senha incorreta! Tente novamente.")

# Mensagem exibida quando a senha estiver correta
print("Senha correta! Acesso permitido.")