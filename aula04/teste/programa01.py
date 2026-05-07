'''
programa01 - aula04 - 28/04
prof: kyrothon gomes
turma: 2 d.s

sistema de sorteios 1,0 
'''

import os 
import random 

lista_nomes = ['Matheus', 'arthur', 'alexandre', 'macaé', 'pedro cintra', 'josé ribeiro', 'natanael', 'tanaka', 'julio',
 'pedro', 'henrique', 'joel', 'pedro abelha']
 

 sorteados = 0 
 while sorteados < 5: 
    nome_sorteado = random.choice (lista_nomes)
    print(f'sorteado: {nome_sorteados}')
    lista_sorteados.append(nome_sorteados)

    for i in lista_sorteados:
        print(f'lista de sorteados (i)')

        sorteados +=1

        print('fim do programa')
        