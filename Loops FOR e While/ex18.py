
peso_maior=0
peso_menor=999999999999
altura_maior=0
altura_menor=99999999999
cont=0
soma=0
while True:
    codigo=str(input("Entre com o seu código: "))
    if codigo==0:
        break
    altura=float(input("Entre com a sua altura: "))
    peso=float(input("entr como seu peso: "))
    if peso>peso_maior:
        peso_maior=peso
        codigo_pmaior=codigo
    if peso<peso_menor:
        peso_menor=peso
        codigo_pmenor=codigo
    if altura>altura_maior:
        altura_maior=altura
        codigo_amaior=codigo
    if altura<altura_menor:
        altura_menor=altura
        codigo_amenor=codigo
    cont+=1
    soma+=peso
    media=soma/cont
print(f'''
O maior é o {codigo_amaior} com {altura_maior}m
o menor é o {codigo_amenor} com {altura_menor}m
o peso maior é o {codigo_pmaior} com {peso_maior}Kg
p peso menor é o {codigo_pmenor} com {peso_menor}Kg
''')