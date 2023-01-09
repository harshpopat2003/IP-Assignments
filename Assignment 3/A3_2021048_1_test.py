import Q1test 
def test_matmul(A, B, true_C):
    t=Q1test.matmul(A, B)
    A=[x1,y1,z1,1]
    r=[[0],[0],[0],[0]]
    for i in range(len(cordinatesmatrix)):
        for j in range(len(matrix1[0])):
            for k in range(len(matrix1)):
                r[i][j] += float(cordinatesmatrix[i][k]) * float(matrix1[k][j])
    if t==r:
        return True
    else:
        return False
def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    t=Q1test.scale(x,y,z,sx,sy,sz)
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
    if t==r:
        return True
    else:
        return False

def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    t=Q1test.translate(x, y, z, tx, ty, tz)
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
    if t==r:
        return True
    else:
        return False
def test_rotate(x, y, z, axis, phi, true_x, true_y, true_z):
    t= Q1test.rotate(x, y, z, axis, phi)
    import math 
    r=[p for p in input("Enter the scalar multiples : ").split()]
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
        if t==r:
            return True
        else:
            return False
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
            if t==r:
                return True
            else:
                return False
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
            if t==r:
                return True
            else:
                return False
    
