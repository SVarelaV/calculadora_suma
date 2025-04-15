from tkinter import Tk, Entry, Button, StringVar

class CalculadoraSuma:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Suma (Enteros)")

        self.entrada_var = StringVar()
        self.entrada = Entry(ventana, textvariable=self.entrada_var, width=20, font=("Arial", 16), bd=5, insertwidth=4, justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.primer_numero = None
        self.operacion = ""

        botones = [
            '7', '8', '9', 'C',
            '4', '5', '6', '+',
            '1', '2', '3', '=',
            '0'
        ]

        fila = 1
        columna = 0
        for boton_texto in botones:
            comando = lambda x=boton_texto: self.click_boton(x)
            if boton_texto == 'C':
                boton = Button(ventana, text=boton_texto, padx=20, pady=20, font=("Arial", 16), command=self.borrar)
            elif boton_texto == '+':
                boton = Button(ventana, text=boton_texto, padx=20, pady=20, font=("Arial", 16), command=self.iniciar_suma)
            elif boton_texto == '=':
                boton = Button(ventana, text=boton_texto, padx=20, pady=20, font=("Arial", 16), command=self.sumar)
            else:
                boton = Button(ventana, text=boton_texto, padx=20, pady=20, font=("Arial", 16), command=comando)

            boton.grid(row=fila, column=columna, padx=5, pady=5, sticky='nsew')
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
        
        ventana.grid_rowconfigure(1, weight=1)
        ventana.grid_rowconfigure(2, weight=1)
        ventana.grid_rowconfigure(3, weight=1)
        ventana.grid_rowconfigure(4, weight=1)
        ventana.grid_columnconfigure(0, weight=1)
        ventana.grid_columnconfigure(1, weight=1)
        ventana.grid_columnconfigure(2, weight=1)
        ventana.grid_columnconfigure(3, weight=1)

    def click_boton(self, valor):
        entrada_actual = self.entrada_var.get()
        self.entrada_var.set(entrada_actual + str(valor))

    def borrar(self):
        self.entrada_var.set("")
        self.primer_numero = None
        self.operacion = ""

    def iniciar_suma(self):
        try:
            self.primer_numero = int(self.entrada_var.get())
            self.operacion = "+"
            self.entrada_var.set("")
        except ValueError:
            self.entrada_var.set("Error: Entero")
            self.primer_numero = None
            self.operacion = ""

    def sumar(self):
        if self.primer_numero is not None and self.operacion == "+":
            try:
                segundo_numero = int(self.entrada_var.get())
                resultado = self.primer_numero + segundo_numero
                self.entrada_var.set(str(resultado))
                self.primer_numero = resultado # Permite seguir sumando
                self.operacion = ""
            except ValueError:
                self.entrada_var.set("Error: Entero")
                self.primer_numero = None
                self.operacion = ""

ventana_principal = Tk()
calculadora = CalculadoraSuma(ventana_principal)
ventana_principal.mainloop()