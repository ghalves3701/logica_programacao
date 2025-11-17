
cont_crian=0
cont_idoso=0
cont_adulto=0

for i in range (1,6):
    nome=str(input("Entre com o nome: "))
    idade=int(input("Entre com a idade: "))
    if idade<14:
        print("Criança")
        cont_crian+=1
    elif idade<70:
        cont_adulto+=1
    else:
        cont_idoso+=1
print(f'''
Total de Idosos: {cont_idoso};
Total Crianças: {cont_crian};
Pessoas que não se enquadram: {cont_adulto}.''')
