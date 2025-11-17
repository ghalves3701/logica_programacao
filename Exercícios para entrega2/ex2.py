#Em uma academia, o preço mensal para a natação é:
#- Criança: R$ 120.00
#- Infantil: R$ 130.00
#- Juvenil: R$ 140.00
#- Adulto: R$ 150.00
#Essas modalidades são tabeladas de acordo com as seguintes faixas de idades:
#De 1 a 8 anos: Criança | De 9 a 15 anos: Infantil | De 16 a 20 anos: Juvenil | Acima de 20 anos: Adulto
#Quem apresentar carteirinha de estudante, terá 20% de desconto no pagamento.
#Dessa forma, desenvolva um algoritmo que receba o nome, a idade e a confirmação de carteirinha de estudante, representada pela letra ‘S’ para “sim” ou pela letra ‘N’ para “não”. 
nome=str(input("Digite seu nome: "))
id=int(input("Digite sua idade: "))
est=str(input("Você é estudante? (S=Sim N=Não):  ")).upper()
if (est=='S') or (est=='N') or (id>=1):
    if(est=='S'):
        if(id<=8):
            cat="Criança"
            valor=120*0.8
        elif(id<=15):
            cat="Infantil"
            valor=130*0.8
        elif(id<=20):
            cat="Juvenil"
            valor=140*0.8
        else:
            cat="Adulto"
            valor=150*0.8
    else:
        if(id<=8):
            cat="Criança"
            valor=120
        elif(id<=15):
            cat="Infantil"
            valor=130
        elif(id<=20):
            cat="Juvenil"
            valor=140
        else:
            cat="Adulto"
            valor=150
    print(f'{nome}, sua categoria é: {cat} e o valor a ser pago é de R$ {valor:.2F}')
else:
    print("Digíto inválido")