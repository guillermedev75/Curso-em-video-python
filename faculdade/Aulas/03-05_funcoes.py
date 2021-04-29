def calcular_quadrado(valor):
    quadrado = valor * valor
    return quadrado

valor = float(input('Informe um número: '))

quadrado = calcular_quadrado(valor)
print(f'O quadrado de {valor} é {quadrado}.')