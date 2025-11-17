#Crie um algoritmo que leia o nome de um aluno, a quantidade de faltas e o número total de aulas. Calcule a porcentagem de presença e exiba: O aluno Pedro tem 90% de presença.
nome=str(input('Entre com o nome do aluno: '))
aulas=int(input('Entre com a quantidade de aulas: '))
faltas=int(input(f'Entre com a quantidade de faltas do aluno {nome}:'))
if (faltas>aulas):
    print('Número inválido')
else:
    porcentagem=(aulas-faltas)/aulas*100
    print(f' O aluno {nome} tem {porcentagem:.0F} % de presença')
