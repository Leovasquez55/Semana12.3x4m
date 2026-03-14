#En una tienda se necesita calcular el total de una 
# compra según el precio de un producto y la cantidad que compra el cliente.

#calcular el total de compras

def calcular_total(precio, cantidad):

    total = precio * cantidad
    
    return total

precio = 15
cantidad = 5
 
resultado = calcular_total(precio, cantidad)

print("El total de la compra es:", resultado)

    