#Crie um programa que receba o nome do aluno, sua média nas disciplinas e a quantidade de faltas. Um aluno é aprovado apenas se atender os dois critérios:
#1. Ter média maior ou igual a 6.0;
#2. Não acumular faltas superiores a 25% do número total de aulas (fixo em 80 aulas, o limite de faltas permitido será 20 faltas).
#Se o aluno for aprovado: Apresente uma mensagem informando que ele foi aprovado e exiba sua média e faltas.
#Caso contrário: Informe o motivo da reprovação, especificando:
#Se a média estiver abaixo do necessário, mostre quantos pontos faltaram para atingir 6.0.
#Se as faltas excederem o limite, informe quantas faltas o aluno excedeu.
#Regras Fixas
#Média mínima: 6.0
#Faltas máximas permitidas: 20 (25% de 80)
#Exemplo 1:
#Nome: Maria
#Média: 7.5
#Faltas: 18
#Maria foi aprovada! Média: 7.5, Faltas: 18.
#Exemplo 2:
#Nome: João
#Média: 5.0
#Faltas: 15
#João não foi aprovado, pois faltaram 1.0 ponto(s) para alcançar a média mínima (6.0). Média atual: 5.0.
nome=str   (input('Entre com o nome do aluno: '))
nota=float (input(f'Entre com a nota do aluno {nome}: '))
faltas=int (input('Entre com o número de faltas: '))
if (faltas<20):
    if (nota>=6):
        print(f'{nome} foi aprovado(a)! Média: {nota}, Faltas: {faltas}.')
    else:
        nota_menor=6-nota
        print(f'{nome} não foi aprovado, pois faltaram {nota_menor} ponto(s) para alcançar a média mínima (6.0). Média atual: {nota}')
else:
    if (nota<=6):
        faltas_maior=faltas-20
        nota_menor=6-nota
        print(f'{nome} não foi aprovado, pois faltaram {nota_menor} ponto(s) para alcançar a média mínima (6.0) e você teve {faltas_maior} faltas além do permitido. Média atual: {nota}, Faltas: {faltas}')
    else:
        print(f'{nome} não foi aprovado, pois teve {faltas_maior} faltas além do permitido. Média atual: {nota}, Faltas: {faltas}')