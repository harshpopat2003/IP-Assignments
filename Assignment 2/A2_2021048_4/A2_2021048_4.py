def getting_final_score_of_student(name_of_file):
    file1=open(name_of_file,"r")
    file_ans_key=open(r"C:\Users\harsh\Desktop\ip final a2\for A2 Q4\Admin\AnswerKey.txt","r")
    f1=file1.read()
    l1=f1.split("\n")
    f2=file_ans_key.read()
    l2=f2.split("\n")
    score=0
    for i in range(len(l1)):
        if l1[i][-1]==l2[i][-1]:
            score=score+4
        elif l1[i][-1]=="-":
            pass
        elif l1[i][-1]!=l2[i][-1]:
            score=score-1
    file1.close()
    file_ans_key.close()
    return score




#READING THE REGISTERED STUDENT FILE 
with open(r"C:\Users\harsh\Desktop\ip final a2\for A2 Q4\Admin\Registered_Students.txt","r") as f:
    list1=f.readlines()
    #print(list1)
    for i in list1:
        list2=i.split(" ")
        y=list2[0]
        x=list2[1]
        t=x.replace("\n","")
        #print(t)
        name_of_file=r"C:\Users\harsh\Desktop\ip final a2\for A2 Q4\Students"+"/"+y+"_"+t+".txt"
        #print(name_of_file)
        d=getting_final_score_of_student(name_of_file)
        fila1=open("FinalReport.txt","a")
        fila1.write(y+" "+t+" "+str(d))
        fila1.write("\n")
        fila1.close()

