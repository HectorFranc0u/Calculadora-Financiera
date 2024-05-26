import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import locale
import math

def validate_float(new_value):
    if new_value == "":
        return True
    
    try:
        float(new_value)
        return True
    except ValueError:
        return False
        
# Crear la ventana principal
window = tk.Tk()
window.title("Aplicación de Ejemplo")
window.geometry("500x300")
window.resizable(False, False)
#validador de punto flotante
vcmd = (window.register(validate_float), '%P')
#settear moneda local
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def show_main_view():
    # Limpiar el contenido de la ventana
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Calculadora de interes compuesto")
    label.pack(pady=10)

    # Crear los botones
    button1 = tk.Button(window, text="interes compuesto", command=show_IC_view)
    button1.pack(pady=10)

    button2 = tk.Button(window, text="valor equivalente", command=show_VE_view)
    button2.pack(pady=10)


def show_IC_view():
    # Limpiar el contenido de la ventana
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Calculo de interes compuesto")
    label.pack(pady=10)
    
    # Crear un botón para regresar a la vista principal

    next_button = tk.Button(window, text="Capital (C)", command=show_Capital_view)
    next_button.pack(pady=10)

    next_button = tk.Button(window, text="Monto (M)", command=show_Monto_view)
    next_button.pack(pady=10)

    next_button = tk.Button(window, text="Tiempo (n)", command=show_Tiempo_view)
    next_button.pack(pady=10)

    next_button = tk.Button(window, text="Tasa de interes (i)", command=show_Tasa_view)
    next_button.pack(pady=10)
    
    back_button = tk.Button(window, text="Regresar", command=show_main_view)
    back_button.pack(pady=10)

def show_VE_view():
    # Limpiar el contenido de la ventana
    for widget in window.winfo_children():
        widget.destroy()
    
    # Crear una Label
    label = tk.Label(window, text="Calculo de valor equivalente")
    label.pack(pady=10)
    
    # Crear un botón para regresar a la vista principal
    back_button = tk.Button(window, text="Regresar", command=show_main_view)
    back_button.pack(pady=10)


    # Limpiar el contenido de la ventana
    for widget in window.winfo_children():
        widget.destroy()
    
    # Crear una Label
    label = tk.Label(window, text="Calculo de tasa efectiva")
    label.pack(pady=10)
    
    # Crear un botón para regresar a la vista principal
    back_button = tk.Button(window, text="Regresar", command=show_main_view)
    back_button.pack(pady=10)

