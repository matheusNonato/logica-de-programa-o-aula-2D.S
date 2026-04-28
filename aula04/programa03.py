
"""

    sistema cauculadora

"""
while true: 
    print(*"=", "cauculadora", 30"=")
    print('1 soma')
    print('2 subtração')
    print('3 multiplicação')
    print('4 divisão')
    opção = input("digite a operação: (+,-,/,*)")

    match opçao
    case '1':
    resultado = num1 +num2
    print(f'{num1} + {num2}= {resultado}')
    break
    case '2':
    resultado = num1 - num2
    print(f'{num1} - {num2}= {resultado}')
    break
    case '3':
    resultado = num1 * num2 
    print(f'{num1} * {num2}= {resultado}')
    case '4':
    resultado = num1 / num2 
    print(f'({num1} / {num2} = {resultado}')
    case _:
    print('digite um numero invalido!')
    break 
