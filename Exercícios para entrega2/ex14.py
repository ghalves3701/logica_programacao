#Escreva um algoritmo que receba o nome e total de votos de três candidatos para gestão de um condomínio. O algoritmo deverá responder nesta ordem:
#- O primeiro colocado foi: Fulano de tal, com X% dos votos.
#- O segundo colocado foi: Ciclano de tal, com y% dos votos.
#- O terceiro colocado foi: Beltrano de tal, com M% dos votos
cndt1=str(input("Entre com o nome do candidato 1: "))
votos1=int(input("Entre com a quantidade de votos: "))

cndt2=str(input("Entre com o nome do candidato 2: "))
votos2=int(input("Entre com a quantidade de votos: "))


cndt3=str(input("Entre com o nome do candidato 3: "))
votos3=int(input("Entre com a quantidade de votos: "))

total_votos=votos1+votos2+votos3
porcent1=votos1/total_votos*100
porcent2=votos2/total_votos*100
porcent3=votos3/total_votos*100

if (cndt1>cndt2) and (cndt1>cndt3):
    primeiro=cndt1
    vprimeiro=porcent1
    if (cndt2>cndt3):
        segundo=cndt2
        vsegundo=porcent2

        terceiro=cndt3
        vterceiro=porcent3
    else:
        segundo=cndt3
        vsegundo=porcent3

        terceiro=cndt2
        vterceiro=porcent2
elif (cndt2>cndt3):
    primeiro=cndt2
    vprimeiro=porcent2
    if (cndt1>cndt3):
        segundo=cndt1
        vsegundo=porcent1

        terceiro=cndt3
        vterceiro=porcent3
    else:
        segundo=cndt3
        vsegundo=porcent3

        terceiro=cndt1
        vterceiro=porcent1
else:
    primeiro=cndt3
    vprimeiro=porcent3
    if cndt1>cndt2:
        segundo=cndt1
        vsegundo=porcent1

        terceiro=cndt2
        vterceiro=porcent2
    else:
        segundo=cndt2
        vsegundo=porcent2

        terceiro=cndt1
        vterceiro=porcent1                
print(f'''O primeiro colocado foi: {primeiro}, com {porcent1}% dos votos.
O segundo colocado foi: {segundo}, com {porcent2}% dos votos.
O terceiro colocado foi: {terceiro}, com {porcent3}% dos votos''')