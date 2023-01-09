def display_specific_Word_count():
    n=input("Enter word: ")
    f=open("question1_input.txt","r")
    text=f.read()
    y=text.split("\n")
    #print(y)
    #print(text)
    sm=0
    for i in y:
        word=i.split(" ")
        #print(word)
        for i in word:
            if i==n:
                sm+=1
    print("Word Count: ",sm)

def dispaly_all_unique_words():
    uni_list=[]
    print("Unique Words")
    f=open("question1_input.txt","r")
    text=f.read()
    f.close()
    y=text.split("\n")
    #print(y)
    list_elements=[]
    for i in y:
        word=i.split(" ")
        for j in word:
            if j not in list_elements:
                list_elements.append(j)
    #print(list_elements)
    for h in list_elements:
        if h not in uni_list:
            uni_list.append(h)

    for a in uni_list:
        print(i,end=" ; ")
        
def all_word_counts():
    print("Word count")
    f={}
    f=open("question1_input.txt","r")
    text=f.read()
    f.close()
    print(text)
    lines=text.split("\n")
    freq = {}
    for i in lines:
        word=i.split(" ")
        for items in word:
            freq[items] = word.count(items)

    #print(freq)     
    for key, value in freq.items():
        print (key,":", value)
    
    #change code as copied from geeks for geeks.

def replace_word():
    find_word=str(input("Enter the word you want to be replaced: "))
    replace_word=str(input("Enter word that will replace it:"))
    file=open("question1_input.txt","r")
    text=file.readlines()
    file.close()
    #print(text)
    new_text=[]
    for i in text:
        y=i.replace(find_word,replace_word)
        new_text.append(y)
    #print(new_text)
    file1=open("question1_input.txt","w")
    file1.writelines(new_text)
    file1.close()
    print("Replaced Sucessfully")

while True:
    print("-------------------------------------------------------------------")
    print("Enter your choice:")
    print("1.Display specific Word Count")
    print("2.Display all Unique Words")
    print("3.Display all Word Counts")
    print("4.Replace word")
    print("5.Quit")
    op=int(input(""))
    if op==1:
        display_specific_Word_count()
    elif op==2:
        dispaly_all_unique_words()
    elif op==3:
        all_word_counts()
    elif op==4:
        replace_word()
    elif op==5:
        break
    else:
        print("Please enter a valid input")
          
