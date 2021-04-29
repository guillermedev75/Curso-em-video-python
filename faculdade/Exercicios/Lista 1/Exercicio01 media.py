#Aplicação para calcular a média de um aluno com 3 notas

#Função que calcula a media das 3 notas do aluno
def calcular_media(n1,n2,n3):
    media = ( n1 + n2 + n3) / 3
    return media

#Variaveis

#Nome do Aluno
nome = input('Qual o nome do aluno? ')

#Notas do aluno
n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))
n3 = float(input('Qual a terceira nota do aluno? '))

#Onda a função é chamada com as notas com atributo
media = calcular_media(n1,n2,n3)

#Onde é impresso o resultado da média do aluno
print(f'A média de {nome} é {media:.1f}')