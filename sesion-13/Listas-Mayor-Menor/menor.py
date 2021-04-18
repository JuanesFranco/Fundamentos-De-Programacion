# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:08:03 2021

@author: TORREX
"""

lista=[]
for x in range(5):
    valor=int(input("ingrese valor"))
    lista.append(valor)
menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x
print("lista completa",lista)
print("el menor de la lista",menor)
print("posicion del menor",posicion)

    