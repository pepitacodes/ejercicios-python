import math

# Ejercicio de matematicas
# Sacar la raiz cuadrada de un número positivo

numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print(f"Error --> {numero} no es un numero positivo")
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")





