total_folha = 0.0
cont_alta = 0
cont_media = 0
cont_abaixo = 0
soma_alta = 0.0
soma_media = 0.0
soma_abaixo = 0.0
maior_salario = 0.0
menor_salario = 999999999.0
nome_maior = ''
nome_menor = ''
for i in range(3):
    nome = input('Digite o nome do funcionário: ').upper()
    salario = float(input('Digite o salário (R$): '))
    if salario >= 5000:
        print(f'{nome} - Alta Renda')
        cont_alta += 1
        soma_alta += salario
    elif salario < 2000:
        print(f'{nome} - Abaixo da Média')
        cont_abaixo += 1
        soma_abaixo += salario
    else:
        print(f'{nome} - Na Média')
        cont_media += 1
        soma_media += salario
    total_folha += salario
    if salario > maior_salario:
        maior_salario = salario
        nome_maior = nome
    if salario < menor_salario:
        menor_salario = salario
        nome_menor = nome
media_salarial = total_folha / 3
perc_alta = (soma_alta / total_folha) * 100
perc_media = (soma_media / total_folha) * 100
perc_abaixo = (soma_abaixo / total_folha) * 100
 
print('\n--- Resultados Finais ---')
print(f'Total da folha: R$ {total_folha:.2f}')
print(f'Média salarial: R$ {media_salarial:.2f}')
 
print(f'Alta Renda: {cont_alta} funcionário(s) ({perc_alta:.2f}% do total de salários)')
print(f'Na Média: {cont_media} funcionário(s) ({perc_media:.2f}% do total de salários)')
print(f'Abaixo da Média: {cont_abaixo} funcionário(s) ({perc_abaixo:.2f}% do total de salários)')
 
print(f'Funcionário com maior salário: {nome_maior}  - R$ {maior_salario:.2f}')
print(f'Funcionário com menor salário: {nome_menor}  - R$ {menor_salario:.2f}')