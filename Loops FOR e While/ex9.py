cont_abaixo=0.00
cont_media=0.00
cont_alta=0.00
sum_nota=0.00
media=0.00


for j in range (1,6):
    nome=str(input(f"Entre com o {j}º nome: "))
    for i in range (1,5):
        nota=float(input(f"Digite a {i}ª nota: " ))
        sum_nota+=nota
    media=sum_nota/4
    if media<4:
        cont_abaixo+=1
    elif media<=5.99:
        cont_media+=1
    else:
        cont_alta+=1


print(f'''{cont_abaixo} alunos tiveram média Abaixo de 4
{cont_media} alunos tiveram média entre 4 e 5,99
{cont_alta} alunos tiveram média acima de 5,99''')

