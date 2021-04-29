
#xuxa = '='
#while xuxa == "+" | "-" | "/" | "*":
#
 #   start = int(input('Insira um número: '))
  #  xuxa = str(input('Soma: +'+'\nSubtração: -'+'\nDivisão: /'+'\nMultiplicação: *'+'\nResultado: ='+'\nInsira a operação: '))

entrada = int(input('digita: '))
soma = 0

while entrada != 0:
    entrada = int(input())
    soma += entrada
    entrada = int(input('digita: '))
print(soma)

verif = 0

while verif != 1:
    