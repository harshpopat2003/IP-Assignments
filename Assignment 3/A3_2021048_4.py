class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        
    def __repr__(self):
        return self.firstname+" "+self.lastname+" "+str(self.age)

    

def sort_attribute(list1,type1):
    if(type1=='firstname'):
        list1.sort(key = lambda x: x.firstname)
        print("Order:")
        for i in list1:
            print(i)
        #print(list1)
    elif(type1=='lastname'):
        list1.sort(key = lambda x: x.lastname)
        print("Order:")
        for i in list1:
            print(i)
        #print(list1)
    elif(type1=='lastname'):
        list1.sort(key = lambda x: x.age)
        print("Order:")
        for i in list1:
            print(i)
        #print(list1)
          
    
while True:
    print("Welcome to the Application!!")
    print()
    n=int(input("Specify number of people to be enrolled: "))
    list1=[]
    for i in range(n):
        first=input(f"Enter Firstname for Person {i+1} : ")
        last=input(f"Enter Lastname for Person {i+1} : ")
        ag=int(input(f"Enter Age for Person {i+1} : "))
        list1.append(Person(first,last,ag))


    m=int(input("Specific No of Queries: "))
    for i in range(m):
        que=input(f"Query {i+1}: ")
        sort_attribute(list1,que)
        
    option=input("Thanks for using the Application, if you wish to restart, press “Y” else press “N” to exit: N")
    if option.lower()=="y":
        pass
    elif option.lower()=="n":
        print("Exits!")
        break
    else:
        print("Please input a valid Choice")
    
    

