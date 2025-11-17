#Crie um programa que simule o cadastro de dois clientes para, na sequência, trocar seus dados em um sistema. O sistema deve receber:
#O nome e a idade do cliente A;
#O nome e a idade do cliente B.
#Depois, o programa deve trocar as informações cadastrais entre os dois clientes. Ou seja, o cliente A ficará com as informações do cliente B e vice-versa. Exiba o resultado claramente, mostrando que a troca de valores foi REALMENTE efetuada na memória e que os dados de ambos foram alterados.
#Exemplo de saída:
#Antes da troca:
#Cliente A: Nome = Ana, Idade = 25
#Cliente B: Nome = João, Idade = 30
#Depois da troca:
#Cliente A: Nome = João, Idade = 30
#Cliente B: Nome = Ana, Idade = 25
#Alerta: Garanta que os valores NÃO estejam apenas trocados no print final, mas sim armazenados corretamente na memória, ou seja, as variáveis devem realmente conter os novos valores.
clienteA=str(input('Entre com o nome do Cliente A: '))
idadeA=int(input('Entre com a idade do Cliente A: '))
clienteB=str(input('Entre com o nome do cliente B: '))
idadeB=int(input('Entre com a idade do Cliente B: '))
print(f'Antes da troca:\nCliente A: {clienteA}\nIdade cliente A: {idadeA}\nCliente B: {clienteB}\nIdade Cliente B: {idadeB}')

#--->troca
nomeA=clienteA
anosA=idadeA
nomeB=clienteB
anosB=idadeB

clienteA=nomeB
idadeA=anosB

clienteB=nomeA
idadeB=anosA


print(f'Depois da troca:\nCliente A: {clienteA}\nIdade cliente A: {idadeA}\nCliente B: {clienteB}\nIdade Cliente B: {idadeB}')