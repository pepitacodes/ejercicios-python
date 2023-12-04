grade = int(input("Digite una calificación entre 0 y 10: "))
if 9 <= grade <= 10:
    print("A")
elif 8 <= grade < 9:
    print("B")
elif 7 <= grade < 8:
    print("C")
elif 6 <= grade < 7:
    print("D")
elif 0 <= grade < 6:
    print("F")
else:
    print("Valor incorrecto")