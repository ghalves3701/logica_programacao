nome=str(input("Entre com o seu nome: "))
tp=str(input("Estado Civil (C=Casado, A=Solteiro, S=Separado, D=Divorciado, V=Viuvo): ")).upper()

while tp not in ("S,C,A,D,V"):
    print("Estado civil e/ou Escolaridade incorreta")
    tp=str(input("Estado Civil (C=Casado, A=Solteiro, S=Separado, D=Divorciado, V=Viuvo): ")).upper()

es=str(input("Escolaridade (A=Ensino Fundamental, B=Ensino Médio, C=Graduação, D=Pós-Graduação): ")).upper()

while es not in ("A,B,C,D"):#Verificando se o estado civil está de acordo com o pedido...
    es=str(input("Escolaridade (A=Ensino Fundamental, B=Ensino Médio, C=Graduação, D=Pós-Graduação): ")).upper
#fim da verificação

numero=int(input("Entre com um número entre 0 e 100 que seja par: "))
x=numero%2

while x!=0 or 0>x>100:#Verificando se o número está de acordo com o pedido... 
    print("Número incorreto")
    numero=int(input("Entre com um número entre 0-100 que seja par: "))
    x=numero%2
#Fim da verificação

#Verificando estado civil...
if tp==("C"):
    ec="Casado"
elif tp==("A"):
    ec="Solteiro"
elif tp==("S"):
    ec= "Separado"
elif tp==("D"):
    ec="Divorciado"
else:
    ec="Viúvo"
#Fim da verificação

#verificando escolaridade
if es==("A"):
    esfim="Ensino Fundamental"
elif es==("B"):
    esfim="Ensino Médio"
elif es==("C"):
    esfim= "Graduação"
else:
    esfim="Pós Graduação"

#Fim da verificação

#prints
print(f"Olá {nome}, Seu estado civil é {ec}, sua escolaridade é {esfim} e o número par digitado é : {numero}")