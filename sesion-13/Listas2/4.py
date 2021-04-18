# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:18:51 2021

@author: TORREX
"""

lista=[]

contador=0
mayor=0
menor=0
for x in range(5):
    altura=float(input("ingrese estatura"))
    lista.append(altura)
    contador+=altura

promedio=contador/5
for x in range(5):
    if lista[x]>promedio:
        mayor+=1
    else:
        if lista[x]<promedio:
            menor+=1
print(lista)
print("el promedio es:",promedio)
print("cantidad de personas mayores que el promedio:",mayor)
print("cantidad de personas menores que el promedio:",menor)
