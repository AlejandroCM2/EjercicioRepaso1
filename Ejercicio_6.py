def calcular_suma(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista_numeros = [int(x) for x in input("Ingrese los números de la lista separados por espacios: ").split()]
resultado = calcular_suma(lista_numeros)
print(f"La suma de los números en la lista es: {resultado}")
