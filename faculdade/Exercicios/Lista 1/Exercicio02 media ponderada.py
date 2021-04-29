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

#Notas do Aluno
n1 = float(input('Qual a primneira nota do aluno: '))
n2 = float(input('Qual a segunda nota do aluno: '))
n3 = float(input('Qual a terceira nota do aluno: '))

#Onde a função para calcular a média é chamada
MP = calular_MP(n1,n2,n3)

#Onde é impresso a média do aluno
print(f'A média ponderada de {nome} é {MP:.1f}')
