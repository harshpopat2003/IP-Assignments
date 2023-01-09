class Laundryservice:
    def __init__(self,name_of_customer,contact_no,email,type_of_cloth,branded,season,customer_id):
        self.name_of_customer = nm
        self.contact_no = contact
        self.email= mail
        self.type_of_cloth=typ_cloth
        self.branded=brd
        self.season=seson
        self.customer_id=cus_id
    

    def customerDetails(self):
        print("-------------------------------------------------------------------------------")
        print("Customer ID: ",end="")
        print(self.customer_id)
        print("Customer Name: ",end="")
        print(self.name_of_customer)
        print("Contact: ",end="")
        print(self.contact_no)
        print("Email: ",end="")
        print(self.email)
        print("Type of Cloth : ",end="")
        print(self.type_of_cloth)
        if self.branded==1:
            print("Branded or Not : True")
        elif self.branded==0:
            print("Branded or Not : False")
    
    def calculatecharge(self):
        self.charge=0
        if self.type_of_cloth.lower()=="cotton":
            self.charge=50
        elif self.type_of_cloth.lower()=="silk":
            self.charge=30
        elif self.type_of_cloth.lower()=="woolen":
            self.charge=90
        elif self.type_of_cloth.lower()=="polyster":
            self.charge=20
        #checking the cost
        if  self.branded==1:
            self.charge=1.5*self.charge
            if  self.season.lower()=="winter":
                self.charge=self.charge/2
            else:
                self.charge=2*self.charge
        elif self.branded==0:
            self.charge=self.charge
            if  self.season.lower()=="winter":
                self.charge=self.charge/2
            else:
                self.charge=2*self.charge
        return(self.charge)
    
    def final_deltails(self):
        self.customerDetails()
        t=self.calculatecharge()
        print("Total Charge: ",end="")
        print(t)
        if t>200:
            print("To be returned in 4 Days")
        else:
            print("To be returned in 7 Days")



cus_id=0
no_of_cus=int(input("Enter the no of Customers:"))
for i in range(no_of_cus):
    cus_id=cus_id+1
    nm=input("Name of Customer : ")
    contact=int(input("Contact No.: "))
    mail=input("Email : ")
    typ_cloth=input("Type of Cloth : ")
    if typ_cloth.lower()== "woolen" or typ_cloth.lower()== "cotton" or typ_cloth.lower()=="silk" or typ_cloth.lower()=="polyster":
        pass
    else:
        raise Exception("The type of cloth has to be either Cotton, Silk, Woolen or Polyster")

    brd=int(input("Branded? : "))
    seson=input("Season: ")
    d=Laundryservice(nm,contact,mail,typ_cloth,brd,seson,cus_id)
    d.final_deltails()

