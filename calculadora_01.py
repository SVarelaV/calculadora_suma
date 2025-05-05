import tkinter as tk

class CalculadoraSuma:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Suma")
        self.numeros = []  # Lista para almacenar los números ingresados
        self.numero_actual = ""  # Número que se está formando

        # Etiqueta para mostrar los números ingresados
        self.display = tk.Label(ventana, text="", font=("Arial", 20), bg="white", anchor="e", relief="sunken", width=15)
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Crear botones numéricos (0-9)
        for i in range(10):
            boton = tk.Button(ventana, text=str(i), font=("Arial", 18), command=lambda i=i: self.agregar_numero(i), width=5, height=2)
            fila = (i - 1) // 3 + 1 if i != 0 else 4
            columna = (i - 1) % 3 if i != 0 else 1
            boton.grid(row=fila, column=columna, padx=5, pady=5)

        # Botón de resultado
        boton_resultado = tk.Button(ventana, text="Resultado", font=("Arial", 18), command=self.mostrar_resultado, width=15, height=2, bg="lightblue")
        boton_resultado.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

    def agregar_numero(self, numero):
        """
        Agrega un número al número actual y lo muestra en el display.
        """
        self.numero_actual += str(numero)
        self.display.config(text=self.numero_actual)

    def mostrar_resultado(self):
        """
        Convierte el número actual en entero, lo agrega a la lista de números,
        calcula la suma y muestra el resultado en el display.
        """
        if self.numero_actual:  # Si hay un número actual
            self.numeros.append(int(self.numero_actual))
            self.numero_actual = ""  # Reiniciar el número actual

        resultado = sum(self.numeros)  # Calcular la suma
        self.display.config(text=f"Resultado: {resultado}")
        self.numeros = []  # Reiniciar la lista de números


# Crear la ventana principal
ventana = tk.Tk()
calculadora = CalculadoraSuma(ventana)
ventana.mainloop()