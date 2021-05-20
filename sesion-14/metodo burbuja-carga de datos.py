# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:35:14 2021

@author: TORREX
"""
lista=[]
def cargardatos (lista):
    print("carga de datos")
    for x in range(10):
        valor=int(input("ingrese los valores"))
        lista.append(valor)
    print(lista)

def burbuja (listaordenada):
    print("datos ordenados")
    for x in range (1,len(listaordenada)-1):
        for i in range(0,len(listaordenada)-1):
            if listaordenada[i]>listaordenada[i+1]:
                aux=listaordenada[i]
                listaordenada[i]=listaordenada[i+1]
                listaordenada[i+1]=aux
    print(lista)                    

cargardatos(lista)
burbuja(lista)
