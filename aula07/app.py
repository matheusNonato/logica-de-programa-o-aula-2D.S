'''
    Manipulação de arquivos: percorrer os meus diretorios, encontrar o arquivo
    passar o comando de abertura de arquivo, passar comando de ação.

    arquivo = open('arquivo.txt', 'modo')

    Modulos de ação:
        - "r" : Leitura do arquivo
        - "w" : Escrita(sobrescreve  o conteudo antigo) 
        - "a" : Adiciona conteudo
        - "x" : Criar um arquivo
        - "b" : Aruqivos binarios
        - "t" : Texto
'''
arquivo = open('primeiro_arquivo.txt', 'w')
arquivo.write('Ola, mundo!!!!Este e meu primeiro arquivo')
arquivo.close()

#Lendo o arquivo
arquivo = open("primeiro_arquivo.txt", 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica
with open('primeiro_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#arquivo com multiplas escreitas
with open('alunos.txt', 'w') as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('joão\n')
    arquivo.write('Lucas\n')
    arquivo.write('Gomes\n')
    arquivo.write('Karython\n')

#Lendo linha a linha
with open('alunos.txt', 'r')as arquivo:
    for linha in arquivo:
        print(linha)

#Usando lista para ezcrever um arquivo
frutas = ['pera', 'abacaxi', 'melancia', 'manga', 'caju']

with open('frutas.txt', 'w') as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

#Converter o arquivo em uma lista
with open('frutas.txt', 'r')as arquivo:
    linhas = arquivo.readlines()
print(type(linhas))
print(linhas)

#Saida: ['pera\n', 'abacaxi\n', 'melancia\n', 'manga\n', 'caju\n']

#limpar a quebra de linha

with open('frutas.txt', 'r')as arquivo:
    for linha in arquivo:
        print(linha.strip(), "\n")


# exemplo para cadastro

while True:
    nome = input('Digite o seu nome: ').title()
    with open('cadastro.xml', 'a') as arquivo:
        arquivo.write(nome + '\n')

    sair = input('Deseja sair do sistema? s/n \n').lower()

    if sair == 's':
        break
    