#Os avanços na geração de energia solar permitem que diferentes tipos de painéis sejam usados para capturar e converter a luz do sol em eletricidade. Imagine que você quer avaliar dois modelos de painéis solares para descobrir qual deles consegue produzir mais energia elétrica ao longo de um ano, considerando sua eficiência, a quantidade máxima de energia que podem produzir por dia e o número de dias ensolarados previstos na região.
#Você deve desenvolver um programa para coletar os seguintes dados para cada painel solar:
#A eficiência do painel, indicada em um valor percentual (%), que representa o aproveitamento da radiação solar.
#A energia máxima gerada diariamente, indicada em quilowatt-hora (kWh).
#O número de dias ensolarados no ano, que será igual para ambos os #painéis.
#Com essas informações, seu programa deve calcular a produção anual de energia elétrica para cada painel e determinar qual deles gera mais energia no ano. Ao final, apresente o total de energia gerada por cada painel e destaque o mais eficiente.
#Exemplo 1: Painel 2 é mais eficiente
#Entrada:
#Eficiência do painel 1: 80%
#Produção máxima do painel 1: 5 kWh por dia
#Eficiência do painel 2: 90%
#Produção máxima do painel 2: 4.8 kWh por dia
#Dias ensolarados no ano: 365 dias
#Saída:
#O painel 2 gera mais energia no ano: 1576.8 kWh. O painel 1 gera 1460.0 kWh.
# ...
#Exemplo 2: Painel 1 é mais eficiente
#Entrada:
#Eficiência do painel 1: 85%
#Produção máxima do painel 1: 6 kWh por dia
#Eficiência do painel 2: 80%
#Produção máxima do painel 2: 6 kWh por dia
#Dias ensolarados no ano: 320 dias
#Saída:
#O painel 1 gera mais energia no ano: 1632.0 kWh. O painel 2 gera 1536.0 kWh.
eficiencia1=float(input('Entre com a Eficiência em porcentagem do painel 1: '))
producao1=float(input('Entre com a Produção máxima do Painel 1: '))
eficiencia2=float(input('Entre com a Eficiência em porcentagem do painel 2: '))
producao2=float(input('Produção máxima do Painel 2: '))
dias_ensolarados=int(input('Entre com os dias ensolarados no ano: '))
painel1=eficiencia1*producao1/100*dias_ensolarados
painel2=eficiencia2*producao2/100*dias_ensolarados

if (painel1>painel2):
    print(f'O painel 1 gera mais energia no ano: {painel1} kWh. O painel 2 gera {painel2} kWh.')
else:
    print(f'O painel 2 gera mais energia no ano: {painel2} kWh. O painel 1 gera {painel1} kWh.')