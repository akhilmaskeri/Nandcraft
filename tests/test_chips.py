from chips import DMux, DMux4Way, DMux8Way, Mux, Mux4Way16, Mux8Way16
import pytest
from core import InvalidInputLengthException

def test_DMux_input_false_sel_false():
    _in = False
    sel = False
    assert DMux(_in, sel) == [False, False]

def test_DMux_input_false_sel_true():
    _in = False
    sel = True
    assert DMux(_in, sel) == [False, False]

def test_DMux_input_true_sel_false():
    _in = True
    sel = False
    assert DMux(_in, sel) == [True, False]

def test_DMux_input_true_sel_true():
    _in = True
    sel = True
    assert DMux(_in, sel) == [False, True]


def test_DMux4Way_sel_length_invalid():
    with pytest.raises(InvalidInputLengthException):
        DMux4Way(True, [True, False, True])  # sel length is not 2

def test_DMux4Way_input_false_sel_00():
    _in = False
    sel = [False, False]
    assert DMux4Way(_in, sel) == [False, False, False, False]

def test_DMux4Way_input_true_sel_00():
    _in = True
    sel = [False, False]
    assert DMux4Way(_in, sel) == [True, False, False, False]

def test_DMux4Way_input_false_sel_01():
    _in = False
    sel = [False, True]
    assert DMux4Way(_in, sel) == [False, False, False, False]

def test_DMux4Way_input_true_sel_01():
    _in = True
    sel = [False, True]
    assert DMux4Way(_in, sel) == [False, False, True, False]

def test_DMux4Way_input_false_sel_10():
    _in = False
    sel = [True, False]
    assert DMux4Way(_in, sel) == [False, False, False, False]

def test_DMux4Way_input_true_sel_10():
    _in = True
    sel = [True, False]
    assert DMux4Way(_in, sel) == [False, True, False, False]

def test_DMux4Way_input_false_sel_11():
    _in = False
    sel = [True, True]
    assert DMux4Way(_in, sel) == [False, False, False, False]

def test_DMux4Way_input_true_sel_11():
    _in = True
    sel = [True, True]
    assert DMux4Way(_in, sel) == [False, False, False, True]


def test_DMux8Way_input_false_sel_000():
    _in = False
    sel = [False, False, False]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_000():
    _in = True
    sel = [False, False, False]
    assert DMux8Way(_in, sel) == [True, False, False, False, False, False, False, False]

def test_DMux8Way_input_false_sel_001():
    _in = False
    sel = [False, False, True]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_001():
    _in = True
    sel = [False, False, True]
    assert DMux8Way(_in, sel) == [False, True, False, False, False, False, False, False]

def test_DMux8Way_input_false_sel_010():
    _in = False
    sel = [False, True, False]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_010():
    _in = True
    sel = [False, True, False]
    assert DMux8Way(_in, sel) == [False, False, True, False, False, False, False, False]

def test_DMux8Way_input_false_sel_011():
    _in = False
    sel = [False, True, True]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_011():
    _in = True
    sel = [False, True, True]
    assert DMux8Way(_in, sel) == [False, False, False, True, False, False, False, False]

def test_DMux8Way_input_false_sel_100():
    _in = False
    sel = [True, False, False]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_100():
    _in = True
    sel = [True, False, False]
    assert DMux8Way(_in, sel) == [False, False, False, False, True, False, False, False]

def test_DMux8Way_input_false_sel_101():
    _in = False
    sel = [True, False, True]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_101():
    _in = True
    sel = [True, False, True]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, True, False, False]

def test_DMux8Way_input_false_sel_110():
    _in = False
    sel = [True, True, False]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_110():
    _in = True
    sel = [True, True, False]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, True, False]

def test_DMux8Way_input_false_sel_111():
    _in = False
    sel = [True, True, True]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, False]

def test_DMux8Way_input_true_sel_111():
    _in = True
    sel = [True, True, True]
    assert DMux8Way(_in, sel) == [False, False, False, False, False, False, False, True]

def test_Mux_a_true_b_true_sel_false():
    a = True
    b = True
    sel = False
    assert Mux(a, b, sel) == True

def test_Mux_a_true_b_false_sel_false():
    a = True
    b = False
    sel = False
    assert Mux(a, b, sel) == True

