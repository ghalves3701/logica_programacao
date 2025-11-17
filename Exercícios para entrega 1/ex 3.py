#Receba a idade de uma pessoa e a idade para aposentadoria. Caso ela tenha a idade a partir da idade de aposentadoria, exiba: "Você está apto a se aposentar, idade: X." Caso contrário, diga: "Faltam Y anos para você se aposentar, idade: Z."
idade_pessoa=float(input('Entre com a sua idade: '))
idade_aposentadoria=float(input('Entre com a idade mínima para se aposentar: '))
if (idade_pessoa>=idade_aposentadoria):
    print(f'Você está apto à se aposentar, idade: {idade_pessoa:.0F}' )
else:
    tempo_aposentar=idade_aposentadoria-idade_pessoa
    print(f'Faltam {tempo_aposentar:.0F} anos para você se aposentar, idad: {idade_pessoa:.0F}')