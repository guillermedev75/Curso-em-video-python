nome=input('Qual seu nome?')
sobrenome=input('Qual seu sobrenome?')
idade=input('Qual sua idade ' + nome+'?')
peso=input('Qual seu peso '+ nome+ '?')
altura=input('Qual sua Altura ' + nome+ '?')

alturaimc=float(altura)*float(altura)
imc=float(peso)/float(alturaimc)

print(  'Nome: ', nome,
        '\nSobrenome: ', sobrenome,
        '\nIdade: ', idade, 'Anos',
        '\nPeso: ', peso, 'Kg',
        '\nAltura: ', altura, 'M')

print(  'Seja bem-vindo ', nome,sobrenome,'!',
        '\nSeu IMC é: ', int(imc))

