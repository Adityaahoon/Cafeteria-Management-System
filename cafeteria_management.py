import mysql.connector as sql
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
from PIL import ImageTk, Image

import os

os.chdir("D:ARMAAN")
a=[]

c=0
o=0
con = sql.connect(host='localhost',user='root',password='12345',database='hotel')
cur=con.cursor()
cur.execute("SELECT * FROM employee")
for x in cur:   
    a.append(str(x))
def AddCustomer():
    

    
    global AddCw
    global MobileE
    global Tk
    AddCw=Toplevel()
    AddCw.grab_set()
    
    
    
    imag = Image.open('bkg1.jpg')
    
    a = ImageTk.PhotoImage(imag)
        

    labe=Label(AddCw,imag = a)
    
    labe.place(x=0,y=0)
    
    
      
    AddCw.title("NEW BOOKING")
    AddCw.geometry("1366x768")


    HeadF=Label(AddCw,text="CUSTOMER DETAILS",font="ar 10 bold") 
    HeadF.place(anchor=CENTER,relx=0.5,rely=0.1)

    
    NameF=Label(AddCw,text="First Name:",font="ar 10 bold")
    NameF.place(anchor=CENTER,relx=0.1,rely=0.22)
    NameFE=Entry(AddCw,width=20,font=("Helvetica",10))
    NameFE.place(relx=0.29,rely=0.22,anchor=CENTER)
    NameFEV=NameFE.get()
    
    NameL=Label(AddCw,text="Last Name:",font="ar 10 bold")
    NameL.place(anchor=CENTER,relx=0.6,rely=0.22)
    NameLE=Entry(AddCw,width=20,font=("Helvetica",10))
    NameLE.place(relx=0.79,rely=0.22,anchor=CENTER)
    NameLEV=NameLE.get()
 
    
    Mobile=Label(AddCw,text="Mobile No.:",font="ar 10 bold")
    Mobile.place(anchor=CENTER,relx=0.1,rely=0.37)
    MobileE=Entry(AddCw,width=20,font=("Helvetica",10))
    MobileE.place(relx=0.29,rely=0.37,anchor=CENTER)
    Mob=MobileE.get()
   
    rt=Label(AddCw,text="Reservation time:",font="ar 10 bold")
    rt.place(anchor=CENTER,relx=0.6,rely=0.37)
    rtE=Entry(AddCw,width=20,font=("Helvetica",10))
    rtE.place(relx=0.79,rely=0.37,anchor=CENTER)
    r=rtE.get()

    nop=Label(AddCw,text="No.of People",font="ar 10 bold")
    nop.place(anchor=CENTER,relx=0.1,rely=0.52)
    nopE=Entry(AddCw,width=20,font=("Helvetica",10))
    nopE.place(relx=0.29,rely=0.52,anchor=CENTER)
    ChekinEV=nopE.get()

    tn=Label(AddCw,text="Table No.:",font="ar 10 bold")
    tn.place(anchor=CENTER,relx=0.6,rely=0.52)
    tnE=Entry(AddCw,width=20,font=("Helvetica",10))
    tnE.place(relx=0.79,rely=0.52,anchor=CENTER)
    ChekoutEV=tnE.get()



   
    
    
    Submit=Button(AddCw,text="Submit",command=lambda: submitD(NameFEV,NameLEV,Mob,r,ChekinEV,ChekoutEV))
    Submit.place(relx=0.47,rely=0.95,anchor=CENTER)
    
    AddCw.mainloop()

def submitD(aa,bb,cc,dd,ee,ff):
    
       global fuji
       global delta
       cur.execute("Select * from customers;")
       alooee=cur.fetchall()
       efcegee=0
     
      
       cur.execute("Insert into customers values('"+aa+"','"+bb+"','"+cc+"','"+dd+"','"+ee+"','"+ff+"')")
       con.commit()

       messagebox.showinfo("Success","Data Succesfully Submitted")




            
     



