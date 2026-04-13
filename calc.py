from calc_lib import op_calc as op
while True:
    inp = input('Conta:')
    if inp in 'Nn':
        break
    res = op.passer_calc(inp)
    res = op.mul_calc(res)
    res = op.soma_calc(inp)
    print(res)
    