#calcular la suma de los numero impares
n=int(input("ingrese el limite de la suma"))
impar=0
for f in range(1,n+1):
    if f %2==1:
        impar=impar+f       
print("la suma de los impares es:",impar)

    
    
