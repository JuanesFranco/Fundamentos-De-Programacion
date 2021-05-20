# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:03:05 2021

@author: TORREX
"""

import random


print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
lista = [random.randint(0,1000) for _ in range(n)]
print(lista)

def ordburbuja(lista):
 
    for dato in range(len(lista)-1,0,-1):
 
        for i in range(dato):
 
            if lista[i]>lista[i+1]:
 
                temp = lista[i]
 
                lista[i] = lista[i+1]
 
                lista[i+1] = temp
 
 
 
ordburbuja(lista)
 
print(lista)
