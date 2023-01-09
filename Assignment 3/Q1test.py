def matmul(A, B):
    A=[x1,y1,z1,1]
    r=[[0],[0],[0],[0]]
    for i in range(len(cordinatesmatrix)):
        for j in range(len(matrix1[0])):
            for k in range(len(matrix1)):
                r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
    return r
def scale(x,y,z,sx,sy,sz):
    for f in range(len(x)): 
            x1=x[f]
            y1=y[f]
            z1=z[f]
            cordinatesmatrix=[x1,y1,z1,1]
            sx=float(h[1])
            sy=float(h[2])
            sz=float(h[3])
            matrix1=[[sx,0,0,0],[0,sy,0,0,0],[0,0,sz,0,0],[0,0,0,1]]
            r=[[0],[0],[0],[0]]
            for i in range(len(cordinatesmatrix)):
                for j in range(len(matrix1[0])):
                    for k in range(len(matrix1)):
                        r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
            x[f]=r[0]
            y[f]=r[1]
            z[f]=r[2]
    return x_dash,y_dash,z_dash
def translate(x, y, z, tx, ty, tz):
     for f in range(len(x)):
            x1=x[f]
            y1=y[f]
            z1=z[f]
            cordinatesmatrix=[x1,y1,z1,1]
            tx=float(h[1])
            ty=float(h[2])
            tz=float(h[3])
            matrix1=[[1,0,0,tx],[0,1,0,ty],[0,0,0,tz],[0,0,0,1]]
            r=[[0],[0],[0],[0]]
            for i in range(len(cordinatesmatrix)):
                for j in range(len(matrix1[0])):
                    for k in range(len(matrix1)):
                        r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
            x[f]=r[0]
            y[f]=r[1]
            z[f]=r[2]
     return x_dash,y_dash,z_dash
def rotate(x, y, z, axis, phi):
     import math 
        #r=[p for p in input("Enter the scalar multiples : ").split()]
       if h[1]=="x":
            for f in range(len(x)):
                x1=x[f]
                y1=y[f]
                z1=z[f]
                cordinatesmatrix=[x1,y1,z1,1] 
                cosphi=round(math.cos(float(h[2]),2))
                sinphi=round(math.sin(float(h[2]),2))
                matrix1=[[1,0,0,0],[0,cosphi,-(sinphi),0],[0,sinphi,cosphi,0],[0,0,0,1]]  
                r=[[0],[0],[0],[0]]
                for i in range(len(cordinatesmatrix)):
                    for j in range(len(matrix1[0])):
                        for k in range(len(matrix1)):
                            r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
                x[f]=r[0]
                y[f]=r[1]
                z[f]=r[2]
            return x_dash,y_dash,z_dash
        elif h[1]=="y":
            for f in range(len(x)):
                x1=x[f]
                y1=y[f]
                z1=z[f]
                cordinatesmatrix=[x1,y1,z1,1] 
                cosphi=round(math.cos(float(h[2]),2))
                sinphi=round(math.sin(float(h[2]),2))
                matrix1=[[cosphi,0,sinphi,0],[0,1,0,0],[-(sinphi),0,cosphi,0],[0,0,0,1]]  
                r=[[0],[0],[0],[0]]
                for i in range(len(cordinatesmatrix)):
                    for j in range(len(matrix1[0])):
                        for k in range(len(matrix1)):
                            r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
                x[f]=r[0]
                y[f]=r[1]
                z[f]=r[2]
            return x_dash,y_dash,z_dash
        elif h[1]=="z":
                for f in range(len(x)):
                    x1=x[f]
                    y1=y[f]
                    z1=z[f]
                    cordinatesmatrix=[x1,y1,z1,1] 
                    cosphi=round(math.cos(float(h[2]),2))
                    sinphi=round(math.sin(float(h[2]),2))
                    matrix1=[[cosphi,-(sinphi),0,0],[sinphi,cosphi,0,0],[0,0,1,0],[0,0,0,1]]  
                    r=[[0],[0],[0],[0]]
                    for i in range(len(cordinatesmatrix)):
                        for j in range(len(matrix1[0])):
                            for k in range(len(matrix1)):
                                r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
                    x[f]=r[0]
                    y[f]=r[1]
                    z[f]=r[2]
                return x_dash,y_dash,z_dash


num=int(input("Enter the number of vertices in the 3D shape: "))
x=[float(i) for i in input().split()]
y=[float(j) for j in input().split()]
z=[float(k) for k in input().split()]
q=int(input("Enter the tranformation queries you want to apply on the matrix: "))
for g in range(q):
    h=[t for t in input("Enter the scalar multiples : ").split()]
    if h[0].lower()=="s":
        scale(x,y,z,sx,sy,sz)
    elif h[1].lower()=="r":
        rotate(x, y, z, axis, phi)
    elif h[2].lower()=="t":
        translate(x, y, z, tx, ty, tz)
