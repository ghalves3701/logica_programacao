'''(problema sem def)...Faça um algoritmo usando vetores que receba o nome e a nota de oito alunos e mostre o relatório a seguir:
Digite o nome do 1º aluno: Carlos 
Digite a  nota do Carlos: 8
Digite o nome do 2 º aluno: Pedro 
Digite a nota do Pedro: 5

Relatórios de notas
Aluno   Nota
Carlos     8.0
Pedro      5.0
...
Média da classe = ??'''

nome=[]
nota=[]
for i in range (3):
    nome.append(str(input(f'Entre com o nome do {i+1}º aluno: ')))
    nota.append(float(input(f'Entre com a nota no {nome[i]}: ')))
print(f'''
=====Relatório de notas=====
    Aluno             nota
''')
for i in range (len(nome)):
    print(f'''
{nome[i]}          {nota[i]}''')
media=sum(nota)/len(nota)
print(f'\nA média da sala foi: {media}\n')