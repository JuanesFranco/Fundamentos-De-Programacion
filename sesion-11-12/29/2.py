def cargar():
    lista=[]
    for x in range(11):
        valor=int(input("ingrese el valor"))
        lista.append(valor)
    return lista

def imprimir(lista):
    for x in range (len(lista)):
        print(lista[x],end="-")

lista=cargar()
imprimir(lista)

    
