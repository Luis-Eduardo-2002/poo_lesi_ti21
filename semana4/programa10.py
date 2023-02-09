"""
   progrma10.py
   #Nombre: Luis Eduardo Silva Islas
   #Fecha: 09 de Febrero del 2023
   #Descripción:
"""
def mayor(numero1:int, numero2:int)-> int | None: 
    result = None
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1: 
        result = numero2
    return result 

print(mayor(2,1))
print(mayor(1,2))
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-1))
print(mayor(-1,-2))
