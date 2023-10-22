"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

#Entrada
def solicitar_numero():
    numero_solicitado = input("Ingrese un número: ")
    while numero_solicitado.isnumeric() != True:
        numero_solicitado = input("Ingrese un número: ")
    return int(numero_solicitado)
        
#Procesado
def comprobar_si_num_primo(numero_entero:int):
    divisor = 2 # se empieza desde el 2 para corrobar de mejor manera 
    while numero_entero % divisor != 0:
        divisor += 1
    if divisor == numero_entero:
        return True
    else:
        return False
#Salida
def mostrar_resultado(numero_metido:int,resultado:bool):
    if resultado:
        print(f"{numero_metido} es primo")
    else:
        print(f"{numero_metido} no es primo")

if __name__ == "__main__":
    #Entrada
    numero_a_comprobar = solicitar_numero()
    #Procesado
    saber_si_es_primo = comprobar_si_num_primo(numero_a_comprobar)
    #Salida
    mostrar_resultado(numero_a_comprobar,saber_si_es_primo)