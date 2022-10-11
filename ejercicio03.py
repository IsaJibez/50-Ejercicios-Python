"""
Dada una palabra, buscarla en una frase y devolver cuantas veces aparece en ella,
la frase y la palabra deben ser parametros de una funcion.
"""

frase = (input("¿Cual es la frase? ")).lower()
palabra = input("¿Cual es la palabra? ")

#eliminacion de caracteres
#https://www.delftstack.com/es/howto/python/remove-certain-characters-from-string-python/#:~:text=replace()-,El%20método%20string.,por%20iteración%20de%20una%20cadena.
caracteres = "!?.,'"
for x in range(len(caracteres)):
    frase = frase.replace(caracteres[x],"")

fraseArreglo = frase.split(sep=" ") #separamos la frase en arreglo
contador = 0
for x in fraseArreglo:
    if x == palabra:
        contador+=1

print(f"Cantidad de veces que {palabra} es repetido:",contador)
