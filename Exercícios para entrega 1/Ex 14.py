#Crie um programa que ajude no controle do estoque de produtos perecíveis. 
#Receba:
#- A quantidade inicial de produtos (por unidade);
#- Quantos são vendidos por dia;
#- O número de dias até o produto perder a validade.
#Calcule quantos produtos seriam desperdiçados ao final do período de validade e exiba:
#"Com uma validade de 10 dias e uma venda de 15 produtos por dia, haverá um desperdício de 20 unidades."

quantidade=float(input('Entre com a quantidade inicial de produtos: '))
vendas=float(input('Entre com a quantidade de vendas diárias: '))
validade=float(input('Entre com os dias restantes para o produto vencer: '))
desperdicio=quantidade-vendas*validade
print(f'Com uma validade de {validade} dias e uma venda de {vendas} produtos por dia, haverá um desperdício de {desperdicio} unidades.')