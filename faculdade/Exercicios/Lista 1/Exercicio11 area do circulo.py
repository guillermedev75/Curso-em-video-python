#Aplicação para calcular a área do circulo

#Importando a biblioteca de matematica do python
import math

#Função para calcular a área
def calc_area_circ(raio):

    #calculo
    area = math.pi * (raio ** 2)12
    return area

#Variaveis

#Entrada do Raio do circulo
raio = float(input('Insira o valor do raio do circulo em centimetros: '))

#Verificação do raio
while(raio <= 0):
    print('Insira um valor valido!')
    raio = float(input('Insira o valor do raio do circulo em centimetros: ')) 

#Onde a função é chamada
area = calc_area_circ(raio)

#Onde o resultado da função é arredondado
areaRound = round(area,2)

#Onde é impresso o resultado da aplicação
print(f'A área do circulo com {raio}Cm de raio é {areaRound}Cm2',
        f'\nPrecisamente {area}Cm2.')
