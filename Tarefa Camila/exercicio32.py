#Programa calculo Fatorial:

print("Faça cálculos com a fatorial de 5")

numero = int(input("Digite um número para encontrar seu fator:"))
contador = 1


for i in range(numero,0,-1):
    contador *= i 
    print(f"{numero}! = {contador}")
    
    
print("Você finalizou o cálculo!")


    