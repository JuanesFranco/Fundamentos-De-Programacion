#import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	#os.system('clS1') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Almacenar las notas en la lista")
	print ("\t2 - Sumar los elementos de la lista")
	print ("\t3 - Calcular el promedio")
    print ("\t4 - Imprimir el mayor y su posicion")
    print ("\t5 - Imprimir el menor y su posicion")
    print ("\t4 - Imprimir cuantos aprobaron")
    print ("\t4 - Imprimir cuantos reprobaron")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("Almacenar las notas en la lista")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("Sumar los elementos de la lista")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("Calcular el promedio")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu=="4":
		print ("Imprimir el mayor y su posicion")
		input("Has pulsado la opción 4...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")