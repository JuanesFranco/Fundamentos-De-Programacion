# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:07:32 2021

@author: TORREX
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


archivoexcel =pd.read_excel("Tabla excel.xlsx")
archivoexcel.head()
df=pd.DataFrame(archivoexcel)
print(archivoexcel) 
print("")
departamento=df["Departamento"]
poblacion=df["Poblacion"]
superficie=df["Superficie"]
def areatotal():
    total=df["Superficie"].sum()
    print("La superficie total es:",total,"Km2")
    
areatotal()
def promedio_axd():
    totalp=df["Superficie"].sum()
    prom=totalp/len(departamento)
    print("El promedio de area por departamento es:","{:.2f}".format(prom))
promedio_axd()
def promedio_pxd():
    pbla=df["Poblacion"].sum()
    prom=pbla/len(departamento)
    print("El promedio de poblacion por departamento es:","{:.2f}".format(prom))
promedio_pxd()
def departamentomenor():
    menor=poblacion[0]
    for x in range(33):
        if poblacion[x]<menor:
            menor=poblacion[x]
            posicion=departamento[x]
    print("El departamento con menor poblacion es:",posicion,"con:",menor,"habitantes")
departamentomenor()
def departamentomayor():
    mayor=poblacion[0]
    for x in range(33):
        if poblacion[x]>mayor:
            mayor=poblacion[x]
            posicion=departamento[x]
    print("El departamento con mayor pobalcion es",posicion,"con:",mayor,"habitantes")
departamentomayor()
def relacion():
    suma=0
    suma2=0
    for x in range(33):
        suma+=superficie[x]
    for x in range(33):
        suma2+=poblacion[x]
    resultado=suma2/suma
    print("En Colombia hay","{:.1f}".format(resultado),"habitantes por Km2")
relacion()
def grafico_dxp():
    #GENERAR GRAFICO
    fig,ax=plt.subplots()
    ax.set_title("Departamento y Poblacion ")
    ax.set_ylabel("Departamento")
    ax.set_xlabel("Poblacion")
    plt.bar(departamento,poblacion)
    plt.show()
grafico_dxp()
def grafico_dxa():
     fig,ax=plt.subplots()
     ax.set_title("Departamento y Area ")
     ax.set_ylabel("Area")
     ax.set_xlabel("Superficie")
     plt.bar(departamento,superficie)
     plt.show()
grafico_dxa()
def horizontal_dxa():
    fig,ax=plt.subplots()
    ax.set_title("Departamento y Poblacion ")
    ax.set_ylabel("Departamento")
    ax.set_xlabel("Poblacion")
    plt.barh(departamento,poblacion)
    plt.show()
horizontal_dxa()
def hori_dxa():
    fig,ax=plt.subplots()
    ax.set_title("Departamento y Superficie ")
    ax.set_ylabel("Departamento")
    ax.set_xlabel("Area")
    plt.barh(departamento,superficie)
    plt.show()
hori_dxa()
def pie_dxp():
    fig,ax=plt.subplots()
    ax.set_title("Poblacion por Departamento ")
    plt.pie(poblacion, labels=departamento)
    plt.show()
pie_dxp()
def pie_dxa():
    fig,ax=plt.subplots()
    ax.set_title("Area por Departamento ")
    plt.pie(superficie, labels=departamento)
    plt.show()
pie_dxa()
