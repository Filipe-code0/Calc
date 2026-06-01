import op_calc as oc

def test_passer_calc_space():
    assert oc.passer_calc('12 + 2') == [12,'+',2]
    assert oc.passer_calc('12 - 2') == [12,'-',2]

def test_passer_calc_results():
    assert oc.passer_calc('12+2') == [12,'+',2]
    assert oc.passer_calc('12-2') == [12,'-',2]

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

def test_prioridade_calc():
    assert oc.prioridade_calc('12(0-2)') == True
    assert oc.prioridade_calc('12((0-2)') == False
    assert oc.prioridade_calc('12(0-2))') == False

