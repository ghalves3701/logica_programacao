#Elabore um algoritmo que calcule por quanto tempo uma fonte de energia (uma bateria, por exemplo) suportará o consumo de dispositivos. Receba:
#A capacidade da fonte de energia em mAh (miliampere-hora);
#O consumo médio de cada dispositivo conectado (em mAh/h);
#A quantidade total de dispositivos conectados.
#Calcule o tempo de duração e exiba algo como:
#"Com uma bateria de 10000 mAh e 4 dispositivos consumindo 500 mAh por hora, a bateria durará 5 horas."
capacidade=int(input('Entre com a capacidade da fonte em mAh: '))
consumo=int(input('Entre com o consumo médio de cada dispositivo em mAh: '))
dispositivos=int(input('Entre com a quantidade de dispositivos conectados: '))
total=dispositivos*consumo
duracao=capacidade/total
print(f'Com uma bateria de {capacidade} mAh e {dispositivos} dispositivos consumindo {total} mAh por hora, a bateria durará {duracao} horas.')