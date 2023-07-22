nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = int(input("Qual é a sua idade? "))
altura_metros = float(input(("Informe sua altura em metros: ")))

ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18


print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print('É maior de idade? ', maior_de_idade)
print('Altura em metros: ', altura_metros)

