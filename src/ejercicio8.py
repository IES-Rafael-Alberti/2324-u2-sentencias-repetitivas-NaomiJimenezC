"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo. 

"""

#Entrada
def solicitar_altura_triangulo():
    altura = input("Ingrese la altura de la pirámide: ")
    while altura.isnumeric() != True and int(altura) < 0:
        altura = input("Ingrese la altura de la pirámide: ")
    return int(altura)
        
#Procesado

def calcular_piramide(altura:int):
    piramide = []
    for fila_piramide in range(1,altura+1,2):
        for relleno_piramide in range(fila_piramide,0,-2):       
            piramide.append(relleno_piramide)
    return piramide

#Salida
def sacar_piramide(piramide:list):
    for fila_piramide in piramide:
        print(fila_piramide, end=" \n")

if __name__ == "__main__":
    altura = solicitar_altura_triangulo()
    piramide = calcular_piramide(altura)
    sacar_piramide(piramide)