a= float(input("Entre com o valor de A: "))
b= float(input("Entre com o valor de B: "))
c= float(input("Entre com o valor de C: "))

if (a<b+c) and (b<a+c) and (c<a+b):

	if (a==b) and (b==c):
	
		mens= "Triângulo Equilátero"
	
	elif (a==b) or (b==c) or (c==a):

		mens= "Triângulo Escaleno"
	
	else:
		mens= "Triângulo Escaleno"
else:
	mens="Informação inválida"
print(mens)

#Entradas ==> Resultado
#a=3; b=4; c=5 ==> Triângulo Escaleno
#a=2; b=2; c=4 ==> Informação Inválida
#a=4; b=4; c=4 ==> Triângulo Equilátero
#a=1; b=1; c=1 ==> Triângulo Equilátero
#a=2; b=2; c=3 ==> Triângulo Isósceles
#a=5; b=3; c=3 ==> Triângulo Isósceles
#a=3; b=2; c=4 ==> Informação Inválida
#a=2; b=6; c=5 ==> Informação inválida
#a=4; b=7; c=4 ==> Triângulo Isósceles