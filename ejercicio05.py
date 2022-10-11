"""
Ejercicio 5:
Cuanto es el X porciento de el numero X.

Ejemplos:
tantoPorCiento(20, 100) //Devuelve 20
tantoPorCiento(43, 897) //Devuelve 385.71
"""

def tantoPorCiento(porcentaje, numero):
    porciento = 0;
    numeroPorcentaje = porcentaje * 0.01;
    porciento =  numero * numeroPorcentaje;


    return  print(f"el {porcentaje}% del numero '{numero}' es:",round(porciento,2))

tantoPorCiento(15,200);