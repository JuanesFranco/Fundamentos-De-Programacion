def mostrar_mensaje (mensaje):
    print("**********")
    print(mensaje)
    print("**********")
def carga_suma():
    valor=int(input("ingreseel primer valor"))
    valor2=int(input("ingrese el segundo valor"))
    suma=valor+valor2
    print("la suma de los vaores es",suma)
#bloque principal
cadena="el programa muestra la suma de los dos valores ingresados por teclado"
mostrar_mensaje(cadena)
carga_suma()
mostrar_mensaje("gracias por usar este mensaje")
