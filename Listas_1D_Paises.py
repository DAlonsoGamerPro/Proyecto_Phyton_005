from tkinter import *
import random
root = Tk()
root.title("Lista de Países")
root.geometry("400x400")

enter_name = Entry(root)
enter_name.place(relx=0.5, rely=0.2, anchor=CENTER)
friend_list = Label(root)
random_number_label = Label(root)
unlucky_friend = Label(root)
list1=[]

def add_friend():
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list["text"]="Lista de Países:  " + str(list1)
    
def random_number():
    length = len(list1)
    random_no = random.randint(0,length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    unlucky_friend["text"] = "El País que salió es...  " + str(generated_random_number)
    
btn = Button(root,text="Añadir Nombre de País a Lista", command=add_friend)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

friend_list.place(relx=0.5, rely=0.4, anchor=CENTER)

btn1 = Button(root,text="¿Quién fué el país elegido?", command=random_number)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

random_number_label.place(relx=0.5,rely=0.6,anchor=CENTER)

unlucky_friend.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()