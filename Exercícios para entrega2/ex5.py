#Crie um programa que receba a idade de uma pessoa e calcule o valor de um plano de saúde conforme as faixas abaixo:
#Até 10 anos: R$ 100,00
#De 11 a 29 anos: R$ 200,00
#De 30 a 45 anos: R$ 300,00
#De 46 a 59 anos: R$ 500,00
#De 60 anos ou mais: R$ 700,00
#O programa deve exibir a idade da pessoa e o valor do plano.
#Exemplo de saída:
#Você tem 35 anos. O valor do plano de saúde é R$ 300,00.

idade=int(input("Entre com a sua idade: "))
if (idade<0):
    print("Idade inesistente")
else:    
    if(idade<=10):
        valor=100
    elif(idade<=29):
        valor=200
    elif(idade<=45):
        valor=300
    elif(idade<=59):
        valor=500
    else:
        valor=700
    print(f'Você tem {idade}. O valor do plano de saúde é R${valor:.2F}.')