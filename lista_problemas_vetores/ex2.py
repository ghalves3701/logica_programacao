'''(problema sem def)...Faça um algoritmo que carregue um vetor com 15 elementos inteiros. Depois de ter recebido os valores, faça o seguinte:
- Input de um valor inteiro para a variável procurar....: procurar = int(input('digite o valor a procurar no vetor: ')
- Novo For para vasculhar o vetor preenchido com todas as suas posições
- Quando o valor na posição do índice do vetor for igual ao valor da variável procurar, apresente a mensagem: 'Valor {x} encontrado na posição {i} de índice do vetor’
- Ao final, apresente quantos valores foram encontrados.'''
vetor=[]
cont=0
for i in range (14):
    vetor.append(int(input(f'Digite o {i+1}º valor: ')))
procurar=int(input('Entre com um valor para localizar: '))
for i in range(len(vetor)):
    if procurar==(vetor[i]):
        cont+=1
        print(f'Valor {procurar} encontrado na posição: {i} ')
print(f'Quantidade de valores encontrados: {cont}')