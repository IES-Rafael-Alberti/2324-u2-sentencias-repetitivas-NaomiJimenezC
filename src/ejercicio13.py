"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""


#Entrada 

def solicitar_palabra():
    palabra = input("Ingrese una palabra: ")
    return palabra

#Procesado

def comprobar_salida(palabra:str):
    if palabra.lower() == "salir":
        return True
    
#Salida

def mostrar_eco(palabra:str):
    while comprobar_salida(palabra) != True:
        repeticion = solicitar_palabra()
        print(repeticion)