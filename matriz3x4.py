asientos = [[0 for i in range (4)] for j in range(3)]

fila = int(input("Ingresa la fila (0 a 2): "))

columna = int(input("Ingresa la columna (0 a 3): "))

asientos [fila][columna] = 1

print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end = " ")

    print()
