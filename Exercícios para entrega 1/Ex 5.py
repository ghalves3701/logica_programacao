#Escreva um algoritmo que entre com o nome e idade de uma pessoa. 
#Caso a idade for menor que 18 ou maior que 58 escreva: “{Nome}, {idade}: Idade Inválida”. Caso contrário, escreva: “{Nome}, {idade}: Idade Válida”.
nome=str(input('Entre com o seu nome: '))
idade=float(input('Entre com a sua idade: '))

if (idade<18 or idade>58):
    print(f'{nome}, {idade:.0F} anos: Idade Inválida')
else:
    print(f'{nome}, {idade:.0F} anos: Idade Válida')