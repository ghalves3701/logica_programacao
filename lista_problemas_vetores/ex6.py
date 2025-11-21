'''#(problema sem def)...códito de base para o problema:
carros = ['Chevrolet! Tracker', 'Fiat Fastback', 'Ford Ranger Cabine Dupla'
          'Renault Duster', 'Jeep Compass', 'Peugeot 3008', 'Citroën C4 Cactus'
          'Hyundai Creta', 'Honda CR-V','Corolla Cross', 'Nissan Frontier']
gasolina = [12.5, 13.0, 9.0, 11.0, 10.5, 11.5, 12.0, 12.2, 11.8, 12.7, 8.5]
alcool = [9.0, 9.5, 6.5, 8.0, 7.8, 8.5, 8.8, 9.0, 8.6, 9.2, 6.0]

a) Apresente em uma lista: O nome do automóvel, o gasto médio de gasolina e o gasto médio 
  
b) Apresente:
                - Nome do carro e gasto médio de menor gasto médio de álcool 
                - Nome do carro e gasto médio de maior gasto médio de álcool
                - Nome do carro e gasto médio de menor gasto médio de gasolina 
                - Nome do carro e gasto médio de maior gasto médio de gasolina
                - Média geral de gasto – álcool
                - Média geral de gasto - gasolina'''

carros = ['Chevrolet Tracker', 'Fiat Fastback', 'Ford Ranger Cabine Dupla',
          'Renault Duster', 'Jeep Compass', 'Peugeot 3008', 'Citroën C4 Cactus',
          'Hyundai Creta', 'Honda CR-V','Corolla Cross', 'Nissan Frontier']

gasolina = [12.5, 13.0, 9.0, 11.0, 10.5, 11.5, 12.0, 12.2, 11.8, 12.7, 8.5]
alcool = [9.0, 9.5, 6.5, 8.0, 7.8, 8.5, 8.8, 9.0, 8.6, 9.2, 6.0]

media_menor_a=10000
media_maior_a=0
media_menor_g=10000
media_maior_g=0

for i in range (len(alcool)): #Como os vetores possuem o mesmo tamanho, faremos no mesmo for
   #Verificando Álcool 
    if (alcool[i]) < media_menor_a:  
        media_menor_a=alcool[i]
        carro_gastao_a=carros[i]
    if (alcool[i])>media_maior_a:
        media_maior_a=alcool[i]
        carro_economico_a=carros[i]
  #Verificando Gasolina      
    if (gasolina[i]) < media_menor_g:
        media_menor_g=gasolina[i]
        carro_gastao_g=carros[i]
    if (gasolina[i]) > media_maior_g:
        media_maior_g=gasolina[i]
        carro_economico_g=carros[i]


media_alcool=sum(alcool)/len(alcool)
media_gasolina=sum(gasolina)/len(gasolina)

print(f'''
 ===Carro===      Consumo Gasolina  Consumo Álcool''')#printando cabeçalho

for j in range (len(gasolina)):#printando carro por carro automaticamente
    print(f'''
{carros[j]}          {gasolina[j]}         {alcool[j]} ''')

print(f'''
Consumo no Álcool:      
O Carro mais econômico é o {carro_economico_a} com seu consumo médio de: {media_maior_a}
O Carro menos econômico é o {carro_gastao_a} com seu consumo médio de: {media_menor_a}
Consumo na Gasolina:
O Carro mais econômico é o {carro_economico_g} com seu consumo médio de: {media_maior_g}
O Carro menos econômico é o {carro_gastao_g} com seu consumo médio de: {media_menor_g}
''')