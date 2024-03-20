from tkinter import *

from Funciones_Matematicas import *
from Pantalla_Calculadora import *

def pulsaciones_teclas(self, valor, es_numero, op):

    if self.num_bot.get() == "No se puede dividir entre 0":
            reestablece(self)

    if es_numero:
        if self.igualado:
            reestablece(self)

        if valor == "0" and self.num_bot.get() == "0":
            pass

        elif valor == "." and (self.num_bot.get() == "" or "." in self.num_bot.get()):
            pass

        elif self.num_bot.get():
            añade_numero_bot(self, valor)

        else:
            mostrar_pantalla_bot(self, valor)

        self.operacion_en_curso = False

    elif valor == "+/-":
        mostrar_pantalla_bot(self, filtra_resultado(invierteSigno(self.num_bot.get())))

    else:
        self.num_bot.set(filtra_resultado(float(self.num_bot.get())))

        if op and self.operacion_en_curso == False:
            
            if valor == "**2" or valor == "//2" or valor == "1/x":

                if self.num_top.get() == "" or "=" in self.num_top.get():
                    self.numero_1 = self.num_bot.get()
                
                else:
                    self.numero_2 = str(self.num_bot.get())
                    self.numero_1 = ejecuta_operacion(self)
                
                self.operacion = valor
                mostrar_pantalla_top(self, valor)
                mostrar_pantalla_bot(self, ejecuta_operacion(self))
                self.igualado = True

            elif self.operacion != "":

                if self.igualado == True:
                    self.numero_1 = self.num_bot.get()
                    mostrar_pantalla_top(self, valor)
                    borrar_pantalla_bot(self)

                else:
                    self.numero_2 = str(self.num_bot.get())
                    resultado = ejecuta_operacion(self)

                    if self.operacion == "/" and resultado == "0":
                        self.num_top.set(self.numero_1 + "/" + "0")
                        mostrar_pantalla_bot(self, "No se puede dividir entre 0")
                        
                    else:
                        self.numero_1 = str(ejecuta_operacion(self))
                        borrar_pantalla_bot(self)
                        mostrar_pantalla_top(self, valor)

                self.igualado = False
                self.operacion_en_curso = True

            else:
                self.numero_1 = self.num_bot.get()
                mostrar_pantalla_top(self, valor)
                borrar_pantalla_bot(self)
                self.igualado = False
                self.operacion_en_curso = True

            self.operacion = valor
            
        elif not op:

            if valor == "CE":
                borrar_pantalla_bot(self)
                self.operacion_en_curso = True

            elif valor == "<-":
                borra_ultimo(self)
                if self.num_bot.get() == "":
                     self.operacion_en_curso = True

            elif valor == "C":
                reestablece(self)

    if valor == "=" and self.operacion_en_curso == False and self.num_top.get() != "":
        print(self.num_top.get())

        if "=" not in self.num_top.get():
            self.numero_2 = str(self.num_bot.get())
            añade_numero_top(self, valor)
            resultado = ejecuta_operacion(self)

            if self.operacion == "/" and resultado == "0":
                mostrar_pantalla_bot(self, "No se puede dividir entre 0")
                
            else:    
                mostrar_pantalla_bot(self, ejecuta_operacion(self))
                self.igualado = True

        else:
            self.numero_1 = str(self.num_bot.get())
            mostrar_pantalla_top(self, self.numero_2+"=", self.operacion)
            mostrar_pantalla_bot(self, ejecuta_operacion(self))

def ejecuta_operacion(self):

    if self.operacion == "%":
        return filtra_resultado(porcentaje(float(self.numero_1), float(self.numero_2)))
    
    elif self.operacion == "1/x":
        return filtra_resultado(fraccion(float(self.numero_1)))

    elif self.operacion == "**2":
        return filtra_resultado(cuadrado(float(self.numero_1)))

    elif self.operacion == "//2":
        return filtra_resultado(raiz_cuadrada(float(self.numero_1)))

    elif self.operacion == "/":
        return filtra_resultado(divide(float(self.numero_1), float(self.numero_2)))

    elif self.operacion == "x":
        return filtra_resultado(multiplica(float(self.numero_1), float(self.numero_2)))

    elif self.operacion == "-":
        return filtra_resultado(resta(float(self.numero_1), float(self.numero_2)))

    elif self.operacion == "+":
        return filtra_resultado(suma(float(self.numero_1), float(self.numero_2)))

def reestablece(self):
    self.numero_1 = ""
    self.numero_2 = ""
    self.num_top.set("")
    self.num_bot.set("")
    self.operacion = ""
    self.operacion_en_curso = False
    self.igualado = False