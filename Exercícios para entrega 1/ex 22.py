#Desenvolva um algoritmo que solicite o nome de um aluno, a quantidade de questões corretas em uma prova e o número total de questões. Calcule a porcentagem de acertos e exiba: O aluno(a) Carlos acertou 80% das questões.
nome=str(input('Entre com o nome do aluno: '))
acertos=int(input('Entre com a quantidade de questões corretas: '))
questoes=int(input('Entre com a quantidade de questões: '))
porcen=acertos/questoes*100
print(f'O aluno(a) {nome} acertou {porcen:.0F}% das questões')
