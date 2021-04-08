# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:02:32 2021

@author: TORREX
"""

import random 
contador=0
numero=0
acumuladortodos=0
acumuladorpositivos=0
acumuladornegativos=0
cantidad=int(input("ingrese la cantidad de numeros"))
for i in range(cantidad):
    numero=random.randint(-100,100)
    print("numero:",numero)
    acumuladortodos=acumuladortodos+numero
    if numero>0:
        acumuladorpositivos=acumuladorpositivos+numero
    else:
        acumuladorsumanegativos=acumuladornegativos+numero
    contador=contador+1
print("la suma de todos los numeros es:",acumuladortodos)
print("la suma de los numeros positivos es:",acumuladorpositivos)  
print("la suma de los numeros negativos es:",acumuladorsumanegativos)  