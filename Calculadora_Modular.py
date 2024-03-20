from tkinter import *

from Botonera_Calculadora import colocar_boton, construir_botones
from Operaciones_Calculadora import *
from Pantalla_Calculadora import *


root=Tk()

class Calculadora:
    def __init__(self, ventana):

        self.ventana=ventana
        self.ventana.title("Calculadora")
        self.ventana.iconbitmap(r"C:\Users\hegoi\Desktop\proyectos_py\Curso_Tutorizado\Practica_Calculadora\calculadora.ico")
        self.numero_1 = ""
        self.numero_2 = ""
        self.num_top = StringVar()
        self.num_bot = StringVar()
        self.operacion = ""
        self.operacion_en_curso = False
        self.igualado = False

        #Agregar display

        display_top=Label(ventana, textvariable=self.num_top, font=("Arial 16"), width=22, bd=2, relief="ridge")
        display_bot=Label(ventana, textvariable=self.num_bot, font=("Arial 16"), width=22, bd=2, relief="ridge")

        #Ubicar display

        display_top.grid(row=0, column=0, columnspan=4)
        display_top.config(background="black", fg="white", anchor="e")
        display_bot.grid(row=1, column=0, columnspan=4, sticky="e")
        display_bot.config(background="black", fg="white", anchor="e")

        #Creacion de botones----fila1-----

        botonPorcent=colocar_boton(self, "%", es_numero=False)
        botonBorraActual=colocar_boton(self, "CE", es_numero=False, op=False)
        botonBorraTodo=colocar_boton(self, "C", es_numero=False, op=False)
        botonBorraUltimo=colocar_boton(self, "<-", es_numero=False, op=False)

        #------------------------fila2-----

        botonFraccion=colocar_boton(self, "1/x", es_numero=False)
        botonCuadrado=colocar_boton(self, "**2", es_numero=False)
        botonRaizCuadrada=colocar_boton(self, "//2", es_numero=False)
        botonDivision=colocar_boton(self, "/", es_numero=False)

        #------------------------fila3-----

        boton7=colocar_boton(self, "7")
        boton8=colocar_boton(self, "8")
        boton9=colocar_boton(self, "9")
        botonMultiplica=colocar_boton(self, "x", es_numero=False)

        #------------------------fila4-----

        boton4=colocar_boton(self, "4")
        boton5=colocar_boton(self, "5")
        boton6=colocar_boton(self, "6")
        botonResta=colocar_boton(self, "-", es_numero=False)

        #------------------------fila5-----

        boton1=colocar_boton(self, "1")
        boton2=colocar_boton(self, "2")
        boton3=colocar_boton(self, "3")
        botonSuma=colocar_boton(self, "+", es_numero=False)

        #------------------------fila6-----

        botonInvierte=colocar_boton(self, "+/-", es_numero=False, op=False)
        boton0=colocar_boton(self, "0")
        botonComa=colocar_boton(self, ".")
        botonIgual=colocar_boton(self, "=", es_numero=False, op=False)

        #--------------------------------

        botones=[botonPorcent,  botonBorraActual, botonBorraTodo, botonBorraUltimo, botonFraccion, botonCuadrado, botonRaizCuadrada, botonDivision, boton7, boton8, 
                 boton9, botonMultiplica, boton4, boton5, boton6, botonResta, boton1, boton2, boton3, botonSuma, botonInvierte, boton0, botonComa, botonIgual]
        
        construir_botones(botones, 6, 4)


mi_calculadora=Calculadora(root)

root.mainloop()    