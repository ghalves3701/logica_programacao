#A empresa Atacadão do Hardware em sua loja do Shopping de Franca, colocou uma configuração específica de notebook Acer em promoção. 
#Os seus três vendedores: Fagner, Rodrigo e Yuri, venderam todos os notebooks. 
#Neste algoritmo, será possível obter a quantidade total de notebooks vendidos com a soma da quantidade de unidades vendida por cada vendedor. 
#A comissão fixa de cada vendedor é de 1% sobre a venda de cada notebook. 
#Sendo assim, escreva um algoritmo que receba: 
#- Valor do notebook nesta promoção; 
#- A quantidade de notebooks vendidas por cada um destes vendedores (o usuário vai simular/inventar cada quantidade) 
#Diante destes dados, calcule e escreva as seguintes respostas na tela: 
#- Quantidade total de notebooks vendidos: S 
#- Fagner vendeu T notebooks e recebeu uma comissão de R$ U 
#- Rodrigo vendeu V notebooks e recebeu uma comissão de R$ X 
#- Yuri vendeu W notebooks e recebeu uma comissão de R$ Y 
#- A soma do valor total de comissão entre todos os vendedores foi de: Z
valor=float(input('Entre com o valor do notebook: '))
fagner=int(input('Entre com a quantidade de notebooks vendidos por Fagner: '))
rodrigo=int(input('Entre com a quantidade de notebooks vendidos por Rodrigo: '))
yuri=int(input('Entre com a quantidade de notebooks vendidos por Yuri: '))
qtd_notebooks_vendidos=fagner+rodrigo+yuri
comissao_fagner=valor*fagner*0.01
comissao_rodrigo=valor*rodrigo*0.01
comissao_yuri=valor*yuri*0.01
total=comissao_fagner+comissao_rodrigo+comissao_yuri
print(f'Quantidade de notebooks vendidos = {qtd_notebooks_vendidos}')
print(f'Fagner vendeu {fagner} notebooks e recebeu uma comissão de: R${comissao_fagner:.2F}')
print(f'Rodrigo vendeu {rodrigo} notebooks e recebeu uma comissão de: R$ {comissao_rodrigo:.2F}')
print(f'Yuri vendeu {yuri} notebooks e recebeu uma comissão de: R$ {comissao_yuri:.2F}')
print(f'A soma do valor total de comissão entre todos os vendedores foi de: R${total:.2F}')