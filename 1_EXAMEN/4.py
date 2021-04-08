# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:29:49 2021

@author: TORREX
"""
z_82202119045=int(input("ingrese la cantidad de numeros a realizar"))
def fibonazi_82202119045(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fibonazi_82202119045(n-1) + fibonazi_82202119045(n-2)

for x in range(z_82202119045):
    print(fibonazi_82202119045(x))
    