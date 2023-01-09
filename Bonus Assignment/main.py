# all modules needed to import  
from tkinter import *
from subprocess import call
from datetime import datetime
from datetime import date

#for display of current date and time 
today=date.today()
d1=today.strftime("%d/%m/%Y")
now=datetime.now()
current_time=now.strftime("%H:%M:%S")


#to check the password and username 
def command1(event):
    if entry1.get()=='harsh' and entry2.get()=='123456': 
        root.destroy()
        call(["python","Hotel_management_system.py"])
    else:
        label=Label(root,text="Wrong Password or Username",fg="red",font="times 15")
        label.pack()
        label2=Label(root,text=" Please retry again.",fg="red",font="times 15")
        label2.pack()
        
    
#defining root base of tkinter program       
root = Tk()
root.iconbitmap('hotel.ico')
root.geometry('500x520')
root.title('LOGIN SCREEN')
hotel_image=PhotoImage(file='HOTEL.gif')
photo=Label(root,image=hotel_image,bg='white')
photo.pack()

#main screen 
mylabelmain=Label(root,text="LOGIN YOUR ACCOUNT",font="Courier 20 bold")
mylabelmain.pack()

#entering username
mylabel=Label(root,text="Username:",font="Courier 15")
mylabel.pack()

entry1=Entry(root,width=25)
entry1.pack()

#entering password
label2=Label(root,text="Password:",font="Courier 15")
label2.pack()

entry2=Entry(root,show='*',width=25)
entry2.pack()
#blind buttontype entry for enter on keyboard 
entry2.bind('<Return>',command1)

#exit the program
button1=Button(root,text='Cancel',font="Courier 12",command=root.destroy)
button1.pack()

#display of date and time in tkinter 
date= Label(root, text=d1, fg="white", bg="black", font="times 13")
date.place(x=390,y=450)

time=Label(root,text=current_time,fg="white", bg="black",font="times 13")
time.place(x=390,y=420)

#infinitly looping the GUI to work 
root.mainloop()
