#Imagine que você está criando um software para avaliar se o peso das malas de um passageiro está dentro do limite permitido. O programa permitirá que o usuário digite o peso suportado pelo limite máximo, de acordo com as regras da companhia aérea. Além disso, o usuário deverá informar o peso das duas malas. Com base nas informações fornecidas, o programa deve:
#Solicitar o peso da primeira mala.
#Solicitar o peso da segunda mala.
#Perguntar qual é o peso limite permitido.
#Calcular o peso total das malas.

peso_mala1=float(input('Digite o Peso da sua Primeira mala: '))
peso_mala2=float(input('Digite o Peso da sua Segunda mala: '))
peso_limite=float(input('Digite o Peso máximo permitido: '))
peso_total=peso_mala1+peso_mala2

if (peso_total<=peso_limite):
    print('Bagagens dentro do Peso permitido')
else:
    exedente=peso_total-peso_limite
    print(f'Bagagem excede o limite do Peso permitido em {exedente} kg')
    
    