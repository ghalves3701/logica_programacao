#Verificação de Velocidade: Crie um programa que receba a velocidade registrada de um veículo (em km/h) e mostre uma mensagem conforme as condições abaixo:
#Até 50 km/h: Dentro do limite
#De 51 a 80 km/h: Acima do limite (leve)
#De 81 a 100 km/h: Multa grave
#Acima de 100 km/h: Multa gravíssima
#O programa deve exibir a velocidade e a classificação correspondente.
#Exemplo de saída:
#Velocidade registrada: 90 km/h. Resultado: Multa grave.

velocidade=int(input("Entre com a velocidade registrada: "))
if (velocidade>0):
    if (velocidade>100):
        resultado="Multa Gravíssima"
    elif(velocidade>=81):
        resultado="Multa Grave"
    elif(velocidade>=51):
        resultado="Acima do Limite"
    else:
        resultado="Dentro do limite"
    print(f'Velocidade registrada: {velocidade} km/h. Resultado: {resultado}.')
else:
    print("Erro de velocidade")