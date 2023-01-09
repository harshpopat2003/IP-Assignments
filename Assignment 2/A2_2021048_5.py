def noteCreate():
    #for major
    notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]*2
    main_notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    major=[0,2,4,5,7,9,11]
    for i in main_notes:
        scale=[]
        root = notes.index(i)
        S = notes[root:root+12]
        for j in major:
            y=S[j]
            scale.append(y)
        f=open("scaleMajor.txt","a")
        for k in scale:
            f.write(k)
            f.write(" ")
        f.write(i)
        f.write("'")
        f.write("\n")
        f.close()

    #for minor
    notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]*2
    main_notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    minor=[0,2,3,5,7,8,10]
    for i in main_notes:
        scale=[]
        root = notes.index(i)
        S = notes[root:root+12]
        for j in minor:
            y=S[j]
            scale.append(y)
        f=open("scaleMinor.txt","a")
        for k in scale:
            f.write(k)
            f.write(" ")
        f.write(i)
        f.write("'")
        f.write("\n")
        f.close()

noteCreate()
#change varible name such as root notes scale
def majorNotes(root):
    f=open("scaleMajor.txt",'r')
    list1=f.readlines()
    for i in list1:
        if i[0]==root:
            print(i)
            break
    f.close()

def minorNotes(root):
    f=open("scaleMinor.txt",'r')
    list1=f.readlines()
    for i in list1:
        if i[0]==root:
            print(i)
            break
    f.close()         


while True:
    root_note=input("Enter the root Note: ")
    type1=input("Enter the type of Scale (Major/ Minor): ")
    if type1.upper()=="MAJOR":
        majorNotes(root_note)
        print("YES=1 NO=0")
        ex=int(input("Want to exit: "))
        if ex==1:
            break
        elif ex==0:
            pass
        else:
            print("please enter valid option")
    elif type1.upper()=="MINOR":
        minorNotes(root_note)
        print("YES=1 NO=0")
        ex=int(input("Want to exit: "))
        if ex==1:
            print("-----------------Thank you--------------------")
            break
        elif ex==0:
            pass
        else:
            print("please enter valid option")

#error in the ex part of want to continue
            

        

