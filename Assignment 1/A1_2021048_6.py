def find_root(l):
    f_x=l.copy()#f_x is not list of exponrts
    f_dash_x=[]#list that will contain diffrentited exponent 
    for i in f_x:
        h=i-1
        f_dash_x.append(h)
    #print(f_x)
    #print(f_dash_x)
    for i in f_dash_x:
        if i<0 and i>(-1):
            return(0)
    x=1
    while True:
        f_n=0
        for i in range(len(f_x)):
            f_n=f_n+(x**f_x[i])
        #print(f_n)
        f_dash_n=0
        for i in range(len(f_dash_x)):
            f_dash_n=f_dash_n+(f_x[i]*(x**f_dash_x[i]))

        xnew=x-(f_n/f_dash_n)
        if abs(xnew-x)<(0.001):
            break
        x=xnew
    return(xnew)




l=[]#list of exponents
r=int(input("Enter the Number of exponets in the equation:"))
for i in range(r):
    y=float(input("enter the exponent: "))
    l.append(y)
t=find_root(l)
print("The root is:",t)
