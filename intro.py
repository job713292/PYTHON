import tkinter as tk
from tkinter import messagebox

def calcular_precio():
    try:
        costo = float(entry_costo.get())
        margen = float(entry_margen.get()) / 100  # Convertimos de porcentaje a decimal
        precio_venta = costo * (1 + margen)
        resultado.set(f"Precio de venta: ${precio_venta:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Precio de Venta")

# Entradas
tk.Label(ventana, text="Costo del producto:").grid(row=0, column=0, padx=10, pady=5)
entry_costo = tk.Entry(ventana)
entry_costo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Margen de ganancia (%):").grid(row=1, column=0, padx=10, pady=5)
entry_margen = tk.Entry(ventana)
entry_margen.grid(row=1, column=1, padx=10, pady=5)

# Botón
tk.Button(ventana, text="Calcular", command=calcular_precio).grid(row=2, column=0, columnspan=2, pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=('Arial', 12, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar ventana
ventana.mainloop()