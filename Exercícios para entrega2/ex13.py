#Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada “+ - * / “. Calcule a resposta e escreva o resultado na tela. Segue uma simulação de interface:

nmr1=float(input("Entre com o 1º valor: "))
nmr2=float(input("Entre com o 2º valor: "))
op=str(input("Entre com o símbolo: "))

if op in ("+", "-", "*", "/"):
    if op=="+":
        resultado=nmr1+nmr2
    elif op=="-":
        resultado=nmr1-nmr2
    elif op=="*":
        resultado=nmr1*nmr2
    else:
        if nmr2==0:
            print("Valor 2 deve ser diferente de zero (0)")
        else:
            resultado=nmr1/nmr2
    if nmr2==0 and op=="/":
        print("=/")
    else:        
        print(f'Resultado......:{resultado}')        
else:
    print("Operação inválida")        