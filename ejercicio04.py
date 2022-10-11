'''
Dado una cadena de texto, darle la vuelta e invertir el orden de sus caracter,
sin usar metodos propios del lenguaje,
solo estructura de control.

como el ejercicio 2. pero con bucle.
'''

palabra =  input("introduce la palabra: ")


def invertir(x):
    arreglo = []
    for letra in range(0, len(x)):
        #print(x[0 - (letra + 1)])
        arreglo.insert(letra,x[0 - (letra + 1)])

    strA = "".join(arreglo)
    print(strA)
invertir(palabra)


#convertir arreglo a strin
#https://www.delftstack.com/es/howto/python/how-to-convert-a-list-to-string/#:~:text=cadena%20en%20Python-,Convertir%20una%20str%20List%20en%20una%20cadena%20en%20Python,datos%20str%20a%20una%20cadena.&text=El%20método%20join%20concatena%20cualquier,inserta%20entre%20cada%20cadena%20dada.