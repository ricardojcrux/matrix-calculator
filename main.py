from tkinter import *
from calculate import *

class Calculadora(Tk):
    def __init__(self) :
        super().__init__()
        matriz_bool = False
        self.title('Calculadora de matrices')
        self.resizable(width=False,height=False)

        #Creamos frame para el titulo y los botones
        title = Frame(self)
        title.pack(padx=10,pady=10)
        ingreso = Frame(self)
        ingreso.pack(padx=10,pady=10)

        #Entrada de información
        titulo = Label(title,text='De que tamaño será la matriz: ')
        titulo.config(font=('20'))
        titulo.pack(side=LEFT)
        self.texto = Entry(title,width=5, font=('30'))
        self.texto.pack()
        self.label = Entry(ingreso,width=40)
        self.label.insert(0,self.texto.get())
        self.label.pack(side=LEFT)
        boton = Button(ingreso,height=1,width=2,text='->',command=self.check)
        boton.pack(padx=10)

        #Variables necesarias
        self.matriz_bool = False
        self.lista_entry = []

    def check(self):
        try:
            cond = int(self.texto.get())
        except ValueError:
            cond = self.texto.get()

        self.label.delete(0,END)

        if type(cond) == str:
            self.label.insert(0,'El numero debe de ser un numero')
        elif cond < 1:
            self.label.insert(0,'El número no puede ser negativo o cero')
        elif cond > 9:
            self.label.insert(0,'El número es muy grande para nuestro proceso')
        else:
            self.label.insert(0,f'Cargando la matríz de {cond}x{cond}')
            self.matrices(cond)
            self.footer()
            self.matriz_bool = True
        self.texto.delete(0,END)

    def matrices(self, cond):
        if self.matriz_bool is True:
            self.matriz.destroy()
            self.lista_entry = []
        self.matriz = Frame(self)
        self.matriz.pack(padx=10,pady=10)
        for i in range(cond):
            fila = []
            for j in range(cond):
                valor = Entry(self.matriz, width=3)
                valor.grid(padx=5,pady=5,row=i,column=j)
                fila.append(valor)
            self.lista_entry.append(fila)

    def limpiar(self):
        for fila in self.lista_entry:
            for box in fila:
                box.delete(0,END)
                
    def calcular(self):
        matrix = []
        for fila in self.lista_entry:
            vector = []
            for valor in fila:
                try:
                    number = int(valor.get())
                except:
                    number = valor.get()
                if type(number) == str:
                    vector.append(0)
                else:
                    vector.append(number)
            matrix.append(vector)

        matri, determinante = numpy_matriz(matrix)
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

    def footer(self):
        if self.matriz_bool is True:
            self.pie.destroy()
        self.pie = Frame(self)
        self.pie.pack(padx=10,pady=10)
        clean = Button(self.pie,text='Limpiar',height=1,width=10,command=self.limpiar)
        clean.pack(padx=10,side=LEFT)
        calculo = Button(self.pie, text='Calcular',height=1,width=10,command=self.calcular)
        calculo.pack(padx=10,side=LEFT)

ventana = Calculadora()
ventana.mainloop()