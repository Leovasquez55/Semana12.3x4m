#Aplicar el uso de funciones con parámetros y retorno de 
# valores mediante la creación de un programa sencillo y 
# la explicación de su funcionamiento.

#Calcular el area de un rectangulo


def calcular_area(base, altura):
    area= base * altura
    return area

base= float(input("Ingresa la base: "))
altura= float(input("Ingrsa la altura: "))

resultado= calcular_area(base, altura)

print("El area de su rectangulo es :" , resultado )