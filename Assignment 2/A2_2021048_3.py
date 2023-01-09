#convert decimal to binary or vice versa 
def decimal_to_binary(n):
    t=n
    binlist=[]
    while True:
        reminder=t%2
        t_new=t//2
        binlist.append(reminder)
        if t_new==0:
            break
        t=t_new
    binlist.reverse()
    for i in binlist:
        print(i,end="")
    print()
    
#binary_to_decimal(10)

def binary_to_decimal(n):
    list1=list(str(n))
    lenght=len(list1)-1
    decimal_list=[]
    for i in range(len(list1)):
        t=int(list1[i])*(2**lenght)
        decimal_list.append(t)
        lenght=lenght-1
    s1=sum(decimal_list)
    print(s1)
        
#binary_to_decimal(10101001)

#-----------------------------------------------------------------------------------------------------------
#2) convert decimal to hexadecimal and vice-versa

def decimal_to_hexadecimal(n):
    t=n
    hex_list=[]
    while True:
        reminder=t%16
        t_new=t//16
        if reminder>=0 and reminder<10:
            hex_list.append(reminder)
        elif reminder==10:
            hex_list.append("A")
        elif reminder==11:
            hex_list.append("B")
        elif reminder==12:
            hex_list.append("C")
        elif reminder==13:
            hex_list.append("D")            
        elif reminder==14:
            hex_list.append("E")
        elif reminder==15:
            hex_list.append("F")
        if t_new==0:
            break
        t=t_new
    hex_list.reverse()
    for i in hex_list:
        print(i,end="")
    print()

    
#decimal_to_hexadecimal(2545)

def hexadecimal_to_decimal(n):
    list1=list(str(n))
    lenght=len(list1)-1
    decimal_list=[]
    for i in range(len(list1)):
        if list1[i]== "0" or list1[i]=="1" or list1[i]=="2" or list1[i]=="3" or list1[i]=="4" or list1[i]=="5" or list1[i]=="6" or list1[i]=="7" or list1[i]=="8" or list1[i]=="9":
            t=int(list1[i])*(16**lenght)
            decimal_list.append(t)
        elif list1[i]=="A":
            t=10*(16**lenght)
            decimal_list.append(t)
        elif list1[i]=="B":
            t=11*(16**lenght)
            decimal_list.append(t)
        elif list1[i]=="C":
            t=12*(16**lenght)
            decimal_list.append(t)
        elif list1[i]=="D":
            t=13*(16**lenght)
            decimal_list.append(t)
        elif list1[i]=="E":
            t=14*(16**lenght)
            decimal_list.append(t)
        elif list1[i]=="F":
            t=15*(16**lenght)
            decimal_list.append(t)
    
        lenght=lenght-1
    s1=sum(decimal_list)
    print(s1)

    
#hexadecimal_to_decimal("1AF")

#--------------------------------------------------------------------------------------------------

#3) Convert decimal to octal and vice-versa.

def decimal_to_octal(n):
    t=n
    octal_list=[]
    while True:
        reminder=t%8
        t_new=t//8
        octal_list.append(reminder)
        if t_new==0:
            break
        t=t_new
    octal_list.reverse()
    for i in octal_list:
        print(i,end="")
    print()
    
#decimal_to_octal(33)

def octal_to_decimal(n):
    list1=list(str(n))
    lenght=len(list1)-1
    decimal_list=[]
    for i in range(len(list1)):
        t=int(list1[i])*(8**lenght)
        decimal_list.append(t)
        lenght=lenght-1
    s1=sum(decimal_list)
    print(s1)
#octal_to_decimal(67)

