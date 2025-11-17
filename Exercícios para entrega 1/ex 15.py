#Crie um algoritmo que receba o nome de uma pessoa, sua idade atual e quantos anos ela deseja somar à sua idade. Calcule a nova idade e exiba: A pessoa João terá 35 anos daqui a 10 anos, no ano de ______. --> entendendo-se que este final sublinhado será o ano que a pessoa terá a idade final somada.
nome=str(input('Entre com seu nome: '))
idade_atual=int(input('Entre com sua idade atual: '))
idade_soma=int(input('Entre com a quantidade de anos que você deseja adicionar à sua idade: '))
ano_atual=2025
soma_idade=idade_atual+idade_soma
ano_soma=ano_atual+idade_soma
print(f'A pessoa {nome} terá {soma_idade} anos daqui a {idade_soma} anos, no ano de {ano_soma}.')
