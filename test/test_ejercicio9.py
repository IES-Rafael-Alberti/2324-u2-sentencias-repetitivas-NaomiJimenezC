from src.ejercicio9 import *

def test_comprobador():
    assert comprobar_intento("pikaku","pikaku") == True
    assert comprobar_intento("pikaku","Pikaku") == False