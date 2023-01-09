#Q1
#Menu driven program for triangle shape.

def right_angled_triangle(n):
    list1=[1]
    count=1
    for i in range(n+1):
        for j in range(i):
            for y in list1:
                print(y,end=' ')
                if y==n:
                    return()
                else:
                    pass
            print()
            count=count+1
            list1.append(count)
            

#right_angled_triangle(5)

def isoceles_triangle(n):
    count=1
    list1=[1]  
    m = (2 * n) - 2  
    for i in range(n):  
        for j in range(m):  
            print(end=" ")   
        m = m - 1
        for r in list1:   
            print(r, end='')   
        count=count+1
        list1.append(count)
        count=count+1
        list1.append(count)
        print()  

#isoceles_triangle(4)

def kite(n):
    count=1
    list1=[1]  
    m = (2 * n) - 2  
    for i in range(n):  
        for j in range(m):  
            print(end=" ")   
        m = m - 1
        for r in list1:   
            print(r, end='')   
        count=count+1
        list1.append(count)
        count=count+1
        list1.append(count)
        print()
    list1.pop()
    list1.pop()
    list1.pop()
    list1.pop()
    m=(2*n)- n
    for i in range(n):  
        for j in range(m):  
            print(end=" ")   
        m = m+1
        for r in list1:   
            print(r, end='')
        if len(list1)==1:
            break
        else:
            list1.pop()
            list1.pop()
        print()  
    
#kite(8)

def half_kite(n):
    count=1
    list1=[1]
    for i in range(n):
        for j in list1:
            print(j,end='')
        print()
        count=count+1
        list1.append(count)
    list1.pop()
    list1.pop()
    for y in range(n-1):
        for r in list1:
            print(r,end='')
        print()
        list1.pop()
#half_kite(5)

def form_X(n):
    list1=[]
    m=1
    for i in range((2*n)-1):#making the list
        list1.append(m)
        m=m+1
    #print(list1)
    m=(2*n)-2
    for i in range(n):  
        for j in range(m):  
            print(end=" ")   
        m = m+1
        for r in list1:   
            print(r, end='')
        if len(list1)==1:
            break
        else:
            list1.pop()
            list1.pop()
        print()
    print()
    count=1
    m = (2*n)+(n-3)
    for i in range(n):  
        for j in range(m):  
            print(end=" ")   
        m = m-1
        for r in list1:   
            print(r, end='')   
        count=count+1
        list1.append(count)
        count=count+1
        list1.append(count)
        print()
        

#form_X(4)



while True:
    print("-----------------------------------------------------------------------")
    print("1.Right Angled Triangle")
    print("2.Isoceles Triangle")
    print("3.Kite")
    print("4.Half kite")
    print("5.Form X shape")
    print("6.Exit"
          )
    print("-----------------------------------------------------------------------")
    option=int(input("Enter your option: "))
    print("-----------------------------------------------------------------------")
    if option==1: #right angled triangle
        n=int(input("Enter value of n : "))
        right_angled_triangle(n)
        print()
        # print("-----------------------------------------------------------------------")
    elif option==2: #isoceles triangle
        n=int(input("Enter value of n : "))
        if n%2==0:
            isoceles_triangle(n)
        else:
            print("Please input an even number")
    elif option==3:#kite
        n=int(input("Enter value of n : "))
        if n%2==0:
            kite(n)
            print()
        else:
            print("Please input a even number")
    elif option==4: #half kite
        n=int(input("Enter value of n : "))
        half_kite(n)
    elif option==5:#form x
        n=int(input("Enter value of n : "))
        if n%2==0:
            form_X(n)
        else:
            print("Please input an even number")
    elif option==6:#exit
        break
    else:
        print("Please input a valid option")
            
        
        






