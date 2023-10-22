"""
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
Si elige una opción incorrecta, informarle del error. 
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
Si elige las opciones 1 ó 2 se imprimirá un texto. 
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""

#Entrada

def ingresar_opcion_menu():
    opcion = input("Ingrese el número de alguna de las 3 opciones (1,2,3): ")
    while opcion.isnumeric() != True:
        opcion = input("Ingrese el número de alguna de las 3 opciones (1,2,3): ")
    return int(opcion)

def bucle_menu(opcion_ingresada:int):
    while opcion_ingresada != 3:
        opcion_ingresada = ingresar_opcion_menu()
        comprobar_opcion(opcion_ingresada)
    

#Procesado

def comprobar_opcion(opcion_ingresada:int):
    if opcion_ingresada == 1 or opcion_ingresada == 2:
        imprimir_texto()
    elif opcion_ingresada == 3:
        exit()
    else:
        print("Se equivocó vuelva a intentar")

#Salida

def imprimir_menu():
    print(f"Seleccione alguno de las 3 opciones \n 1-Comenzar programa \n 2-Imprimir listado \n 3-Finalizar programa")

def imprimir_texto(opcion:int):
    print(f"Hola soy la opción {opcion}")

if __name__ == "__main__":
    imprimir_menu()
    opcion_ingresada = ingresar_opcion_menu()
    bucle_menu(opcion_ingresada)