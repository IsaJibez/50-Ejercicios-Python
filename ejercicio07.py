"""
Ejercicio 7:
Dados dos numeros, devolver cuantos numeros IMPARES
hay entre ellos.

impares(1,100) #Devuelve: 50
"""

def impares(n1,n2):
    contadorImpar = 0

    for x in range(n1,n2+1):
        if x%2 != 0:
            contadorImpar += 1

    return print("numeros impares:",contadorImpar)

impares(int(input("Digita el primer numero: ")),int(input("Digita el segundo numero: ")))