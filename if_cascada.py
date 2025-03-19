'''
If en cascada:
Es una estrcutura selectiva compuesta por multiples condicionales, seguidos unos de otros
Sintaxis:
if condicional 1:
    instruccion1
    instruccion2
elif condicional 2:
    instruccion3
    instruccion4
elif condicional 3:
    instruccion5
    instruccion6
    
NOTA: Cada condicional es MUTUAMENTE EXCLUYENTE 
'''
#EJEMPLO
#Vamos a hacer un pequeño traductor, el programa debe permitir leer por 
#teclado una fruta en español y debe mostrar esa fruta en ingles

fruta_es = input("Ingrese una fruta: ")

if fruta_es == "manzana" or fruta_es == "Manzana":
    print("Apple")
elif fruta_es == "naranja" or fruta_es == "Naranja":
    print("orange")
elif fruta_es == "uvas" or fruta_es == "Uvas":
    print("grape")
elif fruta_es == "sandia" or fruta_es == "Sandia":
    print("watermelon")
elif fruta_es == "banano" or fruta_es == "Banano":
    print("banana")

#Caso por defecto 
#Default
else:
    print("No se encontro traducción")
