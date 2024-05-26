import tkinter as tk
from tkinter import ttk

def mostrar_seleccion():
    seleccion = combobox.get()
    etiqueta_seleccion.config(text="Seleccionaste: " + seleccion)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Desplegable")

# Crear el combobox con múltiples opciones
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
combobox = ttk.Combobox(ventana, values=opciones)
combobox.set("Selecciona una opción")  # Texto inicial del combobox
combobox.pack(pady=10)

# Botón para mostrar la opción seleccionada
boton_mostrar = tk.Button(ventana, text="Mostrar Opción Seleccionada", command=mostrar_seleccion)
boton_mostrar.pack(pady=10)

# Etiqueta para mostrar la opción seleccionada
etiqueta_seleccion = tk.Label(ventana, text="")
etiqueta_seleccion.pack(pady=10)

# Iniciar el bucle de la aplicación
ventana.mainloop()
