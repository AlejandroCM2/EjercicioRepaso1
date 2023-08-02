def es_par(numero):
    return numero % 2 == 0

numero = int(input("Ingrese un número: "))

if es_par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

