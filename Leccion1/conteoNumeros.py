numPositivos = 0
numNegativos = 0
numNeutros = 0

for i in range(10):
    num = int(input(f"{i+1} Ingrese un numero: "))
    if num == 0:
        numNeutros += 1
    elif num > 0:
        numPositivos += 1
    elif num < 0:
        numNegativos += 1
    else:
        print("Numero invalido")

print(f"La cantidad de numeros Positivos es: {numPositivos} ")
print(f"La cantidad de numeros Negativos es: {numNegativos} ")
print(f"La cantidad de numeros Neutros es: {numNeutros} ")


