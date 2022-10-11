"""

Ejercicio 6:
Dibujar un cuadrado hueco con asteriscos.

Ejemplo:
cuadrado(4)

//Devuelve:

****
*  *
*  *
****

Como hacerlo:
- Funcion para crear el lado de arriba y abajo del cuadrado
- Funcion para que haga lo slados y el hueco del cuadrado
- Bucle de 0 al tamaño del lado menos 2 para equilibrar con el lado de arriba y abajo
- Bucle para pintar los espacios, menos 2 para equilibrar con el asterisco de izq. y der.
- Ir concatenando en una variable cada linea del cuadrado.
- Mostrar el cuadrado en la funcion principal.


"""

# ****
def lado(numero):
    lado = ""

    for i in range(0,numero):
        lado += "*"
        
    return lado


def cuadrado(numero):
    dibujo = lado(numero)+"\n"

    contenido = ""
    # Filas
    for i in range(2,numero):
        contenido = "*"
        
        # Contenido vacio (huevo)
        for x in range(0,numero-2):
            contenido += " "

        #lado derecho del cuadrado
        contenido += "*"
        dibujo += contenido + "\n"

    dibujo += lado(numero)

    return dibujo

print(cuadrado(int(input("Area del cuadrado: "))))