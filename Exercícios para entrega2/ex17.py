#Desenvolva um algoritmo que receba valores diferentes para três variáveis do tipo inteiro e escreva os valores em ordem crescente
val1=int(input("Entre com o primeiro valor: "))
val2=int(input("Entre com o segundo valor: "))
val3=int(input("Entre com o terceiro valor: "))

if (val1>val2) and (val1>val3):
    primeiro=val1
    if (val2>val3):
        segundo=val2
        terceiro=val3
    else:
        segundo=val3

        terceiro=val2
elif (val2>val3):
    primeiro=val2
    if (val1>val3):
        segundo=val1

        terceiro=val3
    else:
        segundo=val3

        terceiro=val1
else:
    primeiro=val3
    if val1>val2:
        segundo=val1

        terceiro=val2
    else:
        segundo=val2

        terceiro=val1
print(f'''
Primeiro valor: {primeiro}
Segundo valor : {segundo}
Terceiro valor: {terceiro}''')        
