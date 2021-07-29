#Aplicaçao para calcular a área do quadrado

#Função para calcular a área
def calc_area_quadrado(lado):

    #Calculo
    area = lado ** 2
    return area

#Variaveis

#Entrada do lado do quadrado
lado = float(input('Insira o lado do quadrado em Centimetros: '))

#Verificação do lado
while(lado <= 0):
    print('Insira um valor valido!')
    lado = float(input('Insira o lado do quadrado em Centimetros: '))

#Onde a função é chamada
area = calc_area_quadrado(lado)

#Onde o valor é arredondado
areaRound = round(area,2)

#Onde o valor é impresso
print(f'A área do quadrado de lado {lado}Cm é {areaRound}Cm2' , f'\nPrecisamente {area}Cm2')