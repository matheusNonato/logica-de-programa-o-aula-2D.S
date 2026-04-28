"""
    Calculos e manipulação de variaveis
"""

nome = input("digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = input("Digite o seu peso: ")
altura = input("Digite a sua altura: ")
#tratamento de exceção

try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
except ValueError as e:
    print(e)


imc = peso/(altura*altura)
print("Seu IMC é: ",imc)