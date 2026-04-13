from calc_lib import op_calc as op
while True:
    inp = input('Conta:')
    if inp in 'Nn':
        break
    #passer_calc(inp)
    res = op.mul_calc(inp)
    res = op.soma_calc(inp)
    print(res)
    