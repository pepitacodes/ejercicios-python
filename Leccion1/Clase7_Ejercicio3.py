mes = int(input("Digite un mes del año (1-12): "))
season = None

if mes == 1 or mes == 2 or mes == 3:
    season = "Verano"
elif mes == 4 or mes == 5 or mes == 6:
    season = "Otoño"
elif mes == 7 or mes == 8 or mes == 9:
    season = "Invierno"
elif mes == 10 or mes == 11 or mes == 12:
    season = "Primavera"
else:
    season = "Error, no hay numero para ese mes"
print(f"Para el mes {mes} la estacion es: {season}")