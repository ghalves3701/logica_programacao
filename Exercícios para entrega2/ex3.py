#Escreva um algoritmo que entre com o nome e idade de uma pessoa. Quando a idade estiver entre 18 e 37 anos escreva: “Idade adulta 1”. Se a idade estiver entre 38 e 58, escreva “Idade adulta 2”.  Caso a idade for menor que 18 ou maior que 58 escreva: “Idade Inválida”. Utilize “AND” e “OR”. Ao final, printe uma mensagem na tela, apresentando o nome, a idade e o status da pessoa.
nome=str(input("Entre com o se nome: "))
idade=int(input("Entre com sua idade: "))
if ((idade>=18) and (idade <=37)):
    stridade="Idade Adulta 1"
elif ((idade>=38)and (idade<=58)):
    stridade= "Idade Adulta 2"
else:
    stridade= "idade inválida"
print(f'Olá {nome}, sua idade é {idade} anos e seu status é {stridade}')
