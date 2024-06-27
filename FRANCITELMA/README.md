# Atividade de Aplicação de Estrutura de Repetição


## Descrição


Estes são projetos de atividade de casa da quarta semana do curso de Python: análise de dados solicitado pela professora Stefany Gracy da parte de Lógica III

O projeto usa de inputs do usuário para realizar as tarefas: criação de uma tabuada de um número qualquer inteiro com valor inicial e final determinados, criação de um programa que determine o salário atual de um funcionário em determinado ano com acréscimo de aumento e  outro com valor inicial de salario fornecido pelo usuário,  criação de um programa que calcule o fatorial de um número inteiro , utilizando-se de 'for' e 'while'.


## Implementação


A partir do uso de 'for' e 'while' será criado programas:

Questão 36: O usuário vai fornecer um numero qualquer inteiro, logo em seguida será pedido outro numero qualquer inteiro para multiplica-lo com o primeiro e por ultimo, será pedido mais um numero que será o limite, onde irá parar a multiplicação. Será utilizado o comando "while":

```
while contador <= final:

  resultado = numero * contador

  print(f"{numero} x {contador} = {resultado}")

  contador += 1

  print("Prontinho!")
```


Questão 38: Criação de um programa para saber o salario de um empregado em determinado ano fornecido pelo usuário. O salário inicial e o ano de entrada na empresa já são determinados pelo programa. A partir do ano seguinte, é determinado um aumento salarial, a principio de 1,5% e nos anos subsequentes, o dobro do anterior. Será utilizado o comando "for":

```
ano_inicio = 1995

ano_atual = int(input("Digite o ano de pesquisa: ")) 

salario_inicial = 1000.00

percentual_de_aumento = 0.015 

salario = salario_inicial  

for i in range(ano_inicio + 1, ano_atual + 1):  

   salario += salario * percentual_de_aumento 

   if i <= 1997:                 

​    percentual_de_aumento *= 2

print(f"Salário no ano de {ano_atual}: R$ {salario:.2f}")
```


Logo em seguida, ainda na mesma questão, haverá uma alteração no programa para que o usuário agora digite também o valor inicial do salario, juntamente com o ano que deseja saber a atualização da remuneração. Também será utilizado o comando "for":

```
ano_inicio = 1995

ano_atual = int(input("Digite de pesquisa: ")) 

salario_inicial = float(input("Digite o salário inicial: ")) 

percentual_de_aumento = 0.015 

salario = salario_inicial  

for i in range(ano_inicio + 1, ano_atual + 1):  

   salario += salario * percentual_de_aumento 

   if i <= 1997:                 

​    percentual_de_aumento *= 2

print(f"Salário no ano de {i}: R$ {salario:.2f}")
```


Questão 32: Criação de um programa para calculo de fatorial de um numero qualquer inteiro que será pedido ao usuário. A exibição da resposta será a maneira didática da representação de fatorial. Para esse programa foi usado o comando "for":

```
numero = int (input("Forneça um numero para saber a a fatorial dele:"))

mult = 1

sequencia = ""

for i in range(numero, 0,-1):

  mult *= i

  sequencia += str(i) + "."

sequencia = sequencia.rstrip(".")



print(f"Fatorial de: {numero} \n {numero}! = {sequencia} = {mult}")
```


## Uso do Projeto

- primeira questão;

O usuário dá entrada no input de três números inteiros:

O sistema mostrará uma calculadora gerada com essas informações.

- segunda questão;

O usuário digitara o ano de pesquisa para saber a remuneração de um funcionário no ano especificado, com as atualizações de percentual de aumento:

O sistema mostrará o valor naquele ano fornecido, com o reajuste devido.

O usuário digitara o valor inicial e o ano de pesquisa para saber a remuneração de um funcionário no ano especificado, com as atualizações de percentual de aumento: 

O sistema mostrará o valor naquele ano fornecido, respectivamente proporcional ao valor  cedido, com o reajuste devido.

- terceira questão;

  O usuário fornece um valor inteiro para saber o fatorial dele:

  O sistema mostrará o resultado fatorial desse numero e mostrará de maneira didática seu resultado.