from tkinter import *

raiz=Tk()

raiz.title("Calculador de Resistencias")

raiz.geometry("650x600")

raiz.resizable(0,0)

#----------------------opcion 2-------------------

opcion2=Frame(raiz, width=800, height=800)
opcion2.pack()
opcion2.config()

Label(opcion2, text="DIGITE LA RESISTENCIA", fg="green", font=("Eras Bold ITC", 36)).grid(row=0, columnspan=4)

borrable=StringVar()
valor_resistencia=Entry(opcion2, font=(28), textvariable=borrable)
valor_resistencia.grid(row=1, columnspan=4, pady=80)
valor_resistencia.config()

resultado_calculo1=StringVar()
label1=Label(opcion2, textvariable=resultado_calculo1, font=("Eras Bold ITC", 20))
label1.grid(row=2, column=1, pady=20, sticky="e")

resultado_calculo2=StringVar()
label2=Label(opcion2, textvariable=resultado_calculo2, font=("Eras Bold ITC", 20))
label2.grid(row=3, column=1, pady=20, sticky="e")

resultado_calculo3=StringVar()
label3=Label(opcion2, textvariable=resultado_calculo3, font=("Eras Bold ITC", 20))
label3.grid(row=4, column=1, pady=20, sticky="e")

excepcion=StringVar()
label4=Label(opcion2, textvariable=excepcion, font=(12))
label4.grid(row=1, column=1, sticky="w")

def opcion_2():
    
    excepcion.set("")

    colores=["Negro", "Cafe", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]

    try:
        resistenciaa=valor_resistencia.get()

    except ValueError:
        excepcion.set("El valor \n ingresado \n no es logico")

    try:
        color1=int(resistenciaa[0])
        color2=int(resistenciaa[1])
        color3=len(resistenciaa)-2
        col4=colores[color3]

    except IndexError:
        excepcion.set("El valor \n ingresado \n no es logico")
    except ValueError:
        excepcion.set("El valor \n ingresado \n no es logico")
    
    try:
        col4=colores[color3]
        resultado_calculo1.set(colores[color1])    
        resultado_calculo2.set(colores[color2])   
        resultado_calculo3.set(col4)   
    except UnboundLocalError:
        excepcion.set("El valor \n ingresado \n no es logico")
    except ValueError:
        excepcion.set("El valor \n ingresado \n no es logico")

    if resultado_calculo1.get()=="Negro":
        label1.config(fg="black")
    elif resultado_calculo1.get()=="Cafe":
        label1.config(fg="brown")
    elif resultado_calculo1.get()=="Rojo":
        label1.config(fg="red")
    elif resultado_calculo1.get()=="Naranja":
        label1.config(fg="orange")
    elif resultado_calculo1.get()=="Amarillo":
        label1.config(fg="yellow")
    elif resultado_calculo1.get()=="Verde":
        label1.config(fg="green")
    elif resultado_calculo1.get()=="Azul":
        label1.config(fg="blue")
    elif resultado_calculo1.get()=="Violeta":
        label1.config(fg="purple")
    elif resultado_calculo1.get()=="Gris":
        label1.config(fg="gray")
    elif resultado_calculo1.get()=="Blanco":
        label1.config(fg="silver")

    if resultado_calculo2.get()=="Negro":
        label2.config(fg="black")
    elif resultado_calculo2.get()=="Cafe":
        label2.config(fg="brown")
    elif resultado_calculo2.get()=="Rojo":
        label2.config(fg="red")
    elif resultado_calculo2.get()=="Naranja":
        label2.config(fg="orange")
    elif resultado_calculo2.get()=="Amarillo":
        label2.config(fg="yellow")
    elif resultado_calculo2.get()=="Verde":
        label2.config(fg="green")
    elif resultado_calculo2.get()=="Azul":
        label2.config(fg="blue")
    elif resultado_calculo2.get()=="Violeta":
        label2.config(fg="purple")
    elif resultado_calculo2.get()=="Gris":
        label2.config(fg="gray")
    elif resultado_calculo2.get()=="Blanco":
        label2.config(fg="silver")

    if resultado_calculo3.get()=="Negro":
        label3.config(fg="black")
    elif resultado_calculo3.get()=="Cafe":
        label3.config(fg="brown")
    elif resultado_calculo3.get()=="Rojo":
        label3.config(fg="red")
    elif resultado_calculo3.get()=="Naranja":
        label3.config(fg="orange")
    elif resultado_calculo3.get()=="Amarillo":
        label3.config(fg="yellow")
    elif resultado_calculo3.get()=="Verde":
        label3.config(fg="green")
    elif resultado_calculo3.get()=="Azul":
        label3.config(fg="blue")
    elif resultado_calculo3.get()=="Violeta":
        label3.config(fg="purple")
    elif resultado_calculo3.get()=="Gris":
        label3.config(fg="gray")
    elif resultado_calculo2.get()=="Blanco":
        label2.config(fg="silver")


boton_calculo=Button(opcion2, text="Calcular", command=opcion_2, cursor="hand2")
boton_calculo.grid(row=1, column=3)
boton_calculo.config(font=("Eras Bold ITC",10))

#-----------------------------Opcion 1------------------------

opcion1=Frame(raiz, width=800, height=800)
opcion1.pack()
opcion1.config()

Label(opcion1, text="Elija los colores", fg="blue", font=("Eras Bold ITC", 36)).grid(row=0, columnspan=4)

var1=StringVar(opcion1)
var1.set("Color 1")

opciones1=["Negro", "Cafe", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]
opcionn1=OptionMenu(opcion1, var1, *opciones1)
opcionn1.grid(row=4, column=3, pady=20)
opcionn1.config(width=20, cursor="hand2", font=("Eras Bold ITC",10))

