#Faça um algoritmo que receba o nome e o salário de um funcionário e calcule conforme as regras:
#Salários abaixo de R$ 1.000,00: aumento de 40% | entre 1.000,00 e R$ 1.999,00: aumento de 30%
#Salários entre R$ 2.000,00 até R$ 2.999,00: aumento de 20% |Acima de R$ 3.000,00: calcular 10%
#O algoritmo deverá calcular e escrever o resultado conforme o modelo: Fulano, o valor de aumento do seu salário foi XXX reais e o seu novo salário será yyyy reais.

nome=str(input("Entre com o nome do funcionário: "))
salario=float(input(f"Entre com o salário do funcionário {nome}: "))

if salario < 1000:

    novo_salario = salario*1.4

elif 1000 <= salario <= 1999:

    novo_salario = salario*1.3
    
elif 2000 <= salario <= 3000:

    novo_salario = salario*1.2

else:

    novo_salario = salario*1.1

aumento = novo_salario - salario

print(f'{nome}, o valor de aumento do seu salário foi {aumento:.2F} reais e o seu novo salário será {novo_salario:.2F} reais.')
