# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:44:26 2021

@author: TORREX
"""

lista=[]
for x in range(5):
    valor=int(input("ingrese valor"))
    lista.append(valor)
mayor=0
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print(lista)
print("el mayor de la lista es:",mayor)
