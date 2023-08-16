ent = input("Digite a hora em números inteiros: ")

try:
    hora = int(ent)

    if hora >= 0 and hora <= 11:
        print("Olá bom dia, em que posso lhe ajudar?")
    elif hora >= 12 and hora <= 17:
        print("Olá boa tarde, em que posso lhe ajudar?")
    elif hora >= 18 and hora <= 23:
        print("Olá boa noite, em que posso lhe ajudar?")
    else:
        print("Não conheço essa numeração, tente novamente!")
except:
    print("Por favor, digite apenas números inteiros")