#Aplicação para calcular o IMC(Indice de massa comporal do individuo)

#Função para o calculo do IMC
def calcular_IMC(peso,altura):

    #calculo
    IMC = peso / (altura**2)
    return IMC

#Variaveis

#Nome do indiviuo
nome = input('Qual seu nome? ')

#Atributos
peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

#Onde a função é chamada
IMC = calcular_IMC(peso,altura)

#Onde o resultado é arrendondado
IMC = round(IMC, 1)

#Onde é impresso o resultado da aplicação
print(f'{nome} seu IMC é {IMC}')