from src.ejercicio16 import *

def test_comprobar_ordenacion():
    assert ordenar_lista_num([1,3,2,5,4,6]) == [6,5,4,3,2,1]
    
def test_sacar_num_max():
    assert sacar_numero_mayor([6,5,4,3,2,1]) == 6