"""
Calculadora que solo suma:
    Una pantalla donde se van escribiendo los números.
    Botones para los números del 0 al 9.
    Un botón para el signo más (+).
    Un botón para el signo de igual (=) para ver el resultado.
    Un botón para borrar (C) por si nos equivocamos.
Cuando aprietas un número, operación “+” y otro número, se va mostrando en la pantalla.
Cuando le das al "=", nos da el resultado

Función: click_boton (cuando se presiona un botón con un número)
    Mostrar en la pantalla de la calculadora los números que se van a sumar y el signo suma.
        Obtener el valor actual de la pantalla
        entrada_actual = obtener valor actual de entrada
    Concatenar el valor actual con el nuevo valor
        nuevo_texto = entrada_actual + texto_valor

Función: borrar (cuando se presiona el botón de borrar)
    Poner la pantalla de la calculadora en blanco (sin nada escrito).
        establecer entrada a una cadena vacía ("")
Función: sumar (cuando se presiona el botón de igual)
    Calcular el resultado de la suma que está escrita en la pantalla.
    Mostrar el resultado de ese cálculo en la pantalla.
"""

from tkinter import *

def click_boton(valor):
    entrada_actual = entrada_var.get()
    entrada_var.set(entrada_actual + str(valor))

def borrar():
    entrada_var.set("")

def sumar():
    resultado = eval(entrada_var.get())
    entrada_var.set(resultado)


# Crar la ventana principal
ventana = Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x410")
ventana.resizable(0, 0)  # Deshabilitar el redimensionamiento de la ventana


# Variable para la entrada de texto (pantalla de la calculadora)
entrada_var = StringVar()
entrada = Entry(ventana, textvariable=entrada_var, font=("Arial", 18), justify='right', bd=4)
entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10, padx=10)


# Lista de botones
botones = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('=', 4, 0), ('0', 4, 1), ('+', 4, 2)
]

for (texto, fila, columna) in botones:
    if texto == '=':
        boton = Button(ventana, text=texto, font=("Arial", 14), command=sumar, width=5, height=2)
    else:
        boton = Button(ventana, text=texto, font=("Arial", 14), command=lambda valor=texto: click_boton(valor), width=5, height=2)
    boton.grid(row=fila, column=columna, padx=2, pady=2)

# Botón para borrar
boton_borrar = Button(ventana, text="C", font=("Arial", 14), command=borrar, width=5, height=2)
boton_borrar.grid(row=5, column=0, columnspan=3, padx=2, pady=2)

ventana.mainloop()