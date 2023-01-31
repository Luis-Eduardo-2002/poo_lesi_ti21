"""
   progrma7.py
   #Nombre: Luis Eduardo Silva Islas
   #Fecha: 31 de Enero del 2023
   #Descripción: 
"""

"""
Círculo
"""
print("Bienvendio al mini programa de calcular área y perimetro de un Círculo") #Indica el mensaje de bienvenida

PI = 3.1416 #"PI", en mayuscalas, se indica así por que es una constante. Todo lo que sea una constante se indica siempre con MAYUSCULAS

radio = input("Introduzca el valor del radio: ") #Introducción del dato de radio

area = PI*float(radio)**2 #Realización de la operación y se pone doble "*" para indicar una elevación al cuadrado

diametro = input("Introduzca el valor del diamtro: ")
perimetro = PI*float(diametro) 

print("El área de un círculo de {} cm de radio es de {} ".format(radio, area)) #Lanza el valor asigando por el usuario y el valor del raido 

print("El perímetro de un círculo de {} cm de radio es de {} ".format(radio, perimetro)) #Lanza el valor asignado por el usuario y el valor del perimetro
