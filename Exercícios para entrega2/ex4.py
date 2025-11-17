#Cálculo do Preço Final do Carro com Impostos: Desenvolva um programa que receba o nome do comprador e o preço de fábrica de um carro. O programa deverá calcular o preço final para o consumidor considerando os seguintes valores adicionais:
#Se o preço de fábrica for até R$30.000,00: Adicione 5% de impostos e 10% de lucro.
#Se o preço de fábrica estiver entre R$30.001,00 e R$60.000,00: Adicione 10% de impostos e 15% de lucro.
#Se o preço de fábrica for acima de R$60.000,00: Adicione 15% de impostos e 20% de lucro.
#O sistema deverá exibir o nome do comprador e o valor final do carro.
#Exemplo de saída:
#Antônio, o preço final do carro é R$ 69.000,00
comprador=str(input("Entre com o nome do Comprador: "))
valor_carro=float(input("Entre com o preço de fábrica do carro: "))

if (valor_carro<=30000):
    valor_carro=valor_carro*1.05
    valor_carro=valor_carro*1.10
elif ((valor_carro>30000) and (valor_carro<60000)):
    valor_carro=valor_carro*1.10
    valor_carro=valor_carro*1.15
else:
    valor_carro=valor_carro*1.15
    valor_carro=valor_carro*1.20
print(f'{comprador}, o preço final do carro é R${valor_carro}')