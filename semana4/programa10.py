"""
   progrma10.py
   #Nombre: Luis Eduardo Silva Islas
   #Fecha: 09 de Febrero del 2023
   #Descripción:
"""
def mayor(numero1,numero2): # Define una funcion, en este caso dos parametros
    result = None # Asigna el valor None
    if numero1 > numero2: # Comparacion para ver si "numero1" es mayor
        result = numero1 # Obtiene el valor de la variable "numero1" si es verdadero
    elif numero2 > numero1: # Se compara para ver si "numero2" es mayor
        result = numero2 # Se obtiene el valor de la variable "numero2" si es verdader
    return result # Devuelve el resultado

print(mayor(2,1))
print(mayor(1,2))
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-1))
print(mayor(-1,-2))
