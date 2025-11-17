numero=int(input("Entre com um número maior ou igual a 3: "))
multiplos=0 


while numero<3:
    print("Número inválido, tente novamente.")
    n=int(input("Entre com um número maior ou igual a 3: "))

#tipo 1
while multiplos<numero:
    multiplos=multiplos+3
    if multiplos<=numero:
        print(multiplos)
if multiplos>numero:
    print(numero)
#fim tipo 1

'''  
#tipo 2 (mais eficiente)

n=(numero//3)+1 # pesquisei para saber como armazenar somente a parte inteira da divisão e não trazer variável do tipo float 

for i in range (1,n):
    if multiplos>=numero:
        break  #pesquisei para saber como sair do loop nesse caso o "for". 
    else:
        multiplos=i*3
        print(multiplos)
if numero>multiplos:
    print(numero)    
#fim tipo 2
'''