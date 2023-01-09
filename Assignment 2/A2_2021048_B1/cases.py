def function1(word):
    h=int(word)
    j=h//3
    v=str(word)+"B1_ans.txt"
    file1=open(v,"w")
    file1.write(str(j))
    file1.close()


def generateData():
    n=int(input("No of inputs you want to enter: "))
    list1=[]
    for i in range(n):
        y=input("Enter the data numbers: ")
        list1.append(y)
    for i in list1:
        t=str(i)+"B1.txt"
        file=open(t,"w")
        file.write(i)
        file.close()
    for i in list1:
        function1(i)

generateData()
    
        
