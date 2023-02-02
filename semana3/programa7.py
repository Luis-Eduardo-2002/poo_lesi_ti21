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

print("El perímetro de un círculo de {} cm de diametro es de {} ".format(diametro, perimetro)) #Lanza el valor asignado por el usuario y el valor del perimetro




"""
Cuadrado
"""
print("Ahora calcularesmos el area y perimetro de un Cuadrado") #Inicio del mensaje de bienvenida para resolver la siguiente figura

lado = input("Introduzca el valor de uno de los lados del cuadrado: ") #Introduccion de datos por el usuario

lado = float(lado) #Introduccion del comando "float" para guardar un numero en la variable "lado"

area = lado * lado #Realizacion de la operacion para resolver lo del area

perimetro1 = input("Introduzca el valor de uno de sus 4 lados de su cuadrado: ") #Se le pide al usuario que introduzca el valor de uno de sus lados para resolver la operacion

perimetro = lado + lado + lado + lado #Operacion del perimetro del cuadrado 

print("El area de su cuadrado es {} cm".format(area)) #Mostrar el resultado de la operacion junto con el mensaje

print("El perimetro de su cuadrado es de {} cm".format(perimetro)) #Se muestra el resultado de la operacion acompañada con un mensaje
