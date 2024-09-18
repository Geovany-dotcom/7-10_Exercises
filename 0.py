import tkinter as tk
from tkinter import messagebox

# Clase que maneja la lógica de la matriz
class Matriz:
    def __init__(self):
        self.matriz = [
            [0, 2, 5, 7, 6],
            [0, 0, 0, 3, 8],
            [2, 9, 6, 3, 4],
            [1, 5, 6, 1, 4],
            [0, 9, 2, 5, 0]
        ]

    def contar_ceros_por_renglon(self):
        conteo_ceros = []
        for fila in self.matriz:
            conteo_ceros.append(fila.count(0))
        return conteo_ceros

class InterfazMatriz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Contador de Ceros en la Matriz")
        self.ventana.geometry("400x300")
        self.label_instruccion = tk.Label(ventana, text="Presiona el botón para contar los ceros en cada renglón")
        self.label_instruccion.pack(pady=10)

        self.boton_contar = tk.Button(ventana, text="Contar Ceros", command=self.mostrar_conteo)
        self.boton_contar.pack(pady=10)

        self.label_resultado = tk.Label(ventana, text="", justify="left")
        self.label_resultado.pack(pady=10)

        self.matriz_objeto = Matriz()

    def mostrar_conteo(self):
        resultado = self.matriz_objeto.contar_ceros_por_renglon()

        # Mostrar resultado en la etiqueta
        resultado_texto = ""
        for i, ceros in enumerate(resultado):
            resultado_texto += f"Renglón {i+1}: {ceros} ceros\n"

        self.label_resultado.config(text=resultado_texto)

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazMatriz(ventana)
    ventana.mainloop()
