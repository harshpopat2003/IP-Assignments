from datetime import datetime
class BankAccount:
    def __init__(self,username,password,current_balance):
        self.username = usr
        self.password=passw
        self.current_balance=balance
        f=open(self.username+".txt","a")
        f.close()

    def authenticate(self):
        sec_pass=input("Secret Password:")
        if sec_pass==self.password:
            return True
        else:
            return False

    def deposit(self,amount):
        z=0
        while True:
            z=z+1
            if z<=3:
                pass
            else:
                print("3 Failed attempts so back account locked. PLease Contact the administrator")
                break
            y=self.authenticate()
            if y== True:
                self.current_balance=amount+self.current_balance
                f=open(self.username+".txt","a")
                k=str(datetime.now())
                f.write(k+" "+ f"The amount of Rupees {amount} has been added"+" "+f"Current Balance -> {self.current_balance}"+"\n")
                f.close()
                break
            elif y== False:
                pass

    def withdraw(self,amount):
        z=0
        while True:
            z=z+1
            if z<=3:
                pass
            else:
                print("3 Failed attempts so back account locked. PLease Contact the administrator")
                break
            y=self.authenticate()
            if y== True:
                if self.current_balance>=amount:
                    self.current_balance=self.current_balance-amount
                    f=open(self.username+".txt","a")
                    k=str(datetime.now())
                    f.write(k+" "+ f"The amount of Rupees {amount} has been debited"+" "+f"Current Balance -> {self.current_balance}"+"\n")
                    f.close()
                    break
                else:
                    print("Low Balance ! ! Cannot withdraw now.")
                    break
            elif y== False:
                y=self.authenticate()

    def bankstatement(self):
        z=0
        while True:
            z=z+1
            if z<=3:
                pass
            else:
                print("3 Failed attempts so back account locked. Please Contact the administrator")
                break
            y=self.authenticate()
            if y== True:
                print("Bank Statement")
                print()
                f=open(self.username+".txt","r")
                rd=f.readlines()
                for i in rd:
                    print(i)
                f.close()
                break
            elif y== False:
                y=self.authenticate()

print("Welcome to IIITD Bank")
print()
usr=input("Enter Name: ")
passw=input("Enter Password: ")
balance=float(input("Starting balance for your Account: "))
d=BankAccount(usr,passw,balance)
while True:
    print("--------------------------------------------------------------------------------")
    print("Select your Option ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Bank Statement")
    print("4. Exit ")
    option=int(input("Enter Your Choice: "))
    if option==1:
        amount=float(input("Enter the amount to be deposited: "))
        t=d.deposit(amount)
        print("Deposition Sucessfull!!")
    elif option==2:
        amount=float(input("Enter the amount to be Withdrawn: "))
        t=d.withdraw(amount)
        print("Withdrawal Succesfull!!")
    elif option==3:
        d.bankstatement()
    elif option==4:
        print("Thank you!!")
        break
    else:
        print("Please input a right choice")


 #change in the last yes or no if wanted            
            
                
