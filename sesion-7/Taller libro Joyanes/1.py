n=int(input("ingrese el numero a calcular"))
factorial=1

for f in range(n):
    print (factorial), " * ", n
    factorial *= n
    n -= 1
print("el factorial es:",factorial)    


    
