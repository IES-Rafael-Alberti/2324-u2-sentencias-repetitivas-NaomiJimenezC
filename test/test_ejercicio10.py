from src.ejercicio10 import *

def test_comprobador_primos():
    assert comprobar_si_num_primo(3) == True
    assert comprobar_si_num_primo(10) == False
    
