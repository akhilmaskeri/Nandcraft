import pytest
from chips import Not, Not16, And, And16, Or, Or16, Or8Way, Xor
from core import InvalidInputLengthException

def test_Not_gate() -> None:
    assert Not(True) == False
    assert Not(False) == True

def test_Not16_valid_input():
    input_data = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    expected_output = [False, True, False, True, True, False, True, False, False, True, False, True, True, False, True, False]
    assert Not16(input_data) == expected_output

def test_Not16_invalid_input():
    with pytest.raises(InvalidInputLengthException):
        Not16([True, False, True])  # Input length is not 16

def test_Not16_all_true_input():
    input_data = [True] * 16
    expected_output = [False] * 16
    assert Not16(input_data) == expected_output

def test_Not16_all_false_input():
    input_data = [False] * 16
    expected_output = [True] * 16
    assert Not16(input_data) == expected_output


def test_and_gate() -> None:
    assert And(True, True) == True
    assert And(True, False) == False
    assert And(False, True) == False
    assert And(False, False) == False

def test_And16_valid_input():
    a = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    b = [False, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False]
    expected_output = [False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False]
    assert And16(a, b) == expected_output

def test_And16_invalid_inputs():
    with pytest.raises(InvalidInputLengthException):
        And16([True, False, True], [False] * 16)  # Input length for 'a' is not 16
    
    with pytest.raises(InvalidInputLengthException):
        And16([True] * 16, [False, True, True])  # Input length for 'b' is not 16

def test_And16_all_true_input():
    a = [True] * 16
    b = [True] * 16
    expected_output = [True] * 16
    assert And16(a, b) == expected_output

def test_And16_all_false_input():
    a = [False] * 16
    b = [False] * 16
    expected_output = [False] * 16
    assert And16(a, b) == expected_output

def test_Or():
    assert Or(True, True) == True
    assert Or(True, False) == True
    assert Or(False, True) == True
    assert Or(False, False) == False

def test_Or16_valid_input():
    a = [True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, True]
    b = [False, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False]
    expected_output = [True, True, True, False, False, True, True, True, True, False, True, True, True, True, True, True]
    assert Or16(a, b) == expected_output


def test_Or16_invalid_input():
    with pytest.raises(InvalidInputLengthException):
        Or16([True, False, True], [False] * 16)  # Input length for 'a' is not 16
    
    with pytest.raises(InvalidInputLengthException):
        Or16([True] * 16, [False, True, True])  # Input length for 'b' is not 16
    

def test_Or16_all_true_input():
    a = [True] * 16
    b = [True] * 16
    expected_output = [True] * 16
    assert Or16(a, b) == expected_output

def test_Or16_all_false_input():
    a = [False] * 16
    b = [False] * 16
    expected_output = [False] * 16
    assert Or16(a, b) == expected_output

def test_Or8Way_valid_input():
    input_data = [True, False, True, False, False, True, False, True]
    assert Or8Way(input_data) == True

def test_Or8Way_invalid_input():
    with pytest.raises(InvalidInputLengthException):
        Or8Way([True, False, True])  # Input length is not 8

def test_Or8Way_all_true_input():
    input_data = [True] * 8
    assert Or8Way(input_data) == True

def test_Or8Way_all_false_input():
    input_data = [False] * 8
    assert Or8Way(input_data) == False

def test_Xor_true_false():
    assert Xor(True, False) == True
    assert Xor(False, True) == True
    assert Xor(True, True) == False
    assert Xor(False, False) == False
