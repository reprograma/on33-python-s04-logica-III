#Tabuada de 5

print("Tabuada de 5")
numero = int(input("Digite um número para sua multiplicação:"))
multiplicador = 5

for numero in range(4,8,1):
    resultado = numero * multiplicador
    print(f"O resultado de {multiplicador} x {numero} é : {resultado} ")

print("Resultado final!")
