# 📝 Estruturas de Repetição

## 📚 Descrição da Atividade

Exercicios da semana 04 para casa.

## 📋 Passo a Passo

## 32.
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120

1. definir funcao para calcular o fatorial

        def calcular_fatorial(numero):
             fatorial = 1
             for i in range(1, int(numero) + 1): #tive que transformar #a entrada para int.
             fatorial *= i
        return fatorial      
    
2. solicitar ao usuario um número inteiro
   
        numero = input("Insira um número inteiro: ")

3. chamar a funcao definida acima para calcular o fatorial com o numero inserido pelo usuario.
   
        resultado = calcular_fatorial(numero)

4. exibir o resultado do calculo.
   
        print(f'Fatorial de: {int(numero)}')
        print(f"{int(numero)}! = {' . '.join(str(i) for i in range(int(numero), 0, -1))} = {resultado}")

## 36.
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

1. solicitar ao usuario números
   
       numero = int(input("Digite um número para ser multiplicado: "))
       multiplicador_inicial = int(input("Digite um número para ser o multiplicador inicial:"))
       multiplicador_final = int(input("Digite outro número para ser o multiplicador final:"))

2. calcular a tabuada
   
       while multiplicador_inicial <= multiplicador_final:
           resultado = numero * multiplicador_inicial
           print(f"{numero} x {multiplicador_inicial} = {resultado}")
           multiplicador_inicial += 1

## 38. Part I
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário. 

1. Salário inicial em 1995
   
       salario_inicial = float(1000)

2. Aumento salarial
   
       aumento_inicial = float(1.5/100)

3. calcular o salário anual
   
       for ano in range(1996, 2023):
           salario_inicial += salario_inicial * aumento_inicial
           aumento_inicial *= 2 

       print(f'O salário atual deste funcionário é de: R$ {salario_inicial:.2f}')

## 38. Part II
Altere o programa permitindo que o usuário digite o salário inicial do funcionário.

1. Usuario digita seu salário inicial
   
       salario_inicial = float(input('Digite seu salário em reais: '))

3. ano de contratacao

       ano_contratacao = 1995

4. Variavel de aumento de salário anual.

       aumento_inicial = float(1.5/100)

6. calcular o salário anual

       for ano in range(1996, 2023):
           salario_inicial += salario_inicial * aumento_inicial
           aumento_inicial *= 2 

       print(f'Seu salário atual é de: R$ {salario_inicial}')

## 🔚   
