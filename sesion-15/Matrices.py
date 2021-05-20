# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:52:44 2021

@author: TORREX
"""

import pandas

matriz=[[12,32,56,48],[8,48,18,58],[2,4,6,8]]
#imprecion de la matriz
print(matriz)
#imprimir una matriz determinada
print(matriz[0][2])
#imprecion de la fila 
print(matriz[0])
#Seleccion por teclado
fila=int(input("ingrese la fila"))
colum=int(input("ingrese la columna"))
print("posicion leida por teclado",matriz[fila][colum])
#Imprimir una columna
for f in range(3):
    print(matriz[f][1])
#Imprimir la columna deciada
col=int(input("columna"))
for f in range(3):
    print(matriz[f][col])
   
suma=0
#sumar todos los elementos de la lista 
for f in range(3):
    for c in range(4):
        suma+=matriz[f][c]
    print("la suma de los elementos es:",suma)
    suma=0
    