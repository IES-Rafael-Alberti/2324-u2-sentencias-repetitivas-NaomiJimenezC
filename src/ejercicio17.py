"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
"""

#Entrada
def solicitar_numero():
    numero = input("Ingrese un número (0 para acabar): ")
    while numero.isnumeric() != True:
        numero = input("Ingrese un número: ")
    return numero
#Procesado

def separacion_num_digit(numero:str):
    numeros_separados = list(numero)
    numeros_convertidos = []
    for numero in numeros_separados:
        numeros_convertidos.append(int(numero))
    return numeros_convertidos

def sum_num_digit(lista_de_numeros:list):
    return sum(lista_de_numeros)

#Salida

def mostrar_resultado(numero_ingresado:str,resultado:int):
    print(f"La suma de los dígitos de {numero_ingresado} da igual a {resultado}")

if __name__ == "__main__":
    numero_solicitado = solicitar_numero()
    
    numeros_separados = separacion_num_digit(numero_solicitado)
    resultado = sum_num_digit(numeros_separados)
    
    mostrar_resultado(numero_solicitado,resultado)