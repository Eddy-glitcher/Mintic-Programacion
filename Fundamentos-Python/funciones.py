# print() = Imprime por consola
# int() = define un valor entero
# type() = imprime el tipo de valor
# round() = redondea numero con decimal o
# establece numero máximo de decimales
# max() = selecciona mayor valor de lista
# min() = selecciona menor valor de lista
# help(max) # ayuda sobre palabra reservada



# sum() = suma un rango de valores
# range() = establece un rango
# return() = devuelve argumentos

import math

def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1: "))
    num2 = float(input("Ingrese el numero 2: "))
    print("la suma de", int(num1), " + ", int(num2), " es igual a: ", int(num1 + num2))
    
    
sumarDosnumeros()

def primerNumero(x):
    def segundoNumero(y):
        return x * y
    return segundoNumero
resultado = primerNumero(2)
print(resultado(5))