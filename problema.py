import tkinter as tk
from tkinter import messagebox

# Clase que contiene la lógica para verificar el cuadro mágico
class CuadroMagico:
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)
        self.constante_magica = sum(matriz[0])  # La suma de la primera fila se toma como referencia

    def es_cuadro_magico(self):
        # Verificar filas
        for fila in self.matriz:
            if sum(fila) != self.constante_magica:
                return False
        
        # Verificar columnas
        for col in range(self.n):
            suma_col = sum(self.matriz[fila][col] for fila in range(self.n))
            if suma_col != self.constante_magica:
                return False
        
        # Verificar diagonal principal
        suma_diag_prin = sum(self.matriz[i][i] for i in range(self.n))
        if suma_diag_prin != self.constante_magica:
            return False
        
        # Verificar diagonal secundaria
        suma_diag_sec = sum(self.matriz[i][self.n - i - 1] for i in range(self.n))
        if suma_diag_sec != self.constante_magica:
            return False
        
        return True

# Clase que maneja la interfaz gráfica
class InterfazCuadroMagico:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cuadro Mágico")
        self.ventana.geometry("400x400")

        # Etiqueta de entrada del tamaño del cuadro
        self.label_tamano = tk.Label(ventana, text="Introduce el tamaño del cuadro (n):")
        self.label_tamano.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo de entrada para el tamaño del cuadro
        self.entry_tamano = tk.Entry(ventana)
        self.entry_tamano.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para generar la matriz
        self.boton_generar = tk.Button(ventana, text="Generar matriz", command=self.generar_matriz)
        self.boton_generar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Lista que contendrá las entradas de la matriz
        self.entradas_matriz = []

        # Botón para verificar si es cuadro mágico
        self.boton_verificar = tk.Button(ventana, text="Verificar Cuadro Mágico", state=tk.DISABLED, command=self.verificar_cuadro_magico)
        self.boton_verificar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def generar_matriz(self):
        try:
            self.n = int(self.entry_tamano.get())  # Obtiene el tamaño del cuadro
            if self.n < 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El tamaño debe ser un número entero mayor que 1.")
            return

        # Limpiar las entradas anteriores
        for fila in self.entradas_matriz:
            for entrada in fila:
                entrada.destroy()  # Ahora destruimos cada widget Entry individualmente
        self.entradas_matriz.clear()

        # Crear campos de entrada para la matriz
        for i in range(self.n):
            fila_entradas = []
            for j in range(self.n):
                entrada = tk.Entry(self.ventana, width=5)
                entrada.grid(row=i+4, column=j, padx=5, pady=5)
                fila_entradas.append(entrada)
            self.entradas_matriz.append(fila_entradas)

        # Habilitar el botón de verificar
        self.boton_verificar.config(state=tk.NORMAL)

    def verificar_cuadro_magico(self):
        # Leer la matriz desde los campos de entrada
        matriz = []
        try:
            for fila_entradas in self.entradas_matriz:
                fila = [int(entrada.get()) for entrada in fila_entradas]
                matriz.append(fila)
        except ValueError:
            messagebox.showerror("Error", "Todos los valores deben ser números enteros.")
            return

        # Crear una instancia de CuadroMagico y verificar
        cuadro_magico = CuadroMagico(matriz)
        if cuadro_magico.es_cuadro_magico():
            messagebox.showinfo("Resultado", f"Es un cuadro mágico. La constante mágica es {cuadro_magico.constante_magica}.")
        else:
            messagebox.showinfo("Resultado", "No es un cuadro mágico.")

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazCuadroMagico(ventana)
    ventana.mainloop()
