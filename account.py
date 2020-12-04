from tkinter import*
from tkinter import ttk
from datetime import date
from datetime import timedelta
import tkinter.messagebox
import mysql.connector
from subprocess import call

class account:
    
    def __init__(self,root):
         
        
        fname=StringVar()
        lname=StringVar()
        usn=StringVar()
        sem=StringVar()
        dep=StringVar()
        trans=StringVar()
        datex=StringVar()
        mode=StringVar()
        due=StringVar()
        paid=StringVar()
        finame=StringVar()
        lsname=StringVar()
        usni=StringVar()
        

        def isave():
            f=fname.get()
            l=lname.get()
            u=usn.get()
            s=sem.get()
            d=dep.get()
            t=trans.get()
            da=datex.get()
            mo=mode.get()
            dued=due.get()
            pay=paid.get()
            if not (f and l and u and s and d and t and da and mo and dued and pay):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO account VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(u,f,l,s,d,t,da,mo,pay,dued)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
            
        def ireset():
            fname.set("")
            lname.set("")
            usn.set("")
            sem.set("")
            dep.set("")
            trans.set("")
            datex.set("")
            mode.set("")
            due.set("")
            paid.set("")
            finame.set("")
            lsname.set("")
            usni.set("")
            root.destroy()
            call(["python","account.py"])
            
                
        def idisplay():
            global rows
            f=finame.get()
            l=lsname.get()
            u=usni.get()
            
            
            if not (f and l and u):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mycursor=connection.cursor()
                        sql='Select regno,amount,due from account where regno="{}"'.format(u)
                        mycursor.execute(sql)
                        rows=mycursor.fetchall()
                        total=mycursor.rowcount
                        print("total entries:"+str(total))
                        for i in rows:
                            txtDisplayR.insert('','end',values=i)
                    else:
                        print("Error in db connection")
                except Error as e:
                    print("Error while connecting to MySQL", e)
                
        def iexit():
            result=tkinter.messagebox.askyesno("Account ","Confirm if you want to exit")
            if (result==True):
                root.destroy()
                call(["python","front.py"])
            else:
                root.destroy()
                call(["python","account.py"])
            
        self.root=root
        self.root.title("ACCOUNT DETAILS")
        self.root.geometry("1200x450+50+50")
        self.root.resizable(False,False)

        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label (TitleFrame,font=('Comic Sans MS',40,'bold'),width=38,text="\tACCOUNT DETAIL\t\t",foreground='white', background='purple')
        TitleFrame.pack(side=RIGHT)
        DataFrame=Frame(root,bg="grey",width=1200)
        DataFrame.pack(side=TOP)
        DataFrameleft =LabelFrame(DataFrame, bd=9, width=850, height=400,background="black",fg="white",padx=16, relief=RIDGE, font=('arial',14,'bold'), text="EDIT ACCOUNT:")
        DataFrameleft.pack(side=LEFT)
        DataFrameright=LabelFrame(DataFrame, bd=18,width=850, height=400,background="grey",fg="white",padx=14, relief=RIDGE, font=('arial',16,'bold'), text="SEARCH:")
        DataFrameright.pack(side=RIGHT)
        
        lblname=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="First Name:",background="black",fg="yellow")
        lblname.grid(row=1,column=0)
        txtname =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=fname,  width=25)
        txtname.grid(row=1,column=1)
        
        lblsur=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Last Name:",background="black",fg="yellow")
        lblsur.grid(row=2,column=0)
        txtsur =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=lname,  width=25)
        txtsur.grid(row=2,column=1)
        
        lblUsn=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="USN:",background="black",fg="yellow")
        lblUsn.grid(row=0,column=0)
        txtusn =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=usn,  width=25)
        txtusn.grid(row=0,column=1)
        
        lblsemester=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Semester:",background="black",fg="yellow")
        lblsemester.grid(row=3,column=0)
        txtsem =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=sem,  width=25)
        txtsem.grid(row=3,column=1)
        
        lbldep=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Department:",background="black",fg="yellow")
        lbldep.grid(row=4,column=0)
        txtdep =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=dep,  width=25)
        txtdep.grid(row=4,column=1)
        
        lbltransid=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Transition ID:",background="black",fg="yellow")
        lbltransid.grid(row=5,column=0)
        txttrans=Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=trans,  width=25)
        txttrans.grid(row=5,column=1)
        
        lbldate=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Date of payment:",background="black",fg="yellow")
        lbldate.grid(row=6,column=0)
        txtdate =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=datex,  width=25)
        txtdate.grid(row=6,column=1)
        
        lblmode=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Mode of payment:",background="black",fg="yellow")
        lblmode.grid(row=7,column=0)
        txtmode =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=mode,  width=25)
        txtmode.grid(row=7,column=1)
        
        lbldue=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Due:",background="black",fg="yellow")
        lbldue.grid(row=9,column=0)
        txtdue =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=due,  width=25)
        txtdue.grid(row=9,column=1)
        
        lblpaid=Label(DataFrameleft,font=('Times Roman',14,'bold'),text="Amount paid:",background="black",fg="yellow")
        lblpaid.grid(row=8,column=0)
        txtpaid=Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=paid,  width=25)
        txtpaid.grid(row=8,column=1)
        
        btnsave=Button(DataFrameleft, font=('arial',14,'bold'), text="SAVE",width=12,bg="indigo",fg="white",command=isave)
        btnsave.grid(row=10,column=1)
        
        
        lblnamee=Label(DataFrameright,font=('Times Roman',11,'bold'),text="First Name:",background="grey",fg="yellow")
        lblnamee.grid(row=1,column=0)
        txtnamee=Entry(DataFrameright, font=('arial',11,'bold'),textvariable=finame,  width=20)
        txtnamee.grid(row=2,column=0)
        
        lbllastname=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Last Name:",background="grey",fg="yellow")
        lbllastname.grid(row=3,column=0)
        txtlastname=Entry(DataFrameright, font=('arial',11,'bold'),textvariable=lsname,  width=20)
        txtlastname.grid(row=4,column=0)
        
        lblusni=Label(DataFrameright,font=('Times Roman',11,'bold'),text="USN:",background="grey",fg="yellow")
        lblusni.grid(row=5,column=0)
        txtusni=Entry(DataFrameright, font=('arial',11,'bold'),textvariable=usni,  width=20)
        txtusni.grid(row=6,column=0)
        
        btndisplay=Button(DataFrameright, font=('arial',14,'bold'), text="DISPLAY",width=10,bg="indigo",fg="white",command=idisplay)
        btndisplay.grid(row=7,column=0)
        txtDisplayR=ttk.Treeview(DataFrameright,columns=(1,2,3),show="headings",height=2)
        txtDisplayR.grid(row=8,column=0)
        txtDisplayR.heading(1, text="USN")
        txtDisplayR.heading(2, text="PAID")
        txtDisplayR.heading(3, text="DUE")
        btnexit=Button(DataFrame, font=('arial',12,'bold'), text="EXIT",width=12,bg="red",fg="white",command=iexit)
        btnexit.place(x=880,y=318)
        btnupdate=Button(DataFrame, font=('arial',12,'bold'), text="RESET",width=12,bg="green",fg="white",command=ireset)
        btnupdate.place(x=565,y=318)
        
        
        
        
        
        
root=Tk()
obj=account(root)
root.mainloop()
        

        
    
        
