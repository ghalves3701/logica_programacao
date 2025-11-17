#Desenvolva um algoritmo que solicite a quantidade de peças produzidas por um operário, o valor pago por peça, e o percentual de impostos sobre a produção. 
#Calcule e escreva na tela:
#A) o valor bruto a ser recebido; 
#B) o valor dos impostos; 
#C) o valor líquido a ser pago ao operário.
producao=int(input('Entre com a quantidade de peças produzidas: '))
valor=int(input('Entre com a quantidade de peças produzidas:'))
imposto=float(input('Entre com o percentual de imposto sobre a produção: '))
bruto=producao*valor
valor_imposto=bruto*imposto/100
recebiveis=bruto-valor_imposto
print(f'Valor bruto: R${bruto:.2F}\nValor do imposto: R${valor_imposto:.2F}\nValor líquido: R${recebiveis:.2F}')
