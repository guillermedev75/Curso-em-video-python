#Aplicação para informar quantos litros foram pagos com X valor

#Função que calcular litro
def calcula_litro(prc,vpg): #Preço e Valor Pago

    #calculo
    litros = vpg / prc
    return litros

#Variaveis

#Entrada preço
prc = float(input('Quanto está o litro da gasolina? ')) 

#Verificação preço
while(prc <= 0):
    print('Insira o preço por litro correto!')
    prc = float(input('Quanto está o litro da gasolina? ')) 

#Entrada do Valor pago
vpg = float(input('Quanto foi pago? ')) 

#Verificação do valor pago
while(vpg <= 0):
    print('Insira o valor pago corretamente!')
    vpg = float(input('Quanto foi pago? ')) 

#Onde a função que chamada
litros = calcula_litro(prc,vpg)

#Onde o resultado é arredondado
litros = round(litros, 1)

#Onde é impresso o resultado da aplicação
print(f'Foram abastecidos {litros}Litros')
