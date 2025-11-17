qtd_morango=float(input('Entre com a quantidade de morangos em Kg: '))
qtd_maca=float(input("Entre com a quantidade de maçãs em Kg: "))
qtd_total=qtd_morango+qtd_maca


if qtd_total>8:#pela lógica, precisaremos comparar somente os 8kg, sempre ocorrerá primeiro que R$25,00.
    if qtd_morango>5:
        total_morango=qtd_morango*2.2*0.9
    else:
        total_morango=qtd_morango*2.5*0.9
    if qtd_maca>5:
        total_maca=qtd_maca*1.5*0.9
    else:
        total_maca=qtd_maca*1.8*0.9
else:
    if qtd_morango>5:
        total_morango=qtd_morango*2.2
    else:
        total_morango=qtd_morango*2.5
    if qtd_maca>5:
        total_maca=qtd_maca*1.5
    else:
        total_maca=qtd_maca*1.8

total=total_maca+total_morango

print(f'O total a ser pago é de R${total:.2F}')