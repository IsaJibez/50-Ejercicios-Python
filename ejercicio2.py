"""
Ejercicio 2:
Dado a una cadena de texto, comprobar si es un palindromo o no.
Los palindromo son palabras que se leen igual aun estando invertidas
Por ejemplo: Ana, Bob, Otto, Allivessevilla
"""

cadenaOriginal = (input("Introduce la palabra: ")).lower()
cadenaFlip = cadenaOriginal[::-1]

if cadenaFlip == cadenaOriginal:
    print("Es palindromo")
else:
    print("No es palindromo.")

#print(cadenaFlip)

#https://www.delftstack.com/es/howto/python/reverse-a-string-python/#:~:text=%2C%20%27L%27%5D-,Invierta%20una%20cadena%20en%20Python%20usando%20la%20función%20reversed(),completo%20se%20proporciona%20a%20continuación.