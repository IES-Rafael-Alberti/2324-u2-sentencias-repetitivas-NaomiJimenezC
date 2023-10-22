"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""

#Entrada

def solicitar_numero():
    numero = input("Ingrese un número (0 para acabar): ")
    while numero.isnumeric() != True:
        numero = input("Ingrese un número: ")
    return int(numero)
#Procesado

def comprobar_si_numero_es_cero(numero_ingresado:int):
    if numero_ingresado == 0:
        return True
    
def ordenar_lista_num(lista_numericas_desordenada:list):
    return sorted(lista_numericas_desordenada,reverse=True)

def sacar_numero_mayor(lista_numeros_ordenadas:list):
    return lista_numeros_ordenadas.pop(0)

def sacar_numeros_hasta_cero(numero_ingresado:int):
    lista_num = []
    while comprobar_si_numero_es_cero(numero_ingresado) != True:
        lista_num.append(numero_ingresado)
        numero_ingresado = solicitar_numero()
    return lista_num
#Salida

def numero_mayor(numero_mas_alto:int):
    print(f"El número maś alto es {numero_mas_alto}")

if __name__ == "__main__":
    numero_solicitado = solicitar_numero()
    
    lista_nums = sacar_numeros_hasta_cero(numero_solicitado)
    lista_nums_ordenadas = ordenar_lista_num(lista_nums)
    numero_max = sacar_numero_mayor(lista_nums_ordenadas)
    
    numero_mayor(numero_max)