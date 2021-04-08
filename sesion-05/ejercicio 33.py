suma=0
x=1
n=int(input("cuantas personas va a procesar"))
while x<=n:
    altura=float(input("ingrese la altura"))
    suma=suma+altura
    x=x+1
promedio=suma/n
print("la altura promedio es de",promedio)
