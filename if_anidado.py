'''
If Anidados:
if dentro de otro if
Sintax:
if condicion1:
      if condicion2:
            print("mensaje1")
            if condicion3:
                  print("mensaje2")
                  if condicion4:
                        print("mensaje3")
                  elif condicion5:  
                        print("mensaje4")
                  elif condicion6:
                        print("mensaje5")
      else:
            print("mensaje6")
            
No confundir con elif (if en cascada)

'''

#Ejemplo 1:
#Modifique el ejercicio de la edad para las siguientes condiciones:
#1 Si es mayor de 18 años pero no tiene documento, no puede votar de lo contrario si puede votar 
#2 Si es menor de 18 años no puede votar 
#Utilice estructura de if anidados

edad = int(input("Ingrese su edad: "))
if edad >= 18:
      documento = input("Tiene documento? (si/no): ")
      if documento == "si":
            print("Puede votar, todo en regla")
      else:
            print("No puede votar, no tiene documento")

else:
      print("No puede votar, es menor de edad")