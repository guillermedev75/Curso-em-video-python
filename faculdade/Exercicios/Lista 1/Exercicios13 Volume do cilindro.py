#Aplicação para calcular o volume da uma caixa d'agua, ou de um cilindro

#Importando Biblioteca de matemática do python
import math

#Função para calcular o volume
def calc_vol_cil(raio,altura):

    #calculo
    volume = math.pi * (raio ** 2) * altura
    return volume

#Variaveis

#Entrada do raio do cilindro
raio = float(input('Insira o raio do cilindro em Centimetros: '))

#Verificação do raio
while(raio <= 0):
    print('Insira um valor valido!')
    raio = float(input('Insira o raio do cilindro em Centimetros: '))

#Entrada da altura do cilindro
altura = float(input('Insira a altura do cilindro em Centimetros: '))

#Verificação do raio
while(altura <= 0):
    print('Insira um valor valido!')
    altura = float(input('Insira a altura do cilindro em Centimetros: '))

#Onde a função é chamada
volume = calc_vol_cil(raio,altura)

#Onde o resultado da função é arredondado
volumeRound = round(volume,2)

#Onde o resultado da aplicação é impresso
print(f'O volume do cilindro de {raio}Cm de raio e {altura}Cm de altura é {volumeRound}Cm3',
        f'\nPrecisamente {volume}Cm3.')