value_total=0.0
for i in range (1,6):
    code_product=int(input(f"Entre com o código do produto {i}: "))
    quant_product=int(input(f"Entre com a quantidade do produto {i}: "))
    preco=float(input(f"Entre com o preço unitário do produto {i}: "))
    value_total+= (quant_product*preco)
print(f"O valor total dos itens foi de R${value_total}")