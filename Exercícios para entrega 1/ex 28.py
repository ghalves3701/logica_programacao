#Receba o saldo de um cliente e o valor de uma compra. Caso o saldo seja suficiente, exiba: "Compra aprovada! Saldo restante: R$ X." Caso contrário, mostre: "Saldo insuficiente. Faltam R$ Y."
salario=float(input('Entre com o salário: '))
compra=float(input('Entre com o valor da compra: '))
saldo=abs(salario-compra)
if (compra<=salario):
    print(f'Compra aprovada! Saldo restante: R$ {saldo:.2F}.')
else:
    print(f'Saldo insuficiente. Faltam R${saldo:.2F}')