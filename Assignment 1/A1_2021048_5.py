def getReverse(n):
    t=list(n)
    list1=[]
    for i in range(len(t),0,-1):
        y=t[i-1]
        list1.append(y)
    for i in list1:
        print(i,end='')

#getReverse('1234')

def checkPalindrome(n):
    t=list(n)
    list1=[]
    for i in range(len(t),0,-1):
        y=t[i-1]
        list1.append(y)
    if list1==t:
        print("True")
    else:
        print("False")

#checkPalindrome("1881")
    
def checkNarcissistic(n):
    t=list(n)
    list1=[]
    len_dg=len(t)
    for i in range(len_dg):
        z=int(t[i])**len_dg
        #print(z)
        list1.append(z)
    sum1=0
    for i in list1:
        sum1=sum1+i
    if sum1==int(n):
        print("True")
    else:
        print("False")

#checkNarcissistic('153')

def findDigitSum(n):
    t=list(n)
    if len(t)==1:
        print(n)
    else:
        s=0
        for i in t :
            s=s+int(i)
        return(str(s))

#findDigitSum("153")

def findSquareDigitSum(n):
    t=list(n)
    if len(t)==1:
        print(n)
    else:
        s=0
        list1=[]
        for i in t:
            y=int(i)**2
            list1.append(y)
        for j in list1:
            s=s+j
        return(str(s))

#findSquareDigitSum('153')

while True:
    print("|----------------------------------MENU-------------------------------------|")
    print("1. Get the Reverse of a number")
    print("2. Check Palindrome")
    print("3. Check Narcissistic")
    print("4. Find Digit Sum")
    print("5. Find Square Digit Sum")
    print("6. EXIT")
    print("|------------------------------------------------------------------------------")
    chs=int(input("Enter your Choice:"))
    if chs==1:
        num=input("Enter your number: ")
        getReverse(num)
        print()
    elif chs==2:
        num=input("Enter your number: ")
        checkPalindrome(num)
        print()
    elif chs==3:
        num=input("Enter your number: ")
        checkNarcissistic(num)
        print()
    elif chs==4:
        num=input("Enter your number: ")
        fl=[]
        while True:
            d=findDigitSum(num)
            fl.append(d)
            h=list(d)
            if len(h)==1:
                break
            num=d
        z=0
        for i in fl:
            z=z+int(i)
        print(z)
        print()
    elif chs==5:
        num=input("Enter your number: ")
        fl=[]
        while True:
            d=findSquareDigitSum(num)
            fl.append(d)
            h=list(d)
            if len(h)==1:
                break
            num=d
        z=0
        for i in fl:
            z=z+int(i)
        print(z)
        print()
    elif chs==6:
        print("Thank You")
        break
    else:
        print("Please input a correct choice")
