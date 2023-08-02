def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius:.2f} grados Celsius.")
