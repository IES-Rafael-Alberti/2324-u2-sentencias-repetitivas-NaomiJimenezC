"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

#Entrada
def solicitar_factor():
    factor = input("Ingrese el número del cual quieras ver su tabla de multiplicación: ")
    while factor.isnumeric() != True:
        factor = input("Ingrese el número del cual quieras ver su tabla de multiplicación: ")
    return int(factor)
        
#Proceso

def calcular_multiplicaciones(factor:int):
    resultados= []
    for multiplicacion in range(1,11):
        resultados.append(factor*multiplicacion)
    return resultados

#Salida

def mostrar_tabla(factor:int,resultados:list):
    for operacion in range(1,11):
        for resultado in resultados:
            print(f"{operacion} x {factor} = {resultado} ")

if __name__ == "__main__":
    #Entrada
    factor = solicitar_factor()
    #Proceso
    resultados = calcular_multiplicaciones(factor)
    #Salida
    mostrar_tabla(factor,resultados)
