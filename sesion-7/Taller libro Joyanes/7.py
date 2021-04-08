valor=int(input("ingrese valor"))
continuar=input("ingrese si, si desea continuar.Ingrese no, si desea finalizar")
contador=0
numero=0
while valor !=0:
    if continuar==1:
        contador=contador+1 
        valor=int(input("ingrese valor"))
        continuar=input("ingrese si, si desea continuar.Ingrese no, si desea finalizar") 
        print(continuar+valor)   
    else:
        if continuar==2:
            print(numero+contador)
        else:
            print("codigo incorrecto, intente otra vez")
     
    
