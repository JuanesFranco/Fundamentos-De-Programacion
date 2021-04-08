# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:17:35 2021

@author: TORREX
"""

result=1
i=0
j=0
for i in range(1,10+1):
    for j in range(i):
        result=j*i
        print('',i,"x",j,"=",result)
        print("")
        j=j+1
    print("##########")
    print("")
    i=i+1