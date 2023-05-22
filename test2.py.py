from tkinter import *
from funciones import obtener_resolucion_pantalla
from tkinter import messagebox, simpledialog
import tkinter as tk
import json
import os
from tkinter import filedialog


raiz = Tk()
ancho, alto = obtener_resolucion_pantalla()
ancho_str = str(int(ancho / 2))
alto_str = str(int(alto))
dimension = ancho_str + 'x' + alto_str
raiz.title("Ingreso de alumnos")
raiz.geometry(dimension)
raiz.resizable(False, False)

ventana = Frame(raiz)
ventana.grid(row=1, column=0)

# Etiquetas________________________________________________________
nombres = Label(ventana, text="Nombre(s):")
nombres.grid(row=0, column=0, padx=4, pady=4)

apellido_p = Label(ventana, text="Apellido Paterno:")
apellido_p.grid(row=0, column=1, padx=4, pady=4)

apellido_m = Label(ventana, text="Apellido Materno:")
apellido_m.grid(row=0, column=2, padx=4, pady=4)

edad = Label(ventana, text="Edad:")
edad.grid(row=2, column=0, padx=4, pady=4)

direccion = Label(ventana, text="Direccion:")
direccion.grid(row=2, column=1, padx=4, pady=4)

correo = Label(ventana, text="Correo Electronico:")
correo.grid(row=2, column=2, padx=4, pady=4)

telefono = Label(ventana, text="Telefono:")
telefono.grid(row=4, column=0, padx=4, pady=4)

observaciones = Label(ventana, text="Observaciones:")
observaciones.grid(row=6, column=1, padx=4, pady=4)

carrera = Label(ventana, text="Selecciona la Carrera:")
carrera.grid(row=4, column=1, padx=4, pady=4)

genero = Label(ventana, text="Selecciona el Genero:")
genero.grid(row=4, column=2, padx=4, pady=4)

info_accesada = Label(ventana, text="Verificar la Informacion:")
info_accesada.grid(row=13, column=1, padx=4, pady=4)

analisis = Label(ventana, text="Consola de registros")
analisis.grid(row=17, column=1, padx=4, pady=4)

# Cuadros de texto__________________________________________________

nombres_cuadro = Entry(ventana, width=33)
nombres_cuadro.grid(column=0, row=1, pady=4, padx=4)

apellido_p_cuadro = Entry(ventana, width=33)
apellido_p_cuadro.grid(column=1, row=1, pady=4, padx=4)

apellido_m_cuadro = Entry(ventana, width=33)
apellido_m_cuadro.grid(column=2, row=1, pady=4, padx=4)

edad_cuadro = Entry(ventana, width=33)
edad_cuadro.grid(column=0, row=3, pady=4, padx=4)

direccion_cuadro = Entry(ventana, width=33)
direccion_cuadro.grid(column=1, row=3, pady=4, padx=4)

correo_cuadro = Entry(ventana, width=33)
correo_cuadro.grid(column=2, row=3, pady=4, padx=4)

telefono_cuadro = Entry(ventana, width=33)
telefono_cuadro.grid(column=0, row=5, pady=4, padx=4)

observaciones_cuadro = Entry(ventana)
observaciones_cuadro.grid(column=0, row=7, pady=4, padx=4, columnspan=6)
observaciones_cuadro.config(width=100)
observaciones_cuadro.insert(0, "Sin observaciones")

info_accesada_cuadro = Listbox(ventana)
info_accesada_cuadro.grid(row=14, column=0, padx=4, pady=4, columnspan=5)
info_accesada_cuadro.config(width=100, height=12)

analisis_cuadro = Text(ventana)
analisis_cuadro.grid(row=18, column=0, padx=4, pady=4, columnspan=5)
analisis_cuadro.config(width=80, height=12)

# Menu de Opciones__________________________________________________

carreras = ["", "Ing. Industrial", "Ing. Civil", "Ing. en Mecatrónica"]
carrera_seleccionada = StringVar(ventana)
carrera_seleccionada.set(carreras[0])
combo_carrera = OptionMenu(ventana, carrera_seleccionada, *carreras)
combo_carrera.grid(column=1, row=5, pady=4, padx=4)
combo_carrera.config(width=26)

generos = ["", "Masculino", "Femenino", "Otro"]
genero_seleccionado = StringVar(ventana)
genero_seleccionado.set(generos[0])
combo_genero = OptionMenu(ventana, genero_seleccionado, *generos)
combo_genero.grid(column=2, row=5, pady=4, padx=4)
combo_genero.config(width=26)

# Variables globales
def cargar_datos():
    archivo = "datos.json"
    if os.path.isfile(archivo):
        try:
            with open(archivo, 'r') as file:
                data = json.load(file)
                num_registros = len(data)
                return data, num_registros
        except FileNotFoundError:
            return {}, 0
    else:
        return {}, 0

registros = cargar_datos()
num_registros = len(registros)

# Funciones____________________________________________________

