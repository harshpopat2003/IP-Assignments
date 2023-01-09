def user_input(N):
    matrix=[]
    for i in range(N):
        R=[]
        for j in range(N):
            val=int(input("Enter the value you want to store at index"+"["+str(i)+","+str(j)+"]: "))
            R.append(val)
        matrix.append(R)
    return matrix
def normal_raversing(matrix):
    g=''
    for i in matrix:
        for j in i:
            g=g+" "+str(j)
    print("Normal Traversal : ",end="")
    print(g)

def alternating_traversing(matrix):
    for i in range(len(matrix)):
        if i%2==1:
            matrix[i].reverse()
        else:
            pass
    g=''
    for i in matrix:
        for j in i:
            g=g+" "+str(j)
    print("Alternating traversal : ",end="")
    print(g)   
    


def spiral_traversal(matrix):
    row_count=len(matrix)
    column_count=len(matrix[0])
    rows=0
    column=0
    print("Spiral Traversal: ",end="")
    while (rows<row_count and column<column_count):
        for i in range(column, column_count):
            print(matrix[rows][i], end=" ")
        rows+=1
        for i in range(rows,row_count):
            print(matrix[i][column_count-1], end=" ")
        column_count-=1
        if (rows<row_count):
            for i in range(column_count-1,(column-1),-1):
                print(matrix[row_count-1][i],end=" ")
            row_count-=1
        if (column<column_count):
            for i in range(row_count-1,rows-1,-1):
                print(matrix[i][column],end=" ")
            column+=1
            
def boundary_traversal(matrix):
    fl_list=[]
    l1=matrix[0]
    for i in l1:
        fl_list.append(i)
    for i in range(len(matrix)):
        t=matrix[i][-1]
        fl_list.append(t)
    l2=matrix[-1]
    l2.reverse()
    for i in l2:
        fl_list.append(i)
    l3=matrix.copy()
    del l3[-1]
    del l3[0]
    l3.reverse()
    for i in l3:
        t=i[0]
        fl_list.append(t)
    list1=[]
    for i in fl_list:
        if i not in list1:
            list1.append(i)
    print("Boundary traversal : ",end="")
    for i in list1:
        print(i,end=" ")
    print(list1)
#change code copied from geek for geek 
def diagonal_traversal_right_to_left(n,matrix):
   # code here
   final_list=[]
   list1=[]
   for i in range (2*n - 1):
       list1.append([])
       
   for i in range (n):
       for j in range (n):
           list1[i+j].append(matrix[i][j])
           
   for i in range (len(list1)):
       for j in range (len(list1[i])):
           final_list.append(list1[i][j])
   print("Diagonal traversal from right to left : ",end="")       
   for i in final_list:
        print(i,end=" ")
   #print(final_list)

def diagonaltraversal_left_to_right(n,matrix):
    for i in matrix:
        i.reverse()
    final_list=[]
    list1=[]
    for i in range (2*n - 1):
       list1.append([])
       
    for i in range (n):
       for j in range (n):
           list1[(i)+(j)].append(matrix[i][j])
    for i in range (len(list1)):
       for j in range (len(list1[i])):
           final_list.append(list1[i][j])
    print("Diagonal traversal from left to right : ",end="")
    for i in final_list:
        print(i,end=" ")
    
    #print(final_list)

#N=int(input("Enter the value of N: "))
#matrix=user_input(N)
#print(matrix)
#matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#normal_raversing(matrix)
#alternating_traversing(matrix)
spiral_traversal(matrix)
#boundary_traversal(matrix)
n=4
#diagonal_traversal_right_to_left(n,matrix)
#diagonaltraversal_left_to_right(n,matrix)
