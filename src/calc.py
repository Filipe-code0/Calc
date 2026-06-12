from calc_lib import op_calc as op
while True:
    inp = input('Conta:')
    if inp in 'Nn':
        break
    res = op.passer_calc(inp)
    if res == False:
        print('erro de escrita tente novamente')
        continue
    res = op.mul_calc(res)
    res = op.soma_calc(res)
    print(res)
    
