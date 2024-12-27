a = int(input("Enter the values of a : "))
b = int(input("Enter the values of b : "))
c = int(input("Enter the values of c : "))
D = (b*b)-(4*a*c)
deno = 2*a
if(D>0):
    print ("REAL ROOTS")
    root1 = (-b + D**0.5)/deno
    root2 = (-b - D**0.5)/deno
    print ("Root1 = ",root1, "\tRoot2 = ",root2)
elif(D==0):
    print ("EQUAL ROOTS")
    root1 = -b/ deno
    print("Root1 and Root2 = ",root1)
else:
    print ("IMAGINARY ROOTS")
