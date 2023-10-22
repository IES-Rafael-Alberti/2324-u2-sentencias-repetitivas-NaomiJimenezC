"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

#Entrada
def solicitar_contrasena():
    contrasena = input("Ingrese una contraseña: ")
    while contrasena == "":
        contrasena = input("Ingrese una contraseña: ")
    return contrasena

def exigir_contrasena():
    intento = input("Ingrese la contraseña ingresada antes: ")
    while intento == "":
        intento = input("Intentelo de nuevo: ")
    return intento
#Procesado
def comprobar_intento(contrasena:str,intento:str):
    if contrasena != intento:
        return False
    else:
        return True

#Salida
def mostrar_comprobacion(resultado_comprobacion:bool):
    if resultado_comprobacion:
        print("Contraseña correcta")
    else:
        print("Contraseña INcorrecta")

if __name__ == "__main__":
    #Entrada
    contrasena_usuario = solicitar_contrasena()
    intento_usuario = exigir_contrasena()
    #Procesado
    comprobacion=comprobar_intento(contrasena_usuario,intento_usuario)
    
    #Salida
    mostrar_comprobacion(comprobacion)