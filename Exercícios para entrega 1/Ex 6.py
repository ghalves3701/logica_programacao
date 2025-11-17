#Crie um algoritmo que calcule o custo de produção de um produto personalizado considerando matéria-prima medida em quilos. O programa deve receber:
#O preço da matéria-prima por quilo (R$);
#A quantidade de matéria-prima necessária em quilos;
#A porcentagem de desperdício no processo de fabricação (%);
#O tempo necessário para a produção em horas (h);
#O custo da hora de trabalho (R$/h).
#O algoritmo deve calcular:
#O custo total da matéria-prima, considerando o desperdício;
#O custo total do processo de fabricação baseado nas horas de trabalho; e
#O custo total final do produto com essas variáveis.
#A saída deve ser clara e apresentar o resultado final com a mensagem:
#"Com base nos dados fornecidos, o custo total para fabricar o produto, incluindo matéria-prima e trabalho, será de R$ xxx,xx
valor_materia_prima=float(input('Entre com o Valor da matéria prima por kg: '))
quantidade_materia_prima=float(input('Entre com a Quantidade de matéria prima em kg: '))
desperdicio=float(input('Entre com a porcentagem de desperdício: '))
producao_horas=float(input('Entre com o tempo de produção em horas: '))
custo_hora_trabalho=float(input('Entre com o custo de trabalho R$/h'))
custo_materia_prima=valor_materia_prima*quantidade_materia_prima*(1+desperdicio/100)
custo_fabricacao=producao_horas*custo_hora_trabalho
custo_final=custo_materia_prima+custo_fabricacao
print(f'Com base nos dados fornecidos, o custo total para fabricar o produto, incluindo matéria-prima e trabalho, será de R${custo_final}')