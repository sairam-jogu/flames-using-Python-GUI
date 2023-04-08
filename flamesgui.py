from cProfile import label
from tkinter import *
from tkinter import font


def remove_char(list1,list2):
    for i in range (len(list1)):
        for j in range (len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]

                list1.remove(c)
                list2.remove(c)

                list3 = list1 + ["*"] + list2

                return [list3,True]
    list3 = list1 + ["*"] + list2
    return [list3,False]

def tell_status():

    p1 = player1_field.get()
    p1 = p1.lower()
    p1.replace(" ","")
    p1_list = list(p1)

    p2 = player2_field.get()
    p2.replace(" ","")
    p2_list = list(p2)

    condition_1 = True

    while condition_1 :
        ret_list = remove_char(p1_list,p2_list)
        con_list = ret_list[0]     ##concatenated list
        condition_1 = ret_list[1]      ##here it will check the condition

        star_index = con_list.index("*")
        ## now we can slice the elements 

        p1_list = con_list[:star_index]
        p2_list = con_list[star_index+1 :]

    count = len(p1_list) + len(p2_list)


    result = ["Friends","Love","Affection","Marriage","Enemy","Sister"]

    while len(result) > 1:
        split_index = ((count % len(result)) -1)

        if split_index >= 0:
            right = result[split_index+1: ]
            left = result[ :split_index]
            result = right + left 

        else :
            result = result[ :len(result)-1]
    status_field.insert(10,result[0])

def clear_all():
    player1_field.delete(0,END)
    player2_field.delete(0,END)
    status_field.delete(0,END)
    player1_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.configure(background='black')
    root.geometry("350x125")
    root.title("Flames Project 🧡")
    text1 = Text(root)
    text1.insert(INSERT,"FLAMES PROGRAM")
    text1.tag_config("write here",background="black",font=(40),foreground="white")
    label1 = Label(root,text="Name1: ",fg='orange',bg='blue',font=(20))
    label2 = Label(root,text="Name2: ",fg='orange',bg='blue',font=(20))
    label3 = Label(root,text="Relationship status",fg='black',bg='pink',font=(20))
    label1.grid(row=1,column=0,sticky="E")
    label2.grid(row=2,column=0,sticky="E")
    label3.grid(row=4,column=0,sticky="E")

    player1_field = Entry(root)
    player2_field = Entry(root)
    status_field = Entry(root)

    player1_field.grid(row=1,column=1,ipadx="30")
    player2_field.grid(row=2,column=1,ipadx="30")
    status_field.grid(row=4,column=1,ipadx="30")

    button1 = Button(root,text = 'Submit',bg='white',fg='black',font=(20),command=tell_status)
    
    button2 = Button(root,text = 'Clear',bg='white',fg='black',font=(20),command=clear_all)

    button3 = Button(root,text="Quit",bg='white',fg='black',font=(20),command=quit)

    button1.grid(row=3,column=1)
    button2.grid(row=5,column=1)
    button3.grid(row=6,column=1)
    root.mainloop()





    