def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("elvalor mayor de la lista es:",may)
    print("elvalor menor de la lista es:",men)

#bloque principal
lista=[]
for x in range (5):
    valor=int(input("ingrese valor"))
    lista.append(valor)
mayormenor(lista)
