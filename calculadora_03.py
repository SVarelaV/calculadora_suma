from tkinter import *

# Variables para almacenar los números seleccionados
numero1 = ""
numero2 = ""
fase = 1  # Controla si estamos ingresando el primer o el segundo número

def agregar_numero(numero):
    """
    Agrega un número al número actual (numero1 o numero2) dependiendo de la fase.
    """
    global numero1, numero2, fase
    if fase == 1:
        numero1 += str(numero)  # Concatenar el número al primer número
    elif fase == 2:
        numero2 += str(numero)  # Concatenar el número al segundo número

def cambiar_a_segundo_numero():
    """
    Cambia la fase para comenzar a ingresar el segundo número.
    """
    global fase
    fase = 2

def suma():
    """
    Calcula la suma de los dos números seleccionados y muestra el resultado en la terminal.
    """
    global numero1, numero2
    try:
        resultado = int(numero1) + int(numero2)  # Convertir a enteros y sumar
        print(f"La suma es: {resultado}")  # Mostrar el resultado en la terminal
        # Reiniciar los números y la fase
        numero1 = ""
        numero2 = ""
        fase = 1
    except ValueError:
        print("Error: Asegúrate de seleccionar números válidos")

# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Suma")

# Crear botones numéricos (0-9)
boton_1 = Button(ventana, text="1", font=("Arial", 18), command=lambda: agregar_numero(1), width=5, height=2)
boton_1.grid(row=1, column=0, padx=5, pady=5)

boton_2 = Button(ventana, text="2", font=("Arial", 18), command=lambda: agregar_numero(2), width=5, height=2)
boton_2.grid(row=1, column=1, padx=5, pady=5)

boton_3 = Button(ventana, text="3", font=("Arial", 18), command=lambda: agregar_numero(3), width=5, height=2)
boton_3.grid(row=1, column=2, padx=5, pady=5)

boton_4 = Button(ventana, text="4", font=("Arial", 18), command=lambda: agregar_numero(4), width=5, height=2)
boton_4.grid(row=2, column=0, padx=5, pady=5)

boton_5 = Button(ventana, text="5", font=("Arial", 18), command=lambda: agregar_numero(5), width=5, height=2)
boton_5.grid(row=2, column=1, padx=5, pady=5)

boton_6 = Button(ventana, text="6", font=("Arial", 18), command=lambda: agregar_numero(6), width=5, height=2)
boton_6.grid(row=2, column=2, padx=5, pady=5)

boton_7 = Button(ventana, text="7", font=("Arial", 18), command=lambda: agregar_numero(7), width=5, height=2)
boton_7.grid(row=3, column=0, padx=5, pady=5)

boton_8 = Button(ventana, text="8", font=("Arial", 18), command=lambda: agregar_numero(8), width=5, height=2)
boton_8.grid(row=3, column=1, padx=5, pady=5)

boton_9 = Button(ventana, text="9", font=("Arial", 18), command=lambda: agregar_numero(9), width=5, height=2)
boton_9.grid(row=3, column=2, padx=5, pady=5)

boton_0 = Button(ventana, text="0", font=("Arial", 18), command=lambda: agregar_numero(0), width=5, height=2)
boton_0.grid(row=4, column=1, padx=5, pady=5)

# Botón para cambiar al segundo número
boton_cambiar = Button(ventana, text="Siguiente Número", command=cambiar_a_segundo_numero, font=("Arial", 14))
boton_cambiar.grid(row=5, column=0, columnspan=3, pady=10)

# Botón para realizar la suma
boton_sumar = Button(ventana, text="Sumar", command=suma, font=("Arial", 14))
boton_sumar.grid(row=6, column=0, columnspan=3, pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()