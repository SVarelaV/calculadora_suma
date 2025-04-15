from tkinter import *


#funciones de procesamiento
def suma():
    num1 = float(entry_num1.get())  # Obtener el primer número
    num2 = float(entry_num2.get())  # Obtener el segundo número
    resultado = num1 + num2  # Calcular la suma

    print(f"La suma es: {resultado}")

# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Suma")

# Etiquetas y campos de entrada para los números
label_num1 = Label(ventana, text="Número 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num1 = Entry(ventana)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = Label(ventana, text="Número 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5)

entry_num2 = Entry(ventana)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Crear botones numéricos (0-9) manualmente
boton_1 = Button(ventana, text="1", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 1), width=5, height=2)
boton_1.grid(row=2, column=0, padx=5, pady=5)

boton_2 = Button(ventana, text="2", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 2), width=5, height=2)
boton_2.grid(row=2, column=1, padx=5, pady=5)

boton_3 = Button(ventana, text="3", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 3), width=5, height=2)
boton_3.grid(row=2, column=2, padx=5, pady=5)

boton_4 = Button(ventana, text="4", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 4), width=5, height=2)
boton_4.grid(row=3, column=0, padx=5, pady=5)

boton_5 = Button(ventana, text="5", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 5), width=5, height=2)
boton_5.grid(row=3, column=1, padx=5, pady=5)

boton_6 = Button(ventana, text="6", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 6), width=5, height=2)
boton_6.grid(row=3, column=2, padx=5, pady=5)

boton_7 = Button(ventana, text="7", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 7), width=5, height=2)
boton_7.grid(row=4, column=0, padx=5, pady=5)

boton_8 = Button(ventana, text="8", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 8), width=5, height=2)
boton_8.grid(row=4, column=1, padx=5, pady=5)

boton_9 = Button(ventana, text="9", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 9), width=5, height=2)
boton_9.grid(row=4, column=2, padx=5, pady=5)

boton_0 = Button(ventana, text="0", font=("Arial", 18), command=lambda: agregar_numero(entry_num1, 0), width=5, height=2)
boton_0.grid(row=5, column=1, padx=5, pady=5)

# Botón para realizar la suma
boton_sumar = Button(ventana, text="Sumar", command=suma, font=("Arial", 14))
boton_sumar.grid(row=6, column=0, columnspan=2, pady=10)


# Iniciar el bucle principal de Tkinter
ventana.mainloop()