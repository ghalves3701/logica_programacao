continuar="S"
temp_alta=0
temp_baixa=999
dia_alta=0
mes_alta=0
ano_alta=0
dia_baixa=0
mes_baixa=0
ano_baixa=0
soma_temp=0
cont_temp=0


while continuar=="S":

    dia=int(input('Entre com o dia: '))
    mes=int(input('Entre com o mês em número: '))
    ano=int(input('entre com o ano com 4 digitos: '))
    temp=float(input('Entre com a temperatura: '))

    if temp>temp_alta:
        temp_alta=temp
        dia_alta=dia
        mes_alta=mes
        ano_alta=ano
    if temp<temp_baixa:
        temp_baixa=temp
        dia_baixa=dia
        mes_baixa=mes
        ano_baixa=ano
    cont+=1
    soma_temp+=temp
    media=soma_temp/cont
    continuar=str(input('Deseja continuar? "S"/"N": ')).upper()
print(f'''
Maior temperatura em: {dia_alta}/{mes_alta}/{ano_alta}
Menor temperatura em: {dia_baixa}/{mes_baixa}/{ano_baixa}
Média das temperaturas: {media}''')