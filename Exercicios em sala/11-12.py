nome=[]
telefone=[]
def main():
    print('''
    1 - Cadastro: 
    2 - Consulta
    ''')
    op = int(input('Digite 1 , 2 ou 9 para sair: '))
    def cadastro():
        nome.append(input('Nome: '))
        telefone.append(input('Telefone: '))
    def relatorio():
        for i in range (len(nome)):
            print(f'{i} - {nome[i]} - {telefone[i]}')
    if op ==1:
        cadastro()
        main()
    elif op == 2:
        relatorio()
        main()
    elif op == 9:
        print('Saindo do sistema"')
    else:
        print('Opção inválida!')
        main()
main()












