import tkinter as tk

def obtener_resolucion_pantalla():
    ventana = tk.Tk()
    ventana.withdraw()
    ancho = ventana.winfo_screenwidth()
    alto = ventana.winfo_screenheight()
    ventana.quit()
    return ancho, alto






    
