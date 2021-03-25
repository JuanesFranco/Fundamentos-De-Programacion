def sumaritar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
def mayor(lista):
    may=lista(0)
    for x in range(1,len(lista)):
                   if lista [x]>may:
                       may=lista[x]
    return may
def menor(lista):
    men=lista(0)
    for x in range(1,len(lista)):
        if lista [x]<men:
            men=lista[x]
        return men    
                   


#bloque principal
listavalores=(10,20,30,40,50)
print("lista completa")
print(listavalores)
print("la suma de todos sus elementos es:",sumaritar(listavalores))