def IDCheck():
    global o
    global enter
    l=0

    global b
    
    for y in a:
     if y=="('"+ID.get()+"', '"+Pass.get()+"')":
      messagebox.showinfo("Success","Hello "+ID.get()+". Welcome Back")

      l=1
      root.destroy()
      MainWindow()
      break    
    if l!=1:
      b+=1
      messagebox.showerror("Error","Wrong ID or Password Entered.Try Again.")
      
    if b==5:
        messagebox.showwarning("Warning","You have entered wrong credentials for 5 times.Please Wait for 5 minutes before trying again.")
        enter.destroy()
        enter2=Button(root,text="Enter",state=DISABLED)
        enter2.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        time.sleep(300)
        enter2.destroy()
        enter=Button(root,text="Enter",command=IDCheck)
        enter.place(relx=0.5,rely=0.5,anchor=CENTER)
          
b=0

def IDCheck2():

    global o
    global enter
    l=0

    global b

    for y in a:
     if y=="('"+ID.get()+"', '"+Pass.get()+"')":
      messagebox.showinfo("Success","Hello "+ID.get()+". Welcome Back")

      l=1
      
      root.destroy()
      MainWindow()
      break    
    if l!=1:
      b+=1
      messagebox.showerror("Error","Wrong ID or Password Entered.Try Again.")
      
    if b==5:
        messagebox.showwarning("Warning","You have entered wrong credentials for 5 times.Please Wait for 5 minutes before trying again.")
        enter.destroy()
        enter2=Button(root,text="Enter",state=DISABLED)
        enter2.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        time.sleep(300)
        enter2.destroy()
        enter=Button(root,text="Enter",command=IDCheck)
        enter.place(relx=0.5,rely=0.5,anchor=CENTER)
          
b=0

    
#LOGIN PAGE ELEMENTS
def LoginPage():
 from PIL import ImageTk, Image


 global  ID

 global Pass
 global root
 global enter
 root = Tk()
 imag = Image.open('logo2.png')

 a = ImageTk.PhotoImage(imag)
 label=Label(root,imag = a)
 label.place(x=300,y=25)
 root.geometry("1366x768")
 root.title("Login Page")
 Login=Label(root,text="LOGIN",font="ar 30 bold")
 Login.place(anchor=CENTER,relx=0.5,rely=0.42)



 IDName=Label(root,text="ID:",font="ar 15 bold")
 IDName.place(anchor=CENTER,relx=0.364,rely=0.5)



 PassName=Label(root,text="Password:",font="ar 15 bold")
 PassName.place(anchor=CENTER,relx=0.34,rely=0.55)



 ID=Entry(root,width=30,font="ar 15 bold")
 ID.place(relx=0.5,rely=0.5,anchor=CENTER)



 Pass=Entry(root,width=30,font="ar 15 bold")      
 Pass.place(relx=0.5,rely=0.55,anchor=CENTER)


 enter=Button(root,text="Enter",command=IDCheck)
 enter.place(relx=0.5,rely=0.62,anchor=CENTER)
 root.mainloop()


def LoginPage2():
 from PIL import ImageTk, Image


 global root2
 root2.destroy()
 global  ID
 global Pass
 global root
 global enter
 root = Tk()
 imag = Image.open('logo2.png')

 a = ImageTk.PhotoImage(imag)
 label=Label(root,imag = a)
 label.place(x=300,y=25)
 root.geometry("1369x768")
 root.title("Login Page")
 Login=Label(root,text="LOGIN",font="ar 30 bold")
 Login.place(anchor=CENTER,relx=0.5,rely=0.36)

 IDName=Label(root,text="ID:",font="ar 15 bold")
 IDName.place(anchor=CENTER,relx=0.364,rely=0.47)

 PassName=Label(root,text="Password:",font="ar 15 bold")
 PassName.place(anchor=CENTER,relx=0.34,rely=0.51)

 ID=Entry(root,width=30,font="ar 10 bold")
 ID.place(relx=0.5,rely=0.47,anchor=CENTER)

 Pass=Entry(root,width=30,font="ar 10 bold")
 Pass.place(relx=0.5,rely=0.51,anchor=CENTER)

 enter=Button(root,text="Enter",command=IDCheck)
 enter.place(relx=0.5,rely=0.6,anchor=CENTER)
 root.mainloop()


