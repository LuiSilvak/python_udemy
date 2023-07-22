# comandos if / elif / else
# comandos se / se não se / se não

# Comando de entrada
print("Olá usuário, seja bem vindo!")
comando = input("Digite para acessar: ")

if comando == 'entrar':
    print("Acesso liberado. Pode entrar!")
elif comando == 'sair':
    print("Você saiu!")
else:
    print("Você não informou nenhum dos dois comandos acima, tente novamente!")
print("Fim do Programa!")
