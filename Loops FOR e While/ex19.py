sair=125378200

while sair!=9:
    while sair!=(1 or 2 or 3 or 9 or 125378200):
        print("numero invalido")
        sair=int(input(f'''
        Entre com a operação desejada:
        1 - Tabuada
        2 - Cálculo de produto
        3 - Sequência de números
        9 - Sair'''))
    if sair == 1:
            print("####TABUADA###")
            num= int(input('Numero: '))
            for i in range(1,11):
                print(f'{num} * {i}= {num*i}')
    if sair == 2:
            print("###Cálculo de produto")
            value_total=0.0
            for i in range (1,6):
                code_product=int(input(f"Entre com o código do produto {i}: "))
                quant_product=int(input(f"Entre com a quantidade do produto {i}: "))
                preco=float(input(f"Entre com o preço unitário do produto {i}: "))
                value_total+= (quant_product*preco)
            print(f"O valor total dos itens foi de R${value_total}")
    if sair == 3:
            print("###Sequência de números###")
            num1=int(input("entre com o primeiro número: "))
            num2=int(input("entre com o segundo número:"))

            if num1==num2 or num1>num2:
                print('Número inválido')
            else:
                for i in range(num1, num2+1):
                    print(i)

    sair=int(input(f'''
        Entre com a operação desejada:
        1 - Tabuada
        2 - Cálculo de produto
        3 - Sequência de números
        9 - Sair'''))