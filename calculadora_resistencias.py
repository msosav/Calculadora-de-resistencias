#-----------------------------opcion 1----------------

def resistencia_valor():

    colores=["Negro", "Cafe", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]

    while True:
        resistencia=input("Resistencia en ohm: ")

        try:
            color1=int(resistencia[0])
            color2=int(resistencia[1])
            color3=len(resistencia)-2
            color4=colores[color3]

            break
        except ValueError:
            print("El valor ingresado es incorrecto")
        except IndexError:
            print("El valor ingresado no es logico")


    print("La primera banda es de color " + colores[color1])
    print("La segunda banda es de color " + colores[color2])
    print("La tercera banda es de color " + color4)

#-------------------------------------opcion 2-------------------------

def resistencia_color():

    colores1={"negro":0, "cafe":1, "rojo":2, "naranja":3, "naranjado":3, "amarillo":4, "verde":5, "azul":6, "violeta":7, "morado":7, "gris":8, "blanco":9}

    while True:
        try:
            col1=input("Digite el primer color ").lower()
            col2=input("Digite el segundo color ").lower()
            col3=input("Digite el tercer color ").lower()

            dosnum=str(colores1[col1]) + str(colores1[col2])
            col4=int(dosnum)*1*10**colores1[col3]

            break
        except KeyError:
            print("Alguno de los datos ingresados es erroneo, por favor intentelo de nuevo")


    print("La resistencia es de " + str(col4) + " ohm")

#----------------------------------inicio?----------------

print("Este programa dice los colores de la resistencia segun el valor (opcion 1) o el valor segun los colores (opcion 2)")

while True:
    while True:
        try:
            opcion=int(input("Que opcion desea? "))

            break
        except NameError:
            print("Esa no es una opcion, vuelva a intentarlo")
        except ValueError:
            print("Esa no es una opcion, vuelva a intentarlo")

    if (opcion==1):
        resistencia_valor()
    else:
        if (opcion==2):
            resistencia_color()
        else:
            print("Esa no es una opcion, vuelva a intentarlo")