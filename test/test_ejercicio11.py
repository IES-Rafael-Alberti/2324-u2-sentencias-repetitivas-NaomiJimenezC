from src.ejercicio11 import *

def test_separador_por_letra():
    assert dividir_palabra_en_letras("pikaku") == ['p','i','k','a','k','u']

def test_invertir_palabra():
    assert ordenar_palabras(['p','i','k','a','k','u']) == ['u','k','a','k','i','p']