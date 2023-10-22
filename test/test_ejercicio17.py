from src.ejercicio17 import *

def test_separacion_num():
    assert separacion_num_digit("842") == [8,4,2]

def test_sum_numeros():
    assert sum_num_digit([8,4,2]) == 14