crianca=0
sum_crianca=0
cont_crianca=0
media_crian=0
infantil=0
sum_infantil=0
cont_infantil=0
media_inf=0
juvenil=0
sum_juvenil=0
cont_juvenil=0
media_juv=0
adulto=0
sum_adulto=0
cont_adulto=0
media_adul=0
media=0
for i in range (1,11):
    name=str(input(f"Entre com o {i}º nome: "))
    age=int(input(f"Entre como a idade do {i}º Atleta: "))
    if age <= 8:
        crianca+=1
        sum_crianca+=age
        cont_crianca+=1
        media_crian=sum_crianca/cont_crianca

    elif age <= 15:
        infantil+=1
        sum_infantil+=age
        cont_infantil+=1
        media_inf=sum_infantil/cont_infantil
    elif age <= 20:
        juvenil+=1
        sum_juvenil+=age
        cont_juvenil+=1
        media_juv=sum_juvenil/cont_juvenil
    else:
        adulto+=1
        sum_adulto+=age
        cont_adulto+=1
        media_adul=sum_adulto/cont_adulto
    media+=age
media=media/10 



print(f'''
A Quantidade de Criancas foi de: {cont_crianca}
Com média de {media_crian} anos
A Quantidade de Infantis foi de: {cont_infantil}
Com média de {media_inf} anos
A Quantidade de Juvenis foi de: {cont_juvenil}
Com média de {media_juv} anos
A Quantidade de Adultos foi de: {cont_adulto}
Com média de {media_adul} anos
A Média Geral de idade foi de: {media}''')