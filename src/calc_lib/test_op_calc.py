import op_calc as oc

def test_passer_calc_space():
    assert oc.passer_calc('12 + 2') == [12,'+',2]
    assert oc.passer_calc(' 12 + 2 ') == [12,'+',2]
    assert oc.passer_calc(' 12+2 ') == [12,'+',2]
    assert oc.passer_calc('12   +   2') == [12,'+',2]

def test_passer_calc_results():
    assert oc.passer_calc('12+2') == [12,'+',2]
    assert oc.passer_calc('12-2') == [12,'-',2]
    assert oc.passer_calc('12*2') == [12,'*',2]
    assert oc.passer_calc('12/2') == [12,'/',2]

def test_passer_calc_negatives():
    assert oc.passer_calc('12--2') == [12,'-',-2]
    assert oc.passer_calc('12---2') == False
    assert oc.passer_calc('--12-2') == False
    assert oc.passer_calc('--12') == False

def test_passer_calc_floats():
    assert oc.passer_calc('12.1+21') == [12.1,'+',21]
    assert oc.passer_calc('12+21.1') == [12,'+',21.1]
    assert oc.passer_calc('12.1.1+21') == False
    assert oc.passer_calc('12..12-12') == False
    assert oc.passer_calc('.1-12') == False
    assert oc.passer_calc('12-.1') == False
    assert oc.passer_calc('12.+1') == [12,'+',1]
    assert oc.passer_calc('12.-1') == [12,'-',1]

def test_incomplete_expressions():
    assert oc.passer_calc("") == False
    assert oc.passer_calc("+") == False
    assert oc.passer_calc("12+") == False
    assert oc.passer_calc("+12") == False

def test_prioridade_calc():
    assert oc.prioridade_calc('12(0-2)') == True
    assert oc.prioridade_calc('12((0-2)') == False
    assert oc.prioridade_calc('12(0-2))') == False
    assert oc.prioridade_calc('12[0-2]') == True
    assert oc.prioridade_calc('12[[0-2]') == False
    assert oc.prioridade_calc('12[0-2]]') == False
    assert oc.prioridade_calc('12{0-2}') == True
    assert oc.prioridade_calc('12{{0-2}') == False
    assert oc.prioridade_calc('12{0-2}}') == False

def test_invalid_characters():
    assert oc.passer_calc("12+a") == False
    assert oc.passer_calc("abc") == False
    assert oc.passer_calc("12@2") == False
    assert oc.passer_calc("12+2#") == False

def test_multiple_operators():
    assert oc.passer_calc("12++2") == False
    assert oc.passer_calc("12**2") == False
    assert oc.passer_calc("12//2") == False
    assert oc.passer_calc("12+-2") == [12, '+', -2]

def test_empty_delimiters():
    assert oc.prioridade_calc("()") == True
    assert oc.prioridade_calc("[]") == True
    assert oc.prioridade_calc("{}") == True

def test_crossed_delimiters():
    assert oc.prioridade_calc("([)]") == False
    assert oc.prioridade_calc("{[()]}") == True
    assert oc.prioridade_calc("{[(])}") == False
