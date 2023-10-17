from src.ejercicio3 import *

def test_listas_impares():
    assert len(sacar_impares(6)) == 3
    assert sacar_impares(6) == [1,3,5]