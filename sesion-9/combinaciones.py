# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:27:23 2021

@author: TORREX
"""
#Calculo de la combinatoria 
fact_m=1
fact_n=1
fact_mn=1
m=int(input("ingrese el vaor de m"))
n=int(input("ingrese el vaor de n"))

      
#CALCULAR EL FACTORIAL DE M
for i in range (1,m+1,1):
    fact_m=fact_m*i
    
    

#CALCULAR EL FACTORIAL DE N
vp_conwhile=1
while(vp_conwhile<n):
    fact_n=fact_n*vp_conwhile
    vp_conwhile=vp_conwhile+1


#CALCULAR EL FACTORIAL DE M-N
difmn=m-n
for j in range (1,difmn+1,1):
    fact_mn=fact_mn*j
    
#combinatoria 
combi_mn=fact_m/(fact_n*fact_mn)
#salidas
print("factorial de m",fact_m)
print("factorial de n",fact_n)
print("la combinatoria de mn",fact_mn)
    


