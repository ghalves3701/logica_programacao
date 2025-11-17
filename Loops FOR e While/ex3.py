primeiro=int(input("Entre com o primeiro valor: "))
segundo= int(input("Entre com o segundo valor: "))

while segundo<primeiro:
    print("Segundo valor menor que o primeiro")
    segundo= int(input("Entre com o segundo valor: "))
numeros=segundo-primeiro+1

for i in range (primeiro,segundo+1):
    print(primeiro)
    primeiro+=1
print(f'Foram printados: {numeros} numeros.')
