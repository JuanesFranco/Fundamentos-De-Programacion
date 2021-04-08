# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:04:33 2021

@author: TORREX
"""

n=int(input("ingrese el numero de estudiantes"))
#variables
contadorRepeteciones = 0
cantidadEstudiantesAprobaron=0
cantidadEstudiantesReprobaron=0
sumaDefinitivaEstudiantes=0.0
sumaDefinitivaEstudiantesAprobaron=0.0
sumaDefinitivaEstudiantesReprobaron=0.0
promedioDefinitivaEstudiantes=0.0
promedioDefinitivaEstudiantesAprobaron=0.0
promedioDefinitivaEstudiantesReprobaron=0.0
#proceso
for x in range(n):
    nombre=input("digite el nombre del estudiante")
    nota1=float(input("ingrese nota1"))
    nota2=float(input("ingrese nota2"))
    nota3=float(input("ingrese nota3"))
    definitiva=(nota1+nota2+nota3)/3 
    print("la definitiva es de:",definitiva)
    
    
    if definitiva>=3.0:
        cantidadEstudiantesAprobaron=cantidadEstudiantesAprobaron+1
        sumaDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron+definitiva
        print("la suma definitiva es",sumaDefinitivaEstudiantesAprobaron)
    else:
        cantidadEstudiantesReprobaron=cantidadEstudiantesReprobaron+1
        sumaDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron+definitiva
    contadorRepeteciones=contadorRepeteciones+1
#calcular el promedio del grupo 
promedioDefinitivaEstudiantes=sumaDefinitivaEstudiantes/n  
if (cantidadEstudiantesAprobaron>0):
    promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron/cantidadEstudiantesAprobaron 
if (cantidadEstudiantesReprobaron>0):
    promedioDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron/cantidadEstudiantesReprobaron 
    
if definitiva>3.0:
    print("la nota mayor es de",nombre)    
   

    
print("OTROS CALCULOS")
print("2.  Cantidad de estudiantes que aprobaron : ", cantidadEstudiantesAprobaron)
print("3.  Cantidad de estudiantes que reprobaron : ", cantidadEstudiantesReprobaron)
print(f"4.  Promedio del grupo : {promedioDefinitivaEstudiantes:.2f}")
print("5.  Promedio de estudiantes que aprobaron : ", promedioDefinitivaEstudiantesAprobaron)
print(f"6.  Promedio de estudiantes que reprobaron :{promedioDefinitivaEstudiantesReprobaron:.1f} ")       
    

if definitiva<3.0:
    print("la nota menor es",nombre)
if definitiva>3.0:
   print("la nota mayor es de",nombre)    
      
        
    
    
    

        