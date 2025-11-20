import tkinter as tk
from tkinter import messagebox

ventana = tk.TK()  #crea una ventanna 
ventana.title("ventana simple") #le da un titulo

label = tk.Label(ventana, tex="!Hola mundoooo¡") #crea un widget de texto
label.pack() #lo coloca en la ventana

boton = tk.Button(ventana, text="haz clic aqui") #crea un boton 
boton.pack()

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "!boton presionado¡")

    label = tk.Label (ventana, text="presiona el boton para ver un  mensaje")
    label.pack(pady=10)

    boton = tk.Button(ventana, text="Haz clic aqui", command=mostrar_mensaje)
    boton.pack(pady=10)

    

ventana.mainloop() #muestra la ventana 

