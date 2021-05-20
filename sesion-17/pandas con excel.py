# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:33:08 2021

@author: TORREX
"""

#Lectura de archivos tipo excel 
#Importar libreria 
import pandas as pd 
#Leer archivo 
archivoexcel =pd.read_excel("ventas.xlsx")
#Imprimir los datos 
archivoexcel.head() 
print(archivoexcel) 

