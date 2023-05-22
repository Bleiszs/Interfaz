from tkinter import *
from funciones import obtener_resolucion_pantalla, obtenerDatos
from tkinter import messagebox, simpledialog 
import tkinter as tk
import json 
raiz = Tk()
ancho, alto = obtener_resolucion_pantalla()
ancho_str = str(int(ancho/2))
alto_str = str(int(alto))
dimension = ancho_str+'x'+alto_str
raiz.title("Ingreso de alumnos")
raiz.geometry(dimension)
raiz.resizable(False, False)

ventana = Frame(raiz)
ventana.grid(row=1, column=0)



# Etiquetas__________________________________________________________________________
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

analisis = Label (ventana, text= "Consola de registros")
analisis.grid(row=17, column=1, padx=4, pady=4)

# Cuadros de texto___________________________________________________________________

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

analisis_cuadro = Text (ventana)
analisis_cuadro.grid(row=18, column=0, padx=4, pady=4, columnspan=5)
analisis_cuadro.config(width=80, height=12)

# Menu de Opciones___________________________________________________________________

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
    data = open ('datos.json', 'r')
    data = dict(data)
    return data

registros = cargar_datos()
# Funciones__________________________________________________________________

def sigui():
    global registros

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
##ESTO HAY QUE CAMBIARLO. El registro hay que guardarlo como un diccionario para ingresarlo al JSON.
    '''
    registro = {
    "nombre":"",
    "apellido":"",
    "edad":"",
    }
    '''
numero_de_registro=len(registros)+1   

registro = {"Nombre": str(nombres_cuadro.get()),
        "Apellido paterno" : str(apellido_p_cuadro.get()),
        "Apellido materno" :  str(apellido_m_cuadro.get()),
        "Edad" : str(edad_cuadro.get()),
        "Direccion" :  str(direccion_cuadro.get()),
        "Email" : str(correo_cuadro.get()),
        "Telfonos": str(telefono_cuadro.get()),
        "Carrera" : str(carrera_seleccionada.get()),
         "Genero" : str(genero_seleccionado.get()), 
        "Observaciones" :str (observaciones_cuadro.get())
        }
        
        

registros[numero_de_registro] = registro
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
        for registro in registro:
            f.write(str(registro))

    messagebox.showinfo("Registro", "El registro se ha guardado correctamente.")

def limpiar():
    global registros

    nombres_cuadro.delete(0, "end")
    apellido_p_cuadro.delete(0, "end")
    apellido_m_cuadro.delete(0, "end")
    edad_cuadro.delete(0, "end")
    direccion_cuadro.delete(0, "end")
    correo_cuadro.delete(0, "end")
    telefono_cuadro.delete(0, "end")
    observaciones_cuadro.delete(0, "end")
    observaciones_cuadro.insert(0, "Sin Observaciones")
    carrera_seleccionada.set(carreras[0])
    genero_seleccionado.set(generos[0])
    info_accesada_cuadro.delete(0, END)
    registros = []

def eliminar_registro():
    global registros

    numero_registro = simpledialog.askinteger("Eliminar Registro", "Ingrese el número de registro a eliminar:")
    if numero_registro is not None:
        if messagebox.askyesno("Eliminar Registro", f"¿Estás seguro de eliminar el registro número {numero_registro}?"):
            if 1 <= numero_registro <= len(registros):
                registros.pop(numero_registro - 1)
                info_accesada_cuadro.delete(0, END)
                for registro in registros:
                    for item in registro:
                        info_accesada_cuadro.insert(END, item)
                messagebox.showinfo("Eliminar Registro", "El registro ha sido eliminado correctamente.")
            else:
                messagebox.showinfo("Eliminar Registro", "El número de registro ingresado no es válido.")
        else:
            messagebox.showinfo("Eliminar Registro", "No se eliminó el registro.")




# Botones___________________________________________________________________

boton_siguiente = Button(ventana, text="Siguiente", command=sigui)
boton_siguiente.grid(column=2, row=12, padx=4, pady=4)
boton_siguiente.config(width=15, background="#CDCDB5")

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(column=0, row=15, padx=4, pady=4)
boton_limpiar.config(width=15, background="#FFFF00")

boton_guardar = Button(ventana, text="Guardar", command=guardar)
boton_guardar.grid(column=1, row=15, padx=4, pady=4)
boton_guardar.config(width=27, background="gray65")

boton_eliminar = Button(ventana, text="Eliminar Ultimo Registro", command=eliminar_registro)
boton_eliminar.grid(column=2, row=15, padx=4, pady=4)
boton_eliminar.config(width=20, background="#AFAFEE")

boton_eliminar_registro = Button (ventana, text= "Seleccionar Registro a Eliminar")
boton_eliminar_registro.grid(column=1, row= 25, padx=2, pady=2)
boton_eliminar_registro.config(width=25, background="#AFAFEE" )



raiz.mainloop()