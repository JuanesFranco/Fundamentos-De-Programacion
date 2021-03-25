# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:36:08 2021

@author: TORREX
"""

cuadrado=0
acumulador=0

rango=int(input("ingrese la cantidad de numeros"))
for num in range(rango+1):
    cuadrado=num*num
    acumulador=acumulador+cuadrado
    print("el cuadrado de:",num,"es",cuadrado)
    print("la suma acumulada es:",acumulador)
    
print("la suma de los cuadrados es:",acumulador)    
