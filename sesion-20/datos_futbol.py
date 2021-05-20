# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:49:12 2021

@author: TORREX
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

archivoexcel =pd.read_excel("Futbol_Partidos.xlsx")
archivoexcel.head()
df=pd.DataFrame(archivoexcel)
df_archivoExcel = df_archivoExcel[:10].copy()
print(archivoexcel) 