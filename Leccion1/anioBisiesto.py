def es_anio_bisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True


anio = int(input("Ingrese un año: "))


if es_anio_bisiesto(anio):
    print(f"{anio}, es un año bisiesto.")
else:
    print(f"{anio}, no es un año bisiesto.")
