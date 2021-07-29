#Aplicação para calcular a gorjeta do garçom

#Função para calcular
def gorjeta(total):

    #variaveis
    desc_gorjeta = 10 #Desconto para a gorjeta do garçom

    #calculo
    gorjeta = total * (desc_gorjeta / 100)
    return gorjeta

#Variaveis

#Entrada do total
total = float(input('Qual o total da nota? ')) #Total da nota

#Verificação do total
while(total < 0):
    print('Insira o valor correto')
    total = float(input('Qual o total da nota? '))

#Onde a função é chamada
gorjeta = gorjeta(total)

#Onde o resultado da função é arrendondado
gorjeta = round(gorjeta,2)

#Onde é impresso o resultado da aplicação
print(f'A gorjeta do garço é {gorjeta} de {total}.')