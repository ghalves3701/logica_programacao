maior1_nome = ''
maior1_gols = 0
maior2_nome = ''
maior2_gols = 0
maior3_nome = ''
maior3_gols = 0
i = 1
while i <= 10:
    nome = input(f'Nome do atleta {i}: ')
    gols = int(input('Gols marcados: '))
    if gols >= maior1_gols:
        maior3_nome = maior2_nome
        maior3_gols = maior2_gols
        maior2_nome = maior1_nome
        maior2_gols = maior1_gols
        maior1_nome = nome
        maior1_gols = gols
    elif gols >= maior2_gols:
        maior3_nome = maior2_nome
        maior3_gols = maior2_gols
        maior2_nome = nome
        maior2_gols = gols
    elif gols >= maior3_gols:
        maior3_nome = nome
        maior3_gols = gols
    i += 1
print('\n=== maior 3 Artilheiros ===')
print(f'1º - {maior1_nome}: {maior1_gols} gol(s)')
print(f'2º - {maior2_nome}: {maior2_gols} gol(s)')
print(f'3º - {maior3_nome}: {maior3_gols} gol(s)')