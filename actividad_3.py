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

=> para el casod e prestaciones de servicio se debe solictar :
- el valor del contrato 
- numero de meses del contrato
- antiguedad del empleado (años)
El salario neto, se calcula :
1 - dividir el valor del salario mensual por el numero de meses
2 - restar el 15% del salario mensual por concepto de EPS (salud)
3 - restar el 10% del salario mensual por concepto de pension
4 - si el empleado tiene una antiguedad igual o superior a 10 años terndra una bonificacion del 0.5% sobre el valor mensual

=> Para el caso de contrato a termino indefinido se debe solicitar : 
- Antiguedad (años)
- grado o escalfon (1 - 5)
- el salario minimo

salario mensual se calcula de acuerdo a la siguente tabla :
- grado 1: 1.5 SM
- grado 2: 1.7 SM
- grado 3: 2.0 SM
- grado 4: 2.5 SM
- grado 5: 3.0 SM

la bonificacion estara acorde a los siguentes rangos segun la antiguedad: 
- entre 1 y 5 años: 1% del salario mensual
- entre 6 y 10 años: 2% del salario mensual
- superior a 10 años: 3% del salario mensual
para este caso, los descuentos son ley son: 
- 25% por concepto de EPS
- 22% por concepto de pension
- 0.1 por concepto de ARL


'''
contrato = input("Ingrese el tipo de contrato: ")
#inicializar variables: dar valor icnial a una variable 
salario_neto = 0
if contrato == "a":
    print("Eligió: Contrato a termino indefinido ")
    antiguedad = int(input("Ingrese antiguedad del empleado(años):"))
    grado = int(input("Ingrese grado o escalafon(1-5):"))
    salario_minimo = int(input("Ingrese valor del salario minimo:"))
    salario_mensual = 0
    if grado == 1:
        salario_mensual = salario_minimo * 1.5
    elif grado == 2:
        salario_mensual = salario_minimo * 1.7
    elif grado == 3:
        salario_mensual = salario_minimo * 2.0
    elif grado == 4:
        salario_mensual = salario_minimo * 2.5  
    elif grado == 5:
        salario_mensual = salario_minimo * 3.0
    ##calcular bonificacion
    bonificacion = 0
    if antiguedad >= 1 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
    if antiguedad > 5 and antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
    if  antiguedad > 10:
        bonificacion = salario_mensual * 0.03
    ##descuentos de ley
    eps = salario_mensual * 0.25
    pension = salario_mensual * 0.22    
    arl = salario_mensual * 0.001  
    salario_neto = salario_mensual - eps - pension - arl + bonificacion
    
elif contrato == "b":
    print("Eligio: Contrato por prestacion de servicio")
    valor_contrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el numero de meses: "))
    antiguedad = int(input("Ingrese la antiguedad del empleado: "))
    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05
    salario_neto = salario_mensual - eps - pension 
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificacion
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