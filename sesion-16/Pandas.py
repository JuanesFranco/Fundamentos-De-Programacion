# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:23:34 2021

@author: TORREX
"""

#Interactusr con datos 
#fUENTES DE DATOS 
#Asignar los datos desde la definicion de la estructura 

#Importar la libreria 
import pandas as pd 
#crear la estructura de datos tipo dataframe y se le asignan los datos 
datosestudiantes=pd.DataFrame({"Estudiante":["Juan","Andres","Marta"],"Edad":[15,12,9]})

#Agragra una columna 
datosestudiantes["Vivo"]="TRUE"
datosestudiantes["Genero"]="Masculino"

#Insertar una columna y se asignan los datos
datosestudiantes.insert(3,"Semestre",["Primero","quinto","Noveno"])
datosestudiantes.insert(2,"Genero correcto",["Masculino","Femenino","Femenino"])

#Consultar la estructura
print(datosestudiantes)




#SEGUNDA FORMA SOBREESCRIBIENDO
datosestudiantes=datosestudiantes.assign(Colegio=["Nuestra señora","Filipense","San Luis"])
