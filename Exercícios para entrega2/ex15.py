#Faça um algoritmo que receba a idade e o peso de uma pessoa. De acordo com a tabela, verifique e mostre qual o grupo de risco essa pessoa se encaixa apresentando na tela o modelo de resposta: Você se encaixa no Grupo 9: Menores de 20 anos e até 60 quilos!

idade=int(input("Entre com a idade: "))
peso=float(input("Entre com o peso:"))

if (idade<=20):
    if(peso<60):
        print('Você se encaixa no Grupo 9: Menores de 20 anos e até 60 quilos!')
    elif (60<peso<=90):
        print('Você se encaixa no Grupo 8: Menores de 20 anos entre 60 e 90 quilos!')
    else:
        print('Você se encaixa no Grupo 7: Menores de 20 anos e mais de 90 quilos!')
elif (21<=idade<=50):
    if(peso<60):
        print('Você se encaixa no Grupo 6: Entre 21 e 50 anos e até 60 quilos!')
    elif(60<=peso<=90):
        print('Você se encaixa no Grupo 5: Entre 21 e 50 anos entre 60 e 90 quilos!')
    else:
        print('Você se encaixa no Grupo 4: Entre 21 e 50 anos e mais de 90 quilos!')
else:
    if(peso<60):
        print('Você se encaixa no Grupo 3: Maiores de 50 anos e até 60 quilos!')
    elif(60<=peso<=90):
        print('Você se encaixa no Grupo 2: Maiores de 50 anos entre 60 e 90 quilos!')
    else:
        print('Você se encaixa no Grupo 1: Maiores de 50 anos e mais de 90 quilos!')
