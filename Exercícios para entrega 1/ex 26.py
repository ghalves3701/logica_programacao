#Entrada em um Cinema: Elabore um programa que receba o nome e a idade de uma pessoa. Caso ela tenha 12 anos ou mais, exiba uma mensagem: "João pode entrar na sessão, idade: 14.". Caso contrário, informe: "Maria não pode entrar, idade: 10."
nome=str(input('Entre com o nome: '))
idade=int(input('Entre com a idade: '))
if (idade>=12):
    print(f'{nome} pode entrar na sessão, idade: {idade}.')
else:
    print(f'{nome} não pode entrar, idade: {idade}')