##Ex 12
nome_maior=''
nome_menor=''
idade_maior=0
idade_menor=9999999999999999999999
cont_maior=0
cont_menor=0

for i in range (1,6):
    nome=str(input("Entre com o nome: "))
    idade=int(input("Entre com a idade: "))
    if idade < 18:

        cont_menor+=1

        if idade_menor>idade:
          nome_menor=nome
          idade_menor=idade
          
    else:

        cont_maior+=1

        if idade_maior<idade:
          nome_maior=nome
          idade_maior=idade
        
print(f'''
Quantidade de Maiores: {cont_maior}
Quantidade de Menores: {cont_menor}
      
A menor idade digitada foi do(a): {nome_menor},  com {idade_menor} anos
A maior idade digitada foi do(a): {nome_maior}, com {idade_maior} ''') 
