from src.ejercicio18 import *

def test_sacar_pares():
    assert sacar_pares([1,2,3,4,5,6]) == [2,4,6]

def test_comprobar_menos_uno():
    assert comprobar_si_menos_uno("-1") == True
    assert comprobar_si_menos_uno("4") == None