from tkinter import  *
import random as rd
import datetime 
import mysql.connector as sqltor
import tkinter.messagebox

con=sqltor.connect(host="localhost",user="root",password="tiger")
cur=con.cursor()
cur = con.cursor(buffered=True) 
cur.execute("create database if not exists result_management")

cur.execute("use result_management")

cur.execute("create table if not exists st_details"
            "("
            "st_id varchar(12) not null,"
            "firstname char(20),"
            "lastname char(20),"
            "age int,"
            "gender char(1),"
            "phone varchar(10),"
            "PRIMARY KEY (st_id))")

#STUDENT RECORD FUNCTIONS
def entry():
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
      
    cur.execute("insert into st_details values('%s','%s','%s','%s','%s','%s')"%(p1,p2,p3,p4,p5,p6))
    con.commit()
    tkinter.messagebox.showinfo("DONE", "RECORD HAS BEEN ADDED!")
    root2.destroy()

def create_srec():
    global root2
    root2=Tk()
    label=Label(root2,text="CREATE STUDENT RECORD",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=500,width=400)
    frame.pack()

    global e1,e2,e3,e4,e5,e6
    l1=Label(root2,text="Student ID")
    l1.place(x=10,y=130)
    e1=Entry(root2)
    e1.place(x=100,y=130)
    l2=Label(root2,text="First Name")
    l2.place(x=10,y=170)
    e2=Entry(root2)
    e2.place(x=100,y=170)
    l3=Label(root2,text="Last Name")
    l3.place(x=10,y=210)
    e3=Entry(root2)
    e3.place(x=100,y=210)
    l4=Label(root2,text="Age")
    l4.place(x=10,y=250)
    e4=Entry(root2)
    e4.place(x=100,y=250)
    l5=Label(root2,text="Gender (M\F)")
    l5.place(x=10,y=290)
    e5=Entry(root2)
    e5.place(x=100,y=290)
    l6=Label(root2,text="Phone")
    l6.place(x=10,y=330)
    e6=Entry(root2)
    e6.place(x=100,y=330)
    
    b=Button(root2,text="SUBMIT",command=entry)
    b.place(x=150,y=410)

def searchrec():
    global en1
    p1=en1.get()
    cur.execute('select * from st_details where st_id=(%s)',(p1,))
    dat=cur.fetchall()
    if len(dat)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        global root4
        root4=Tk()
        label0= Label(root4,text="SEARCH RESULT",font='arial 23 bold')
        label0.pack()
        frame=Frame(root4,height=150,width=600)
        frame.pack()
        Label(root4,text="Student ID").place(x=50,y=50)
        Label(root4,text=dat[0][0]).place(x=50,y=80)
        Label(root4,text="First Name").place(x=160,y=50)
        Label(root4,text=dat[0][1]).place(x=160,y=80)
        Label(root4,text="Last Name").place(x=240,y=50)
        Label(root4,text=dat[0][2]).place(x=240,y=80)
        Label(root4,text="Age").place(x=320,y=50)
        Label(root4,text=dat[0][3]).place(x=320,y=80)
        Label(root4,text="Gender").place(x=400,y=50)
        Label(root4,text=dat[0][4]).place(x=400,y=80)
        Label(root4,text="Phone").place(x=480,y=50)
        Label(root4,text=dat[0][5]).place(x=480,y=80)
        Label(root4,text="----------"*10).place(x=30,y=65)
    root3.destroy()

def search_srec():
    global root3
    root3=Tk()
    label=Label(root3,text="SEARCH STUDENT RECORD",font='arial 25 bold')
    label.pack()
    frame=Frame(root3,height=250,width=250)
    frame.pack()
    
    global en1
    l1=Label(root3,text="Enter Student ID")
    l1.place(x=10,y=130)
    en1=Entry(root3)
    en1.place(x=120,y=130)
    b=Button(root3,text="SUBMIT",command=searchrec)
    b.place(x=150,y=200)