#---------------------------------------------------------------------------------------------------
#4) Convert binary to hexadecimal and vice-versa.
#error check and rectify
def binary_to_hexadecimal(n):
    list1=list(str(n))
    list1.reverse()
    if len(list1)%4==0:
      pass
    elif len(list1)%4==1:
        list1.append("0")
        list1.append("0")
        list1.append("0")
    elif len(list1)%4==2:
        list1.append("0")
        list1.append("0")
    elif len(list1)%4==3:
        list1.append("0")
    list1.reverse()
    l1=list1.copy()
    hex_dict={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
    fl_list=[]
    hex_list=[]
    while True:
        t=l1[:4]
        fl_list.append(t)
        l1=l1[4:]
        if len(l1)==0:
            break
    for i in fl_list:
        g=""
        for j in i:
            g=g+str(j)
        #print(g)
        y=hex_dict.get(g)
        hex_list.append(y)
    for i in hex_list:
        print(i,end="")
    print()

#binary_to_hexadecimal(100001111)

def hexadecimal_to_binary(n):
    list1=list(str(n))
    bin_list=[]
    hex_dict={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    for i in list1:
        y=hex_dict.get(i)
        bin_list.append(y)
    for i in bin_list:
        print(i,end="")
    print()
#hexadecimal_to_binary("F7B")

#----------------------------------------------------------------------------------------------
#5) Convert binary to octal and vice-versa.
def binary_to_octal(n):
    list1=list(str(n))
    list1.reverse()
    if len(list1)%3==1:
        list1.append("0")
        list1.append("0")
    elif len(list1)%3==2:
        list1.append("0")
    list1.reverse()
    l1=list1.copy()
    oct_dict={"000":"0","001":"1","010":"2","011":"3","100":"4","101":"5","110":"6","111":"7"}
    fl_list=[]
    oct_list=[]
    while True:
        t=l1[:3]
        fl_list.append(t)
        l1=l1[3:]
        if len(l1)==0:
            break
    for i in fl_list:
        g=""
        for j in i:
            g=g+str(j)
        #print(g)
        y=oct_dict.get(g)
        oct_list.append(y)
    for i in oct_list:
        print(i,end="")  
    print()
    
#binary_to_octal(1111001010010100001)

def octal_to_binary(n):
    list1=list(str(n))
    bin_list=[]
    oct_dict={"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
    for i in list1:
        y=oct_dict.get(i)
        bin_list.append(y)
    for i in bin_list:
        print(i,end="")
    print()
#octal_to_binary(616)

#-----------------------------------------------------------------------------------------------------------
#6) Convert hexadecimal to octal and vice-versa.

def hexadecimal_to_octal(n):
    #hexadecimal to binary 
    list1=list(str(n))
    bin_list=[]
    hex_dict={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    for i in list1:
        y=hex_dict.get(i)
        bin_list.append(y)
    #print(bin_list)
    g=''
    for i in bin_list:
        g=g+i
    #print(g)
    
    #binary to octal
    list1=list(str(g))
    list1.reverse()
    if len(list1)%3==1:
        list1.append("0")
        list1.append("0")
    elif len(list1)%3==2:
        list1.append("0")
    list1.reverse()
    l1=list1.copy()
    oct_dict={"000":"0","001":"1","010":"2","011":"3","100":"4","101":"5","110":"6","111":"7"}
    fl_list=[]
    oct_list=[]
    while True:
        t=l1[:3]
        fl_list.append(t)
        l1=l1[3:]
        if len(l1)==0:
            break
    for i in fl_list:
        g=""
        for j in i:
            g=g+str(j)
        #print(g)
        y=oct_dict.get(g)
        oct_list.append(y)
    for i in oct_list:
        print(i,end="")
    print()

#hexadecimal_to_octal("1AC")
    
def octal_to_hexadecimal(n):
    #octal to binary
    list1=list(str(n))
    bin_list=[]
    oct_dict={"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
    for i in list1:
        y=oct_dict.get(i)
        bin_list.append(y)
    #print(bin_list)
    g=''
    for i in bin_list:
        g=g+i
        
    #binary to hexadecimal
    list1=list(str(g))
    list1.reverse()
    if len(list1)%4==0:
      pass
    elif len(list1)%4==1:
        list1.append("0")
        list1.append("0")
        list1.append("0")
    elif len(list1)%4==2:
        list1.append("0")
        list1.append("0")
    elif len(list1)%4==3:
        list1.append("0")
    list1.reverse()
    l1=list1.copy()
    hex_dict={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
    fl_list=[]
    hex_list=[]
    while True:
        t=l1[:4]
        fl_list.append(t)
        l1=l1[4:]
        if len(l1)==0:
            break
    for i in fl_list:
        g=""
        for j in i:
            g=g+str(j)
        #print(g)
        y=hex_dict.get(g)
        hex_list.append(y)
    for i in hex_list:
        print(i,end="")
    print()
#octal_to_hexadecimal("0654")


#7) convert to any number
def ord_val(x):
    if (x>="0" and x<="9"):
        return ord(x)-48
    else:
        return ord(x)-55
def num_to_decimal(num,base):
    lgt=len(num)-1
    pwr=1
    nm=0
    for i in range(lgt,-1,-1):
        if ord_val(num[i])>= base:
            print("not a proper number")
            return False
        nm+=ord_val(num[i])*pwr
        pwr=pwr*base
    return nm

def chr_val(x):
    if x>=0 and x<=9:
        return chr(x+48)
    else:
        return chr(x+55)
def decimal_to_final(nm,base):
    f=""
    while nm>0:
        f+=chr_val(nm%base)
        nm=nm//base
    f=f[::-1]
    return f
def convert_to_base(l,a,b):
    d=num_to_decimal(l,a)
    s=decimal_to_final(d,b)
    print(s)
#convert_to_base("CA91",13,17)

#loop
while True:
    print("-----------------------------------------------------------------------------------------------------------")
    print("1) Convert decimal to binary and vice-versa")
    print("2) Convert decimal to hexadecimal and vice-versa")
    print("3) Convert decimal to octal and vice-versa.")
    print("4) Convert binary to hexadecimal and vice-versa.")
    print("5) Convert binary to octal and vice-versa.")
    print("6) Convert hexadecimal to octal and vice-versa.")
    print("7) Convert number with radix A to radix B. Here A,B <= 36. In this case, you must take A,B as input.")
    print("8) Exit")
    print("--------------------------------------------------------------------------------------------------------------")
    en=int(input("Enter your Choice: "))
    if en==1:
        print("1.Decimal to Binary")
        print("2.Binary to Decimal")
        r=int(input("Enter :"))
        if r==1:
            n=int(input("Enter what you want to convert"))
            decimal_to_binary(n)
        elif r==2:
            n=int(input("Enter what you want to convert"))
            binary_to_decimal(n)
        else:
            print("please enter right choice")
    elif en==2:
        print("1.Decimal to HexaDecimal")
        print("2.Hexadecimal to Decimal")
        r=int(input("Enter :"))
        if r==1:
            n=int(input("Enter what you want to convert"))
            decimal_to_hexadecimal(n)
        elif r==2:
            n=input("Enter what you want to convert")
            hexadecimal_to_decimal(n)
        else:
            print("please enter right choice")
    elif en==3:
        print("1.Decimal to octal")
        print("2.Octal to Decimal")
        r=int(input("Enter :"))
        if r==1:
            n=int(input("Enter what you want to convert"))
            decimal_to_octal(n)
        elif r==2:
            n=int(input("Enter what you want to convert"))
            octal_to_decimal(n)
        else:
            print("please enter right choice")

    elif en==4:
        print("1.Binary to Hexadecimal")
        print("2.Hexadecimal to Binary")
        r=int(input("Enter :"))
        if r==1:
            n=input("Enter what you want to convert")
            binary_to_hexadecimal(n)
        elif r==2:
            n=input("Enter what you want to convert")
            hexadecimal_to_binary(n)
        else:
            print("please enter right choice")
            
    elif en==5:
        print("1.Binary to Octal")
        print("2.Octal to Binary")
        r=int(input("Enter :"))
        if r==1:
            n=input("Enter what you want to convert")
            binary_to_octal(n)
        elif r==2:
            n=input("Enter what you want to convert")
            octal_to_binary(n)
        else:
            print("please enter right choice")

    elif en==6:
        print("1.Hexadecimal to octal")
        print("2.Octal to Hexadecimal")
        r=int(input("Enter :"))
        if r==1:
            n=input("Enter what you want to convert")
            hexadecimal_to_octal(n)
        elif r==2:
            n=input("Enter what you want to convert")
            octal_to_hexadecimal(n)
        else:
            print("please enter right choice")

    elif en==7:
        print("Convert Num from radix A to radix B")
        num=input("Enter what you want you wnat to convert:")
        a=int(input("Radix A:"))
        b=int(input("Radix B:"))
        convert_to_base(num,a,b)

    elif en==8:
        print("--------------------------Thank You------------------------")
        break
    else:
        print("Please enter a valid choice")
              

        

    
