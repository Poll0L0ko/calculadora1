from calculator import suma, resta, multiplicacion, division

print("Calculadora simple")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", suma(a, b))
print("Resta:", resta(a, b))
print("Multiplicación:", multiplicacion(a, b))
print("División:", division(a, b))