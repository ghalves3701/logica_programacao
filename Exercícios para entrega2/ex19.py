dia=int(input("Qual dia você nasceu?"))
if dia<1 or dia>31:
  print('dia inválido')
mes=int(input("Qual mês você nasceu?"))
if mes<1 or mes>12:
  print("Mês Inválido")
ano=int(input("Qual ano você nasceu?"))
if ano < 1900 or ano > 2013:
  print("ano inválido")
print(f'Data válida, {dia}, {mes}, {ano}') 