#Você é responsável por aprovar um dos dois projetos para uma empresa. Cada projeto tem um custo estimado e um prazo de execução. Para saber qual deles é a melhor escolha econômica, é necessário determinar qual tem o menor custo diário (custo total dividido pelo prazo em dias). O projeto economicamente mais viável é aquele com menor custo por dia, pois ele oferece melhor relação financeira entre o investimento e o tempo necessário para concluí-lo.
#Seu programa deve:
#Solicitar o custo total estimado (em reais) de dois projetos.
#Solicitar o prazo de execução em dias para cada projeto.
#Calcular o custo diário de cada projeto.
#Comparar os custos diários e determinar qual projeto é mais viável ou se ambos possuem o mesmo custo por dia.
#Apresentar os resultados, mostrando o custo diário de ambos os projetos e indicando o mais econômico.
#Exemplo 1:
#Custo total do Projeto 1: R$ 50.000  
#Prazo do Projeto 1: 30 dias  
#Custo total do Projeto 2: R$ 40.000  
#Prazo do Projeto 2: 50 dias
#Projeto 1 é mais viável com custo/prazo de R$ 1.667 por dia. Projeto 2 tem custo/prazo de R$ 800 por dia.
#Exemplo 1:
#Custo total do Projeto 1: R$ 100.000  
#Prazo do Projeto 1: 50 dias  
#Custo total do Projeto 2: R$ 120.000  
#Prazo do Projeto 2: 60 dias  
#Ambos os projetos têm o mesmo custo/prazo de R\$ 2.000 por dia
C1=float(input('Entre com o custo total do primeiro projeto: '))
P1=int(input('Entre com a quantidade de dias necessários para a execução do primeiro projeto: '))
C2=float(input('Entre com o custo total do segundo projeto: '))
P2=int(input('Entre com a quantidade de dias necessários para a execução do segundo projeto: '))
custo1=C1/P1
custo2=C2/P2
if (custo1==custo2):
    print(f'Ambos os projetos têm o mesmo custo/prazo de R$ {custo1:.2F} por dia.')
else:
    if (custo1<custo2):
        print(f'Projeto 1 é mais viável com custo/prazo de R$ {custo1:.2F} por dia. Projeto 2 tem custo/prazo de R$ {custo2:.2F} por dia.')
    else:
        print(f'Projeto 2 é mais viável com custo/prazo de R$ {custo2:.2F} por dia. Projeto 1 tem custo/prazo de R$ {custo1:.2F} por dia.')

