cont_fem = 0
cont_masc = 0
cont_utr = 0
for i in range ( 1 , 6 ):
    nome1=str(input("Entre com o nome: "))
    sexo1=str(input("Qual é o sexo (M=masculino, F=feminino)?: ")).upper
    if sexo1 == "F":
        cont_fem += 1
    elif sexo1 == "M":
        cont_masc += 1
    else:
        cont_utr += 1


print(f'''
-Quantidade de pessoas do sexo feminino: {cont_fem}
-Quantidade de pessoas do sexo masculino: {cont_masc}
-Outros: {cont_utr}''')