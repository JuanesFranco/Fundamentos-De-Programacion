# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:37:00 2021

@author: TORREX
"""

lista=[9,8,7,1,2,3,10]
contador=0
x=0

while x<len(lista):
    if lista[x]>=7:
        print("elemento mayor o igual a 7 de la lista:",lista[x])
        contador+=1
    x=x+1
print("la cantidad de elementos mayores o iguales a 7 son:",contador)