#Aprovação em um Teste: Crie um algoritmo para receber a nota de um aluno e dizer se ele foi aprovado ou reprovado. Aprovado se a nota for maior ou igual a 6, caso contrário, exiba: "Reprovado com a nota X."
nota=float(input('Entre com a nota: '))
minimo=6
if (nota>=6):
    print('Aprovado')
else:
    print(f'Reprovado com a nota: {nota}')