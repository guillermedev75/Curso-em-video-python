#Aplicação para calcular a área do retângulo

#função para calcular a área
def calc_area_retn(base,altura):

    #calculo
    area = base * altura
    return area

#Variaveis

#Entrada da base
base = float(input('Insira o valor da base do retângulo em Centimetros: '))

#Verificação da base
while(base <= 0):
    print('Insira um valor valido!')
    base = float(input('Insira o valor da base do retângulo em Centimetros: '))

#Entrada da Altura
altura = float(input('Insira o valor da altura do retângulo em Centimetros: '))

#Verificação da Altura
while(altura <= 0):
    print('Insira um valor valido!')
    altura = float(input('Insira o valor da altura do retângulo em Centimetros: '))

#Onde a função é chamada
area = calc_area_retn(base,altura)

#Onde o resultado é arredondado
areaRound = round(area,2)

#Onde o resutado da aplicação é impresso
print(f'A área do retângulo com a base de {base}Cm e altura de {altura}Cm é {areaRound}Cm2',
        f'\nPrecisamente {area}Cm2.')