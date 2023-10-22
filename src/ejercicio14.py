"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""
#Entrada

def solicitar_numero():
    numero = input("Ingrese un número (0 para acabar): ")
    while numero.isnumeric() != True:
        numero = input("Ingrese un número: ")
    return int(numero)
#Procesado

def comprobar_si_numero_es_cero(numero_ingresado:int):
    if numero_ingresado == 0:
        return True


#Salida
def sumatorio(numero_ingresado:int):
    sumatorio = 0
    while comprobar_si_numero_es_cero(numero_ingresado) != True:
        sumatorio += numero_ingresado
        numero_ingresado = solicitar_numero()
    return sumatorio

def imprimir_resultado(sumatorio:int):
    print(f"El sumatorio es de {sumatorio}")

if __name__ == "__main__":  
    
    numero_ingresado = solicitar_numero()
    resultado_sumatorio = sumatorio(numero_ingresado)
    imprimir_resultado(resultado_sumatorio)