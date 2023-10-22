"""
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
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

def comprobar_posicion(frase_ingresada:str,letra:str):
    no_coincidencias = []
    coincidencia = []
    for posicion,letra_frase in enumerate(frase_ingresada):
        if letra_frase != letra:
            no_coincidencias.append(posicion)
        else:
            coincidencia.append(posicion)
            break
    return (no_coincidencias, coincidencia)

#Salida

def mostrar_no_coincidencias(posiciones_malas:list):
    for mala_posicion in posiciones_malas:
        print(f"Mala posicion en la posición {mala_posicion}")
def mostrar_posicion_buena(posicion_buena:list):
    if len(posicion_buena) != 0:
        print(f"La buena posición es {posicion_buena[0]}")
    else:
        print("No se encontró esta letra en la frase")
if __name__ == "__main__":
    
    frase = solicitar_frase()
    letra = solicitar_letra()
    
    posiciones_calculadas = comprobar_posicion(frase,letra)
    
    mostrar_no_coincidencias(posiciones_calculadas[0])
    mostrar_posicion_buena(posiciones_calculadas[1])
