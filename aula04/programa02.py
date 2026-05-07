'''
    Programa 01 - Aula04 28/04
    Prof: Karython Gomes
    Turma: 2º DS

    Sistema de sorteio 2.0
'''
import os
import random
import time

lista_nomes = []
lista_sorteados = []

print (30*"-","Bem vindo ao sistema de sorteios", 30*"-")

while True:
    nome = input ("Digite um nome para ser selecionado: ")
    lista_nomes.append(nome)
    
    opcao = input ("\nDeseja adicionar mais?\n (s - sim, Enter para parar.)\n")

    if opcao != "s":
        break

while True:    
    if not lista_nomes:
        print ("A lista de nomes esta vazia.")
        break
    else:
        nome_sorteado = random.choice(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        lista_sorteados.append(nome_sorteado)
        os.system('cls')


    for i in range (5):
        time.sleep(1)
        os.system('cls')
        print(f'Contagem regressiva...{i}')
        i -= 1 

    os.system('cls')

    print (f'O sorteado foi... {nome_sorteado}')

    sortear_novamente = input ("\nDeseja adicionar mais?\n (s - Sim | n - Não)\n") 

    if sortear_novamente == 'n':
        break
    else:
        continue
        print("lista_sorteados")
print ("Fim do programa.")