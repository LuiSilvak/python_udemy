nome = input("Informe o seu nome: ")
altura = float(input("Digite o seu altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura ** 2)

#print(f"Olá {nome}! O seu IMC é igual a {imc:.2f}")
print(f"{nome} tem {altura} de altura,")
print(f"pesa {peso:.1f} quilos e seu IMC é")
print(f"{imc:.2f}")