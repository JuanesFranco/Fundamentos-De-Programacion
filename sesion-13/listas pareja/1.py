# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:03:24 2021

@author: TORREX
"""

lista=[]
lista2=[]

for x in range(5):
    nombre=input("ingrese el nombre de la persona")
    lista.append(nombre)
    edad=int(input("ingrese edad"))
    lista2.append(edad)

for x in range(5):
    if lista2[x]>=18:
        print(lista[x])