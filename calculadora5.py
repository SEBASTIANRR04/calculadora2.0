import tkinter as tk

def click(event): #Nos da acceso al boton que se creo
    text = event.widget.cget("text") #Nos da el texto del botón en el que se hizo clic

    #Botones especiales 
    if text == "=":
        try: #Condicional que verifica =
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result)) #tk.ENd Resultado insertara al final del contenido

    #Si hay una exepcion se maneja dentro de except
        except Exception as e:
            entry.delete(0, tk.END) #Eliminar la entrada 
            entry.insert(tk.END, "Error") #Decirle al ususario que cometio un error

    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

#Crear la ventana principal
root = tk.Tk()
root.title("Calculadora") #Se crea el titulo de la ventana 

#Crear un widget de entrada
entry = tk.Entry(root, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #padx y pady establecen el relleno entre los botones

#Definir los botones
#Organizo: Texto del boton, fila y columna 
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

# Agregar los botones a la ventana
for (text, row, col) in buttons: #Bucle que contendra texo
    
    #Root sirve para establecer el boton en la pantalla principal
    button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5) #Se usa el metodo grid para colocar el boton en la pantalla
    button.bind("<Button-1>", click)#Click en el boton, se llama la funcion click

# Incio del Bucle
root.mainloop()