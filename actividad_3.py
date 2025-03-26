'''
Actividad 3:
Elabore un programa que permita calcular el salario neto de un empleado despues de descontar los descuentos por 
conceptos de:
Salud, pension, ARL
1. El programa debe solicitar el tipo de empleado:
      a. Contrato a termino indefinido
      b. Contrato por prestacion de servicio 
      c. Contrato de aprendizaje 
      d. Contrato por jornal (Freelance)
      
=> Para el caso de jornal:
se debe solictar
 -numero de horas trabajadas
 -el valor a pagar por hora 
 * el total de salario se calcula de multiplicar el numero de horas por el valor a pagar por hora 

'''
contrato = input("Ingrese el tipo de contrato: ")
#inicializar variables: dar valor icnial a una variable 
salario_neto = 0
if contrato == "a":
    print("Eligio: Contrato a termino indefinido")
elif contrato == "b":
    print("Eligio: Contrato por prestacion de servicio")
elif contrato == "c":
    print("Eligio: Contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el salario minimo: "))
    salario_neto = salario_minimo - (salario_minimo * 0.25)
elif contrato == "d":
    print("Eligio: Contrato por jornal (Freelance)")
    #variable local: variable que solo se puede utilizar en un bloque de codigo
    numero_horas = int(input("Ingrese el numero de horas trabajadas: "))
    valor_hora = int(input("Ingrese el valor a pagar por hora: "))
    salario_neto = numero_horas * valor_hora
else:
    print("Tipo de contrato no existente")
print("El salario neto es: ", salario_neto)
print("Fin del programa")