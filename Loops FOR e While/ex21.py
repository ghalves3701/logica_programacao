nome=''
tempo_maior=0.0
tempo_menor=99999999999999999999999999999.99
cont=0
sum_tempo=0
while nome!="X":
    if tempo>tempo_maior:
        tempo_maior=tempo
        nome_maior=nome
    if tempo<tempo_menor:
        tempo_menor=tempo
        nome_menor=nome
    cont+=1
    sum_tempo+=tempo
    media=sum_tempo/cont
    nome=input("Entre com o nome: ")
    tempo=input("Entre com o tempo: ")
print(f'''
 O atleta mais rápido foi o {nome_menor} com o tempo de {tempo_menor} min
 O atleta mais lento foi o {nome_maior} com o tempom de {tempo_maior} min
 Quantidade de atletas: {cont}
 Tempo médio de prova: {media}
      ''')