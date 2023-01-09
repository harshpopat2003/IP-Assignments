def function2(file_path):
    file2=open(file_path, 'r')
    d=int(file2.read())
    #print(d)
    t=d//3
    import os
    path= r"C:\Users\harsh\Desktop\Assignment 2 IP\B1"
    os.chdir(path)
    for j in os.listdir():
        if j.endswith(f"{d}B1_ans.txt"):
            file_path_ans = f"{path}\{j}"
            file4=open(file_path_ans,"r")
            s=int(file4.read())
            #print(s)
            if s==t:
                return("Success")
            else:
                return("Failed")
            



def testing():
    import os
    path= r"C:\Users\harsh\Desktop\Assignment 2 IP\B1"
    os.chdir(path)  
    for i in os.listdir():
        if i.endswith("B1.txt"):
            file_path = f"{path}\{i}"
            m=function2(file_path)
            list2=[]
            if m=="Success" or "Failed":
                if m not in list2:
                    list2.append(m)        
    return(list2)            

f=testing()
y = len(set(f)) == 1 
if y:
    print("SUCCESS")
else:
    print("FAILED")


