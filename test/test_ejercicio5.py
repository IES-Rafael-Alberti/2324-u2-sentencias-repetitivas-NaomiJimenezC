from src.ejercicio5 import *


def test_comprobar_porcentajes():
    assert convertir_porcentaje_a_float("95%") == 0.95
    assert convertir_porcentaje_a_float("0%") == 0.0
    assert convertir_porcentaje_a_float("33%") == 0.33
    assert convertir_porcentaje_a_float("7%") == 0.07

def test_calcular_interes_anual():
    assert calcular_interes_anual(15000,"25%") == 18750