# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:22:37 2021

@author: TORREX
"""
matriz1=[]
filas=int(input("ingrese el numero de columnas"))
print("Fila 1")
for x in range(filas):
    datos=int(input("ingrese datos"))
    matriz1.append(datos)
matriz2=[]
print("Fila 2")
for x in range(filas):
    datos=int(input("ingrese datos"))
    matriz2.append(datos)
matriz3=[]
print("Fila 3")
for x in range(filas):
    datos=int(input("ingrese datos"))
    matriz3.append(datos)
    
matriz=[matriz1,matriz2,matriz3]
print(matriz)

suma=0
for f in range(3):
    for c in range(filas):
        suma+=matriz[f][c]
    print("la suma de la fila es:",suma)
    suma=0