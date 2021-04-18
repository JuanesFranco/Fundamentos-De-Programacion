# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:41:28 2021

@author: TORREX
"""

lista=[]
for x in range(5):
    nombre=str(input("ingrese nombre"))
    lista.append(nombre)
    
names=lista[0]
for x in range(1,5):
    if lista[x]<names:
        name=lista[x]
print(lista)
print(names)