"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

def solicitar_cantidad_a_invertir():
    capital_invertido = input("Ingrese el capital que se desea invertir: ")
    while capital_invertido.isnumeric() != True:
        capital_invertido = input("Ingrese el capital que se desea invertir: ")
    return int(capital_invertido)

def preguntar_interes_anual():
    interes_anual = input("Ingrese el porcentaje de interés actual (XX%) :")
    while interes_anual.endswith("%") != True:
        interes_anual = input("Ingrese el porcentaje de interés actual (XX%) :")
    return interes_anual

def solicitar_anios_inversion():
    anos_invertidos = input("Ingrese la cantidad de años que quieres invertir: ")
    while anos_invertidos.isnumeric() != True:
         anos_invertidos = input("Ingrese la cantidad de años que quieres invertir: ")
    return int(anos_invertidos)

def convertir_porcentaje_a_float(porcentaje:str) -> float:
    porcentaje_convertido_sin_porcentaje = porcentaje.replace("%","")
    porcentaje_convertido = float(porcentaje_convertido_sin_porcentaje)/100
    return porcentaje_convertido

