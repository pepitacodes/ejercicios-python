def suma_primeros_n_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


n = int(input("Ingrese un número: "))

resultado = suma_primeros_n_numeros(n)

print("La suma de los primeros", n, "números es:", resultado)
