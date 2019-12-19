from tkinter import *
masterwindow =Tk()
masterwindow.title("login")
username =StringVar()
password= StringVar()
masterwindow.geometry("+500+500")
masterwindow.minsize(1000,500)
def sayhello():
    username=userEntery.get()
    password=passEntery.get()
    print("username is",username,"password",password)

l1=Label(masterwindow,text="User Name:",bg="grey",font=("Arial",12,"italic"),relief=GROOVE)
l2=Label(masterwindow,text="PASSWORD:",bg="grey",font=("Arial",12,"bold"),relief=RIDGE)
b1 = Button(masterwindow, bg="gold",fg="red",   text = 'Click me !',command =sayhello)
b2=Button(masterwindow,text="cancel",)

userEntery=Entry(masterwindow)
passEntery=Entry(masterwindow,show=".")

l1.place(x=20,y=40)
userEntery.place(x=150,y=40)

l2.place(x=20,y=80)
passEntery.place(x=150,y=80)

b1.place(x=50,y=150)
b2.place(x=150,y=150)


mainloop()