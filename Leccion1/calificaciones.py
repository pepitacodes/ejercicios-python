suma = 0
calificacionBaja = 99999

for i in range(10):
    calificacion = float(input(f"{i+1} Ingrese una califiacion:"))
    suma += calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion


promedioCalificaciones = suma/10

print(f"La calificacion promedio es: {promedioCalificaciones}")
print(f"La calificacion mas baja es: {calificacionBaja}")

