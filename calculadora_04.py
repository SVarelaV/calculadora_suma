from tkinter import *


def click_boton(valor):
    entrada_actual = entrada_var.get()
    entrada_var.set(entrada_actual + str(valor))

def borrar():
    entrada_var.set("")

def sumar():
    resultado = eval(entrada_var.get())
    entrada_var.set(resultado)


# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Suma")


# Variable para almacenar la entrada
entrada_var = StringVar()

entrada = Entry(ventana, textvariable=entrada_var, font=("Arial", 18), justify='right', bd=8)
entrada.grid(row=0, column=0, columnspan=4, padx=8, pady=10)

# Crear botones numéricos (0-9)
boton_1 = Button(ventana, text="1", font=("Arial", 14), command=lambda: click_boton(1), width=3, height=1)
boton_1.grid(row=1, column=0, padx=5, pady=5)

boton_2 = Button(ventana, text="2", font=("Arial", 14), command=lambda: click_boton(2), width=3, height=1)
boton_2.grid(row=1, column=1, padx=5, pady=5)

boton_3 = Button(ventana, text="3", font=("Arial", 14), command=lambda: click_boton(3), width=3, height=1)
boton_3.grid(row=1, column=2, padx=5, pady=5)

boton_4 = Button(ventana, text="4", font=("Arial", 14), command=lambda: click_boton(4), width=3, height=1)
boton_4.grid(row=2, column=0, padx=5, pady=5)

boton_5 = Button(ventana, text="5", font=("Arial", 14), command=lambda: click_boton(5), width=3, height=1)
boton_5.grid(row=2, column=1, padx=5, pady=5)

boton_6 = Button(ventana, text="6", font=("Arial", 14), command=lambda: click_boton(6), width=3, height=1)
boton_6.grid(row=2, column=2, padx=5, pady=5)

boton_7 = Button(ventana, text="7", font=("Arial", 14), command=lambda: click_boton(7), width=3, height=1)
boton_7.grid(row=3, column=0, padx=5, pady=5)

boton_8 = Button(ventana, text="8", font=("Arial", 14), command=lambda: click_boton(8), width=3, height=1)
boton_8.grid(row=3, column=1, padx=5, pady=5)

boton_9 = Button(ventana, text="9", font=("Arial", 14), command=lambda: click_boton(9), width=3, height=1)
boton_9.grid(row=3, column=2, padx=5, pady=5)

boton_0 = Button(ventana, text="0", font=("Arial", 14), command=lambda: click_boton(0), width=3, height=1)
boton_0.grid(row=4, column=1, padx=5, pady=5)

# Botón para borrar
boton_borrar = Button(ventana, text="C", font=("Arial", 14), command=borrar, width=3, height=1)
boton_borrar.grid(row=4, column=0, padx=5, pady=5)

# Botón para sumar (evaluar la expresión)
boton_sumar = Button(ventana, text="=", font=("Arial", 14), command=sumar, width=3, height=1)
boton_sumar.grid(row=4, column=2, padx=5, pady=5)

# Botón para la operación de suma
boton_suma = Button(ventana, text="+", font=("Arial", 14), command=lambda: click_boton("+"), width=3, height=1)
boton_suma.grid(row=4, column=3, padx=5, pady=5)

ventana.mainloop()
