numero=int(input('Entre com o número: '))
fatorial=1
print('5!= ')
for i in range (0,numero):
    decresc=numero-i # 5 4 3 2 1
    print(f'{decresc}*')
    pre_fatorial=decresc*fatorial #5 20 60 120
    fatorial=pre_fatorial #5 20 60 120 
print(f'={fatorial}')
