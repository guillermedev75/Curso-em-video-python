#Aplicação que calcula a área da esfera

#Importando a Biblioteca de matemática do python
import math

#Função para calcular a área
def calc_area_esfe(raio):

    #calculo
    area = (math.pi * 4) * (raio ** 2)
    return area

#Variaveis

#Entrada do raio
raio = float(input('Insira o valor do raio da esfera em Centimetros: '))

#Verficação do raio
while(raio <= 0):
    print('Insira o valor correto do raio da esfera!')
    raio = float(input('Insira o valor do raio da esfera em Centimetros: '))

#Onde a função é chamada
area = calc_area_esfe(raio)

#Onde o resultado da função é arredondado
areaRound = round(area,2)

#Onde o resutado da aplicação é impresso
print(f'A área da esfera com raio de {raio}Cm é {areaRound}Cm2',
        f'\nPrecisamente {area}Cm2.')