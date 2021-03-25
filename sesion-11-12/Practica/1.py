a=int(input("ingrese a"))
b=int(input("ingrese b"))
c=int(input("ingrese c"))
if a>b and a>c:
    print(a)
    if b>c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b>a and b>c:
    print(b)
    if a>c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
elif c>a and c>b:
    print(c)
    if a>b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
    
