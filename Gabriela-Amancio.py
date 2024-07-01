# 1. Calculadora com Inputs do Usuário

def calculadora():
    while True:
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        escolha = input("Digite a escolha (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Saindo da calculadora.")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif escolha == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Erro! Divisão por zero.")
        else:
            print("Escolha inválida, tente novamente.")

calculadora()

#2. Sistema para Calcular o Aumento de Salário

def aumento_salario():
    while True:
        salario_atual = float(input("Digite o salário atual do funcionário: "))
        percentual_aumento = float(input("Digite o percentual de aumento: "))
        
        novo_salario = salario_atual + (salario_atual * percentual_aumento / 100)
        print(f"Novo salário após aumento de {percentual_aumento}%: {novo_salario}")
        
        continuar = input("Deseja calcular o aumento para outro salário? (s/n): ")
        if continuar.lower() != 's':
            break

aumento_salario()


#3. Sistema que Calcula o Fatorial de um Número Inteiro
def calcular_fatorial():
    while True:
        numero = int(input("Digite um número inteiro para calcular o fatorial: "))
        
        if numero < 0:
            print("Número inválido! O fatorial não é definido para números negativos.")
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f"O fatorial de {numero} é {fatorial}")
        
        continuar = input("Deseja calcular o fatorial de outro número? (s/n): ")
        if continuar.lower() != 's':
            break

calcular_fatorial()
