# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:03:21 2021

@author: TORREX
"""

lista=[]
valor=int(input("ingrese valor(0 para finalizar)"))
while valor!=0:
    lista.append(valor)
    valor=int(input("ingrese valor(0 para finalizar)"))
    
print(lista)
print(len(lista)