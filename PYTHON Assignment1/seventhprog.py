#find roots of quadratic equation
a=int(input("Enter cofficient of a: "))
b=int(input("Enter cofficient of b: "))
c=int(input("Enter cofficient of c: "))
d=b**2-4*a*c
rootd=d**0.5
if d>0:
    root1=(-b-rootd)/2*a
    root2=(-b+rootd)/2*a
    print("real and distinct roots : ",root1,root2)
elif d==0:
        print("equal and real roots: ",-b/2*a)
else:                                                 #d<0 imaginary roots 
        print("no real roots")
