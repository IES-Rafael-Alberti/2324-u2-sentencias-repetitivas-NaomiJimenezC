"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

#Entrada

def solicitar_palabra():
    palabra = input("Ingrese una palabra: ")
    while len(palabra.split()) != 1:
        palabra = input("Ingrese una palabra: ")
    return palabra
        
#Procesado

def dividir_palabra_en_letras(palabra:str):
    palabra_por_letra = list(palabra)
    return palabra_por_letra

def ordenar_palabras(palabra_por_letras:list):
    return palabra_por_letras[::-1]

#Salida

def mostar_palabra_invertida(palabra_ingresada:str,palabra_inversa:list):
    print(f"{palabra_ingresada} de forma inversa es:")
    for letra_invertida in palabra_inversa:
        print(letra_invertida,end=" ")

if __name__ == "__main__":
    #Entrada
    palabra_a_invertir=solicitar_palabra()
    #Procesado
    division_por_letra = dividir_palabra_en_letras(palabra_a_invertir)
    invertir_letras = ordenar_palabras(division_por_letra)
    #Salida
    mostar_palabra_invertida(palabra_a_invertir,invertir_letras)