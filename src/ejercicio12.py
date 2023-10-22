"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

#Entrada

def solicitar_frase():
    frase = input("Ingrese una frase: ")
    while frase == "":
        frase = input("Ingrese una frase: ")
    return frase

def solicitar_letra():
    letra = input("Ingrese una letra: ")
    while len(list(letra)) != 1:
        letra = input("Ingrese una letra: ")
    return letra

#Procesado

def contar_repeticiones_letra(frase:str,letra_introducida:str):
    contador = 0
    for letra in frase:
        if letra == letra_introducida:
            contador +=1
    return contador
        

#Salida

def mostrar_repeticiones(letra_introducida:str,repeticiones:int):
    print(f"La letra {letra_introducida} se repite {repeticiones} veces en la frase")

if __name__ == "__main__":
    frase = solicitar_frase()
    letra = solicitar_letra
    
    repeticiones = contar_repeticiones_letra(frase,letra)
    
    mostrar_repeticiones(letra,repeticiones)
