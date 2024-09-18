import tkinter as tk
from tkinter import messagebox

# Clase para manejar las operaciones con matrices
class OperacionesMatrices:
    def __init__(self, matriz1, matriz2):
        self.matriz1 = matriz1
        self.matriz2 = matriz2

    def suma(self):
        return [
            [self.matriz1[0][0] + self.matriz2[0][0], self.matriz1[0][1] + self.matriz2[0][1]],
            [self.matriz1[1][0] + self.matriz2[1][0], self.matriz1[1][1] + self.matriz2[1][1]]
        ]

    def resta(self):
        return [
            [self.matriz1[0][0] - self.matriz2[0][0], self.matriz1[0][1] - self.matriz2[0][1]],
            [self.matriz1[1][0] - self.matriz2[1][0], self.matriz1[1][1] - self.matriz2[1][1]]
        ]

    def producto(self):
        return [
            [self.matriz1[0][0] * self.matriz2[0][0], self.matriz1[0][1] * self.matriz2[0][1]],
            [self.matriz1[1][0] * self.matriz2[1][0], self.matriz1[1][1] * self.matriz2[1][1]]
        ]

    def division(self):
        return [
            [self.matriz1[0][0] / self.matriz2[0][0] if self.matriz2[0][0] != 0 else "Inf", self.matriz1[0][1] / self.matriz2[0][1] if self.matriz2[0][1] != 0 else "Inf"],
            [self.matriz1[1][0] / self.matriz2[1][0] if self.matriz2[1][0] != 0 else "Inf", self.matriz1[1][1] / self.matriz2[1][1] if self.matriz2[1][1] != 0 else "Inf"]
        ]

# Clase para la interfaz gráfica
class InterfazMatrices:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Operaciones con Matrices 2x2")

        # Entradas para la Matriz 1
        tk.Label(ventana, text="Matriz 1").grid(row=0, column=0, columnspan=2)
        self.entry_m1_11 = tk.Entry(ventana, width=5)
        self.entry_m1_12 = tk.Entry(ventana, width=5)
        self.entry_m1_21 = tk.Entry(ventana, width=5)
        self.entry_m1_22 = tk.Entry(ventana, width=5)
        self.entry_m1_11.grid(row=1, column=0)
        self.entry_m1_12.grid(row=1, column=1)
        self.entry_m1_21.grid(row=2, column=0)
        self.entry_m1_22.grid(row=2, column=1)

        # Entradas para la Matriz 2
        tk.Label(ventana, text="Matriz 2").grid(row=0, column=3, columnspan=2)
        self.entry_m2_11 = tk.Entry(ventana, width=5)
        self.entry_m2_12 = tk.Entry(ventana, width=5)
        self.entry_m2_21 = tk.Entry(ventana, width=5)
        self.entry_m2_22 = tk.Entry(ventana, width=5)
        self.entry_m2_11.grid(row=1, column=3)
        self.entry_m2_12.grid(row=1, column=4)
        self.entry_m2_21.grid(row=2, column=3)
        self.entry_m2_22.grid(row=2, column=4)

        # Botón para realizar las operaciones
        tk.Button(ventana, text="Calcular", command=self.realizar_operaciones).grid(row=3, column=0, columnspan=5, pady=10)

        # Etiquetas para mostrar los resultados
        self.label_suma = tk.Label(ventana, text="Suma:")
        self.label_resta = tk.Label(ventana, text="Resta:")
        self.label_producto = tk.Label(ventana, text="Producto:")
        self.label_division = tk.Label(ventana, text="División:")
        self.label_suma.grid(row=4, column=0, columnspan=2)
        self.label_resta.grid(row=5, column=0, columnspan=2)
        self.label_producto.grid(row=4, column=3, columnspan=2)
        self.label_division.grid(row=5, column=3, columnspan=2)

    # Método para leer las matrices y realizar las operaciones
    def realizar_operaciones(self):
        try:
            # Leer los valores de las matrices desde los campos de entrada
            matriz1 = [
                [int(self.entry_m1_11.get()), int(self.entry_m1_12.get())],
                [int(self.entry_m1_21.get()), int(self.entry_m1_22.get())]
            ]
            matriz2 = [
                [int(self.entry_m2_11.get()), int(self.entry_m2_12.get())],
                [int(self.entry_m2_21.get()), int(self.entry_m2_22.get())]
            ]

            # Crear una instancia de la clase OperacionesMatrices
            operaciones = OperacionesMatrices(matriz1, matriz2)

            # Realizar las operaciones
            suma = operaciones.suma()
            resta = operaciones.resta()
            producto = operaciones.producto()
            division = operaciones.division()

            # Mostrar los resultados
            self.label_suma.config(text=f"Suma:\n{suma[0][0]} {suma[0][1]}\n{suma[1][0]} {suma[1][1]}")
            self.label_resta.config(text=f"Resta:\n{resta[0][0]} {resta[0][1]}\n{resta[1][0]} {resta[1][1]}")
            self.label_producto.config(text=f"Producto:\n{producto[0][0]} {producto[0][1]}\n{producto[1][0]} {producto[1][1]}")
            self.label_division.config(text=f"División:\n{division[0][0]} {division[0][1]}\n{division[1][0]} {division[1][1]}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos en todas las casillas.")

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazMatrices(ventana)
    ventana.mainloop()
