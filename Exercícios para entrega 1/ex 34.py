#Receba a potência (em HP) de duas máquinas industriais e exiba qual delas apresenta maior potência. Caso sejam iguais, informe: "Ambas as máquinas possuem potência igual: X HP."
#Exemplo de saída:
#"A máquina 1 tem maior potência: 150 HP. A máquina 2 tem menor potência: 130 HP."
maquina1=float(input('Entre com a Potência da primeira máquina em HP: '))
maquina2=float(input('Entre com a Potência da segunda máquina em HP: '))

if (maquina1==maquina2):
    print(f'Ambas as máquinas possuem potência igual: {maquina2} HP')
else:
    if(maquina1>maquina2):
        print(f'A máquina 1 tem maior potência: {maquina1} HP. A máquina 2 tem menor potência: {maquina2} HP.')
    else:
        print(f'A máquina 2 tem maior potência: {maquina2} HP. A máquina 1 tem menor potência: {maquina1} HP.')