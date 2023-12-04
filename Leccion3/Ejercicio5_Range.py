# Ejercicio 5: Factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero
# positivo

num = int(input("Ingrese un numero: "))
while num < 0:
    print("Error, el numero ingresado no es positivo")
    num = int(input("Ingrese un numero positivo: "))
factorial = 1  # La variable para calcular el factorial
for i in range(1, num+1):
    factorial *= i
print(f"\nEl factorial del numero {num} ingresado es: {factorial} ")



