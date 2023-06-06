from tkinter import Tk, Button, Entry

def suma():
    num1 = float(pantalla.get())
    pantalla.delete(0, 'end')
    operacion['operador'] = '+'
    operacion['valor'] = num1

def resta():
    num1 = float(pantalla.get())
    pantalla.delete(0, 'end')
    operacion['operador'] = '-'
    operacion['valor'] = num1

def multiplicacion():
    num1 = float(pantalla.get())
    pantalla.delete(0, 'end')
    operacion['operador'] = '*'
    operacion['valor'] = num1

def division():
    num1 = float(pantalla.get())
    pantalla.delete(0, 'end')
    operacion['operador'] = '/'
    operacion['valor'] = num1

def calcular():
    num2 = float(pantalla.get())
    pantalla.delete(0, 'end')
    operador = operacion['operador']
    num1 = operacion['valor']
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    pantalla.insert(0, str(resultado))

# Configuración ventana principal
root = Tk()
root.title("Calculadora")
root.resizable(0, 0)
root.geometry("290x260")

# Configuración pantalla de salida
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=5)

# Configuración botones
operacion = {'operador': '', 'valor': 0}

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_1.configure(command=lambda: pantalla.insert('end', '1'))

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.configure(command=lambda: pantalla.insert('end', '2'))

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.configure(command=lambda: pantalla.insert('end', '3'))

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.configure(command=lambda: pantalla.insert('end', '4'))

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.configure(command=lambda: pantalla.insert('end', '5'))

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.configure(command=lambda: pantalla.insert('end', '6'))

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.configure(command=lambda: pantalla.insert('end', '7'))

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.configure(command=lambda: pantalla.insert('end', '8'))

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.configure(command=lambda: pantalla.insert('end', '9'))

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.configure(command=calcular)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_punto.configure(command=lambda: pantalla.insert('end', '.'))

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_mas.configure(command=suma)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_menos.configure(command=resta)

boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.configure(command=multiplicacion)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.configure(command=division)

root.mainloop()
