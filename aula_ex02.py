"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print("Olá usuário! Tudo bem?")
pergunta = input("Que horas são? ")

if pergunta.isdigit():
    hora = int(pergunta)
    if (hora >= 0) and (hora <= 11):
        print("Bom dia, em que posso ajudar?")
    elif (hora >= 12) and (hora <= 17):
        print("Boa tarde, em que posso ajudar?")
    elif (hora >= 18) and (hora <= 23):
        print("Boa noite, em que posso ajudar")
    else:
        print("Ultrapassou da numeração permitida, tente novamente!")
else:
    print("Dígito errado, tente novamente!")