# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:40:23 2021

@author: TORREX
"""
#Contadores
masculino_82202119045=0
femenino_82202119045=0
horastrabajadas_82202119045=0
pagomenorresultado_82202119045=0
pagomayorresultado_82202119045=0
totalpagomenor_82202119045=0
totalpagomayor_82202119045=0
seccion1_82202119045=0
seccion2_82202119045=0
seccion3_82202119045=0
efectivo_82202119045=0
x=1
#Ciclo
n_82202119045=int(input("ingrese la cantidad de trabajadores a evaluar"))
while x<=n_82202119045:
    nombre_82202119045=str(input("ingrese nombre de empleado"))
    genero_82202119045=int(input("ingrese 1 si es masculino o 2 si es femenino*:"))
    if genero_82202119045==1:
        masculino_82202119045+=1
    else:
        if genero_82202119045==2:
            femenino_82202119045+=1
    seccion_82202119045=int(input("ingrese en que seccion trabaja(1,2 o 3)"))
    if seccion_82202119045==1:
        seccion1_82202119045=seccion1_82202119045+1
    else :
        if seccion_82202119045==2:
            seccion2_82202119045+=1
        else:
            if seccion_82202119045==3:
                seccion3_82202119045+=1    
    #horas de trabajo            
    horastrabajadas_82202119045=int(input("ingrese el total de horas trabajadas"))
    #Tarifa por hora
    tarifa_82202119045=int(input("ingrese la tarifa por hora"))
    #si horas < a 35
    if horastrabajadas_82202119045<35:
        totalpagomenor_82202119045=horastrabajadas_82202119045*tarifa_82202119045
        pagomenorresultado_82202119045+=totalpagomenor_82202119045
    #si horas > 35
    else:
        if horastrabajadas_82202119045>35:
            totalpagomayor_82202119045=(horastrabajadas_82202119045*tarifa_82202119045)*1.5
            pagomayorresultado_82202119045+=totalpagomayor_82202119045
    if horastrabajadas_82202119045<35:
        #impuestos a deducir
        impuestos_82202119045=totalpagomenor_82202119045*0.165
        #salario final
        impuestos2_82202119045=totalpagomenor_82202119045-impuestos_82202119045
        efectivo_82202119045+=impuestos2_82202119045
    else:
        impuestos3_82202119045=totalpagomayor_82202119045*0.165
        #salario final
        impuestos4_82202119045=totalpagomayor_82202119045-impuestos3_82202119045
        efectivo_82202119045+=impuestos4_82202119045
    x=x+1
    #Salidas de los daos de los empleados
    #si las horas trabajadas son < 35
    if horastrabajadas_82202119045<35:
        print("**********Datos Empleado**********")
        if genero_82202119045==1:
            print("Genero: Masculino")
        else:
            print("Genero: Femenino")
        print("Nombre:",nombre_82202119045)
        
        print("Seccion:",seccion_82202119045)
        print("Total horas trabajadas:",horastrabajadas_82202119045)
        print("salario resultante:",impuestos2_82202119045)
    #Si las horas trabajadas son > a 35    
    else:
         print("**********Datos Empleado**********")
         print("Nombre:",nombre_82202119045)
         if genero_82202119045==1:
            print("Genero: Masculino")
         else:
             print("Genero: Femenino")
         print("Nombre:",nombre_82202119045)
         print("Seccion:",seccion_82202119045)
         print("Total horas trabajadas:",horastrabajadas_82202119045)
         print("salario resultante:",impuestos4_82202119045)

#Salidas datos de la empresa
print("**********Datos empresa**********")
print("el total de empleados masculinos son:",masculino_82202119045)
print("el total de empleados femeninos son:",femenino_82202119045)
print("el total de empleados en la seccion 1 son:",seccion_82202119045)
print("el total de empleados en la seccion 2 son:",seccion2_82202119045)
print("el total de empleados en la seccion 3 son:",seccion3_82202119045)
print("el total de gastos de la empresa en salarios es de:",efectivo_82202119045)



        
        
    
    
    
    
        
        
    
        
    
        