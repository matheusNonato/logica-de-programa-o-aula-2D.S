#função com parametro
'''def funcão_segundo_grau(a, b, c):
    return a +b +c 

#chamando a função e armazenando o valor em uma variavel 
x = funcão_segundo_grau(1, 2, 3)
print(x)

def soma(a,b):
    resultado = a + b 
    return resultado 

num1 = int(input("digite um numero qualquer"))
num2 = int(input("digite um numero qualquer"))

resultado = soma(num1,num2)
print(resultado) '''''


def mostrar_saudacao(nome):
    print(f'olá {nome}, seja bem-vindo!')

mostrar_saudacao('Matheus')

#função recursiva
def fatorial(n):
    # n!
    return 1 if n == 0 else n*fatorial(n-1)

import os 

#função lambda
somar = lambda x, y: x+y
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
# algoritimo principal
if __name__ == "__main__":
    try:
        
        x = int(input("informe o valor de x: "))
        y = int(input("informe o valor de y: "))
        result = somar(x,y)

        limpar()
        print(f"o resultado da soma é. {result}.")
    except Exception as e:
        print(f'não foi possivel somar {e}.')