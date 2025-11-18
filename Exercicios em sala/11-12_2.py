#Adicione o comando "alterar" ao programa anterior
#inicie listando todos os registros
#peça para o usuário digitar o numero do índice do registro que queira alterar
#Enquanto o valor não for um dos índices cadastrados, peça para a pessoa digitar novamente
#peça ao usuário digitar o novo nome e o novo telefone, caso ele não digitar nada, manter os dados atuais
nome=[]
telefone=[]
def main():
    print('''
    1 - Cadastro 
    2 - Consulta
    3 - Alterar cadastro
    ''')
    op = int(input('Digite 1, 2, 3 ou 9 para sair: '))
    def cadastro():
        nome.append(input('Nome: ')) #append = auto incremento
        telefone.append(input('Telefone: '))
    def relatorio():
        for i in range (len(nome)):
            print(f'{i} - {nome[i]} - {telefone[i]}')
    def alterar():
        if (len(nome))==0 and len(telefone) == 0:
            print('''
                                Cadastro vazio
                  Por favor, cadastre um usuário primeiro!''')
            main()
        else:
            relatorio()
            posicao=int(input('Qual item você deseja alterar?: '))
            nome2=input('Entre com o nome: ')
        if nome2 != '':
            nome[posicao]=nome2
        telefone2=input('Entre com o telefone: ')
        if telefone2 != '':
            telefone[posicao]=telefone2

    if op ==1:
        cadastro()
        main()
    elif op == 2:
        relatorio()
        main()
    elif op == 3:
        alterar()
        main()
    elif op == 9:
        print('Saindo do sistema')
    else:
        print(f'\n Você digitou "{op}": Opção inválida!')
        main()
main()