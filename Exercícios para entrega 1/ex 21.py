#Receba a quantidade de água (em litros) atual e a capacidade máxima do tanque. Caso a quantidade seja igual ou superior ao máximo, exiba: "O tanque já está cheio (X litros)." Caso contrário, exiba: "Faltam Y litros para encher o tanque (atual: Z litros)."
atual=float(input('Entre com a quantidade atual de água em litros: '))
capacidade=float(input('Entre com a capacidade do tanque em litros: '))
if (capacidade>atual):
    falta=capacidade-atual
    print(f'Faltam {falta} litros para encher o tanque (atual: {atual} litros)')
else:
    print(f'o tanque está cheio ({atual} litros)')
