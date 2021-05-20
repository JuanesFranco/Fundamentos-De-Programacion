# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:44:56 2021

@author: TORREX
"""
#LIBRERIA PANDAS 

#instalacion por si ocurren problemas
#anaconda prompt 
#condalist
#conda install pandas 

import pandas as pd 
notas=pd.DataFrame ({"estudiante":["Carlos","Andres"],"nota parcial":[3.8,4.7],
                     "edad":[17,20]})
print(notas)
