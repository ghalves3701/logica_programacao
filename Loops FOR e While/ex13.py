##Ex 13
verificador=''
cont_morador=0
idade_maior=0
tempo_maior=0
soma_idade=0


while verificador!='N':
    nome=str(input("Entre com o nome: "))
    tempo=int(input("Entre com o tempo que mora no condomínio: "))
    idade=int(input("entre com a sua idade: "))
    print()

    if idade>idade_maior:
      idade_maior=idade
      nome_velho=nome
    if tempo>tempo_maior:
      tempo_maior=tempo
      nome_tempo=nome

    soma_idade+=idade
    cont_morador+=1
    verificador=str(input("Você deseja continuar? S=sim, N=não: ")).upper()
    print()

media=soma_idade/cont_morador

print(f'''
A quantidade de moradores cadastrados é de: {cont_morador}
O Morador mais velho é o {nome_velho}, com {idade_maior} anos
A pessoa que mora a mais tempo no condomínio é o {nome_tempo} e 
mora no condomínio há {tempo_maior} anos''')