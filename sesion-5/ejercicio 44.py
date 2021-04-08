aprobado=0
reprobado=0
for f in range(10):
    nota=int(input("ingrese las notas"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobado=reprobado+1
print("cantidad de aprobadas",aprobado)
print("cantidad de reprobados",reprobado)
