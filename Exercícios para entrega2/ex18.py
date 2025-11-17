#Faça um algoritmo que receba quatro números inteiros e escreva uma mensagem apontando qual é o maior.
n1=int(input("Número 1: "))
maior=n1
n2=int(input("Número 2: "))
if (n2>maior):
    maior=n2
n3=int(input("Número 3: "))
if (n3>maior):
    maior=n3
n4=int(input("Número 4: "))
if (n2>maior):
    maior=n4
print(f'Maior: {maior}')