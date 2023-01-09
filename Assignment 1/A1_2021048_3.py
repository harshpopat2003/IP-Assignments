def polynomial(deg,coeff,lwr_x,upr_x,increment_x):
    cof=coeff.copy()
    print("--------------------------------------------")
    for r in range(lwr_x,upr_x+1,increment_x):
        eq=0
        if len(coeff)==1:
            eq=cof[0]
            print("|",end='')
            for h in range(eq):
                print("*",end="")
            print()
        elif len(coeff)==2:#degree of poly = 1
            eq=cof[0]*r+coeff[1]
            print("|",end='')
            for h in range(eq):
                print("*",end="")
            print()
        elif len(coeff)==3:#degree of poly = 2
            eq=(cof[0]*r*r)+ (cof[1]*r) + cof[2]
            print("|",end='')
            for h in range(eq):
                print("*",end="")
            print()
        elif len(coeff)==4: #degree of poly = 3 
            eq=(cof[0]*r*r*r)+(cof[1]*r*r)+ (cof[2]*r) + cof[3]
            print("|",end='')
            for h in range(eq):
                print("*",end="")
            print()
        else:
            print("MAX range of polynomial is 3")

       
coeff=[]
deg=int(input("Enter the degree of the polynomial: "))
for i in range(deg+1):
    coff=int(input(f"Enter the Coefficient {i+1} : "))
    coeff.append(coff)
#print(coeff)
lwr_x=int(input("Enter the lower bond: "))
upr_x=int(input("Enter the upper bond: "))
increment_x=int(input("Enter the increment x:"))
polynomial(deg,coeff,lwr_x,upr_x,increment_x)
