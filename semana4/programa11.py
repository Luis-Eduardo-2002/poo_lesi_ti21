"""
   progrma10.py
   #Nombre: Luis Eduardo Silva Islas
   #Fecha: 09 de Febrero del 2023
   #Descripción:
"""
def mayor(numero1:int, numero2:int)-> int | None: # Se definio una funcion de dos parametros, dando el tipo de dato y el tipo de salida
    result = None # Se indica varaible de None
    if numero1 > numero2: # Se ve si la variable "numero1" es mayor
        result = numero1 # Se ve si la variable "numero1" es la verdadera
    elif numero2 > numero1: # Se hace una comparacion para ver si la variable "numero2" es mayor
        result = numero2 # Se obtienen el valor de la variable "numero1", si es verdadera
    return result # Regresa el resultado

print(mayor(2,1))
print(mayor(1,2))
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-1))
print(mayor(-1,-2))
