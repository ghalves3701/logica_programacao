#Receba o valor do salário de um cliente e a prestação mensal de um empréstimo. Caso o valor da prestação seja menor ou igual a 30% do salário, exiba: "Empréstimo aprovado." Caso contrário, diga: "Empréstimo negado. Prestação superior a 30% do salário."
salario=float(input('Entre com o valor do salário: '))
parcela=float(input('Entre com o valor da parcela: '))
porcentagem=parcela/salario
if (porcentagem<=0.3):
    print('Emprestimo Aprovado')
else:
    print('Emprestimo negado. Prestação superior a 30% do salário')
