class Student:
    def __init__(self,name,cgpa,branch):
        self.name=name
        self.cgpa=cgpa
        self.branch=branch
        self.isplaced=False

    def isEligible(self,comp):
        req_cgpa=comp.requiredcgpa
        branch_lst=comp.branches_list
        set_branch_lst=set(branch_lst)
        if self.isplaced==False:
            if self.branch in set_branch_lst:
                if self.cgpa>=req_cgpa:
                    print("Student"+" "+self.name+" "+"is eligible for the company"+" "+comp.company_name)
                    return True
                else:
                    print("Student"+" "+self.name+" "+"is  not eligible for the company"+" "+comp.company_name)
                    return False
            else:
                 print("Student"+" "+self.name+" "+"is  not eligible for the company"+" "+comp.company_name)
                 return False
        else:
             print("Student"+" "+self.name+" "+"is  not eligible for the company"+" "+comp.company_name)
             return False

    def apply(self,d):
        d.appliedStudents.append(self)

    def getPlaced(self):
        self.isplaced=True
        

class Company:
    def __init__(self,company_name,requiredcgpa,branches_list,positionOpen):
        self.company_name=company_name
        self.requiredcgpa=requiredcgpa
        self.branches_list=branches_list
        self.positionOpen=positionOpen
        self.appliedStudents=[]
        self.applicationOpen=True
        #self.appliedStudents.append(Student.name)

    def hireStudents(self):
        cgpa_list=[]
        cgpa_dict={}                                    
        for i in self.appliedStudents:
            cgpa_dict[i.cgpa]=i                          
            cgpa_list.append(i.cgpa)
        cgpa_list.sort(reverse=True)
        cgpa_final_open=[]
        cgpa_final_open=cgpa_list[:self.positionOpen]
        print(f"The Comapany {self.company_name} has hired the following students: ")            
        print()
        hired=[]
        for i in cgpa_final_open:
            std=cgpa_dict[i]                            
            print(std.name)
            hired.append(std)
            std.isplaced=True
            #Student.getPlaced()
            self.positionOpen=self.positionOpen-1
        self.closeApplication(hired)


    def closeApplication(self,hired):
        print(f"The company has hired {len(hired)} student")



no_of_student=int(input("Enter the number of students : "))
std_list=[]
company_list=[]
#change the i thing 
#while no_of_student>0:
for i in range(no_of_student):
    name=input(f"Enter the name of the Student {i+1}: ")
    cgpa=float(input(f"Enter cgpa of student {i+1}: "))
    if cgpa < 0 or cgpa > 10:
      raise Exception("Kindly provide correct and valid cgpa")
    #put exception of cgpa to be only between 0 and 10.
    branch=input(f"Enter Branch of student {i+1}: ")
    #if branch =="CSE" or branch =="CSAM" or branch =="ECE":
    std_list.append(Student(name,cgpa,branch))
    #else:
      #print("Please input the data again as branch not in CSE or CSAM or ECE")
      #no_of_student+=1


no_of_companies=int(input("Enter the number of comapany: "))
for i in range(no_of_companies):
    company_name=input(f"Enter name of company {i+1} ")
    requiredcgpa=float(input(f"Enter required cgpa of Company {i+1} "))
    if requiredcgpa < 0 or requiredcgpa > 10:
      raise Exception("Kindly provide correct and valid cgpa")
    branches_comp=input(f"Enter space seperated branches of Company {i+1} ")
    branches_list=branches_comp.split()
    positionOpen=int(input(f"Enter number of positions Open of Company {i+1} "))
    comp=Company(company_name,requiredcgpa,branches_list,positionOpen)
    company_list.append(comp)
    for h in range(no_of_student):
        hi=std_list[h]
        if hi.isEligible(comp):
            hi.apply(comp)
    comp.hireStudents()


