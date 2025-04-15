from tkinter import *

class Numero:
    def __init__(self, numero):
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, nuevo_numero):
        self._numero = nuevo_numero

class ListaNumeros:
    def __init__(self):
        self.numeros = []

    def agregar_numero(self, numero):
        self.numeros.append(numero)

    def sumar_numeros(self):
        return sum(numero.numero for numero in self.numeros)

lista_numeros = ListaNumeros()

def calcular_suma():
    # Obtener la cadena de números ingresada por el usuario
    cadena_numeros = entrada_numeros.get()  # Obtener los números ingresados
    numeros = cadena_numeros.split(',')  # Dividir la cadena en una lista
    lista_numeros.numeros = []  # Reiniciar la lista

    for num in numeros:
        numero = int(num)
        lista_numeros.agregar_numero(Numero(numero))

    # Calcular la suma y mostrar el resultado en la terminal
    resultado = lista_numeros.sumar_numeros()
    print(f"La suma es: {resultado}")


# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Suma")

# Crear etiquetas
etiqueta_numeros = Label(ventana, text="Números que se suman:")
etiqueta_numeros.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Crear etiquetas
etiqueta_numeros = Label(ventana, text="Ingresa los números:")
etiqueta_resultado = Label(ventana, text="Resultado")


# Crear campo de entrada para múltiples números
entrada_numeros = Entry(ventana)

# Crear botones numéricos (0-9) manualmente
boton_1 = Button(ventana, text="1", font=("Arial", 18), command=..., width=5, height=2)
boton_1.grid(row=2, column=0, padx=5, pady=5)

boton_2 = Button(ventana, text="2", font=("Arial", 18), command=..., width=5, height=2)
boton_2.grid(row=2, column=1, padx=5, pady=5)

boton_3 = Button(ventana, text="3", font=("Arial", 18), command=..., width=5, height=2)
boton_3.grid(row=2, column=2, padx=5, pady=5)

boton_4 = Button(ventana, text="4", font=("Arial", 18), command=..., width=5, height=2)
boton_4.grid(row=3, column=0, padx=5, pady=5)

boton_5 = Button(ventana, text="5", font=("Arial", 18), command=..., width=5, height=2)
boton_5.grid(row=3, column=1, padx=5, pady=5)

boton_6 = Button(ventana, text="6", font=("Arial", 18), command=..., width=5, height=2)
boton_6.grid(row=3, column=2, padx=5, pady=5)

boton_7 = Button(ventana, text="7", font=("Arial", 18), command=..., width=5, height=2)
boton_7.grid(row=4, column=0, padx=5, pady=5)

boton_8 = Button(ventana, text="8", font=("Arial", 18), command=..., width=5, height=2)
boton_8.grid(row=4, column=1, padx=5, pady=5)

boton_9 = Button(ventana, text="9", font=("Arial", 18), command=..., width=5, height=2)
boton_9.grid(row=4, column=2, padx=5, pady=5)

boton_0 = Button(ventana, text="0", font=("Arial", 18), command=..., width=5, height=2)
boton_0.grid(row=5, column=1, padx=5, pady=5)


# Crear el botón de sumar
boton_sumar = Button(ventana, text="Sumar", font=("Arial", 18), command=calcular_suma, width=15, height=2, bg="lightblue")
boton_sumar.grid(row=6, column=0, columnspan=3, pady=10)


# Iniciar el bucle principal de Tkinter
ventana.mainloop()