#Escreva um algoritmo que receba o nome de um time de futebol, o número de vitórias, empates e derrotas. Calcule a pontuação total do time sabendo que: (vitória = 3 pontos, empate = 1 ponto, derrota = 0 pontos) e exiba: O time Corinthians tem 25 pontos no campeonato.
time=str(input('Entre com o nome do time: '))
vitoria=int(input(f'Entre com o número de Vitórias do {time}: '))
empate=int(input(f'Entre com o número de Empates do {time}: '))
derrota=int(input(f'Entre com o número de Derrotas do {time}: '))
pontos=vitoria*3+empate
print(f'O time {time} tem {pontos} pontos no campeonato.')