var2=StringVar(opcion1)
var2.set("Color 2")

opciones2=["Negro", "Cafe", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]
opcionn2=OptionMenu(opcion1, var2, *opciones2)
opcionn2.grid(row=5, column=3, pady=20)
opcionn2.config(width=20, cursor="hand2", font=("Eras Bold ITC",10))

var3=StringVar(opcion1)
var3.set("Color 3")

opciones3=["Negro", "Cafe", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]
opcionn3=OptionMenu(opcion1, var3, *opciones3)
opcionn3.grid(row=6, column=3, pady=20)
opcionn3.config(width=20, cursor="hand2", font=("Eras Bold ITC",10))

resultado1=StringVar()
resultado=Entry(opcion1, textvariable=resultado1, font=(28))
resultado.grid(row=8, columnspan=4, pady=70)
resultado.config(width=35)

def calculo_1():

    if var1.get()=="Negro":
        var1.set(0)
    elif var1.get()=="Cafe":
        var1.set(1)
    elif var1.get()=="Rojo":
        var1.set(2)
    elif var1.get()=="Naranja":
        var1.set(3)
    elif var1.get()=="Amarillo":
        var1.set(4)
    elif var1.get()=="Verde":
        var1.set(5)
    elif var1.get()=="Azul":
        var1.set(6)
    elif var1.get()=="Violeta":
        var1.set(7)
    elif var1.get()=="Gris":
        var1.set(8)
    elif var1.get()=="Blanco":
        var1.set(9)
    elif var1.get()=="Color 1":
        resultado1.set("Alguno de los valores no es valido")

    if var2.get()=="Negro":
        var2.set(0)
    elif var2.get()=="Cafe":
        var2.set(1)
    elif var2.get()=="Rojo":
        var2.set(2)
    elif var2.get()=="Naranja":
        var2.set(3)
    elif var2.get()=="Amarillo":
        var2.set(4)
    elif var2.get()=="Verde":
        var2.set(5)
    elif var2.get()=="Azul":
        var2.set(6)
    elif var2.get()=="Violeta":
        var2.set(7)
    elif var2.get()=="Gris":
        var2.set(8)
    elif var2.get()=="Blanco":
        var2.set(9)
    elif var2.get()=="Color 2":
        resultado1.set("Alguno de los valores no es valido")

    if var3.get()=="Negro":
        var3.set(0)
    elif var3.get()=="Cafe":
        var3.set(1)
    elif var3.get()=="Rojo":
        var3.set(2)
    elif var3.get()=="Naranja":
        var3.set(3)
    elif var3.get()=="Amarillo":
        var3.set(4)
    elif var3.get()=="Verde":
        var3.set(5)
    elif var3.get()=="Azul":
        var3.set(6)
    elif var3.get()=="Violeta":
        var3.set(7)
    elif var3.get()=="Gris":
        var3.set(8)
    elif var3.get()=="Blanco":
        var3.set(9)
    elif var3.get()=="Color 3":
        resultado1.set("Alguno de los valores no es valido")

    dosnum=str(var1.get()) + str(var2.get())
    col4=int(dosnum)*1*10**int(var3.get())

    resultado1.set("La resistencia es de " + str(col4) + " ohm")

    var1.set("Color 1")
    var2.set("Color 2")
    var3.set("Color 3")

botonCalcular=Button(opcion1, text="Calcular", command=calculo_1, cursor="hand2")
botonCalcular.grid(row=7, columnspan=4, pady=70)
botonCalcular.config(font=("Eras Bold ITC",10))

#-----------------------------Pagina de inicio-------------------------

inicio=Frame(raiz, width=800, height=800)
inicio.pack()
inicio.config()

textoInicio=Label(inicio, text="CALCULADORA DE \n RESISTENCIAS")
textoInicio.grid(row=1, columnspan=3, pady=20)
textoInicio.config(fg="red", font=("Eras Bold ITC", 36))

resis=PhotoImage(file="resistencia.gif")
label=Label(inicio, image=resis, width=200, height=200)
label.grid(row=3, columnspan=3)

#-----------------------------Boton avanzar a opciones----------------

opcion1.pack_forget()

def aparecer_1():

    inicio.pack_forget()
    opcion1.pack()
    resultado1.set("")

opcion2.pack_forget()

def aparecer_2():

    inicio.pack_forget()
    opcion2.pack()
    borrable.set("")
    resultado_calculo1.set("")    
    resultado_calculo2.set("")   
    resultado_calculo3.set("")     

botonOpcion1=Button(inicio, text="El valor segun \n los colores", command=aparecer_1, cursor="hand2")
botonOpcion1.grid(row=2, column=0, pady=50)
botonOpcion1.config(font=("Eras Bold ITC",14), bg="yellow")

botonOpcion2=Button(inicio, text="Los colores de la \n resistencia segun \n el valor", command=aparecer_2, cursor="hand2")
botonOpcion2.grid(row=2, column=2, pady=50)
botonOpcion2.config(font=("Eras Bold ITC",14), bg="yellow")

#------------------------Boton para regresar a pantalla de inicio----------

def regresar1():

    opcion1.pack_forget()
    inicio.pack()

botonRegresar1=Button(opcion1, text="Regresar", command=regresar1, cursor="hand2")
botonRegresar1.grid(row=8, column=5)
botonRegresar1.config(font=("Eras Bold ITC",10), fg="red")

def regresar2():

    opcion2.pack_forget()
    inicio.pack()

botonRegresar2=Button(opcion2, text="Regresar", command=regresar2, cursor="hand2")
botonRegresar2.grid(row=8, column=3)
botonRegresar2.config(font=("Eras Bold ITC",10), fg="red")

raiz.mainloop()