#Crie um programa que calcule a economia de combustível obtida distribuindo passageiros de um carro em caronas. O programa deve receber:
#O consumo do carro (quantos km/l);
#A distância em quilômetros da viagem;
#A quantidade de pessoas que dividirão o custo do combustível;
#O preço do litro de combustível.
#Exiba uma mensagem como:
#"Com uma viagem de 300 km e 4 pessoas dividindo, cada uma pagará R$ 37.50 pelo combustível."
consumo=float(input('Entre com o consumo do carro em km/l: '))
distancia=float(input('Entre com a distância em kilômetros da viagem: '))
pessoas=int(input('Entre com a quantidade de pessoas que dividirão o custo do combustível: '))
if (pessoas<=0):
    print("Por Favor, entre com um número válido de pessoas!")
else:
    valor_combustivel=float(input('Entre com o valor do litro do combustível em reais: '))
    valor=valor_combustivel*distancia/consumo/pessoas
    print(f'Com uma viagem de {distancia:.0f} km e {pessoas} pessoas dividindo, cada uma pagará R${valor:.2F} pelo combustível.')



