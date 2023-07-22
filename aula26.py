"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input("Informe um número: ")

try:
    numero_float = float(numero)
    print('FLOAT: ',numero_float)
    print(f"O dobro do número {numero_float} é igual a {numero_float * 2:.2f}")
except:
    print("Isso não é um número")

#if numero.isdigit():

#else:
    #print("Isso não é um número")