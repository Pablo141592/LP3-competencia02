
import os


def crear_archivo(nombre,contenido):
    archivo = open( nombre , "wt")
    archivo.write(contenido)
    archivo.close()

def leer_archivo(nombre):
    noticia = open(nombre,"rt" , encoding = ("utf8"))
    dato_noticia = noticia.read()
    print(dato_noticia)


def agregar_contenido(nombre , contenido):
    archivo = open(nombre , "at")
    archivo.write("\n" + contenido)
    archivo.close()


def eliminar_archivo (nombre):
    os.remove(nombre)

