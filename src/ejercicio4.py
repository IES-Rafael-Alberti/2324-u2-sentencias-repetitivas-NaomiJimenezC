
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

def solicitar_numero()->int:
    numero = input("Ingrese un número entero positivo: ")
    while numero.isnumeric() != True:
         numero = input("Ingrese un número entero positivo: ")
    return int(numero)

def sacar_numeros(numero_ingresado:int)-> list:
    listita_de_numeros= []
    for numero in range(0,numero_ingresado+1):
        listita_de_numeros.append(numero)
    return listita_de_numeros

def imprimir_numeros(numeros_a_imprimir:list):
    for numero in numeros_a_imprimir[::-1]:
        print(numero,end=",")

if __name__ == "__main__":
    numero_usuario = solicitar_numero()
    numeros_a_imprimir = sacar_numeros(numero_usuario)
    imprimir_numeros(numeros_a_imprimir)