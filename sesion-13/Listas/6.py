# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:43:42 2021

@author: TORREX
"""

lista=["juan","santiago","lau","strella","daniel"]
cantidad=0
x=0
while x<len(lista):
    if len(lista[x])>=5:
        cantidad+=1
        print(lista[x])
    x=x+1
print("la cantidad de nombre con caracteres mayores o iguales a 5 es:",cantidad)