from tkinter import*
from tkinter import ttk
import random
from datetime import date
from datetime import timedelta
import tkinter.messagebox
from subprocess import call
import mysql.connector

class returnbook():
    def __init__(self,root):
        fname=StringVar()
        lname=StringVar()
        ido=StringVar()
        dep=StringVar()
        todaydate=StringVar()
        BookID=StringVar()
        fine=int()
               #============================================================frame setting======================================================================
        self.root=root
        self.root.title("RETURN BOOK")
        self.root.geometry("1105x550+50+50")
        self.root.resizable(False,False)
        
        self.bg=PhotoImage(file="librarybg.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.logo_icon=PhotoImage(file="f://python/project/back.PNG")

        def returnd():
            fn=fname.get()
            ln=lname.get()
            ids=ido.get()
            d=dep.get()
            bo=BookID.get()
            today=date.today()
            d1=today.strftime("%Y-%m-%d")
            todaydate.set(d1)
            t=todaydate.get()
            if not (fn and ln and ids and d and bo and t):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mycur=connection.cursor()
                        sql='Select datedue from library where bookid="{}" and registeredno="{}"'.format(bo,ids)
                        mycur.execute(sql)
                        rows=mycur.fetchall()
                        total=mycur.rowcount
                        for i in rows:
                            txtDisplayR.insert('','end',values=i)
                        tkinter.messagebox.showinfo("FINE", "FINE is calculated by number of days of late submission * 2 ")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "DATABASE NOT CONNECTED.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
        def iexit():
            result=tkinter.messagebox.askyesno("Library","Confirm if you want to exit return page")
            if (result==True):
                root.destroy()
                call(["python","libraryhome.py"])
            else:
                root.destroy()
                call(["python","returnbook.py"])
                
        def iconfirm():
            fn=fname.get()
            ln=lname.get()
            ids=ido.get()
            d=dep.get()
            bo=BookID.get()
            t=todaydate.get()
            if not (fn and ln and ids and d and bo and t):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO returned VALUES ("{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(ids,fn,ln,d,bo,t,"PAID")
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Book returned", "Book return is registered")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)            

        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label (TitleFrame,font=('Comic Sans MS',40,'bold'),width=35,text=" BOOK RETURN ",foreground='green',bg='black')
        TitleFrame.pack(side=RIGHT)
        DataFrame=Frame(root)
        DataFrame.pack(side=TOP)
        DataFrame=LabelFrame(DataFrame, bd=9, width=800,height=700,background="grey",fg="red",padx=11, relief=RIDGE, font=('arial',14,'bold'), text="Return:")
        DataFrame.place(relx = 1, x =-2, y = 2, anchor = NE)
        DataFrame.pack()
        

        ButtonFrame=Frame(root)
        ButtonFrame.pack(side=RIGHT)
        

        lblname=Label(DataFrame,font=('Times Roman',14,'bold'),text="First Name:",background="grey",fg="black")
        lblname.grid(row=0,column=0)
        txtname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=fname,  width=25)
        txtname.grid(row=0,column=1)
        
        lblsur=Label(DataFrame,font=('Times Roman',14,'bold'),text="Last Name:",background="grey",fg="black")
        lblsur.grid(row=0,column=2)
        txtsur =Entry(DataFrame, font=('arial',11,'bold'),textvariable=lname,  width=25)
        txtsur.grid(row=0,column=3)
        
        lblido=Label(DataFrame,font=('Times Roman',14,'bold'),text="ID:",background="grey",fg="black")
        lblido.grid(row=1,column=0)
        txtido =Entry(DataFrame, font=('arial',11,'bold'),textvariable=ido,  width=25)
        txtido.grid(row=1,column=1)
        
        lbldep=Label(DataFrame,font=('Times Roman',14,'bold'),text="Department:",background="grey",fg="black")
        lbldep.grid(row=1,column=2)
        txtdep =Entry(DataFrame, font=('arial',11,'bold'),textvariable=dep,  width=25)
        txtdep.grid(row=1,column=3)
        

        lblbookid=Label(DataFrame,font=('Times Roman',14,'bold'),text="Book ID:",background="grey",fg="black")
        lblbookid.grid(row=2,column=0)
        txtbookid=Entry(DataFrame, font=('arial',11,'bold'),textvariable=BookID,  width=25)
        txtbookid.grid(row=2,column=1)

        btnsave=Button(DataFrame, font=('arial',11,'bold'), text="CHECK",width=15,bg="indigo",fg="white",command=returnd)
        btnsave.grid(row=3,column=3)

        lbldate=Label(DataFrame,font=('Times Roman',14,'bold'),text="Return date:",background="grey",fg="black")
        lbldate.grid(row=3,column=0)
        txtdate=Entry(DataFrame, font=('arial',11,'bold'),textvariable=todaydate,  width=25)
        txtdate.grid(row=3,column=1)
        
        lblfine=Label(DataFrame,font=('Times Roman',14,'bold'),text="Fine:",background="grey",fg="blue")
        lblfine.grid(row=4,column=2)

        txtDisplayR=ttk.Treeview(DataFrame,columns=(1),show="headings",height=2)
        txtDisplayR.grid(row=4,column=3)
        txtDisplayR.heading(1, text="Date of Borrow")

        btnconfirm=Button(DataFrame, font=('arial',11,'bold'), text="CONFIRM",width=15,bg="indigo",fg="white",command=iconfirm)
        btnconfirm.grid(row=5,column=3)
        

        lblIM=Label(DataFrame,image=self.logo_icon)
        lblIM.grid(row=4,column=1)

        

        btnexit=Button(ButtonFrame, font=('arial',11,'bold'), text="EXIT",width=10,bg="indigo",fg="white",command=iexit)
        btnexit.place(x=10,y=845)
        btnexit.pack()
        
        
        

        



root= Tk()
obj=returnbook(root)
root.mainloop()

    


