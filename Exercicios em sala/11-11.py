vetor = [5.3, 6.8, 7.3, 1.5, 2.5]
print(f'Posição 0: {vetor[0]}')
print(f'Quantidade de itens: {len(vetor)}')
print(f'Soma dos itens: {sum(vetor)}')
print(f'Media dos itens {(sum(vetor)/len(vetor)):.2f}')
print(f'Maior Valor: {max(vetor)}')
print(f'Menor Valor: {min(vetor)}')
vetor[2] = 6.5
print(f'Posição 2: {vetor[2]}')
vetor.append(float(input('NUMERO: ')))
print(f'ultima posição {len(vetor)-1} - Vlr: {vetor[len(vetor)-1]}')
print(vetor)