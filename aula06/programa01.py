'''
1. crie um programa que o usuario posssa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente.

2. crie um programa que o usuario possa digitar a quantidade desejada de notas de um determinado aluno (nota minima  0 e nota maxima 10) e o programa caucula  a media desse aluno,
 e ao final imprima se o aluno esta (aprovado >=7, reprovado recuperação >= 5) 
'''
# atividade 
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
