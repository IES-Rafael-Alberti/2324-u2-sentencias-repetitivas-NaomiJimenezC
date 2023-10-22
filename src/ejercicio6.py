"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. 
"""
##print("*"*(i+1))

##Entrada
def solicitar_altura_triangulo():
    altura = input("Ingrese la altura del triangulo rectángulo: ")
    while altura.isnumeric() != True and int(altura) <1:
        altura = input("Ingrese la altura del triangulo rectángulo: ")
    return int(altura)

#Procesado

def crear_piramide(altura:int):
    piramide = []
    for altura in range(altura):
        piramide.append("*"*(1+altura))
    return piramide

#Salida

def mostrar_piramide(partes_piramide:list):
    for parte in partes_piramide:
        print(parte)

if __name__ == "__main__":
    #Entrada
    altura_triangulo = solicitar_altura_triangulo()
    #Procesado
    piramide = crear_piramide(altura_triangulo)
    #Salida
    mostrar_piramide(piramide)