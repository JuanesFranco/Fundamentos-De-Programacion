# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:33:23 2021

@author: TORREX
"""

lista=[10,20,30,40,345,1234,1235,60]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad+=1
    x=x+1

print("la lista contiene los valores",lista)
print("la cantidad de valores mayores a 100 son:",cantidad)
