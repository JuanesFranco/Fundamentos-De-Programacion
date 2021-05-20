# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:06:44 2021

@author: TORREX
"""

import random 

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	
	print ("\nSelecciona una opción")
	print ("\t1 - Almacenar datos"),print ("\t2 - Ordenamiento burbuja"),print ("\t3 - Ordenamiento incersion")
	print("\t4 - Ordenamiento shell"),print("\t5 - Salir")
	
lista=[]  

def cargardatos (lista):
    print("carga de datos")
    for x in range(10):
        valor=int(input("ingrese los valores"))
        lista.append(valor)
    print(lista)


def burbuja (listaordenada):
    print("datos ordenados")
    for x in range (1,len(listaordenada)-1):
        for i in range(0,len(listaordenada)-1):
            if listaordenada[i]>listaordenada[i+1]:
                aux=listaordenada[i]
                listaordenada[i]=listaordenada[i+1]
                listaordenada[i+1]=aux
    print(listaordenada)  
                  
def insercion(arr):
  
    
    for i in range(1, len(arr)):
  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def ord_shell(lista):
    n=len(lista)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lista[i]
            j = i
            while j >= interval and lista[j - interval] > temp:
                lista[j] = lista[j - interval]
                j -= interval

            lista[j] = temp
        interval //= 2
    print(lista)

    
while True:
    menu()
    opcion=int(input("Ingrese una opcion segun el menu"))
    if opcion==1:
        print("lista desordenada")
        cargardatos(lista)
        input("Has pulsado la opción 1...\npulsa enter para continuar")
    if opcion==2:  
        print(burbuja(lista))  
       
        input("Has pulsado la opción 2...\npulsa enter para continuar")
        
    if opcion==3:
        print(insercion(lista))
                
        input("Has pulsado la opción 3...\npulsa enter para continuar")
    if opcion==4:
        print(ord_shell(lista))
        input("Has pulsado la opción 4...\npulsa enter para continuar")
   
    elif opcion==5:
        break
    elif opcion<1 or opcion>5:
    	print ("")
    	input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

