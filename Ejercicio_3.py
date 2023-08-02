import random

cantidad_numeros = 10
rango_inicio = 1
rango_fin = 100

lista_aleatoria = [random.randint(rango_inicio, rango_fin) for _ in range(cantidad_numeros)]

for numero in lista_aleatoria:
    print(numero)
