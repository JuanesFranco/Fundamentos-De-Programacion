x=int(input("ingrese coordenada x"))
y=int(input("ingrese coordenada y"))
if x>0 and y>0:
    print("se encuentra en el primer cuadrante")
else:
    if x<0 and y>0:
        print("se encuentra en el segundo cuadrante")
    else:
        if x<0 and y<0:
            print("se encuentra en el tercer cuadrante")
        else:
            if x>0 and y<0:
                print(" se encuentra en el cuarto cuadrante")
            else:
                print("se encuentra sobre un eje")
