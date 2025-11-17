#Ao final do brasileirão deste ano, deseja-se saber quem foi o artilheiro do campeonato. Faça um algoritmo que leia o nome e o número de gols dos três jogadores com mais gols no brasileirão e mostre o nome do artilheiro.
jg1=str(input("Entre com o nome do Jogador 1: "))
gol1=int(input(f"Entre com a quantidade de gols do {jg1}: "))
gol=gol1
artilheiro=jg1
jg2=str(input("Entre com o nome do Jogador 2: "))
gol2=int(input(f"Entre com a quantidade de gols do {jg2}: "))
if (gol2>gol):
    gol=gol2
    artilheiro=jg2
jg3=str(input("Entre com o nome do Jogador 3: "))
gol3=int(input(f"Entre com a quantidade de gols do {jg3}: "))
if (gol3>gol):
    gol=gol3
    artilheiro=jg3
print(f'O artilheiro foi {artilheiro} com {gol} gols')