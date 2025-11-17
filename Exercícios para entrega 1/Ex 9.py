#Crie um algoritmo que receba o nome e a idade de uma pessoa. Caso a idade seja acima de 17 anos, escreva uma mensagem na tela conforme o modelo: Fulano, está apto para a carteira de motorista, idade: X. Caso contrário, calcule o tempo que falta até 18 anos e emita uma mensagem no modelo: Fulano, falta(m) X ano(s) para tirar a sua carta, idade: Y.
nome=str(input('Entre com o nome: '))
idade=float(input("Entre com a idade: "))
if (idade>17):
    print(f'{nome}, está apto para a carteira de motorista')
else:
    maioridade=18-idade
    print(f'{nome}, falta(m) {maioridade:.0F} ano(s) para tirar a sua carta, idade: {idade:.0F}')