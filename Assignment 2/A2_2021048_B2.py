PQ=input("Enter value of P and Q (Space seperated): ")
list1=PQ.split(" ")
MN=input("Enter value of M ans N (Space seperated): ")
list2=MN.split(" ")
fl_list=[]
m=int(list2[0])
n=int(list2[1])


while m>0:
    l1=input("")
    if len(l1)==4:
        fl_list.append(l1)
        m=m-1
    else:
        print(f"the line should contain {n} characters")
#print(fl_list)
fl_lt=[]
for i in fl_list:
    z=list(i)
    fl_lt.append(z)
#print(fl_lt)


matrix=fl_lt[:]
#print(fl_list)
#print(matrix)
doja_cat_grammy=int(list1[0])-1
dj_snack_grammy=int(list1[1])-1
doja_list=[]
dj_list=[]
for i in range(n):
    doja_cat_grammy=doja_cat_grammy+1
    dj_snack_grammy=dj_snack_grammy+1
    if i%2==0:
        sum_list=[]
        for j in range(n):
           sum1=0
           for h in fl_list:
               if ord(h[j])==49 or ord(h[j])==48:
                   sum1=sum1+int(h[j])
           sum_list.append(sum1)
        height=max(sum_list)
        #print(height)
        index=sum_list.index(height)
        fame=height*doja_cat_grammy
        doja_list.append(fame)
        #print(doja_list)
        for k in matrix:
            if k[index]=="1":
                k[index]="D"
        #for h in fl_list:
            #del h[index]
        #print(fl_list)
        #print(matrix)

    elif i%2==1:
            sum_list=[]
            for j in range(n):
               sum1=0
               for h in fl_list:
                   if ord(h[j])==49 or ord(h[j])==48:
                       sum1=sum1+int(h[j])
               sum_list.append(sum1)
            height=max(sum_list)
            #print(height)
            index=sum_list.index(height)
            fame=height*dj_snack_grammy
            dj_list.append(fame)
            #print(dj_list)
            for k in matrix:
                if k[index]=="1":
                    k[index]="S"
            #for h in fl_list:
                #del h[index]
            #print(fl_list)
            #print(matrix)




print(sum(doja_list),"",sum(dj_list))
print()
for i in matrix:
    for x in i:
        print(x,end="")
    print()
               
           
