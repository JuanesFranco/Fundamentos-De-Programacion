# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:47:49 2021

@author: TORREX
"""
valor1=int(input("ingrese valor"))
valor2=int(input("ingrese valor"))
valor3=int(input("ingrese valor"))
    
def operacion(v1=2,v2=4,v3=5):
    print("el numero mayor es:")
    if v1>v2 and v1>v3:
        print(v1)
    else: 
        if v2>v1 and v2>v3:
            print(v2)
        else:
            if v3>v1 and v3>v2:
                print(v3)

operacion(valor1,valor2,valor3)





        
