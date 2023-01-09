from tkinter import *

def searching_data():
    import csv
    gst=[]
    f1=open("guest_list.csv","r")
    gs=e1.get()
    gst=csv.reader(f1)

    for row in gst:
        if row==[]:
            pass
        elif row[0]==gs:
            name=row[0]
            address=row[1]
            phone_no=row[2]
            email_id=row[3]
            room_no=row[4]
            room_type=row[5]
            cost_of_stay=row[7]
            check_in_date=row[8]
            check_in_time=row[9]
            divider=Label(root,text="-------------------------------------------------------------------------------------------------------------------------------------",font="times 15 bold")
            divider.place(x=0,y=160)
            label2=Label(root,text="Guest name    :",font="times 15 bold")
            label2.place(x=50,y=200)
            label3=Label(root,text=name,font="times 15 bold")
            label3.place(x=200,y=200)
            label4=Label(root,text="Guest Address   :",font="times 15 bold")
            label4.place(x=50,y=230)
            label5=Label(root,text=address,font="times 15 bold")
            label5.place(x=200,y=230)
            label6=Label(root,text="Guest phone no :",font="times 15 bold")
            label6.place(x=50,y=260)
            label7=Label(root,text=phone_no,font="times 15 bold")
            label7.place(x=200,y=260)
            label8=Label(root,text="Guest Email_ID:",font="times 15 bold")
            label8.place(x=50,y=290)
            label9=Label(root,text=email_id,font="times 15 bold")
            label9.place(x=200,y=290)
            label10=Label(root,text="Guest room no :",font="times 15 bold")
            label10.place(x=50,y=320)
            label11=Label(root,text=room_no,font="times 15 bold")
            label11.place(x=200,y=320)
            label12=Label(root,text="Room Type :",font="times 15 bold")
            label12.place(x=50,y=350)
            label13=Label(root,text=room_type,font="times 15 bold")
            label13.place(x=200,y=350)              
            label14=Label(root,text="Check in Date/Time: :",font="times 15 bold")
            label14.place(x=50,y=380)
            label15=Label(root,text=check_in_date,font="times 15 bold")
            label15.place(x=230,y=380)
            label16=Label(root,text=check_in_time,font="times 15 bold")
            label16.place(x=330,y=380)

        else:
            label17=Label(root,text="GUEST NAME WRONG OR DOES NOT EXIST",fg='red',font="times 15 bold")
            label17.place(x=50,y=200)
            divider2=Label(root,text="-------------------------------------------------------------------------------------------------------------------------------------",font="times 15 bold")
            divider2.place(x=0,y=160)
            label18=Label(root,text="Please enter correct guest name",fg='red',font='times 15 bold')
            label18.place(x=50,y=230)

root = Tk()
root.iconbitmap('hotel.ico')
root.geometry('1000x500')
root.title('SEARCHING DATA')


label1=Label(root,text="YOU CHOICE WAS : SEARCHING GUEST DETAILS",font="times 30 bold")
label1.place(x=10,y=30)

label2=Label(root,text="---------------------------------------------------------------------------------------------",font="times 25 bold")
label2.place(x=0,y=75)

#entering room no to be checked out 
label3=Label(text="ENTER THE GUEST NAME:",font="times 20 bold")
label3.place(x=20,y=120)

e1=Entry(root,width=35,font="times 18")
e1.place(x=380,y=125)

#button to diplay all data of the room no entered 
button1=Button(root,text="OK",font="times 15 bold",command=searching_data)
button1.place(x=820,y=120)
root.mainloop()

