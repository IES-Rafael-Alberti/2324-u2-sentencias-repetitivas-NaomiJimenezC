from src.ejercicio13 import *

def test_comprobar_salida():
    assert comprobar_salida("salir") == True
    assert comprobar_salida("patata") == None