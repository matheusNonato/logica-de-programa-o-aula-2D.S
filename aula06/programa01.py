'''
1. crie um programa que o usuario posssa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente.

2. x
'''
# Atividade 1
l_num = []

while True:
     num = float(input("digite um numero"))
     l_num.append(num)

     add = input('pressione +/= para adicionar mais um numero\n pressioneenter para continuar o programa.0\n')

     if add != "=":
        break
     else:
        False 
l_num.sort()
print(l_num)

lista_numeros = []




# Atividade 2 
