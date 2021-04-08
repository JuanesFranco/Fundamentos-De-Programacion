def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("ingrese valor"))
        li.append(valor)
    return li

def retornar_mayormenor(li):
    may=li[0]
    men=li[0]
    for x in range (1,len(li)):
        if li[x]>may:
            may=li[x]
        else:
            if li[x]<men:
                men=li[x]
    return [men,may]

#bloque principal
lista=carga_lista()
rango=retornar_mayormenor(lista)
print("el menor elemento de la lista es",rango[0])
print("el mayor elemento de la lista es",rango[1])
                   
