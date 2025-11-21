'''(problema sem def)...Construa um algoritmo que receba valores float para um vetor de 8 posições. Após receber os dados, apresente qual é o maior e o menor valor, a soma e a média de todos os valores. Utilize as funções Python: max, min, len, sum'''
valor=[]
for i in range (8):
    valor.append(float(input(f'Digite o {i+1}º valor: ')))

maior=max(valor)
menor=min(valor)
media=sum(valor)/len(valor)

print(f'''O maior valor é o {maior};
O menor valor é o {menor};
A média dos números é {media}.''')