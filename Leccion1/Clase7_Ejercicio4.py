edad = int(input("Ingrese su edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad < 40:
    mensaje = "Trabajar y esforzarse"
elif 40 <= edad < 50:
    mensaje = "La familia y los amigos"
elif 50 <= edad < 60:
    mensaje = "El cuidado de uno mismo"
elif 60 <= edad < 70:
    mensaje = "Tener una rutina saludable"
elif 70 <= edad < 80:
    mensaje = "Mantener la mente activa"
else:
    mensaje = "Error"
print(f"Tu edad es: {edad}, {mensaje}")


