# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:49:45 2021

@author: TORREX
"""

lista=[]

for x in range(5):
    numero=int(input("ingrese valor"))
    lista.append(numero)

listamayor=lista[0]
for x in range(1,5):
    if lista[x]>listamayor:
        listamayor=lista[x]
cantidad=0
for x in range(5):
    if lista[x]==listamayor:
        cantidad+=1
if cantidad>=1:
  print("el valor mayor esta repetido")
    
print(lista)
print(listamayor)
