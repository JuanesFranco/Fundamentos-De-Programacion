# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:10:44 2021

@author: TORREX
"""

lista=[]

contador=0
for x in range(5):
    sueldo=int(input("ingrese sueldo"))
    lista.append(sueldo)
    contador+=sueldo

promedio=contador/5
print("el total de salarios es:",contador)
print("el promedio es:",promedio)
print(lista)
    