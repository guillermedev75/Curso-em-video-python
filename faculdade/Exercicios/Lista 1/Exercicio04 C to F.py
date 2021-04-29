#Apilicação que converte a representção da temperatura de Celsius para Fahrenheit

#Função de conversão C to F
def converte_CtoF(tempC):

    #Calculo
    tempF = ( tempC * 9/5 ) + 32
    return tempF

#Variaveis

#Temperatura em Celsius
tempC = float(input('Insira a temperatura em celsius: '))

#Onde a função é chamada
tempF = converte_CtoF(tempC)

#Onde o resultado em fahrenheit é arredondado
tempF = round(tempF,2)

#Onde é impresso o resultado da aplicação
print(f'A temperatura é {tempF}°F')