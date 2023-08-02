def encontrar_extremos(lista):
    if not lista:
        return None, None

    maximo = minimo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo

lista_numeros = [int(x) for x in input("Ingrese los números de la lista separados por espacios: ").split()]
numero_mas_grande, numero_mas_pequeno = encontrar_extremos(lista_numeros)

if numero_mas_grande is None:
    print("La lista está vacía.")
else:
    print(f"El número más grande en la lista es: {numero_mas_grande}")
    print(f"El número más pequeño en la lista es: {numero_mas_pequeno}")
