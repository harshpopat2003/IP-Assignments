num=int(input("Enter the number of vertices in the 3D shape: "))
x=[int(i) for i in input().split()]
y=[int(j) for j in input().split()]
z=[int(k) for k in input().split()]
q=int(input("Enter the tranformation queries you want to apply on the matrix: "))
for i in range(q):
    r=[int(t) for t in input("Enter the scalar multiples : ").split()]
    #scaling
    if r[0]=="S":
        for i in range(len(x)): 
            x1=x[i]
            y1=y[i]
            z1=z[i]
            cordinatesmatrix=[x1,y1,z1,1]
            sx=r[1]
            sy=r[2]
            sz=r[3]
            matrix1=[[sx,0,0,0],[0,sy,0,0,0],[0,0,sz,0,0],[0,0,0,1]]
            r=[[0],[0],[0],[0]]
            for i in range(len(cordinatesmatrix)):
                for j in range(len(matrix1[0])):
                    for k in range(len(matrix1)):
                        r[i][j] += cordinatesmatrix[i][k] * matrix1[k][j]
            x[i]=r[0]
            y[i]=r[1]
            z[i]=r[2]
            

    #transversing 
    elif r[0]=="T":
        for i in range(len(x)):
            x1=x[i]
            y1=y[i]
            z1=z[i]
            cordinatesmatrix=[x1,y1,z1,1]
            tx=r[1]
            ty=r[2]
            tz=r[3]
            matrix1=[[1,0,0,tx],[0,1,0,ty],[0,0,0,tz],[0,0,0,1]]
            r=[[0],[0],[0],[0]]
            for i in range(len(cordinatesmatrix)):
                for j in range(len(matrix1[0])):
                    for k in range(len(matrix1)):
                        r[i][j] += cordinatesmatrix[i][k] * matrix1[k][j]
            x[i]=r[0]
            y[i]=r[1]
            z[i]=r[2]

    #Rotation
    elif r[0]=="R":
        import math 
        r=[p for p in input("Enter the scalar multiples : ").split()]
        if r[1]=="x":
            for i in range(len(x)):
                x1=x[i]
                y1=y[i]
                z1=z[i]
                cordinatesmatrix=[x1,y1,z1,1] 
                cosphi=round(math.cos(r[2],2))
                sinphi=round(math.sin(r[2],2))
                matrix1=[[1,0,0,0],[0,cosphi,-(sinphi),0],[0,sinphi,cosphi,0],[0,0,0,1]]  
                r=[[0],[0],[0],[0]]
                for i in range(len(cordinatesmatrix)):
                    for j in range(len(matrix1[0])):
                        for k in range(len(matrix1)):
                            r[i][j] += cordinatesmatrix[i][k] * matrix1[k][j]
                x[i]=r[0]
                y[i]=r[1]
                z[i]=r[2]
        elif r[1]=="y":
            for i in range(len(x)):
                x1=x[i]
                y1=y[i]
                z1=z[i]
                cordinatesmatrix=[x1,y1,z1,1] 
                cosphi=round(math.cos(r[2],2))
                sinphi=round(math.sin(r[2],2))
                matrix1=[[cosphi,0,sinphi,0],[0,1,0,0],[-(sinphi),0,cosphi,0],[0,0,0,1]]  
                r=[[0],[0],[0],[0]]
                for i in range(len(cordinatesmatrix)):
                    for j in range(len(matrix1[0])):
                        for k in range(len(matrix1)):
                            r[i][j] += cordinatesmatrix[i][k] * matrix1[k][j]
                x[i]=r[0]
                y[i]=r[1]
                z[i]=r[2] 
        elif r[1]=="z":
                for i in range(len(x)):
                    x1=x[i]
                    y1=y[i]
                    z1=z[i]
                    cordinatesmatrix=[x1,y1,z1,1] 
                    cosphi=round(math.cos(r[2],2))
                    sinphi=round(math.sin(r[2],2))
                    matrix1=[[cosphi,-(sinphi),0,0],[sinphi,cosphi,0,0],[0,0,1,0],[0,0,0,1]]  
                    r=[[0],[0],[0],[0]]
                    for i in range(len(cordinatesmatrix)):
                        for j in range(len(matrix1[0])):
                            for k in range(len(matrix1)):
                                r[i][j] += cordinatesmatrix[i][k] * matrix1[k][j]
                    x[i]=r[0]
                    y[i]=r[1]
                    z[i]=r[2]  
