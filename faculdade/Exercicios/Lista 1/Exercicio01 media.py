#Aplicação para calcular a média de um aluno com 3 notas

#Função que calcula a media das 3 notas do aluno
def calcular_media(n1,n2,n3):
    media = ( n1 + n2 + n3) / 3
    return media

#Variaveis

#Nome do Aluno
nome = input('Qual o nome do aluno? ')

#Entrada da nota 1
n1 = float(input('Qual a primeira nota do aluno? '))

#Verificação do valor da nota 1
while(n1 > 10):
    print('Digite uma nota com valor maximo de 10!')
    n1 = float(input('Qual a primeira nota do aluno? '))

#Entrada da nota 2
n2 = float(input('Qual a segunda nota do aluno? '))

#Verificação do valor da nota 2
while(n2 > 10):
    print('Digite uma nota com valor maximo de 10!')
    n2 = float(input('Qual a segunda nota do aluno? '))

#Entrada da nota 3
n3 = float(input('Qual a terceira nota do aluno? '))

#Verificação do valor da nota 3
while(n3 > 10):
    print('Digite uma nota com valor maximo de 10!')
    n3 = float(input('Qual a terceira nota do aluno? '))

#Onda a função é chamada com as notas com atributo
media = calcular_media(n1,n2,n3)

#Onde é impresso o resultado da média do aluno
print(f'A média de {nome} é {media:.1f}')