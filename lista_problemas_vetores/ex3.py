'''Desenvolva um algoritmo com a def vogal(): 
- A def deverá receber uma letra via input, digitada pelo usuário
- Caso a letra digitada não esteja entre a, e, i, o e u, apresente a mensagem: 'Letra Inválida! ' e, depois, reexecute a def vogal() chamando-a novamente e recomeçando o processo.
- Sendo uma letra vogal digitada entre a, e, i, o e u, digite a mensagem 'Letra ok: {letra} '''
def vogal():
    letra=str(input("Entre com uma letra: ")).upper()
    if letra in ('A', 'E', 'I', 'O', 'U'):
        print(f'Letra ok: {letra}')
    else:
        print('\n Letra inválida \n')
        vogal()
vogal()   