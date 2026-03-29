#Registra nombre de estudiantes en una lista

estudiantes = []

def nuevo ():

    print("--------Registro de estudiantes--------")
    estudiante = {
        "nombre": input("ingrese el nomnbre: "),
        "edad" :  input("ingrese la edad del estudiante : "),
        "curso":  input("ingrese el curso del estudiante: ")
    }

    estudiantes.append(estudiante)
    print (f"se guardo correctamente el estudiante {estudiante['nombre']}")
    print("-"*30)
    
def listar ():
        print("--------lista de estudiantes--------")
        for estudiante in estudiantes:
         print(estudiante)
        print("-"*30)

def eliminar ():
            print("--------Ingrese el nombre que eliminara--------")

            nombre = input("ingrese el nombre que eliminara: ")   
            for estudiante in estudiantes :
              if estudiante ["nombre"] == nombre:
               estudiantes.remove(estudiante)
              print("estudiante eliminado ")
              return
            print("no encontrado.")

while True:
     print("\n-------- sistema de estudiantes-------- ")    
     print("1. agregar estudiante")      
     print("2. lista de estudiantes")   
     print("3. eliminar estudiantes")      
     print("4. salir ")      

     
     opcion = input("opcion:")
   
     if opcion == "1":
         nuevo()
     elif opcion == "2":
         listar()
     elif opcion == "3":
         eliminar()
     elif opcion == "4":
         print ("saliendo del sistema")
         break






