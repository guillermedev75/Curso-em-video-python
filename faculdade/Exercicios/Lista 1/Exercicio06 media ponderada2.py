#Aplicação para calcular média do aluno com duas notas sendo a segunda de peso 2

#Função para calular a média
def calcula_media(n1,n2):
    
    #Varieaveis de peso
    p1 = 1
    p2 = 2

    #calculo
    media = ((n1 * p1) * (n2 * p2)) /  (p1 + p2)
    return media

#Variaveis

#Nome do aluno
nome = input("Qual nome do aluno? ")

#Entrada da nota1
n1 = float(input('Qual a primeira nota do aluno? '))

#Verificação do valor da nota1
while(n1 > 10):
    print('Digite uma nota com o valor maximo de 10!')
    n1 = float(input('Qual a primeira nota do aluno? '))


#Entrada da nota2
n2 = float(input('Qual a segunda nota do aluno? '))

#Verificação da nota2
while(n2 > 10):
    print('Digite uma nota com o valor maximo de 10!')
    n2 = float(input('Qual a segunda nota do aluno? '))


#Onde é chamada a função
media = calcula_media(n1,n2)

#Onde o resutado da função é arredondado
media = round(media,1)

#Onde é impresso o resultado da aplicação
print(f'A média do aluno {nome} é {media}.')