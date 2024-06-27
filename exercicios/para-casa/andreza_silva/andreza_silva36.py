#Exercicio 36
numero = int(input('Escolha um número: '))

print(f'Hoje vamos calcular a tabuada do {numero}, da maneira que você escolher.')
fator1 = int(input('Começa por: '))
fator2 = int(input('Termina em: '))


while fator1 < fator2:
    resultado = numero * fator1
    print(f'O {numero} multiplicado por {fator1} é igual: {resultado}')
    fator1 += 1

if fator1 <= fator2:
     print('Os dados estão corretos!')
else:
    print('O número inicial deve ser menor que o final!')

