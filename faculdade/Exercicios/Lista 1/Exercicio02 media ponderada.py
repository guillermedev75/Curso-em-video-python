#Aplicação que calcula a média ponderada do aluno com 3 notas

#Função que calcula a média ponderada do aluno
def calular_MP(n1,n2,n3):

    #Variaveis de peso
    p1 = 1
    p2 = 2
    p3 = 3

    #calculo de média
    MP = (( n1 * p1 ) + ( n2 * p2 ) + ( n3 * p3 )) / ( p1 + p2 + p3 )
    return MP

#Variaveis

#Nome do Aluno
nome = input('Qual o nome do aluno: ')

#Entrada da nota 1
n1 = float(input('Qual a primneira nota do aluno: '))

#Verificação da nota 1
while(n1 > 10):
    print("Digite um nota até no maximo 10!")
    n1 = float(input('Qual a primneira nota do aluno: '))


#Entrada nota 2
n2 = float(input('Qual a segunda nota do aluno: '))

#Verificação da nota 2
while(n2 > 10):
    print("Digite um nota até no maximo 10!")
    n2 = float(input('Qual a segunda nota do aluno: '))


#Entrada nota 3
n3 = float(input('Qual a terceira nota do aluno: '))

#Verificação da nota 3
while(n3 > 10):
    print("Digite um nota até no maximo 10!")
    n3 = float(input('Qual a terceira nota do aluno: '))


#Onde a função para calcular a média é chamada
MP = calular_MP(n1,n2,n3)

#Onde é impresso a média do aluno
print(f'A média ponderada de {nome} é {MP:.1f}')
