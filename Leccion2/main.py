# in this class we will see the sentence if else

condition = False

# condition = 10
# Dara condición verdadera porque la variable tiene un valor
# Si la variable estuviese vacía sería falso#


if condition:
    print('Condition True')
else:
    print('Condition False')

num = int(input('Digite un numero en el rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Numero fuera de rango"

print(f"El numero ingresado es: {num} - {numTexto} ")

