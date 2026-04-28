#NOTE: boletim escolar 2.0


import os

os.system("cls")

print(30*"=", "boletim escolar", 30*"=")
lista_notas = []
nome= input("digite o nome do aluno: ").title()
curso = input("digite o curso: ").upper()

while True:
    notas = input("digite uma nota: ")
    notas = float(notas)
    lista_notas .append(notas)
    print(lista_notas)

    opcao = input("deseja adicionar mais notas? (s - sim | não)")

    if opcao == "n":
        break
media = sum(lista_notas) / len(lista_notas)
print(media)