def sigui():
    global registros, num_registros

    if nombres_cuadro.get() == "" or apellido_p_cuadro.get() == "" or apellido_m_cuadro.get() == "" or edad_cuadro.get() == "" or direccion_cuadro.get() == "" or correo_cuadro.get() == "" or telefono_cuadro.get() == "" or carrera_seleccionada.get() == "" or genero_seleccionado.get() == "" or observaciones_cuadro.get() == "":
        mensaje = "Faltan espacios por completar"
        messagebox.showinfo("Advertencia", mensaje)
        info_accesada_cuadro.delete(0, END)
        return

    if not telefono_cuadro.get().isdigit():
        mensaje = "El teléfono solo debe contener números"
        messagebox.showinfo("Advertencia", mensaje)
        telefono_cuadro.delete(0, END)
        return

    if not edad_cuadro.get().isdigit():
        mensaje = "La Edad solo debe contener números"
        messagebox.showinfo("Advertencia", mensaje)
        edad_cuadro.delete(0, END)
        return

    num_registros += 1

    registro = {
        "Nombre": nombres_cuadro.get(),
        "Apellido paterno": apellido_p_cuadro.get(),
        "Apellido materno": apellido_m_cuadro.get(),
        "Edad": edad_cuadro.get(),
        "Direccion": direccion_cuadro.get(),
        "Email": correo_cuadro.get(),
        "Telfonos": telefono_cuadro.get(),
        "Carrera": carrera_seleccionada.get(),
        "Genero": genero_seleccionado.get(),
        "Observaciones": observaciones_cuadro.get()
    }

    registros[num_registros] = registro
    info_accesada_cuadro.delete(0, END)
    for key, value in registro.items():
        info_accesada_cuadro.insert(END, value)

def guardar():
    global registros

    if len(registros) == 0:
        messagebox.showinfo("Guardar", "No hay información para guardar.")
        return

    archivo = "datos.json"
    with open(archivo, "w") as f:
        json.dump(registros, f)

    messagebox.showinfo("Registro", "El registro se ha guardado correctamente.")

def limpiar():
    global registros, num_registros

    nombres_cuadro.delete(0, END)
    apellido_p_cuadro.delete(0, END)
    apellido_m_cuadro.delete(0, END)
    edad_cuadro.delete(0, END)
    direccion_cuadro.delete(0, END)
    correo_cuadro.delete(0, END)
    telefono_cuadro.delete(0, END)
    observaciones_cuadro.delete(0, END)
    observaciones_cuadro.insert(0, "Sin Observaciones")
    carrera_seleccionada.set(carreras[0])
    genero_seleccionado.set(generos[0])
    info_accesada_cuadro.delete(0, END)
    registros = {}
    num_registros = 0

def eliminar_registro():
    global registros

    if len(registros) == 0:
        messagebox.showinfo("Eliminar Registro", "No hay registros para eliminar.")
        return

    numero_registro = simpledialog.askinteger("Eliminar Registro", "Ingrese el número de registro a eliminar:")
    if numero_registro is not None:
        if 1 <= numero_registro <= len(registros):
            if messagebox.askyesno("Eliminar Registro", f"¿Estás seguro de eliminar el registro número {numero_registro}?"):
                registros.pop(str(numero_registro))  # Convert to string before popping
                info_accesada_cuadro.delete(0, END)
                for registro in registros.values():
                    for item in registro.values():
                        info_accesada_cuadro.insert(END, item)
                        
                guardar_en_archivo('datos.json', registros)  # Save the updated records to the file

                messagebox.showinfo("Eliminar Registro", "El registro ha sido eliminado correctamente.")
            else:
                messagebox.showinfo("Eliminar Registro", "No se eliminó el registro.")
        else:
            messagebox.showinfo("Eliminar Registro", "El número de registro ingresado no es válido.")

def guardar_en_archivo(archivo, data):
    with open(archivo, "w") as f:
        json.dump(data, f)

def cargar_archivos():
    global registros, num_registros

    registros, num_registros = cargar_datos()

    analisis_cuadro.delete("1.0", END)
    for i, registro in enumerate(registros.values(), 1):
        nombre = registro.get("Nombre", "")
        apellido_paterno = registro.get("Apellido paterno", "")
        telefono = registro.get("Telefono", "")
        analisis_cuadro.insert(END, f"Número de Registro: {i}\n")
        analisis_cuadro.insert(END, f"Nombre: {nombre}\n")
        analisis_cuadro.insert(END, f"Apellido Paterno: {apellido_paterno}\n")
        analisis_cuadro.insert(END, f"Teléfono: {telefono}\n")
        analisis_cuadro.insert(END, "---------------------\n")
    analisis_cuadro.insert(END, f"Número de Registros: {num_registros}\n")

# Botones____________________________________________________

boton_siguiente = Button(ventana, text="Siguiente", command=sigui)
boton_siguiente.grid(column=2, row=12, padx=4, pady=4)
boton_siguiente.config(width=15, background="#CDCDB5")

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(column=0, row=15, padx=4, pady=4)
boton_limpiar.config(width=15, background="#FFFF00")

boton_guardar = Button(ventana, text="Guardar", command=guardar)
boton_guardar.grid(column=1, row=15, padx=4, pady=4)
boton_guardar.config(width=27, background="gray65")

boton_eliminar_registro = Button(ventana, text="Seleccionar Registro a Eliminar", command=eliminar_registro)
boton_eliminar_registro.grid(column=2, row=15, padx=4, pady=4)
boton_eliminar_registro.config(width=20, background="#AFAFEE")

boton_cargar_archivos = Button(ventana, text="Cargar Archivos", command=cargar_archivos)
boton_cargar_archivos.grid(row=19, column=1, padx=4, pady=4)
boton_cargar_archivos.config(width=27, background="gray65")

raiz.mainloop()
