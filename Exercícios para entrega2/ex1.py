#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


periodo=str(input("Entre com o turno em que você estuda:\nM-Matutino, V-Vespertino, N-Noturno: ")).upper()
if(periodo=='M'):
    msg="Bom dia"
elif(periodo=='V'):
    msg="Boa Tarde"
else:
    msg="Boa Noite"
print(msg)
