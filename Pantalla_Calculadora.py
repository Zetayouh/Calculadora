from tkinter import *

def mostrar_pantalla_top(self, valor, simbolo=""):
    if valor == "**2" or valor =="//2":
        self.num_top.set(self.numero_1 + valor + "=")
    elif valor == "1/x":
        self.num_top.set("1/" + self.numero_1 + "=")
    else:
        self.num_top.set(self.numero_1 + simbolo + valor)

def añade_numero_top(self, valor):
    self.num_top.set(self.num_top.get()+self.num_bot.get()+valor)

def actualiza_pantalla_top(self):
    if "." in self.resultado:
        self.resultado=filtra_resultado(self.resultado)

    self.num_top.set(self.resultado + self.operacion)

def borrar_pantalla_top(self):
    self.num_top.set("")

def mostrar_pantalla_bot(self, valor):
    self.num_bot.set(valor)

def añade_numero_bot(self, valor):
    self.num_bot.set(self.num_bot.get()+valor)

def borrar_pantalla_bot(self):
    self.num_bot.set("")

def borra_ultimo(self):
    self.num_bot.set(self.num_bot.get()[:-1])

def filtra_resultado(num): 
    num=str(round(float(num), 3))
    for n in num[-1]:
        if n == "0" or n==".":
            return num[:-2]
        else: 
            return num
            
