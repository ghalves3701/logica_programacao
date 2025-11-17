#Em uma escolinha de Futebol, o pagamento de instrutores é com base em hora/aula. Faça um algoritmo que leia o nível e a quantidade de horas ministradas pelo instrutor para poder calcular seu salário. Sabe-se que o valor da hora/aula pode ser visto a seguir:
#Nível 1 – R$ 30,00 por hora/aula
#Nível 2 – R$ 37,50 por hora/aula
#Nível 3 – R$ 45,00 por hora/aula

nivel=int(input("Entre com o seu Nível: "))
if nivel in (1,2,3):
    horas=float(input("Entre com a quantidade de horas: "))
    if (nivel==1):
        salario=horas*30.00
    elif (nivel==2):
        salario=horas*37.5
    else:
        salario=horas*45.00
    print(f'Olá, seu Nível é {nivel} e seu salário é de R${salario:.2F}')
else:
    print("Nível não encontrado")