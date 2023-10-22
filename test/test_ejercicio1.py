from src.ejercicio1 import repetir_diez_veces

def test_repetision_palabra():
    assert len(repetir_diez_veces("patata")) == 10
    