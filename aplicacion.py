import gestion_archivos

def menu():
    print ("*******Menu principal*********")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido del archivo")
    print("5. Salir")
    
    
    
def crear():
    print ("--Crear archivo--")
    archivo = input("Archivo:  ")
    contenido = input("Contenido : ")
    gestion_archivos.crear_archivo(archivo, contenido)

def eliminar ():
    print("--Eliminar Archivo--")
    archivo=input("Archivo : ")
    gestion_archivos.eliminar_archivo(archivo)

def agregar():
    archivo = input ("Archivo : ")
    #archivo = input("Archivo")
    contenido = input("contenido: ")
    gestion_archivos.agregar_contenido(archivo, contenido)
    
def listar():
    print("--Mostrar contenido de un archivo--")
    archivo = input("Archivo : ")
    print(gestion_archivos.leer_archivo(archivo))
    
def salir():
    print ("gracias por su visita ")
    
    
def error():
    print ("opcion incorrecta")
    
opcion = 1
while opcion != 5 :
    menu()
    opcion=int(input("opcion : "))
    if opcion==1:
        crear()
    elif opcion==2:
        eliminar()
    elif opcion ==3:
        agregar()
    elif opcion == 4 :
        listar()
    elif opcion == 5 :
        salir()
    else:
        error()
        