##Main window
def MainWindow():
    from PIL import ImageTk, Image


    global root2
    global NewC
    global Exc
    global Service
    global LvC
    global Sgnout
    
    root2 = Tk()
    imag = Image.open('logo2.png')

    a = ImageTk.PhotoImage(imag)
    label=Label(root2,imag = a)
    label.place(x=300,y=25)
    
    root2.geometry("1366x768")
    root2.title("Main Page")
    
    NewC=Button(root2,text="TABLE RESERVATION",command=AddCustomer)
    NewC.place(relx=0.5,rely=0.45,anchor=CENTER)
    Exc=Button(root2,text="RESERVED TABLE",command=EXCD)
    Exc.place(relx=0.5,rely=0.5,anchor=CENTER)
    Service=Button(root2,text="MENU",command=Menu)
    Service.place(relx=0.5,rely=0.55,anchor=CENTER)

    
    Sgnout=Button(root2,text="Sign Out",command=LoginPage2)
    Sgnout.place(relx=0.5,rely=0.6,anchor=CENTER)
    root2.mainloop()



def EXCD():
    cur.execute("Select * from customers;")
    oloo=cur.fetchall()
    AddCw3=Toplevel()
    AddCw3.grab_set()
    AddCw3.geometry("1366x768")
    AddCw3.title("Existing Customers")
    
    HeadLx=Label(AddCw3,text="Existing Customers",font="ar 20 bold")
    HeadLx.place(anchor=CENTER,relx=0.5,rely=0.1)
    
    
    NAMEEXC=Label(AddCw3,text="First Name",font="ar 12 bold")
    NAMEEXC.place(anchor=CENTER,relx=0.07,rely=0.2)
    NAMELEXC=Label(AddCw3,text="Last Name",font="ar 12 bold")
    NAMELEXC.place(anchor=CENTER,relx=0.17,rely=0.2)
    CITYEXC=Label(AddCw3,text="Mobile",font="ar 12 bold")
    CITYEXC.place(anchor=CENTER,relx=0.27,rely=0.2)
    MOBILEEXC=Label(AddCw3,text="Reservation time",font="ar 12 bold")
    MOBILEEXC.place(anchor=CENTER,relx=0.37,rely=0.2)
    CHECKIN=Label(AddCw3,text="No. of people",font="ar 12 bold")
    CHECKIN.place(anchor=CENTER,relx=0.47,rely=0.2)
    CHECKOUT=Label(AddCw3,text="Table No.",font="ar 12 bold")
    CHECKOUT.place(anchor=CENTER,relx=0.57,rely=0.2)
   
    xyx=0
    for iyi in range(100):
     LINE=Label(AddCw3,text="-")
     LINE.place(anchor=CENTER,relx=xyx,rely=0.225)
     xyx+=0.01
    yyyy=0.25
    
    for lll in oloo:
        xxxx=0.07
        for i in range(6):
        
         DATA=Label(AddCw3,text=lll[i],font=("Helvetica",20))
         DATA.place(anchor=CENTER,relx=xxxx,rely=yyyy)
         xxxx+=0.1
        yyyy+=0.05


def Menu():
    AddCw6=Toplevel()
    AddCw6.grab_set()
    AddCw6.geometry("600x400")
    AddCw6.title("Menu")
    cur.execute("Select * from menu;")
    yoyo=cur.fetchall()
    MenuX=Label(AddCw6,text="Menu",font="ar 20 bold")
    MenuX.place(anchor=CENTER,relx=0.5,rely=0.1)
    MenuItemName=Label(AddCw6,text="Item Name",font="ar 15 bold")
    MenuItemName.place(anchor=CENTER,relx=0.3,rely=0.21)
    MenuXPrice=Label(AddCw6,text="Price",font="ar 15 bold")
    MenuXPrice.place(anchor=CENTER,relx=0.7,rely=0.21)
    gfe=0
    for iyis in range(100):
     LINEpp=Label(AddCw6,text="-")
     LINEpp.place(anchor=CENTER,relx=gfe,rely=0.16)
     gfe+=0.01
    xyxyx=0
    for iyis in range(100):
     LINElll=Label(AddCw6,text="-")
     LINElll.place(anchor=CENTER,relx=xyxyx,rely=0.26)
     xyxyx+=0.01
    yyyygs=0.32
    
    for abcd in yoyo:
        xxxxgs=0.3
        for isk in range(2):
        
         DATA=Label(AddCw6,text=abcd[isk],font=("Helvetica",10))
         DATA.place(anchor=CENTER,relx=xxxxgs,rely=yyyygs)
         xxxxgs+=0.4
        yyyygs+=0.07

LoginPage()
try:
 os.remove("CT.txt")
except:
 print("")
