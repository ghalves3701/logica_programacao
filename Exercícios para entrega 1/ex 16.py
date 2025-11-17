#Escreva um algoritmo que calcule quantos litros de um líquido são necessários para preencher uma determinada quantidade de recipientes. O programa deve receber:
#A capacidade de um recipiente em mililitros;
#A quantidade de recipientes usados;
#O volume total do líquido necessário (em mililitros).
#A saída deve apresentar algo como:
#"Para preencher 15 recipientes de 500 ml, você precisará de 7,5 litros de líquido."
capacidade = float(input('Entre com a capacidade do recipente em ml: '))
quantidade_recipiente = int(input('Entre com a quantidade de recipientes disponíveis: '))
volume_total_ml=capacidade*quantidade_recipiente
volume_total_l=volume_total_ml/1000
print(f'Para preencher {quantidade_recipiente} recipientes de {capacidade:.0F} ml, você precisará de {volume_total_l} litros de líquido')