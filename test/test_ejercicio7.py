from src.ejercicio7 import calcular_multiplicaciones


def test_calcular_multiplicaciones():
    assert len(calcular_multiplicaciones(1)) == 10
    assert calcular_multiplicaciones(1) == [1,2,3,4,5,6,7,8,9,10]