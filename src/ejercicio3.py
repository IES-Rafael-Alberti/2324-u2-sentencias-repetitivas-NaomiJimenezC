"""
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def solicitar_numero()->int:
    numero = input("Ingrese un número entero positivo: ")
    while numero.isnumeric() != True:
         numero = input("Ingrese un número entero positivo: ")
    return int(numero)

def sacar_impares(numero_ingresado:int):
    lista_de_impares = []
    for numero_impar in range(1,numero_ingresado+1):
        if numero_impar % 2 != 0:
            lista_de_impares.append(numero_impar)
    return lista_de_impares

def imprimir_impares(lista_de_impares:list):
    for numero_impar in lista_de_impares:
        print(numero_impar, end=",")
        
if __name__ == "__main__":
    numero_ingresado = solicitar_numero()
    numeros_impares = sacar_impares(numero_ingresado)
    imprimir_impares(numeros_impares)