def show_Capital_view():
    for widget in window.winfo_children():
        widget.destroy()
        
    def on_button_click():
        M = float(entry1.get())
        n = float(entry2.get())
        tasa = float(entry3.get())

        if opcion.get() == "1":
            i = tasa/12/100
            C = M/((1+i)**n)
            Capital = round(C, 2)
            resultado = "El Capital o valor actual obtenido con estos datos es: " + locale.currency(Capital, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "2":
            i = tasa/6/100
            C = M/((1+i)**n)
            Capital = round(C, 2)
            resultado = "El Capital o valor actual obtenido con estos datos es: " + locale.currency(Capital, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "3":
            i = tasa/4/100
            C = M/((1+i)**n)
            Capital = round(C, 2)
            resultado = "El Capital o valor actual obtenido con estos datos es: " + locale.currency(Capital, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "4":
            i = tasa/3/100
            C = M/((1+i)**n)
            Capital = round(C, 2)
            resultado = "El Capital o valor actual obtenido con estos datos es: " + locale.currency(Capital, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "5":
            i = tasa/2/100
            C = M/((1+i)**n)
            Capital = round(C, 2)
            resultado = "El Capital o valor actual obtenido con estos datos es: " + locale.currency(Capital, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "6":
            i = tasa/1/100
            C = M/((1+i)**n)
            Capital = round(C, 2)
            resultado = "El Capital o valor actual obtenido con estos datos es: " + locale.currency(Capital, grouping=True)
            messagebox.showinfo("resultado", resultado)
    
    label = tk.Label(window, text="Encontrar capital")
    label.pack(pady=10)

    fila1 = tk.Frame(window)
    fila2 = tk.Frame(window)
    fila3 = tk.Frame(window)
    fila4 = tk.Frame(window)
    fila5 = tk.Frame(window)

    fila1.pack()
    fila2.pack()
    fila3.pack()
    fila4.pack()
    fila5.pack()

    #declarar el Monto
    label1 = tk.Label(fila1, text="Monto (M):")
    label1.pack(side=tk.LEFT, pady=5)
    entry1 = tk.Entry(fila1, validate='key', validatecommand=vcmd)
    entry1.pack(side=tk.LEFT, pady=5)

    #declarar la tasa de interes
    label3 = tk.Label(fila3, text="tasa (i):")
    label3.pack(side=tk.LEFT, pady=5)
    entry3 = tk.Entry(fila3, validate='key', validatecommand=vcmd)
    entry3.pack(side=tk.LEFT, pady=5)

    
    #declarar el tiempo
    label2 = tk.Label(fila2, text="Tiempo (n):")
    label2.pack(side=tk.LEFT, pady=5)
    entry2 = tk.Entry(fila2, validate='key', validatecommand=vcmd)
    entry2.pack(side=tk.LEFT, pady=5)
   
    label4 = tk.Label(fila4, text="periodo de capitalizacion:")
    label4.pack(pady=5)
    # Variable para almacenar la opción seleccionada
    opcion = tk.StringVar()

    # Crear los radiobuttons
    rb1 = tk.Radiobutton(fila5, text="mensual", variable=opcion, value="1")
    rb1.pack(side=tk.LEFT)

    rb2 = tk.Radiobutton(fila5, text="bimensual", variable=opcion, value="2")
    rb2.pack(side=tk.LEFT)

    rb3 = tk.Radiobutton(fila5, text="trimestral", variable=opcion, value="3")
    rb3.pack(side=tk.LEFT)

    rb4 = tk.Radiobutton(fila5, text="cuatrimestral", variable=opcion, value="4")
    rb4.pack(side=tk.LEFT)

    rb5 = tk.Radiobutton(fila5, text="semestral", variable=opcion, value="5")
    rb5.pack(side=tk.LEFT)
    
    rb6 = tk.Radiobutton(fila5, text="anual", variable=opcion, value="6")
    rb6.pack(side=tk.LEFT)
    
    # Crear y colocar el botón
    button = tk.Button(window, text="Enviar", command=on_button_click)
    button.pack(pady=10)

    back_button = tk.Button(window, text="Regresar", command=show_IC_view)
    back_button.pack(pady=10)

def show_Monto_view():
    for widget in window.winfo_children():
        widget.destroy()
        
    def on_button_click():
        C = float(entry1.get())
        n = float(entry2.get())
        tasa = float(entry3.get())

        if opcion.get() == "1":
            i = tasa/12/100
            M = C*((1+i)**n)
            Monto = round(M, 2)
            resultado = "El Monto o valor Futuro obtenido con estos datos es: " + locale.currency(Monto, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "2":
            i = tasa/6/100
            M = C*((1+i)**n)
            Monto = round(M, 2)
            resultado = "El Monto o valor Futuro obtenido con estos datos es: " + locale.currency(Monto, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "3":
            i = tasa/4/100
            M = C*((1+i)**n)
            Monto = round(M, 2)
            resultado = "El Monto o valor Futuro obtenido con estos datos es: " + locale.currency(Monto, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "4":
            i = tasa/3/100
            M = C*((1+i)**n)
            Monto = round(M, 2)
            resultado = "El Monto o valor Futuro obtenido con estos datos es: " + locale.currency(Monto, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "5":
            i = tasa/2/100
            M = C*((1+i)**n)
            Monto = round(M, 2)
            resultado = "El Monto o valor Futuro obtenido con estos datos es: " + locale.currency(Monto, grouping=True)
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "6":
            i = tasa/1/100
            M = C*((1+i)**n)
            Monto = round(M, 2)
            resultado = "El Monto o valor Futuro obtenido con estos datos es: " + locale.currency(Monto, grouping=True)
            messagebox.showinfo("resultado", resultado)
    
    label = tk.Label(window, text="Encontrar capital")
    label.pack(pady=10)

    fila1 = tk.Frame(window)
    fila2 = tk.Frame(window)
    fila3 = tk.Frame(window)
    fila4 = tk.Frame(window)
    fila5 = tk.Frame(window)

    fila1.pack()
    fila2.pack()
    fila3.pack()
    fila4.pack()
    fila5.pack()

    #declarar el Monto
    label1 = tk.Label(fila1, text="Capital (C):")
    label1.pack(side=tk.LEFT, pady=5)
    entry1 = tk.Entry(fila1, validate='key', validatecommand=vcmd)
    entry1.pack(side=tk.LEFT, pady=5)

    #declarar la tasa de interes
    label3 = tk.Label(fila3, text="tasa (i):")
    label3.pack(side=tk.LEFT, pady=5)
    entry3 = tk.Entry(fila3, validate='key', validatecommand=vcmd)
    entry3.pack(side=tk.LEFT, pady=5)

    
    #declarar el tiempo
    label2 = tk.Label(fila2, text="Tiempo (n):")
    label2.pack(side=tk.LEFT, pady=5)
    entry2 = tk.Entry(fila2, validate='key', validatecommand=vcmd)
    entry2.pack(side=tk.LEFT, pady=5)
   
    label4 = tk.Label(fila4, text="periodo de capitalizacion:")
    label4.pack(pady=5)
    # Variable para almacenar la opción seleccionada
    opcion = tk.StringVar()

    # Crear los radiobuttons
    rb1 = tk.Radiobutton(fila5, text="mensual", variable=opcion, value="1")
    rb1.pack(side=tk.LEFT)

    rb2 = tk.Radiobutton(fila5, text="bimensual", variable=opcion, value="2")
    rb2.pack(side=tk.LEFT)

    rb3 = tk.Radiobutton(fila5, text="trimestral", variable=opcion, value="3")
    rb3.pack(side=tk.LEFT)

    rb4 = tk.Radiobutton(fila5, text="cuatrimestral", variable=opcion, value="4")
    rb4.pack(side=tk.LEFT)

    rb5 = tk.Radiobutton(fila5, text="semestral", variable=opcion, value="5")
    rb5.pack(side=tk.LEFT)
    
    rb6 = tk.Radiobutton(fila5, text="anual", variable=opcion, value="6")
    rb6.pack(side=tk.LEFT)
    
    # Crear y colocar el botón
    button = tk.Button(window, text="Enviar", command=on_button_click)
    button.pack(pady=10)

    back_button = tk.Button(window, text="Regresar", command=show_IC_view)
    back_button.pack(pady=10)

def show_Tiempo_view():
    for widget in window.winfo_children():
        widget.destroy()
        
    def on_button_click():
        C = float(entry1.get())
        M = float(entry2.get())
        tasa = float(entry3.get())

        if opcion.get() == "1":
            i = tasa/12/100
            log1 = math.log((M/C), 10)
            log2 = math.log((1+i), 10)
            n = log1/log2
            tiempo = round(n, 2)
            resultado = "El tiempo calculado para esta operacion es: " + str(tiempo) + " meses."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "2":
            i = tasa/6/100
            log1 = math.log((M/C), 10)
            log2 = math.log((1+i), 10)
            n = log1/log2
            tiempo = round(n, 2)
            resultado = "El tiempo calculado para esta operacion es: " + str(tiempo) + " bimestres."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "3":
            i = tasa/4/100
            log1 = math.log((M/C), 10)
            log2 = math.log((1+i), 10)
            n = log1/log2
            tiempo = round(n, 2)
            resultado = "El tiempo calculado para esta operacion es: " + str(tiempo) + " trimestres."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "4":
            i = tasa/3/100
            log1 = math.log((M/C), 10)
            log2 = math.log((1+i), 10)
            n = log1/log2
            tiempo = round(n, 2)
            resultado = "El tiempo calculado para esta operacion es: " + str(tiempo) + " cuatrimestres."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "5":
            i = tasa/2/100
            log1 = math.log((M/C), 10)
            log2 = math.log((1+i), 10)
            n = log1/log2
            tiempo = round(n, 2)
            resultado = "El tiempo calculado para esta operacion es: " + str(tiempo) + " semestres."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "6":
            i = tasa/1/100
            log1 = math.log((M/C), 10)
            log2 = math.log((1+i), 10)
            n = log1/log2
            tiempo = round(n, 2)
            resultado = "El tiempo calculado para esta operacion es: " + str(tiempo) + " años."
            messagebox.showinfo("resultado", resultado)
    
    label = tk.Label(window, text="Encontrar capital")
    label.pack(pady=10)

    fila1 = tk.Frame(window)
    fila2 = tk.Frame(window)
    fila3 = tk.Frame(window)
    fila4 = tk.Frame(window)
    fila5 = tk.Frame(window)

    fila1.pack()
    fila2.pack()
    fila3.pack()
    fila4.pack()
    fila5.pack()

    #declarar el Monto
    label1 = tk.Label(fila1, text="Capital (C):")
    label1.pack(side=tk.LEFT, pady=5)
    entry1 = tk.Entry(fila1, validate='key', validatecommand=vcmd)
    entry1.pack(side=tk.LEFT, pady=5)

    #declarar la tasa de interes
    label3 = tk.Label(fila3, text="tasa (i):")
    label3.pack(side=tk.LEFT, pady=5)
    entry3 = tk.Entry(fila3, validate='key', validatecommand=vcmd)
    entry3.pack(side=tk.LEFT, pady=5)

    
    #declarar el tiempo
    label2 = tk.Label(fila2, text="Monto (M):")
    label2.pack(side=tk.LEFT, pady=5)
    entry2 = tk.Entry(fila2, validate='key', validatecommand=vcmd)
    entry2.pack(side=tk.LEFT, pady=5)
   
    label4 = tk.Label(fila4, text="periodo de capitalizacion:")
    label4.pack(pady=5)
    # Variable para almacenar la opción seleccionada
    opcion = tk.StringVar()

    # Crear los radiobuttons
    rb1 = tk.Radiobutton(fila5, text="mensual", variable=opcion, value="1")
    rb1.pack(side=tk.LEFT)

    rb2 = tk.Radiobutton(fila5, text="bimensual", variable=opcion, value="2")
    rb2.pack(side=tk.LEFT)

    rb3 = tk.Radiobutton(fila5, text="trimestral", variable=opcion, value="3")
    rb3.pack(side=tk.LEFT)

    rb4 = tk.Radiobutton(fila5, text="cuatrimestral", variable=opcion, value="4")
    rb4.pack(side=tk.LEFT)

    rb5 = tk.Radiobutton(fila5, text="semestral", variable=opcion, value="5")
    rb5.pack(side=tk.LEFT)
    
    rb6 = tk.Radiobutton(fila5, text="anual", variable=opcion, value="6")
    rb6.pack(side=tk.LEFT)
    
    # Crear y colocar el botón
    button = tk.Button(window, text="Enviar", command=on_button_click)
    button.pack(pady=10)

    back_button = tk.Button(window, text="Regresar", command=show_IC_view)
    back_button.pack(pady=10)

def show_Tasa_view():
    for widget in window.winfo_children():
        widget.destroy()
        
    def on_button_click():
        C = float(entry1.get())
        M = float(entry2.get())
        n = float(entry3.get())

        if opcion.get() == "1":
            i = (((M/C) ** (1/n)) - 1) * 100
            tasa = round(i, 2)
            resultado = "la tasa de interes es de: " + str(tasa) + "% mensual."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "2":
            i = (((M/C) ** (1/n)) - 1) * 100
            tasa = round(i, 2)
            resultado = "la tasa de interes es de: " + str(tasa) + "%" + " bimensual."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "3":
            i = (((M/C) ** (1/n)) - 1) * 100
            tasa = round(i, 2)
            resultado = "la tasa de interes es de: " + str(tasa) + "%" + " trimestral."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "4":
            i = (((M/C) ** (1/n)) - 1) * 100
            tasa = round(i, 2)
            resultado = "la tasa de interes es de: " + str(tasa) + "%" + " cuatrimestral."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "5":
            i = (((M/C) ** (1/n)) - 1) * 100
            tasa = round(i, 2)
            resultado = "la tasa de interes es de: " + str(tasa) + "%" + " semestral."
            messagebox.showinfo("resultado", resultado)
        elif opcion.get() == "6":
            i = (((M/C) ** (1/n)) - 1) * 100
            tasa = round(i, 2)
            resultado = "la tasa de interes es de: " + str(tasa) + "%" + " anual."
            messagebox.showinfo("resultado", resultado)
    
    label = tk.Label(window, text="Encontrar capital")
    label.pack(pady=10)

    fila1 = tk.Frame(window)
    fila2 = tk.Frame(window)
    fila3 = tk.Frame(window)
    fila4 = tk.Frame(window)
    fila5 = tk.Frame(window)

    fila1.pack()
    fila2.pack()
    fila3.pack()
    fila4.pack()
    fila5.pack()

    #declarar el Monto
    label1 = tk.Label(fila1, text="Capital (C):")
    label1.pack(side=tk.LEFT, pady=5)
    entry1 = tk.Entry(fila1, validate='key', validatecommand=vcmd)
    entry1.pack(side=tk.LEFT, pady=5)

    #declarar la tasa de interes
    label3 = tk.Label(fila3, text="tiempo (n):")
    label3.pack(side=tk.LEFT, pady=5)
    entry3 = tk.Entry(fila3, validate='key', validatecommand=vcmd)
    entry3.pack(side=tk.LEFT, pady=5)

    
    #declarar el tiempo
    label2 = tk.Label(fila2, text="Monto (M):")
    label2.pack(side=tk.LEFT, pady=5)
    entry2 = tk.Entry(fila2, validate='key', validatecommand=vcmd)
    entry2.pack(side=tk.LEFT, pady=5)
   
    label4 = tk.Label(fila4, text="periodo de capitalizacion:")
    label4.pack(pady=5)
    # Variable para almacenar la opción seleccionada
    opcion = tk.StringVar()

    # Crear los radiobuttons
    rb1 = tk.Radiobutton(fila5, text="mensual", variable=opcion, value="1")
    rb1.pack(side=tk.LEFT)

    rb2 = tk.Radiobutton(fila5, text="bimensual", variable=opcion, value="2")
    rb2.pack(side=tk.LEFT)

    rb3 = tk.Radiobutton(fila5, text="trimestral", variable=opcion, value="3")
    rb3.pack(side=tk.LEFT)

    rb4 = tk.Radiobutton(fila5, text="cuatrimestral", variable=opcion, value="4")
    rb4.pack(side=tk.LEFT)

    rb5 = tk.Radiobutton(fila5, text="semestral", variable=opcion, value="5")
    rb5.pack(side=tk.LEFT)
    
    rb6 = tk.Radiobutton(fila5, text="anual", variable=opcion, value="6")
    rb6.pack(side=tk.LEFT)
    
    # Crear y colocar el botón
    button = tk.Button(window, text="Enviar", command=on_button_click)
    button.pack(pady=10)

    back_button = tk.Button(window, text="Regresar", command=show_IC_view)
    back_button.pack(pady=10)

# Mostrar la vista principal al inicio
show_main_view()

# Iniciar el bucle de eventos
window.mainloop()