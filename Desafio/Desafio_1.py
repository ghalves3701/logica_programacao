#Faça um programa em pyton que receba 15 valores inteiros. Aponte os números que se repetem e quantas vezes se repetem.
v=[]
cont=0
igual=[]
numero=[]
for i in range (15):
    v.append(int(input(f'Entre com o {i+1}º Valor: ')))
    

for i in range (len(v)):
    
    if v[i] not in numero: # lembrando do exercício de excluir vogais para verificar consoantes
        #print(f' vetor de verificação: {numero}')
        for j in range (len(v)):
            if v[i]==v[j]:
                cont+=1
                #print(f'contando número {v[i]}: {cont} Ignorar print')

        if cont>1:        
            print (f'o número {v[i]} aparece {cont} vezes')

        cont=0

        numero.append(v[i])
        