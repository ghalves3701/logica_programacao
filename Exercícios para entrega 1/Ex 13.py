#Imagine que você trabalha em uma loja que precisa calcular o imposto pago sobre dois produtos diferentes. Cada produto possui um preço de venda e uma alíquota de imposto (%). O programa que você criará deve ajudar o lojista a determinar:
#O valor do imposto pago sobre cada produto (valor absoluto em reais);
#Qual produto paga mais imposto;
#Exibir o imposto calculado para cada produto.
#Entradas do Programa
#O programa solicitará ao usuário as seguintes informações:
#Preço do Produto 1 (em reais);
#Alíquota do imposto sobre o Produto 1 (em percentual, ex.: 10%);
#Preço do Produto 2 (em reais);
#Alíquota do imposto sobre o Produto 2 (em percentual, ex.: 8%).
#Cálculos Necessários
#Calcule o valor do imposto pago para cada produto utilizando a fórmula:
#Imposto = preco + (alíquota / 100)
#Compare os valores absolutos dos impostos para determinar qual produto paga mais.
#Exiba os resultados de forma clara.
# Exemplo 1:
#Preço do Produto 1: R$ 100, Alíquota do Produto 1: 10%
#Preço do Produto 2: R$ 150, Alíquota do Produto 2: 8%
# O produto 2 paga mais imposto: R$ 12.00. Produto 1 paga R$ 10.00.
#Exemplo 2:
#Preço do Produto 1: R$ 200, Alíquota do Produto 1: 15%
#Preço do Produto 2: R$ 150, Alíquota do Produto 2: 10%
# O produto 1 paga mais imposto: R$ 30.00. Produto 2 paga R$ 15.00.
produto1=float(input('Entre com o valor do produto 1: '))
imposto1=float(input('Entre com a alíquota de imposto do produto 1: '))
produto2=float(input('Entre com o valor do produto 2: '))
imposto2=float(input('Entre com a alíquota de imposto do produto 2: '))
valor_imposto1=produto1*imposto1/100
valor_imposto2=produto2*imposto2/100
total1= valor_imposto1 + produto1
total2=valor_imposto2 + produto2

if(valor_imposto1<valor_imposto2):
    print(f'Preço do Produto 1: R$ {total1:.2F}, Alíquota : {imposto1}%')
    print(f'Preço do Produto 2: R$ {total2:.2F}, Alíquota : {imposto2}%')
    print(f'O produto 2 paga mais imposto: R$ {valor_imposto2:.2F}. Produto 1 paga R$ {valor_imposto1:.2F}.')
else:
    print(f'Preço do Produto 1: R$ {total1:.2F}, Alíquota : {imposto1}%')
    print(f'Preço do Produto 2: R$ {total2:.2F}, Alíquota : {imposto2}%')
    print(f'O produto 1 paga mais imposto: R$ {valor_imposto1:.2F}. Produto 2 paga R$ {valor_imposto2:.2F}.')