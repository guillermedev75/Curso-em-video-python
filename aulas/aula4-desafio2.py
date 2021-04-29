nome=input('Qual seu nome? ')
dia=input(nome+' em que dia você nasceu? ')
mes=input(nome+ ' em que mês você nasceu? ')
ano=input(nome+ ' em que ano você nasceu? ')
anohoje=input(nome+ ' em que ano estamos? ')

idade=float(anohoje)-float(ano)

print(
    'Olá ', nome,
    '\nVocê nasceu em: ', dia, ' de ', mes, ' de ', ano,
    ' e tem ', idade, 'anos'
)