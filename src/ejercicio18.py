"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen.
La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""

#Entrada

def solicitar_numero():
    numero = input("Ingrese un número (-1 para acabar): ")
    while numero.isnumeric() != True and numero != "-1":
        numero = input("Ingrese un número: ")
    return numero

def entrada_masiva_numeros():
    numero_ingresado = solicitar_numero()
    lista_numeros_ingresados = []
    while comprobar_si_menos_uno(numero_ingresado) != True:
        lista_numeros_ingresados.append(numero_ingresado)
        numero_ingresado = solicitar_numero()
    return lista_numeros_ingresados
#Procesado

def comprobar_si_menos_uno(numero_ingresado:str):
    if numero_ingresado == "-1":
        return True

def separacion_num_digit(numero:str):
    numeros_separados = list(numero)
    numeros_convertidos = []
    for numero in numeros_separados:
        numeros_convertidos.append(int(numero))
    return numeros_convertidos

def sum_num_digit(lista_de_numeros:list):
    return sum(lista_de_numeros)

def convertir_listaStr_listaInt(lista_str:list):
    lista_convertida = []
    for numero_str in lista_str:
        lista_convertida.append(int(numero_str))
    return lista_convertida

def sacar_pares(lista_de_numeros:list):
    lista_convertida = convertir_listaStr_listaInt(lista_de_numeros)
    numeros_pares = []
    for numero in lista_convertida:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

#Salida

def mostrar_suma_digitos(lista_de_numeros:str):
    for numero in lista_de_numeros:
        separacion_num = separacion_num_digit(numero)
        suma_num = sum_num_digit(separacion_num)
        print(suma_num)

def mostrar_pares(lista_numeros:list):
    lista_de_pares = sacar_pares(lista_numeros)
    print("La lista de pares es:")
    for par in lista_de_pares:
        print(par,end=" ")

if __name__ == "__main__":
    lista_numeros_masivos = entrada_masiva_numeros()
    
    mostrar_suma_digitos(lista_numeros_masivos)
    
    mostrar_pares(lista_numeros_masivos)