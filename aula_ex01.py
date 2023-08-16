"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

print("Seja bem vindo usuário!")
entrada = input("Digite um número inteiro: ")

if entrada.isdigit():
    num_int = int(entrada)
    if num_int % 2 == 0:
        print("Este número é par!")
    else:
        print("Este número é ímpar!")
else:
    print("Você não digitou um número inteiro!")