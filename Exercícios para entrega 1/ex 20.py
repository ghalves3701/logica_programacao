#Desenvolva um algoritmo que peça o nome de um animal, o peso dele em quilogramas e a quantidade de ração consumida por dia em gramas. Calcule quantos dias um saco de ração de 10 kg durará para esse animal e exiba: O saco de ração durará 20 dias para o(a) Rex.
nome=str(input('Entre com o nome do animal: '))
peso=float(input('Entre com o peso do animal em kilograma: '))
racao=int(input('Entre com a quantidade de ração que ele consome por dia em gramas: '))
saco_racao=10
dias=saco_racao/(racao/1000)
print(f'O saco de ração durará {dias:.2F} dias para o(a) {nome}.')
