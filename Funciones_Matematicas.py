import math

def porcentaje(base, porcentaje):
    return base*(porcentaje/100)

def fraccion(num):
    return 1/num

def cuadrado(num):
    return num*num

def raiz_cuadrada(num):
    return math.sqrt(num)

def divide(base, divisor):
    if divisor != 0:
        return base/divisor  
    else:
        return "0"

def multiplica(num1, num2):
    return num1*num2

def resta(num1, num2):
    return num1-num2

def suma(num1, num2):
    return num1+num2

def invierteSigno(num):
    return(-float(num))

