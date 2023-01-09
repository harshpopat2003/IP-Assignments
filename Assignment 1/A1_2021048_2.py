def square():
    s=int(input("Enter side of square: "))
    p=4*s
    a=s*s
    print("Perimeter: ",p)
    print("Area: ",a)
    print("...........................................................................")
    
def rectangle():
    l=int(input("Enter Length: "))
    b=int(input("Enter Breadth: "))
    p=2*(l+b)
    a=l*b
    print("Perimeter:",p)
    print("Area:",a)
    print("...........................................................................")

def rhombus():
    a=int(input("Enter side"))
    d1=int(input("Enter diagonal 1: "))
    d2=int(input("Enter diagonal 2: "))
    p=4*a
    area=(d1*d2)/2
    print("Perimeter: ",p)
    print("Area: ",area)
    print("...........................................................................")

def parallelogram():
    l=int(input("Enter Length: "))
    b=int(input("Enter Breadth: "))
    h=int(input("Enter Height: "))
    p=2*(l+b)
    a=b*h
    print("Perimeter: ",p)
    print("Area: ",a)
    print("...........................................................................")
    
def circle():
    r=int(input("Enter Radius: "))
    p=2*(3.14)*r
    a=(3.14)*r*r
    print("Perimeter: ",p)
    print("Area: ",a)
    print("...........................................................................")

#3d shapes
    
def cube():
    s=int(input("Enter side"))
    csa=4*s*s
    tsa=6*s*s
    v=s**3
    print("Curved Surface Area: ",csa)
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    
def cuboid():
    l=int(input("Enter Length: "))
    b=int(input("Enter Breadth: "))
    h=int(input("Enter Height: "))
    csa=2*(l+b)*h
    tsa=2*((l*b)+(b*h)+(h*l))
    v=l*b*h
    print("Curved Surface Area: ",csa)
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    
def rigth_circular_cone():
    l=int(input("Enter Slant Hieght: "))
    r=int(input("Enter Radius: "))
    h=int(input("Enter Height: "))
    csa=(3.14)*r*l
    tsa=(3.14)*r*(r+l)
    v=((3.14)*r*r*h)/3
    print("Curved Surface Area: ",csa)
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    
def hemisphere():
    r=int(input("Enter Radius: "))
    csa=2*(3.14)*r*r
    tsa=3*(3.14)*r*r
    v=(2*(3.14)*r*r*r)/3
    print("Curved Surface Area: ",csa)
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    
def sphere():
    r=int(input("Enter Radius: "))
    tsa=4*(3.14)*r*r
    v=(4*(3.14)*r*r*r)/3
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    
def solid_cylinder():
    r=int(input("Enter Radius: "))
    h=int(input("Enter Height: "))
    csa=2*(3.14)*r*h
    tsa=2*(3.14)*r*(r+h)
    v=(3.14)*r*r*h
    print("Curved Surface Area: ",csa)
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    
def hollow_cylinder():
    r1=int(input("Enter Radius 1: "))
    r2=int(input("Enter Radius 2: "))
    h=int(input("Enter Height: "))
    csa=2*(3.14)*h*(r1+r2)
    tsa=(2*(3.14)*h*(r1+r2))+(2*(3.14)*(abs(r1-r2)))
    v=(3.14)*(abs(r1-r2))*h
    print("Curved Surface Area: ",csa)
    print("Total Surface Area: ",tsa)
    print("Volume: ",v)
    print("...........................................................................")
    



n=int(input("Enter the no of students: "))
while n>0:
    print("--------------------------------------MENU-------------------------------------")
    print("1.Square")
    print("2.Rectangle")
    print("3.Rhombus")
    print("4.Parallelogram")
    print("5.Circle")
    print("6.Cube")
    print("7.Cuboid")
    print("8.Right circular cone")
    print("9.Hemisphere")
    print("10.Sphere")
    print("11.Solid cylinder")
    print("12.Hollow cylinder input")
    print("--------------------------------------------------------------------------")
    shape=int(input("Enter your choice: "))
    if shape==1:
        square()
    elif shape==2:
        rectangle()
    elif shape==3:
        rhombus()
    elif shape==4:
        parallelogram()
    elif shape==5:
        circle()
    elif shape==6:
        cube()
    elif shape==7:
        cuboid()
    elif shape==8:
        rigth_circular_cone()
    elif shape==9:
        hemisphere()
    elif shape==10:
        sphere()
    elif shape==11:
        solid_cylinder()
    elif shape==12:
        hollow_cylinder()
    else:
        print("Please enter a valid choice")
        n=n+1
    n=n-1
print("-------------------------------THANK YOU--------------------------------")   
