#Aplicação para voto obrigatorio

#Função para verificar a idade obrigatoria
def voto_obrigatorio(idade):

    #Verificação
    return idade >= 18 and idade < 70

idade = int(input('Qual sua idade; '))
print(voto_obrigatorio(idade))