#Aplicação para calcular o IMC(Indice de massa comporal do individuo)

#Função para o calculo do IMC
def calcular_IMC(peso,altura):

    #calculo
    IMC = peso / (altura**2)
    return IMC

#Variaveis

#Nome do indiviuo
nome = input('Qual seu nome? ')

#Entrada do peso
peso = float(input('Qual seu peso? '))

#Verificação do peso
while(peso <= 0 or peso >= 500):
    print('Insira um peso valido!')
    peso = float(input('Qual seu peso? '))


#Entrada da altura
altura = float(input('Qual sua altura? '))

#Verificação da altura
while(altura <= 0 or altura >= 3):
    print('Insira uma altura valida!')
    altura = float(input('Qual sua altura? '))


#Onde a função é chamada
IMC = calcular_IMC(peso,altura)

#Onde o resultado é arrendondado
IMC = round(IMC, 1)

#Onde é impresso o resultado da aplicação
print(f'{nome} seu IMC é {IMC}')