lista = ['matheus, miguel, lucas, ribeiro']

print('lista')

#imprimindo valor especifico da lista
print('lista[0]')

#imprimindo ultimo indice 
print('lista[-1]')

#imprimir intervalo
print('lista[2:4]')

#ordenar esta lista
lista.sort()

# adicionado na lista
lista.append('matheus')

# inserindo a posição especifica
lista.insert(2,'joão')

# inserindo varios valores
lista.extend(['matheus','miguel','lucas'])
numeros = []

for i in range(10):
    numeros.append(i * 2)
print(numeros)

#removendo itens da lista
print(f'lista antes de remover {lista}')

# pop-remove pelo indice
lista.pop(0)

# removendo o ultimo indice
lista.pop()

#removendo pelo valor, (remove a primeira ocorrencia)
lista.remove('matheus')



lista_numeros = [ n for n in range(1,11)]
# removendo intervalo de valores 
print(f'lista antes de remover{lista_numeros}')
del lista_numeros[2:4]


print(f'lista depois de remover {lista}')

listanomes= ['matheus', 'miguel', 'lucas', 'ribeiro']
# alteração valor da lista
listanomes[1] = 'lucas'

print(listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[1] * 2
        print(numeros)

numeros2 = [10,20,30,40,50]       

# list compriension
numeros2 = [n * 2 if n > 20 else n for n in numero2]
print(numeros)
