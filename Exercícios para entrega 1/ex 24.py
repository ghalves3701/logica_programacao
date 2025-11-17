#Checagem de Velocidade Permitida: Receba a velocidade de um carro. Caso ela ultrapasse 80 km/h, exiba uma mensagem de multa com o valor de R$ 5 por km acima do limite. Caso contrário, informe: "Velocidade dentro do limite permitido: X km/h."
carro=float(input('entre com a velocidade atual do carro em km/h: '))
velocidade_maxima=80
if (carro<=velocidade_maxima):
    print(f'Velocidade dentro do limite permitido: {carro} km/h.')
else:
    acima=carro-velocidade_maxima
    multa=acima*5
    print(f'Você está acima da velocidade permitida \nMulta no valor de R${multa:.2F}')
