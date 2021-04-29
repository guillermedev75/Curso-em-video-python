#Aplicação para informar quantos litros foram pagos com X valor

#Função que calcular litro
def calcula_litro(prc,vpg): #Preço e Valor Pago

    #calculo
    litros = vpg / prc
    return litros

#Variaveis

#Atributos (Preço e Valor Pago)
prc = float(input('Quanto está o litro da gasolina? ')) 
vpg = float(input('Quanto foi pago? ')) 

#Onde a função que chamada
litros = calcula_litro(prc,vpg)

#Onde o resultado é arredondado
litros = round(litros, 1)

#Onde é impresso o resultado da aplicação
print(f'Foram abastecidos {litros}Litros')
