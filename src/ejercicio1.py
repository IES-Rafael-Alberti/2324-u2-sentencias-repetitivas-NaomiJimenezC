"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""


#Entrada
def solicitar_palabra()-> str:
    palabra_ingresada = input("Ingrese una palabra: ")
    while not palabra_ingresada:
        palabra_ingresada = input("Ingrese una palabra: ")
    return palabra_ingresada

#Procesado

def repetir_diez_veces(palabra:str)-> list:
    lista_palabra = []
    for repeticion_palabra in range(1,11):
        lista_palabra.append(palabra)
    return lista_palabra

#Salida

def imprimir_lista(lista_de_palabra:list):
    for palabra in lista_de_palabra:
        print(palabra)


if __name__ == "__main__":
    palabra_ingresada_por_usuario = solicitar_palabra()
    
    lista_de_la_palabra_ingresada = repetir_diez_veces(palabra_ingresada_por_usuario)
    
    imprimir_lista(lista_de_la_palabra_ingresada)