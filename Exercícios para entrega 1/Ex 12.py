#Crie um algoritmo que peça o nome de um livro, o preço de capa, e um percentual de imposto. Calcule o preço final do livro com o imposto e exiba: O livro Python Passo-a-Passo custa R$ 45.00 com 10% de imposto.
nome=str(input('Entre com o nome do livro: '))
preco=float(input('Entre com o valor de capa do livro: '))
imposto=float(input('Entre com o valor do imposto: '))
preco_final= preco*imposto/100 + preco
print(f'O livro Python Passo-a-Passo custa R$ {preco_final:.2F} com {imposto}% de imposto.')