def updaterec():
    global en2,p2,x4,xx
    p2=en2.get()
    cur.execute('select * from st_details where st_id=(%s)',(p2,))
    dat=cur.fetchall()   
    if len(dat)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
      global root6
      root6=Tk()
      frame=Frame(root6,height=500,width=800)
      frame.pack()
      l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
      l1.place(x=50,y=10)
      l2=Label(root6,text='WHAT DO YOU WANT TO CHANGE')
      l2.place(x=50,y=140)
      l3=Label(root6,text='1   FIRST NAME')
      l3.place(x=50,y=170)
      l4=Label(root6,text='2   LAST NAME')
      l4.place(x=50,y=190)
      l5=Label(root6,text='3   AGE')
      l5.place(x=50,y=210)
      l6=Label(root6,text='4   GENDER')
      l6.place(x=50,y=230)
      l7=Label(root6,text='5   PHONE')

      x2=Label(root6,text='Enter')
      x2.place(x=50,y=320)
      x4=Entry(root6)
      x4.place(x=100,y=320)
      xx=Entry(root6)
      xx.place(x=160,y=350)
      Label(root6,text="Student ID").place(x=50,y=80)
      Label(root6,text=dat[0][0]).place(x=50,y=110)
      Label(root6,text="First Name").place(x=160,y=80)
      Label(root6,text=dat[0][1]).place(x=160,y=110)
      Label(root6,text="Last Name").place(x=240,y=80)
      Label(root6,text=dat[0][2]).place(x=240,y=110)
      Label(root6,text="Age").place(x=320,y=80)
      Label(root6,text=dat[0][3]).place(x=320,y=110)
      Label(root6,text="Gender").place(x=400,y=80)
      Label(root6,text=dat[0][4]).place(x=400,y=110)
      Label(root6,text="Phone").place(x=480,y=80)
      Label(root6,text=dat[0][5]).place(x=480,y=110)
      Label(root6,text="--------"*20).place(x=20,y=65)
      b=Button(root6,text='Submit',command=mod_fun)
      b.place(x=50,y=420)
      L1=Label(root6,text='OLD DETAILS')
      L1.place(x=50,y=50)
      L2=Label(root6,text='ENTER NEW DETAIL')
      L2.place(x=50,y=350)
      root6.mainloop()
      root5.destroy()

def mod_fun():
    global p2,xx,x4
    val=xx.get()
    col=IntVar()
    col=x4.get()
    c=int(col)
    if c==3:
        v=int(val)
    else:
        v=str(val)

    if c==1:
        cur.execute("update st_details set firstname = '%s' where st_id ='%s'"%(v,p2))
        con.commit()
        tkinter.messagebox.showinfo(" ","YOUR DATA HAS BEEN MODIFIED")

    elif c==2:
        cur.execute("update st_details set lastname = '%s' where st_id = '%s'"%(v,p2))
        con.commit()
        tkinter.messagebox.showinfo(" ","YOUR DATA HAS BEEN MODIFIED")
        
    elif c==3:
        cur.execute("update st_details set age = %s where st_id = '%s'"%(v,p2))
        con.commit()
        tkinter.messagebox.showinfo(" ","YOUR DATA HAS BEEN MODIFIED")
        
    elif c==4:
        cur.execute("update st_details set gender = '%s' where st_id = '%s'"%(v,p2))
        con.commit()
        tkinter.messagebox.showinfo(" ","YOUR DATA HAS BEEN MODIFIED")
        
    elif c==5:
        cur.execute("update st_details set phone = '%s' where st_id= '%s'"%(v,p2))
        con.commit()
        tkinter.messagebox.showinfo(" ","YOUR DATA HAS BEEN MODIFIED")

    root6.destroy()
    
def update_srec():
    global root5
    root5=Tk()
    label=Label(root5,text="UPDATE STUDENT RECORD",font='arial 25 bold')
    label.pack()
    frame=Frame(root5,height=250,width=250)
    frame.pack()
    
    global en2
    l1=Label(root5,text="Enter Student ID")
    l1.place(x=10,y=130)
    en2=Entry(root5)
    en2.place(x=160,y=130)
    b=Button(root5,text="SUBMIT",command=updaterec)
    b.place(x=150,y=200)

def delrec():
    global en3
    p3=en3.get()
    cur.execute('select * from st_details where st_id=(%s)',(p3,))
    dat=cur.fetchall()
    if len(dat)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        cur.execute('delete from st_details where st_id=(%s)',(p3,))
        tkinter.messagebox.showinfo("DONE", "STUDENT RECORD HAS BEEN DELETED")
    root7.destroy()

def delete_srec():
    global root7
    root7=Tk()
    label=Label(root7,text="DELETE STUDENT RECORD",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=250,width=250)
    frame.pack()
    
    global en3
    l1=Label(root7,text="Enter Student ID")
    l1.place(x=10,y=130)
    en3=Entry(root7)
    en3.place(x=160,y=130)
    b=Button(root7,text="SUBMIT",command=delrec)
    b.place(x=150,y=200)

#MAIN WINDOW
root1=Tk()
root1.title("Tkinter Project")
root1.configure(background='black')
frame=Frame(root1,height=1000,width=2000,bg='black')
frame.pack()

head=Label(root1,text="STUDENT MANAGEMENT SYSTEM",font="arial 30 bold",bg='thistle1')
head.place(x=375,y=0)
photo1= PhotoImage(file="resultf.png")
pic=Label(root1, image=photo1,bg='black')
pic.place(x=550,y=80)

b1=Button(text="Create Record",font="arial 20 bold",bg='snow',command=create_srec)
b1.place(x=20,y=400)
b2=Button(text=" Search Record",font="arial 20 bold",bg='snow',command=search_srec)
b2.place(x=20,y=500)
b3=Button(text="Update Record",font="arial 20 bold",bg='snow',command=update_srec)
b3.place(x=20,y=600)
b4=Button(text="Delete Record",font='arial 20 bold',bg='snow',command=delete_srec)
b4.place(x=1000,y=450)
b5=Button(text="Exit",font='arial 20 bold',bg='snow',command=root1.destroy)
b5.place(x=1000,y=550)

root1.mainloop()

