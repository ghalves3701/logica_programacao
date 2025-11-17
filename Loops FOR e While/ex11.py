peso_maior=0.00
peso_menor=999999999999999999999999.00
nome_maior=''
nome_menor=''
cont=''


while cont!="N": 

    nome=str(input("Entre com o nome do boi: "))
    peso=float(input(f"Entre com o peso do boi {nome}: "))

    if (peso>peso_maior):
        peso_maior=peso
        nome_maior=nome
    if (peso<peso_menor):
        peso_menor=peso
        nome_menor=nome
    
    cont=str(input("Você quer continuar? S= sim, N=não: ")).upper()
    
print(f'''
Entendi, vamos ao resultado...

O boi de menor peso é o {nome_menor} com {peso_menor}:.2FKg
O boi de maior peso é o {nome_maior} com {peso_maior}:.2FKg
''')