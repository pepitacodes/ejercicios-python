# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado
# y guarde en una lista su tabla de multiplicar hasta
# el número 10
# Ejemplo 5 [5,10,15,20,25,30,35,40,45,50]

num = int(input("Digite un numero: "))
tabla = []
for i in range(1, 11):
    print()
    tabla.append(i*num)
print(f'\n Tabla de multiplicar del numero {num}: \n {tabla}')

for indice, i in enumerate(tabla):
    # Formato de tabla de multiplicar
    print(f"{indice} x {num} = {tabla[indice]}")


