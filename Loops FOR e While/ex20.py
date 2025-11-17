continuacao="S"
cont_baixo=0
cont_eutrofia=0
cont_sobrepeso=0
cont_obesidade=0
cont_maior=0
cont=0
peso_maior=0.0
peso_menor=999999999999999.99
while continuacao == "S":
    nome=str("Entre com o nome: ")
    peso=float("entre com o seu peso em Kg: ")
    altura=float("Eentre com a sua altura em m: ")
    imc=peso/altura/altura
    if imc<18.5:
        print("Baixo peso")
        cont_baixo+=1
    elif 18.5<=imc<=24.9:
        print("Eutrofia")
        cont_eutrofia+=1
    elif 24.9<=imc<=29.9:
        print("Sobrepeso")
        cont_sobrepeso+=1
    else:
        print("Obesidade")
        cont_obesidade+=1
    if imc>35:
        cont_maior+=1
    if imc>peso_maior:
        peso_maior=imc
        nome_maior=nome
    if imc<peso_menor:
        peso_menor=imc
        nome_menor=nome
    soma_imc+=imc
    cont+=1
    media=soma_imc/cont
    continuacao=str(input('Deseja continuar? ("S"=sim)/("N"=não): ')).upper()
print(f'''
Quantidade de Baixo peso: {cont_baixo}
Quantidade de Eutrofia: {cont_eutrofia}
Quantidade de Sobrepeso: {cont_eutrofia}
Quantidade de Obeso: {cont_obesidade}
Quantidade de imc>35: {cont_maior}
Média geral obesidade{media}
O maior IMC foi do {nome_maior} com IMC={peso_maior}
O menor IMC foi o do {nome_menor} com IMC={peso_menor} 
 ''')