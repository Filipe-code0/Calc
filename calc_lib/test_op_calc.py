from op_calc import passer_calc

def test_passer_calc_space():
    assert passer_calc('12 + 2') == [12,'+',2]
    assert passer_calc('12 - 2') == [12,'-',2]

def test_passer_calc_results():
    assert passer_calc('12+2') == [12,'+',2]
    assert passer_calc('12-2') == [12,'-',2]

def test_passer_calc_negatives():
    assert passer_calc('12--2') == [12,'-',-2]
    assert passer_calc('12---2') == False
    assert passer_calc('--12-2') == False

def test_passer_calc_floats():
    assert passer_calc('12.1+21') == [12.1,'+',21]
    assert passer_calc('12+21.1') == [12,'+',21.1]
    assert passer_calc('12.1.1+21') == False

