pessoas=int(input("Entre com a quantidade de pessoas: "))

loop=pessoas+1

peso= 0.0
peso_total=0.0

for i in range (1,loop):
    
    peso=float(input(f"Entre com o peso da {i}ª pessoa: "))
    peso_total=(peso_total + peso)
    
media=peso_total/pessoas
print(f"A média de pesos é: {media}Kg")