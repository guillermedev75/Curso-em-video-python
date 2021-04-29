def calcular_imc(valor1,valor2):
    valor2q = valor2 ** 2
    imc = valor1 / valor2q
    return imc

valor1 = float(input('Qual seu peso: '))
valor2 = float(input('Qual sua altura: '))


imc = calcular_imc(valor1,valor2)
print(f'Seu imc é {imc:.1f}.')