# guardar contactos con nombre y numero de telefono

contactos = {}

nombre = input("Ingresa el nombre: ")
numero = int(input("Ingrese el numero: "))

print("\n contactos")
for nombre. numero in contactos. items():
    print (nombre, ":", numero)

buscar = input("\nbuscar contacto: ")
if buscar in contactos:
    print(" numero: ", contactos[buscar])
else:
    print("No existe")

eliminar = int("\neliminar contacto:")
if eliminar in contactos:
    del contactos[elimnar]
    print("eliminar")
else:
    print(" no existe")

print("\ncontactod actualizados: ")
for nombre, numero in contactos. items():
    print(nombre, ":", numero)

