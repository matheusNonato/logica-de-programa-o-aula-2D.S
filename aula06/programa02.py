'''

Desenvolva um sistema de gerenciamento de Carros com realizações do CRUD

'''
import os
import time

carros = []
proximo_id = 1


while True:
    os.system('cls')
    print(6*'=', 'Sistema de carros', 6*'=')
    print('1 -Cadastrar carro')
    print('2 - Listar carros')
    print('3 - Atualizar carro')
    print('4 - Deletar carro')
    print('0- Sair')

    opcao = input('Escolha uma opção: ')
    #criar
    if opcao == '1':
        modelo = input('Digite o modelo do carro: ').title()
        preco = float(input('Digite o preço: '))
        marca = input('Digite a marca: ').title()

        carro = {
            "id" : proximo_id,
            "modelo" : modelo,
            "preco" : preco,
            "marca" : marca
        }

        carros.append(carro)
        proximo_id += 1

        print('✅ Carro cadastrado com sucesso!\n')
        time.sleep(3)
    #read
    elif opcao == '2':
        if not carros:
            print('⚠️  Não há nenhum carro registrado')
        else:
            print('\n 📋 Lista de carros')
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preco']} | Marca: {carro['marca']}\n')
                time.sleep(3)
    
    elif opcao == '3':
        print('\n 📋 Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preco']} | Marca: {carro['marca']}')
            time.sleep(1.5)
        id_busca = int(input('Digite o ID do carro para alterar: '))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo = input('Digite o novo modelo:').title()
                novo_preco = float(input('Digite o novo preço:').replace(',', '.'))
                nova_marca = input('Digite a nova marca:').title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = nova_marca

                print('✅ Carro atualizado com sucesso! \n')
                encontrado = True
                time.sleep(3)
                break
        if not encontrado:
                print('❌ Carro não encontrado!\n')
                time.sleep(3)
    #delta
    elif opcao == '4':
        print('\n 📋 Lista de carros')

        if not carros:
            print('⚠️  Não há nenhum carro registrado')
        else:
            for carro in carros:
                print(f"ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preco']} | Marca: {carro['marca']}")
                time.sleep(1.5)

            id_busca = int(input('Digite o ID do carro para deletar: '))

            encontrado = False

            for carro in carros:
                if carro['id'] == id_busca:
                    carros.remove(carro)
                    print('✅ Carro deletado com sucesso!\n')
                    encontrado = True
                    time.sleep(3)
                    break

            if not encontrado:
                print('❌ Carro não encontrado!\n')
                time.sleep(3)
    #sair
    elif opcao == '0':
        total = 20
        barra = ""
        print('Saindo do sistema...')
        for i in range(1, total+1): 
            barra += '🟩'
            porcentagem = int((i/total)*100)
            vazio = '🔳'*(total -i)
            print(f'\r[{barra}{vazio}] {porcentagem}%', end="")
            time.sleep(0.3)
        break
    else: 
        print('❌ Opção invalida!')