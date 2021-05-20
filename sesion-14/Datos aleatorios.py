# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:24:37 2021

@author: TORREX
"""

import random


print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
lista2 = [random.randint(0,1000) for _ in range(n)]
print(lista2)

