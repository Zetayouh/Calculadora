from tkinter import *

from Operaciones_Calculadora import*

def construir_botones(botones, filas, columnas):
    contador=0
    for fila in range(2, filas+2):
        for columna in range(columnas):
            botones[contador].grid(row=fila, column=columna)
            contador+=1
    
def colocar_boton(self, valor, es_numero=True, op=True, ancho=8, alto=2):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9), command=lambda:pulsaciones_teclas(self, valor, es_numero, op))