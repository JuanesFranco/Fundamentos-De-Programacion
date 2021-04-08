def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("ingrese valor"))
        li.append(valor)
    return li

def imprimir_mayores10(li):
    print("elementos de la lista mayores a 10")
    for x in range (len(li)):
        if li[x]>10:
             print(li[x])


#bloque principal
lista=carga_lista()
print(lista)
imprimir_mayores10(lista)
