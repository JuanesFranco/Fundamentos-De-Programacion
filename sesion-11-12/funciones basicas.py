# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:28:02 2021

@author: TORREX
"""
import math
   

def titulo():
    print("calculo de la hipotenuza de un triangulo rectangulo")

def calcularhipotenuza(p_cateto,p_catetodos):
#programa que calcula la hipotenuza y el area de un triangulo 
   
    #entradas 
    
    #proceso
    
    vps_radicando= math.sqrt(math.pow(p_cateto,2)+math.pow(p_catetodos,2))
    vps_hipotenusa=math.sqrt(vps_radicando)
    
    return vps_hipotenusa
    #salidas
def despedida():
    print("gracias por usar este programa, Adios ")
    
    
#fin del desarrollo de la hipotenuza   
titulo()
ve_cateto=int(input("digite cateto uno"))
ve_catetodos=int(input("digite cateto dos"))
hip=calcularhipotenuza(ve_cateto,ve_catetodos)       
print("la hipotenusa es:",hip)       
despedida()        
                            
