#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. 
# A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

n = int(input('Digite um número inteiro: '))  # Aqui entra o numero do fatorial
numero = 1


for n in range (n, 0, - 1):
    print(n)
    
    numero *= n 

print(f'O fatorial desse número corresponde ao resultado da multiplicação dos números acima, que é {numero}.')
