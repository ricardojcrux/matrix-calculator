import numpy as np
from tkinter import *

iterante = 0
inter = 0

def matriz(lista : list):
    matriz = np.array(lista)
    determ = np.linalg.det(matriz)
    return matriz, int(determ)

def inversa(matriz, determ):
    if determ == 0:
        return 'La matriz no tiene inversa'
    else:
        return (np.linalg.inv(matriz)*determ)

def check():
    try:
        cond = int(texto.get())
    except ValueError:
        cond = texto.get()

    label.delete(0,END)

    if type(cond) == str:
        label.insert(0,'El numero debe de ser un numero')
    elif cond < 1:
        label.insert(0,'El número no puede ser negativo o cero')
    elif cond > 9:
        label.insert(0,'El número es muy grande para nuestro proceso')
    else:
        label.insert(0,f'Cargando la matríz de {cond}x{cond}')
        destruir(inter)
        matrices(cond)
        footer()
    texto.delete(0,END)

def matrices(cond):
    global variables, valores, cajas, iterante, inter
    variables = [''] * cond
    valores = []
    for i in range(cond):
        variables[i] = Frame(ventana)
        variables[i].pack(padx=5,pady=5)
        cajas = [''] * cond
        for j in range(cond):
            cajas[j] = Entry(variables[i],width=3,bg='black',fg='white', justify='right')
            cajas[j].pack(padx=5,pady=5,side=LEFT)
        else:
            valores.append(cajas)
    iterante += 1
    inter = cond

def destruir(cond):
    global variables, cajas, iterante
    if iterante > 0:
        for i in range(cond):
            for j in range(cond):
                cajas[j].destroy()
            variables[i].destroy()
        pie.destroy()
        clean.destroy()
        calculo.destroy()

def limpiar():
    global inter
    for cajas in valores:
        for j in cajas:
            j.delete(0,END)

def calcular():
    matrix = []
    for cajas in valores:
        vector = []
        for j in cajas:
            try:
                number = int(j.get())
            except:
                number = j.get()
            if type(number) == str:
                vector.append(0)
            else:
                vector.append(number)
        else:
            matrix.append(vector)

    matri, determinante = matriz(matrix)
    inverse = inversa(matri,determinante)

    if determinante == 0:
        cadena = f'La matriz ingresada es: \n{matri}\nSu determinante es {determinante}\nY por lo tanto {inverse}'
    else:
        cadena = f'La matriz ingresada es: \n{matri}\nSu determinante es {determinante}\nY la inversa de la matriz ingresada es: \n{inverse}'
    
    segunda = Toplevel()
    segunda.resizable(width=False,height=False)
    text = Text(segunda)
    text.pack()
    text.insert(1.0,cadena)

def footer():
    global clean, calculo, pie
    pie = Frame(ventana)
    clean = Button(pie,text='Limpiar',height=1,width=10,command=limpiar)
    clean.pack(padx=10,side=LEFT)
    calculo = Button(pie, text='Calcular',height=1,width=10,command=calcular)
    calculo.pack(padx=10,side=LEFT)
    pie.pack(padx=10,pady=10)
            
ventana = Tk()
ventana.title('Calculadora de matrices')
ventana.resizable(width=False,height=False)
title = Frame(ventana)
title.pack(padx=10,pady=10)
cond = Frame(ventana)
cond.pack(padx=10,pady=10)
titulo = Label(title,text='De que tamaño será la matriz: ')
titulo.config(font=('20'))
titulo.pack(side=LEFT)
texto = Entry(title,width=5, font=('30'))
texto.pack()
label = Entry(cond,width=40)
label.insert(0,texto.get())
label.pack(side=LEFT)
boton = Button(cond,height=1,width=2,text='->',command=check)
boton.pack(padx=10,side=LEFT)
ventana.mainloop()
ventana = Tk()

