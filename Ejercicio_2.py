def area_circulo(radio):
    return 3.14 * (radio ** 2)

radio = float(input("Ingresa el radio del círculo: "))
area = area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area)

