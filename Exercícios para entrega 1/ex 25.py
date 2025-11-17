#Escreva um algoritmo que receba o salário bruto de um funcionário, o percentual de desconto do INSS, e o percentual de desconto do IR. Calcule o valor do desconto do INSS, depois o desconto do IR sobre o valor restante. Atenção: o desconto do IR sobre o valor restante do cálculo feito com o INSS. Por fim o salário líquido do funcionário. Apresente a mensagem de resultado: O salário bruto X com o desconto de INSS no valor de Y e o desconto de IR no valor W, gerou o salário líquido Z.
sb=float(input('Entre com o salário bruto: '))
inss=float(input('Entre com o desconto em % do INSS: '))
ir=float(input('Entre com o desconto em % do IR: '))
vinss=(sb*inss/100)
vir=(sb-vinss)*(ir/100)
sl=sb-vinss-vir
print(f'O Salário bruto de R${sb:.2F} com desconto de INSS no valor de {vinss:.2F}R$ \nO desconto de IR no valor de R${vir}\nGerou um salário líquido no valor de R${sl:.2F}')