def test_Mux_a_false_b_true_sel_false():
    a = False
    b = True
    sel = False
    assert Mux(a, b, sel) == False

def test_Mux_a_false_b_false_sel_false():
    a = False
    b = False
    sel = False
    assert Mux(a, b, sel) == False

def test_Mux_a_true_b_true_sel_true():
    a = True
    b = True
    sel = True
    assert Mux(a, b, sel) == True

def test_Mux_a_true_b_false_sel_true():
    a = True
    b = False
    sel = True
    assert Mux(a, b, sel) == False

def test_Mux_a_false_b_true_sel_true():
    a = False
    b = True
    sel = True
    assert Mux(a, b, sel) == True

def test_Mux_a_false_b_false_sel_true():
    a = False
    b = False
    sel = True
    assert Mux(a, b, sel) == False

def test_Mux4Way16_valid_input():
    a = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    b = [False, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False]
    c = [True, True, False, False, True, False, False, True, False, True, False, True, False, True, True, False]
    d = [False, False, False, True, True, False, True, True, True, False, False, False, False, True, False, True]
    sel = [False, True]
    expected_output = [False, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False]
    assert Mux4Way16(a, b, c, d, sel) == expected_output

def test_Mux4Way16_invalid_input_a():
    with pytest.raises(InvalidInputLengthException):
        Mux4Way16([True, False, True], [False] * 16, [True] * 16, [False] * 16, [False, True])  # Input length for 'a' is not 16

def test_Mux4Way16_invalid_input_b():
    with pytest.raises(InvalidInputLengthException):
        Mux4Way16([True] * 16, [False, True, True], [True] * 16, [False] * 16, [False, True])  # Input length for 'b' is not 16

def test_Mux4Way16_invalid_input_c():
    with pytest.raises(InvalidInputLengthException):
        Mux4Way16([True] * 16, [False] * 16, [True, True, False], [False] * 16, [False, True])  # Input length for 'c' is not 16

def test_Mux4Way16_invalid_input_d():
    with pytest.raises(InvalidInputLengthException):
        Mux4Way16([True] * 16, [False] * 16, [True] * 16, [False, False, False], [False, True])  # Input length for 'd' is not 16

def test_Mux4Way16_invalid_input_sel():
    with pytest.raises(InvalidInputLengthException):
        Mux4Way16([True] * 16, [False] * 16, [True] * 16, [False] * 16, [False, True, True])  # sel length is not 2

def test_Mux8Way16_valid_input():
    a = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    b = [False, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False]
    c = [True, True, False, False, True, False, False, True, False, True, False, True, False, True, True, False]
    d = [False, False, False, True, True, False, True, True, True, False, False, False, False, True, False, True]
    e = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    f = [False, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False]
    g = [True, True, False, False, True, False, False, True, False, True, False, True, False, True, True, False]
    h = [False, False, False, True, True, False, True, True, True, False, False, False, False, True, False, True]
    sel = [False, False, False]
    expected_output = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    assert Mux8Way16(a, b, c, d, e, f, g, h, sel) == expected_output

def test_Mux8Way16_invalid_input_a():
    with pytest.raises(InvalidInputLengthException):
        Mux8Way16([True, False, True], [False] * 16, [True] * 16, [False] * 16, [True] * 16, [False] * 16, [True] * 16, [False] * 16, [False, False, False])  # Input length for 'a' is not 16

def test_Mux8Way16_invalid_input_b():
    with pytest.raises(InvalidInputLengthException):
        Mux8Way16([True] * 16, [False, True, True], [True] * 16, [False] * 16, [True] * 16, [False] * 16, [True] * 16, [False] * 16, [False, False, False])  # Input length for 'b' is not 16

def test_Mux8Way16_invalid_input_c():
    with pytest.raises(InvalidInputLengthException):
        Mux8Way16([True] * 16, [False] * 16, [True, True, False], [False] * 16, [True] * 16, [False] * 16, [True] * 16, [False] * 16, [False, False, False])  # Input length for 'c' is not 16

def test_Mux8Way16_invalid_input_d():
    with pytest.raises(InvalidInputLengthException):
        Mux8Way16([True] * 16, [False] * 16, [True] * 16, [False, False, False], [True] * 16, [False] * 16, [True] * 16, [False] * 16, [False, False, False])  # Input length for 'd' is not
