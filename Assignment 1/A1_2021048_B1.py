price_item1=int(input("Price of Item1: "))
price_item2=int(input("Price of Item2: "))
price_item3=int(input("Price of Item3: "))
print("<----------------------------------------------------------------------")
print("---------------------------------------------------------------------->")
print("Discount Details")

dis_combo_1=int(input("Provide discount(in percentage) for the 1st sever combo: "))
dis_combo_2=int(input("Provide discount(in percentage) for the 2nd saver combo: "))
dis_combo_3=int(input("Provide discount(in percentage) for the 3rd saver combo: "))
print("<------------------------------------------------------------------")

phone_no=int(input("Provide your 10 digit contact number :"))

#all calculations
combo1=(price_item1+price_item2)*(dis_combo_1/100)
combo2=(price_item1+price_item3)*(dis_combo_2/100)
combo3=(price_item2+price_item3)*(dis_combo_3/100)
super_saver=(price_item1+price_item2+price_item3)*0.28

total_1=(price_item1+price_item2)-combo1
total_2=(price_item1+price_item3)-combo2
total_3=(price_item2+price_item3)-combo3
total_saver=(price_item1+price_item2+price_item3)-super_saver

print("The resulting catalogue is:")
print("<----------------------------------------------------------------------")
print(".......................................................................")
print("Delhi Days")
print("R-Block,Model Town 3")
print("Delhi: 110009")
print("<----------------------------------------------------------------------")
print(".......................................................................")
print(f"""          Item         Price(perPack)
          |            |
          Item1        {price_item1}
          Item2        {price_item2}
          Item3        {price_item3}
          ComboPack1   {total_1}
          ComboPack2   {total_2}
          ComboPack3   {total_3}
          SuperSaver   {total_saver}""")
print("<----------------------------------------------------------------------")
print(".......................................................................")
print("For home deliver, contact here: ",phone_no)
