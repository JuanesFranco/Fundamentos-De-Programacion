# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:11:29 2021

@author: TORREX
"""
#Librerias
import matplotlib
import matplotlib.pyplot as plt

#GENERAR DATOS
#INTERACTUAR CON LISTAS

producto=["arroz","azucar","leche","huevos"]
ventas=[100,50,30,20]

#FUNCIONES DE LAS PREGUNTAS
def totalventas():
    suma=0
    for x in range(4):
        suma+=ventas[x]
    return(suma)

def promedioventas():
    promedio=0
    promedio=totalventas()/len(ventas)
    return(promedio)
totalventas()
print("el total de ventas es:",totalventas())
promedioventas()
print("el promedio de ventas es:",promedioventas())



#GENERAR GRAFICO
fig, ax=plt.subplots()
ax.set_title("VENTAS DE LA EMPRESA")
ax.set_ylabel("valor")
ax.set_xlabel("Producto")

#CREAR GRAFICO 

#Construyo
plt.bar (producto,ventas)
#Muestro
plt.show()

