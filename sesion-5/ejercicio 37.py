suma1=0
suma2=0
x=1
print("carga de la primera lista")
while x<=15:
    valor=int(input("ingrese valor"))
    suma1=suma1+valor
    x=x+1
x=1
print("carga de la segunda lista")
while x<=15:
    valor=int(input("ingrese valor"))
    suma2=suma2+valor
    x=x+1
if suma1>suma2:
    print("la lista 1 tiene un valor acumulado mayor")
else:
    if suma2>suma1:
        print("la lista 2 tiene un valor acumulado mayor")
    else:
        print("las listas tienen un valor acumulado igual")
