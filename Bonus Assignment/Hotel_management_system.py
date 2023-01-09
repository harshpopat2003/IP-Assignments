#all modules needed imported 
from tkinter import *
from subprocess import call

#all the functions to call program based on choice 
def check_in_call():
    call(["python","check_in.py"])
def check_out_call():
    call(["python","check_out.py"])
def restaurent_call():
    call(["python","room_check_for_restaurant.py"])
def guest_list():
    call(["python","show_guest_list.py"])
def guest_details():
    call(["python","searching_guest_data_by_name.py"])

#basic defination of tkinter window
root = Tk()
root.title("Hotel Mangement System")
root.iconbitmap('hotel.ico')
root.geometry("650x750")

#Topmost label
myLabel= Label(root,text="WELCOME TO HOTEL MANGEMENT SYSTEM !!!",font="Courier 20 bold")
myLabel.pack()

#Check in button
mybutton = Button(root,text="1. CHECK INN", padx=91, pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=check_in_call)
mybutton.pack()

#show all the guest list button
mybutton2 = Button(root,text="2. SHOW GUEST LIST",padx=43, pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=guest_list)
mybutton2.pack()

#show guest details
mybutton6= Button(root,text= "3. SHOW GUEST DETAILS",padx=19, pady=30 ,bg='navy blue', fg='white',font="Courier 20 bold",command=guest_details)
mybutton6.pack()

#function call to check out the guest 
mybutton3= Button(root,text= "4. CHECK OUT",padx=91, pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=check_out_call)
mybutton3.pack()

#restaurent button
mybutton5=Button(root,text="5. RESTAURENT",padx=83,pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=restaurent_call)
mybutton5.pack()

#exit button 
mybutton7= Button(root,text= "6. EXIT",padx=130, pady=30 ,bg='navy blue', fg='white',font="Courier 20 bold",command=root.destroy)
mybutton7.pack()

#infinite loop for GUI to work 
root.mainloop()
