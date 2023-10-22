"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def pedir_edad_usuario()->int:
    edad = input("Ingrese su edad: ")
    while edad.isnumeric() != True:
        edad = input("Ingrese su edad: ")
    return int(edad)

def sacar_anios_cumplidos(edad:int):
    listas_anios_cumplidos = []
    for edad_cumplida in range(1,edad+1):
        listas_anios_cumplidos.append(edad_cumplida)
    return listas_anios_cumplidos

def mostrar_anios_cumplidos(listas_anios_cumplidos):
    for edad_cumplida in listas_anios_cumplidos:
        print(edad_cumplida)
        
if __name__ == "__main__":
    edad_usuario = pedir_edad_usuario()
    
    anios_cumplidos = sacar_anios_cumplidos(edad_usuario)
    
    mostrar_anios_cumplidos(anios_cumplidos)