cost_i=int(input("Enter the initial cost of the car:"))
depre_rt=int(input("Enter the depreciation rate:"))
mant_cst=0
mant_cst_list=[]
mant_6_15=0
for i in range(5):
    mant_cst=mant_cst+0.01*cost_i
    mant_cst_list.append(mant_cst)
    
for i in range(5,15):
    new_mant= mant_cst_list[-1]*(0.5)
    mant_6_15=(mant_cst_list[-1])+ new_mant
    mant_cst_list.append(mant_6_15)

cost=cost_i
val_of_own=[]    
for i in range(15):
    cost=cost-((depre_rt/100)*cost_i)-mant_cst_list[i]
    val_of_own.append(cost)


value=50
km=6000
using_it=[]
for i in range(14):
    new_val=0.1*value
    value=new_val+value
    yer_cst=value*6000
    using_it.append(yer_cst)


for i in range(15):
    if val_of_own[i] < using_it[i]:
        print("The right time to sell the car is :",i+1,"years")
        break
    
if using_it[-1]<val_of_own[-1]:
    print("Sell the car after 15 years")


