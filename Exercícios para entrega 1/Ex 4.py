#Crie um programa que calcule a quantidade total de água necessária para irrigar uma plantação, com base nas informações fornecidas pelo usuário. O programa deve receber:
#A área total da plantação (em metros quadrados);
#A quantidade de água necessária para irrigar cada metro quadrado por dia (em litros);
#O número de dias durante os quais a plantação será irrigada.
#Com os dados fornecidos, o programa deverá calcular a quantidade total de água necessária e apresentar o resultado em uma mensagem como:
#"Para irrigar uma plantação de 2000 m² durante 10 dias, serão necessários 20000 litros de água."
area_plantacao=float(input('Entre com a área total da plantação em m²: '))
quantidade_agua=float(input('Entre com a quantidade de água diária, em litros, necessária por dia para cada m²: '))
dias_irrigacao=float(input('Entre com a quantidade de dias que a plantação deverá ser irrigada: '))

total_agua=area_plantacao*quantidade_agua*dias_irrigacao

print(f'Para irrigar uma plantação de {area_plantacao} m² durante {dias_irrigacao} dias, serão necessários {total_agua} litros de água.')