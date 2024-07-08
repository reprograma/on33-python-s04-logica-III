#Calculo Salário Funcionário

#ano contratação = 1995
#valor inicial = 1000
#ano2 = 1000 + 1,5% de 1000
#ano3 = (1000 + 1,5% de 1000) x 2
#salarioatual???

ano1 = 1995
ano2 = 1996

salario1 = 1000
percentual_aumento = 1.5
salario2 = salario1 + (salario1 * percentual_aumento/100)

print("Descubra o valor do seu salário por ano")
ano = int(input("Digite o ano: "))

for ano in range(1997,ano,1):
    percentual_aumento *= 2
    salarioatual = salario2 + (salario2 * percentual_aumento/100)
print(f"O salário para {ano} é {salarioatual}")

    
