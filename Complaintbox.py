from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


w=Tk()
w.geometry('1000x500')
w.title('Comlaint_Box')
ctype=StringVar()
cspec=StringVar()
gend=StringVar()




#Labels
l1=Label(w, text='Select your complaint type',width=30)
l1.grid(row=0, column=0)
l2=Label(w, text='Specify your complaint',width=30)
l2.grid(row=1, column=0)
l3=Label(w, text='First name',width=30)
l3.grid(row=2, column=0)
l4=Label(w, text='Last name',width=30)
l4.grid(row=3, column=0)
l5=Label(w, text='Email',width=30)
l5.grid(row=4, column=0)
l6=Label(w, text='Adress',width=30)
l6.grid(row=5, column=0)
l7=Label(w, text='Phone No.',width=20)
l7.grid(row=6, column=0)
l8=Label(w, text='Gender',width=30)
l8.grid(row=7, column=0)
l9=Label(w, text='Enter complaint',width=30)
l9.grid(row=8, column=0)




#Function to store
def add():
    db=mysql.connector.connect(host='localhost',user='root',password='Akash@2000',database='complaintbox')
    cur=db.cursor()
    s='insert into complaints(ctype,cspec,fname,lname,email,address,gender,comp) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    k1=ctype.get()
    k2=cspec.get()
    k3=e3.get()
    k4=e4.get()
    k5=e5.get()
    k6=e6.get()
    k8=gend.get()
    k9=e9.get()
    b=(k1,k2,k3,k4,k5,k6,k8,k9)
    cur.execute(s,b)
    messagebox.showinfo('stock','Data stored...')
    db.commit()




#Function to fetch
def fetch():
    db=mysql.connector.connect(host='localhost',user='root',password='Akash@2000',database='complaintbox')
    cur=db.cursor()
    cur.execute('select *from complaints')
    data=cur.fetchall()
    fr=ttk.Frame(w, width=300,height=200)
    fr.grid(column=0, row=8)
    view=ttk.Treeview(fr,columns=(1,2,3,4,5,6,7,8), show='headings', height=8)
    view.grid(column=0, row=0)
    view.heading(1, text='CType')
    view.heading(2, text='CSpec')
    view.heading(3, text='Fname')
    view.heading(4, text='Lname')
    view.heading(5, text='Email')
    view.heading(6, text='Address')
    view.heading(7, text='Gender')
    view.heading(8, text='Complaint')
    for i in data:
        view.insert('','end',values=i)
        print(i)




#Function to clear entry boxes
def clear():
    ctype.set("")
    cspec.set("")
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    gend.set("")
    e9.delete(0,END)




#Entries
e3=Entry(w, width=25)
e3.grid(row=2, column=1)
e4=Entry(w, width=25)
e4.grid(row=3, column=1)
e5=Entry(w, width=25)
e5.grid(row=4, column=1)
e6=Entry(w, width=25)
e6.grid(row=5, column=1)
e7=Entry(w, width=25)
e7.grid(row=6, column=1)
e9=Entry(w, width=25)
e9.grid(row=8, column=1)




#Combobox


    #For l1
cptype=("Police complaints","Vehicle complaints","Financial complaints",)
com1=ttk.Combobox(w, values=cptype, textvariable=ctype, width=22)
com1.grid(row=0, column=1)


    #For l2
cpspec=('harrassed', 'raped', 'molested', 'battery', 'theft', 'robbery', 'car', 'bike', 'mileage', 'tire', 'suspension', 'engine', 'payment', 'card', 'authentication', 'declined', 'banking',)
com2=ttk.Combobox(w, values=cpspec, textvariable=cspec, width=22)
com2.grid(row=1, column=1)


#Radiobutton
male=Radiobutton(w, text='Male', variable=gend, value='male')
female=Radiobutton(w, text='Female', variable=gend, value='female')
male.grid(row=7, column=1)
female.grid(row=7, column=2)


#Buttons
b1=Button(w,text="Store",padx=7,pady=2,command=add)
b1.grid(row=0,column=3)
b2=Button(w,text="Show",padx=7,pady=2,command=fetch)
b2.grid(row=2,column=3)
#b4=Button(w,text="Reset",padx=7,pady=2,command=clear)
#b4.grid(row=4,column=3)
b3=Button(w,text="Reset",padx=7,pady=2,command=clear)
b3.grid(row=4,column=3)
w.mainloop()
