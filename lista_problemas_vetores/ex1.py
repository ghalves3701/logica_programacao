valor = [] #não precisa ser criada redeclarada como global
negativos = 0 #Variável Global
positivos = 0 #Variável Global
def main(): 
  print('\n1 - Ler Valor\n2 - Contar Negativos\n3 - Contar Positivo')
  op = int(input('Escolha uma opção (1,2,3 ou 9 para sair: )'))
  def lervalor():  
    if (len(valor)==10):
      print('\nValores já cadastrados!')
    else:
      print('\nLoop For com append em valor:')
      for i in range (9):
        valor.append(int(input(f'Digite o {i+1}º valor: ')))
  def contarnegativos():
    global negativos #variáveis 'não vetor' declaradas como globais
    negativos = 0 #zerar para contar novamente 
    for i in range (len(valor)) : #Programar for i ... len(valor).. com if para contar negativos 
      if valor[i] < 0:
        negativos += 1

  def contarpositivos():
    global positivos #variáveis 'não vetor' declaradas como globais 
    positivos = 0 #zerar para contar novamente 
    for i in range (len(valor)): #Programar for i ... len(valor).. com if para contar positivos
      if valor [i]>=0:
        positivos += 1
  if (op == 1):
    lervalor()
    main() 
  elif (op == 2):
    contarnegativos()
    print(f'Quandidade de negativos: {negativos}\n')
    main() 
  elif (op == 3):
    contarpositivos()
    print(f'\nQuantidade Final de Positivos: {positivos}\n')
    main()
  elif (op == 9):
    print('Fechando o Sistema!')
  else:
    print('Opção Inválida!')
    main()
#Após a def no ínicio da linha:
main()
print(f'\nQuantidade Final de Positivos: {positivos}\n')
print(f'Quandidade Final de negativos: {negativos}\n')

