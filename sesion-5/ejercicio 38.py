pares=0
impares=0
x=1
n=int(input("cuantos numeros ingresados"))
while x<=n:
    valor=int(input("ingrese el valor"))
    if valor%2==0:
         pares=pares+1
    else:
        impares=impares+1
    x=x+1
print("cantidad de pares",pares)
print("cantidad de impares",impares)

    
      
   
