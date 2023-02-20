"""
   progrma7.py
   #Nombre: Luis Eduardo Silva Islas
   #Fecha: 02 de Febrero del 2023
   #Descripción: 
"""
numero1 = int(input("numero1: ")) # Indicamos al usuario que asigne valores enteros, "int": comando para numeros enteros, y "input": para que el usuario asigne un valor
numero2 = int(input("numero2: ")) # Indicamos al usuario que asigne valores enteros, "int": comando para numeros enteros, y "input": para que el usuario asigne un valor

if numero1 > numero2: #Compara dos numeros con mayor y menor
    print("El numero mayor es ",numero1) # Imprime el numero que sea mayor

elif numero2 > numero1: # Compara lo de arriba en caso de que no sea verdad
     print("El numero mayor es ",numero2) # Imprime el numero que es mayor

else: # En caso de que ninguna de las anteriores ea verdad imprime None
   print(None) # Imprime None
    