entrada = input('Digite algo: ')

print(
    'Você digitou {}, que pode ser...' .format(entrada),
    '\nPode ser númerico:', entrada.isnumeric(),
    '\nPode ser alphabetico:', entrada.isalpha(),
    '\nPode ser alphanúmerico:', entrada.isalnum()
)