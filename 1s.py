import tkinter as tk
from tkinter import messagebox

# Clase que genera la matriz con 1's en la diagonal principal y 0's en las demás posiciones
class MatrizDiagonal:
    def __init__(self, n):
        self.n = n  # Guardamos el tamaño de la matriz

    def generar_matriz(self):
        """
        Genera una matriz cuadrada de tamaño n x n con 1's en la diagonal principal y 0's en el resto.
        :return: Matriz generada como una lista de listas.
        """
        matriz = []
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                if i == j:
                    fila.append(1)  # Coloca 1 en la diagonal principal
                else:
                    fila.append(0)  # Coloca 0 en las demás posiciones
            matriz.append(fila)
        return matriz

# Clase para la interfaz gráfica
class InterfazMatriz:
    def __init__(self, ventana):
        """
        Constructor que inicializa la interfaz gráfica y permite generar la matriz con 1's en la diagonal principal.
        """
        self.ventana = ventana
        self.ventana.title("Generador de Matriz Diagonal")

        # Etiqueta para que el usuario introduzca el tamaño de la matriz
        tk.Label(ventana, text="Tamaño de la matriz:").grid(row=0, column=0, padx=10, pady=10)

        # Campo de entrada para el tamaño de la matriz
        self.entry_tamano = tk.Entry(ventana)
        self.entry_tamano.grid(row=0, column=1, padx=10, pady=10)

        # Botón para generar la matriz
        tk.Button(ventana, text="Generar Matriz", command=self.mostrar_matriz).grid(row=1, column=0, columnspan=2, pady=10)

        # Etiqueta donde se mostrará la matriz generada
        self.label_matriz = tk.Label(ventana, text="")
        self.label_matriz.grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_matriz(self):
        """
        Lee el tamaño de la matriz desde el campo de entrada, genera la matriz y la muestra en la ventana.
        """
        try:
            # Obtenemos el tamaño de la matriz que el usuario introdujo
            n = int(self.entry_tamano.get())
            if n < 1:
                raise ValueError  # Si el tamaño es menor que 1, mostramos un error

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número entero positivo.")
            return

        # Generar la matriz usando la clase MatrizDiagonal
        matriz = MatrizDiagonal(n).generar_matriz()

        # Convertir la matriz a un formato legible para mostrarla
        matriz_str = ""
        for fila in matriz:
            matriz_str += " ".join(map(str, fila)) + "\n"

        # Mostrar la matriz en la ventana
        self.label_matriz.config(text=matriz_str)

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazMatriz(ventana)
    ventana.mainloop()
