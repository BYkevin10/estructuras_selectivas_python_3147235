'''
if else;
determinar dos caminos de ejecucion, basados en la evaluacion de una condicional

Sintaxis:
if condicional:
    instruccion 1
    instruccion 2
else: 
    instruccion 3
    instruccion 4
'''

#Ejemplo
#Elabore un programa en python que determine si una persona es mayor o menor de edad y por tanto, habilitada para votar

edad = 20
documento = False


if edad >= 18 and documento == True:
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("Fin del programa")