#Faça um algoritmo que receba:
#O nome do atleta;
#O objetivo de distância total a ser corrida (em quilômetros);
#O número de dias para alcançar o objetivo.
#O programa deve calcular a distância média diária que o atleta deve percorrer e exibir:
#"O atleta João deverá correr 5 km por dia para alcançar 25 km em 5 dias."
nome=str(input('Entre como o nome: '))
objetivo=float(input('Entre com o seu objetivo em kilômetros '))
dias=int(input('Em quantos dias você quer alcançar o seu objetivo:'))
total=objetivo/dias
print(f'O atleta {nome} deverá correr {total} km por dia para alcançar {objetivo} km em {dias} dias.')