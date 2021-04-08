# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:21:17 2021

@author: TORREX
"""

import math

#FORMULA DE HERON 

#Entradas

#lado1
lado1_82202119045=int(input("ingrese el lado1"))
#lado2
lado2_82202119045=int(input("ingrese el lado2"))
#lado3
lado3_82202119045=int(input("ingrese el lado3"))

#PROCESO

#semiperimetro
s_82202119045=(lado1_82202119045+lado2_82202119045+lado3_82202119045)/2
#area
area_82202119045=math.sqrt(s_82202119045*(s_82202119045-lado1_82202119045)*(s_82202119045-lado2_82202119045)*(s_82202119045-lado2_82202119045))
#Perimetro
perimetro_82202119045=lado1_82202119045+lado2_82202119045+lado3_82202119045
#SALIDAS
print("el area del triangulo con la formula de Heron es:",area_82202119045)
print("el perimetro del triangulo es:",perimetro_82202119045)





