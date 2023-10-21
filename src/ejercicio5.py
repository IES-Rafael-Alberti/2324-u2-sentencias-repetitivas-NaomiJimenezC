"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""


#Entrada
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

#Procesado

def convertir_porcentaje_a_float(porcentaje:str) -> float:
    porcentaje_convertido_sin_porcentaje = porcentaje.replace("%","")
    porcentaje_convertido = float(porcentaje_convertido_sin_porcentaje)/100
    return porcentaje_convertido

def calcular_interes_anual(capital:int,porcentaje_interes:str) -> int:
    porcentaje_convertido = convertir_porcentaje_a_float(porcentaje_interes)
    capital_interes = capital * (1+porcentaje_convertido)
    return capital_interes

def intereses_por_ano(capital_base:int,porcentaje_interes:str,anios_a_invertir:int)-> list:
    interes_por_cada_anio = []
    for interes in range(1,anios_a_invertir+1):
        interes_por_cada_anio.append(calcular_interes_anual(capital_base,porcentaje_interes))
    return interes_por_cada_anio

#Salida

def mostrar_intereses_por_anio(lista_capital_anio:list):
    for anio in lista_capital_anio:
        print(f"En el año {lista_capital_anio.index(anio)} tienes")
    

if __name__ == "__main__":
    
    #entrada
    capital_base_invertido = solicitar_cantidad_a_invertir()
    porcentaje_interes = preguntar_interes_anual()
    anios_a_invertir = solicitar_anios_inversion()
    
    #Procesado
    resultado_inversiones = intereses_por_ano(capital_base_invertido,porcentaje_interes,anios_a_invertir)
    
    #Salida
    mostrar_intereses_por_anio(resultado_inversiones)
    
    #TODO(revisa esto naomi)