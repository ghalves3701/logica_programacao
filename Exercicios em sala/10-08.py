soma=0.0
maior=0.0
menor=9999999999999999999999999 #sujar variável
nome_maior=''
nome_menor=''
for i in range (1,4):
  nome=input(f'{i}º Nome: ')
  salario=float(input('Salário: '))
  if salario>maior:
    maior=salario
    nome_maior=nome
  if salario<menor:
    menor=salario
    nome_menor=nome
  soma+=salario #=acumula variável "soma" e soma(+) salário
print(f'A soma de todos os salários: R${soma:.2F}')
media=soma/(i)
print(f'média dos salários: {media}')
print(f' {nome_maior} tem o maior salário:R${maior:.2f}')
print(f' {nome_menor} tem o menor salário:R${menor:.2f}')