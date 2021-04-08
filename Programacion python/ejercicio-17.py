num=int(input("ingrese numero de 1 y 999:"))
if num<10:
    print("tiene un digito")
else:
    if num<100:
        print("tiene dos digitos")
    else:
        if num<1000:
            print("tiene tres digitos")
        else:
            print("error en la entrada de digitos")
            
print("fin del programa")
