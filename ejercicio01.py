#Enunciado 1:
#Dado un numero, devolver su tabla de multiplicar completa.

numero = int(input("Introduce un numero: "))

print(f"\n# Tabla de {numero} #\n")
for x in range(1,11):
    print(f"{numero} * {x} = {numero * x}")