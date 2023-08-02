def generar_matriz(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    numero = 1
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = numero
            numero += 1
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz_generada = generar_matriz(filas, columnas)
imprimir_matriz(matriz_generada)
