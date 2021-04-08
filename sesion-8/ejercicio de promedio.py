# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:38:53 2021

@author: TORREX
"""

suma=0
med=0
cantEle=0
salida=False

while(salida==False):
    num=int(input("digite su edad"))
    if (num>0):
        suma=suma+num
        cantEle=cantEle+1
    else:
        salida=True 
    med=suma/cantEle
    print("el promedio es:",med)   
 
        

