precio_m = int(input("Ingrese el precio de la matricula: "))
edad = int(input("Ingrese su edad: "))
estrato = input("Ingrese su estrato: ")


if edad < 18 and estrato == "1":
      descuento = precio_m * 0.20
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad >= 18 and estrato == "1":
      descuento = precio_m * 0.15
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad < 18 and estrato == "2":
      descuento = precio_m * 0.10
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad >= 18 and estrato == "2":
      descuento = precio_m * 0.05
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
else:
      print("No tiene descuento")