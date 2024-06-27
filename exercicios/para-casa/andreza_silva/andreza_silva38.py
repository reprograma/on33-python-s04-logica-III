#Exercicio 38
'''Um funcionário de uma empresa recebe aumento salarial anualmente: 
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;

Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

ano_inicial = int(input('Digite o ano de contratação: '))
ano_atual = int(input('Digite o ano atual: '))
salario_inical = float(input('Digite o seu salário inicial: '))
percentual = 0.015

novo_salario = salario_inical 

for i in range(ano_inicial, ano_atual + 1):
     novo_salario += salario_inical * percentual
     if i <= 1997:
          percentual *= 2
     print(f'Salário no ano {i}: R$ {novo_salario:.2f}')