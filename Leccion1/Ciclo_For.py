cadena = "Hello"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo For")


for letra in "Alemania":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break
    else:
        print("Fin del ciclo For")