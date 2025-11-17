#Um restaurante cobra R$ 30 por prato principal e R$ 5 por bebida. Escreva um algoritmo que receba a quantidade de pratos principais e bebidas consumidos por um cliente.
#Calcule e exiba:   
#    O valor total dos pratos principais;  
#    O valor total das bebidas;  
#    O valor total da conta;  
#    O valor final com um desconto sobre o total de um percentual(%) que será digitado pelo usuário.
principal=int(input('Entre com a quantidade de pratos principais: '))
bebida=int(input('Entre com a quantidade de bebidas: '))
desconto=float(input('Entre com o valor do desconto em %: '))
valor_principal=30
valor_bebida=5
valor_principal_total=principal*valor_principal
valor_bebida_total=valor_bebida*bebida
valor_total=valor_principal_total+valor_bebida_total
valor_desconto=valor_total-(valor_total*desconto/100)
print(f'O valor dos pratos principais foi R${valor_principal_total:.2F}\nO valor das bebidas foi de R${valor_bebida_total:.2F}\nO valor da conta ficou R${valor_total:.2F}\nO valor da conta com desconto ficou R${valor_desconto:.2F}')
