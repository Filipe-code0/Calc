def soma_calc(inp):
    lista = inp.copy()
    for i in range(1, len(inp), 2):
        if len(lista) == 1:
            break
        elif lista[1] in '+':
            lista[0] = lista[0] + lista[2]
            lista.pop(1)
            lista.pop(1)
        elif lista[1] in '-':
            lista[0] = lista[0] - lista[2]
            lista.pop(1)
            lista.pop(1)
    return lista

def mul_calc(inp):
    lista = inp.copy()
    i = 1
    while True:
        if len(lista) == 1 or i >= len(lista):
            break
        elif lista[i] == '*':
            lista[i-1] = lista[i-1] * lista[i+1]
            lista.pop(i)
            lista.pop(i)
        elif lista[i] == '/':
            lista[i-1] = lista[i-1] / lista[i+1]
            lista.pop(i)
            lista.pop(i)
        else:
            i += 2
    return lista

def passer_calc(inp):
    txt = inp.strip()
    txt = f'{txt}_'
    opts = '+-/*_.'
    buffer = ''
    flag_ponto = False
    lista = []
    for i in range(0, len(txt)):
        if len(txt) == 1:
            return False
        elif txt[i].isnumeric() or txt[i] in '-' and buffer == '' and i != (len(txt)-2):
            buffer += txt[i]
        elif txt[i] in opts:
            if txt[i] not in '-' and i == 0: 
                return False
            elif txt[i] in '_' and i != (len(txt)-1):
                return False
            elif txt[i] in '+/*-' and i == (len(txt)-2):
                return False
            elif txt[i] in '+/*' and buffer == '':
                return False
            elif txt[i] in '.':
                if flag_ponto == True:
                    return False
                flag_ponto = True
                buffer += txt[i]
            else:
                try:
                    num = float(buffer)
                except:
                    return False
                lista.append(num)
                buffer = ''
                flag_ponto = False
                flag_ponto
                if txt[i] != '_':
                    lista.append(txt[i])
    return lista

