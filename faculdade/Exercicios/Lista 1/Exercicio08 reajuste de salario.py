#Aplicaçao para calcular o reajuste do salario

#Função para calcular o reajuste
def calc_reajuste(salario_atual,reajuste):

    ##Calcula o reajuste do salario
    reajusteSalario = salario_atual * (reajuste / 100)

    #Soma o salario atual com o reajuste
    salario_reajustado = salario_atual + reajusteSalario
    return salario_reajustado

#Variaveis

#Entrada do salario atual
salario_atual = float(input('Insira o salario atual do funcionario: '))

#Verificação do salario
while(salario_atual <= 0): #O salario n pode ser igual ou menor que zero
    print('Insira o salario correto!')
    salario_atual = float(input('Insira o salario atual do funcionario: '))

#Entrada da porcentagem de reajuste
reajuste = float(input('Insira a porcentagem de resjuste do salario: '))

#Verificação do reajuste
while(reajuste <= -100): #O reajuste não pode ser maior ou igual a -100% do salario 
    print('Insira o reajsute correto!')
    reajuste = float(input('Insira a porcentagem de resjuste do salario: '))

#Onde a Função é chamada
salario_reajustado = calc_reajuste(salario_atual,reajuste)

#Onde os dados são arredados
salario_atual = round(salario_atual,2)
salario_reajustado = round(salario_reajustado,2)

#Onde é impresso o resultado da aplicação
print(f'O salario de {salario_atual} sofreu um reajuste de {reajuste}% e foi para {salario_reajustado}.')