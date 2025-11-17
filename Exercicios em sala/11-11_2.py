#Faça um programa que receba cinco numeros num vetor e mostr a saida a seguir conforme o modelo:
#Digite o 1º número: 5
#Digite o 2º número: 3
#Digite o 3º número: 2
#Digite o 4º número: 0
#Digite o 5º número: 2
# Os números digitados foram: 5 + 3 + 0 + 2 = 12
vet=[]
for i in range (5):
    vet.append(int(input(f' Digite o {i+1}º Número:')))
for  i in range (len(vet)):#len="lengt:tamanho"
    print(vet[i], end='')
    if (i != len(vet)-1):
        print('+', end='')
print(f'={sum(vet)}')
