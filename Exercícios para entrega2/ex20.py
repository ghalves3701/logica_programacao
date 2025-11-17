#Classificação de Índice de Massa Corporal (IMC)
#Crie um programa que receba o nome, o peso (em kg) e a altura (em metros) de uma pessoa. Com base no cálculo do índice de massa corporal (IMC), classifique a pessoa nas faixas abaixo:
#IMC abaixo de 18.5: Abaixo do peso
#IMC de 18.5 a 24.9: Peso normal
#IMC de 25 a 29.9: Sobrepeso
#IMC de 30 a 34.9: Obesidade Grau I
#IMC de 35 a 39.9: Obesidade Grau II
#IMC acima de 40: Obesidade Grau III
#Imprima o nome da pessoa, o valor do IMC e sua classificação.
#Exemplo de saída:
#Cláudia, seu IMC é 22.5 e sua classificação é: Peso normal.

nome=str(input("Entre com o seu nome: "))
peso=float(input("Entre com o seu peso em kg: "))
h=float(input("Entre com a sua altura em metros: "))

imc=peso/(h*h)

if imc<18.5:
    clas="Abaixo do peso"
elif 18.5<=imc<25:
    clas="Peso normal"
elif 25<=imc<30:
    clas="Sobrepeso"
elif 30<=imc<35:
    clas="Obesidade Grau I"
elif 35<=imc<40:
    clas='Obesidade Grau II'
else:
    clas="Obesidade Grau III"
print(f'{nome}, seu IMC é {imc:.2F} e sua classificação é: {clas}')