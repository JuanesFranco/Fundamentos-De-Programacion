# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:07:30 2021

@author: TORREX
"""
import pandas as pd 

df_archivoExcel=pd.read_excel('ventas_productos_1.xlsx',index_col="Producto")
df_archivoExcel=df_archivoExcel[:10].copy()
print(df_archivoExcel)

#Grafica vertical
df_archivoExcel.plot(kind="bar")
#Grafica horizontal 
df_archivoExcel.plot(kind="barh")
#Vertical ocupando todo el espacio
df_archivoExcel.plot(kind="barh",width=1)
#Grosor de las columnas (width)
df_archivoExcel.plot(kind="barh",width=2)
# Gráfica Apilada
df_archivoExcel.plot(kind = 'bar', 
                     stacked = 'True',          # Muestra las barras apiladas
                     alpha = 0.4,               # nivel de transparencia
                     width = 0.9,               # Grosor de las barras para dejar espacio entre ellas
                     figsize=(9,4));   



































