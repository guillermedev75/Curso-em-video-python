#Aplicação para decobrir o participante com maior nota

#Número de participantes
num_participantes = int(input('Quantos participantes são: '))

#Variaveis globais
participante_vencedor = 'ninguem'
nota_vencedor = 0

#Laço para calcular a maior nota
for contador in range(num_participantes):

    #Nome e nota do participante atual
    participante = input(f'Qual o nome do {contador+1}° Participante: ')
    nota = float(input(f'Qual a nota do {contador+1}° Participante: '))

    #Virifica se é o primeiro participante
    if contador == 0 or nota > nota_vencedor:

        #nota vencedora atual
        participante_vencedor = participante
        nota_vencedor = nota

#Impresso o participante vencedor
print(f'{participante_vencedor} venceu com nota {nota_vencedor}!')