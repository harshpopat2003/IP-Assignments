#origin of light ray
e=input("Enter the origin of light ray (in vectors,space seperated): ")
e_list=e.split(' ')
e_1=int(e_list[0])
e_2=int(e_list[1])
e_3=int(e_list[2])

#sphere origin
print("Enter the sphere origin")
x0=float(input("X0: "))
y0=float(input("Y0: "))
z0=float(input("Z0: "))

#radius of sphere
r=int(input("Enter the radius of sphere"))

#direction  of light ray
d=input("Enter the direction of light in vector form(space seperated):")
d_list=d.split(' ')
dx=float(d_list[0])
dy=float(d_list[1])
dz=float(d_list[2])

#enter t
#t=int(input("Enter the vakue of T: "))

#ray can be written as p(t)=e+td
#ray=e+td
#sphere_Eq   (x1-x0)**2+(y1-y0)**2+(z1-z0)**2 = r**2
z_1=e_1-x0
z_2=e_2-y0
z_3=e_3-z0
#forming the equation
#t^2((dx*dx)+(dy*dy)+(dz*dz))+2t((dx*z_1)+(dy*z_2)+(dz*z_3))+(z_1*z_1+z_2*z_2+z_3*z_3)-r^2=0

#solving it
a=((dx*dx)+(dy*dy)+(dz*dz))
b=2*((dx*z_1)+(dy*z_2)+(dz*z_3))
c=(z_1*z_1+z_2*z_2+z_3*z_3)-r**2

discriminant=(b*b)-(4*a*c)
sq_val=abs(discriminant)**0.5
if discriminant > 0:
    t1=(-b+sq_val)/(2*a)
    t2=(-b-sq_val)/(2*a)
    #for x
    x1=e_1+(dx*t1)
    x2=e_1+(dx*t2)
    #for y
    y1=e_2+(dy*t1)
    y2=e_2+(dy*t2)
    #for z
    z1=e_3+(dz*t1)
    z2=e_3+(dz*t2)
    print(f"Point of interswction are:[ {x1}, {y1}, {z1} ]")
    print(f"Point of interswction are:[ {x2}, {y2}, {z2} ]")
elif discriminant==0:
    t1=(-b/(2*a))
    #for x
    x1=e_1+(dx*t1)
    #for y
    y1=e_2+(dy*t1)
    #for z
    z1=e_3+(dz*t1)
    print(f"Point of interswction are:[ {x1}, {y1}, {z1} ]")




