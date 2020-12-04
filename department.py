from tkinter import*
from tkinter import ttk
from datetime import date
from datetime import timedelta
import tkinter.messagebox
import mysql.connector
from subprocess import call

class department:
    def __init__(self,root):
        fname=StringVar()
        lname=StringVar()
        doj=StringVar()
        dep=StringVar()
        salary=StringVar()
        empid=StringVar()
        enumber=StringVar()
        epass=StringVar()
        eemail=StringVar()
        
        stufname=StringVar()
        stulname=StringVar()
        studid=StringVar()
        depart=StringVar()
        year=StringVar()
        snumber=StringVar()
        section=StringVar()
        ssem=StringVar()
        
        course=StringVar()
        code=StringVar()
        
        
        self.root=root
        self.root.title("DEPARTMENT")
        self.root.geometry("1200x600+50+50")
        self.root.resizable(False,False)
        self.bg=PhotoImage(file="F://python/project/depart.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        def reset():
            fn=fname.set("")
            ln=lname.set("")
            do=doj.set("")
            d=dep.set("")
            s=salary.set("")
            ids=empid.set("")
            mob=enumber.set("")
            p=epass.set("")
            em=eemail.set("")

        def iexam():
            
            fn=fname.get()
            ln=lname.get()
            do=doj.get()
            d=dep.get()
            s=salary.get()
            ids=empid.get()
            mob=enumber.get()
            p=epass.get()
            em=eemail.get()
            if not (ids and fn and ln and do and d and mob and em and p and s):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
                extra()
            else:
                ###Database COMMAND
                if (d=="EXAM"):
                    try:
                        connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                        if connection.is_connected():
                            mysql_insert= 'INSERT INTO exammember VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(ids, fn, ln, do, p, em, s, d, mob)
                            cursor = connection.cursor()
                            cursor.execute(mysql_insert)
                            connection.commit()
                        
                            tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                            extra()
                            
                        else:
                            tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                    except Error as e:
                        print("Error while connecting to MySQL", e)
                else:
                    tkinter.messagebox.showwarning("Fields error", "Please check the field department.")
                    extra()
                
        def iaccount():
            
            fn=fname.get()
            ln=lname.get()
            do=doj.get()
            d=dep.get()
            s=salary.get()
            ids=empid.get()
            mob=enumber.get()
            p=epass.get()
            em=eemail.get()
            if not (ids and fn and ln and do and d and mob and em and p and s):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
                extra()
            else:
                if(d=="ACCOUNT"):
                ###Database COMMAND
                    try:
                        connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                        if connection.is_connected():
                            mysql_insert= 'INSERT INTO accountmember VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(ids, fn, ln, em, do, p, mob, d, s)
                            cursor = connection.cursor()
                            cursor.execute(mysql_insert)
                            connection.commit()
                        
                            tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                            extra()
                        else:
                            tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                    except Error as e:
                        print("Error while connecting to MySQL", e)
                else:
                    tkinter.messagebox.showwarning("Fields error", "Please check the field department.")
                    extra()

        def ilibrary():
            
            fn=fname.get()
            ln=lname.get()
            do=doj.get()
            d=dep.get()
            s=salary.get()
            ids=empid.get()
            mob=enumber.get()
            p=epass.get()
            em=eemail.get()
            if not (ids and fn and ln and do and d and mob and em and p and s):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
                extra()
            else:
                if(d=="LIBRARY"):
                ###Database COMMAND
                    try:
                        connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                        if connection.is_connected():
                            mysql_insert= 'INSERT INTO librarymember VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(ids, fn, ln, em, do, p, mob, d, s)
                            cursor = connection.cursor()
                            cursor.execute(mysql_insert)
                            connection.commit()
                        
                            tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                            extra()
                        else:
                            tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                    except Error as e:
                        print("Error while connecting to MySQL", e)
                else:
                    tkinter.messagebox.showwarning("Fields error", "Please check the field department.")
                    extra()

        def extra():
            
            reset()
            extra=Toplevel(root)
            extra.title("DEPARTMENT")
            extra.geometry("1200x600+50+50")
            extra.resizable(False,False)
            extra.bg=PhotoImage(file="F://python/project/depart.png")
            extra.bg_image=Label(extra,image=extra.bg).place(x=0,y=0,relwidth=1,relheight=1)
            extra.bgtea=PhotoImage(file="F://python/project/depicon.PNG")
            TitleFrame =Frame(extra)
            TitleFrame.pack(side=TOP)
            TitleFrame=Label (TitleFrame,font=('Arial',40,'bold'),text="DEPARTMENT",foreground='red',bg='black')
            TitleFrame.pack(side=RIGHT)
            DataFrame=Frame(extra,bd=15)
            DataFrame.pack(side=TOP)
            DataFrame=Label (DataFrame,font=('Arial',40,'bold'))
            DataFrame.pack(side=LEFT)
            ButtonFrame=Frame(extra)
            ButtonFrame.pack(side=TOP)
            lblemp=Label(DataFrame,font=('Times Roman',14,'bold'),text="EMPLOYEE",fg="red")
            lblemp.grid(row=0,column=0)

            lblname=Label(DataFrame,font=('Times Roman',14,'bold'),text="First Name:")
            lblname.grid(row=1,column=0)
            txtname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=fname,  width=20)
            txtname.grid(row=1,column=1)

            lblsurname=Label(DataFrame,font=('Times Roman',14,'bold'),text="Last Name:")
            lblsurname.grid(row=1,column=2)
            txtsurname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=lname,  width=20)
            txtsurname.grid(row=1,column=3)

            lbldoj=Label(DataFrame,font=('Times Roman',14,'bold'),text="Date of join:")
            lbldoj.grid(row=2,column=0)
            txtdoj =Entry(DataFrame, font=('arial',11,'bold'),textvariable=doj,  width=20)
            txtdoj.grid(row=2,column=1)

            lbldep=Label(DataFrame,font=('Times Roman',14,'bold'),text="Department:")
            lbldep.grid(row=2,column=2)
            txtdep =Entry(DataFrame, font=('arial',11,'bold'),textvariable=dep,  width=20)
            txtdep.grid(row=2,column=3)
        
            lblsal=Label(DataFrame,font=('Times Roman',14,'bold'),text="Salary:")
            lblsal.grid(row=3,column=0)
            txtsal =Entry(DataFrame, font=('arial',11,'bold'),textvariable=salary,  width=20)
            txtsal.grid(row=3,column=1)
        
            lblempid=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee Id:")
            lblempid.grid(row=3,column=2)
            txtempid=Entry(DataFrame, font=('arial',11,'bold'),textvariable=empid,  width=20)
            txtempid.grid(row=3,column=3)
        
            lblempn=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee no:")
            lblempn.grid(row=4,column=0)
            txtempn =Entry(DataFrame, font=('arial',11,'bold'),textvariable=enumber,  width=20)
            txtempn.grid(row=4,column=1)

            lblempemail=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee email:")
            lblempemail.grid(row=4,column=2)
            txtempemail=Entry(DataFrame, font=('arial',11,'bold'),textvariable=eemail,  width=20)
            txtempemail.grid(row=4,column=3)

            lblemppass=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee Password:")
            lblemppass.grid(row=5,column=0)
            txtemppass =Entry(DataFrame, font=('arial',11,'bold'),textvariable=epass, show="*", width=20)
            txtemppass.grid(row=5,column=1)
            Image_label=Label(DataFrame,image=extra.bgtea).grid(row=5,column=3)

            btnsave=Button(ButtonFrame, font=('arial',14,'bold'), text="SAVE Accountant's Data",width=25,bg="green",fg="white",command=iaccount)
            btnsave.grid(row=6,column=3)

            btnsave2=Button(ButtonFrame, font=('arial',14,'bold'), text="SAVE Examiner's Data",width=25,bg="orange",fg="white",command=iexam)
            btnsave2.grid(row=6,column=1)

            btnsave3=Button(ButtonFrame, font=('arial',14,'bold'), text="SAVE Librarian's Data",width=25,bg="indigo",fg="white",command=ilibrary)
            btnsave3.grid(row=6,column=2)
            
            extra.mainloop()
        
        def iadd():
            fn=fname.get()
            ln=lname.get()
            do=doj.get()
            d=dep.get()
            s=salary.get()
            ids=empid.get()
            mob=enumber.get()
            p=epass.get()
            em=eemail.get()
            if not (ids and fn and ln and do and d and mob and em and p and s):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                ###Database COMMAND
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO department1 VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(ids, fn, ln, do, d, mob, em, p, s)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)

        def isave():
            fn=stufname.get()
            ln=stulname.get()
            u=studid.get()
            d=depart.get()
            y=year.get()
            sn=snumber.get()
            s=ssem.get()
            sec=section.get()
            if not (fn and ln and u and s and d and y and sn and sec ):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO student VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(fn, ln, fn+"@gmail.com", sn, u, s, sec, y, d)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    
        def isave2():
            cou=course.get()
            c=code.get()
            if not (cou and c):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO department3 VALUES ("{}","{}")' \
                                      .format(c,cou)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    
        def iexit():
            result=tkinter.messagebox.askyesno("Department","Confirm if you want to exit")
            if (result==True):
                root.destroy()
                call(["python","front.py"])
            else:
                root.destroy()
                call(["python","department.py"])
        reset()
        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label (TitleFrame,font=('Arial',40,'bold'),text="DEPARTMENT",foreground='red',bg='black')
        TitleFrame.pack(side=RIGHT)
        DataFrame=Frame(root,bd=15)
        DataFrame.pack(side=TOP)
        DataFrame=Label (DataFrame,font=('Arial',40,'bold'))
        DataFrame.pack(side=LEFT)
        lblemp=Label(DataFrame,font=('Times Roman',14,'bold'),text="EMPLOYEE",fg="red")
        lblemp.grid(row=0,column=0)

        lblname=Label(DataFrame,font=('Times Roman',14,'bold'),text="First Name:")
        lblname.grid(row=1,column=0)
        txtname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=fname,  width=20)
        txtname.grid(row=1,column=1)

        lblsurname=Label(DataFrame,font=('Times Roman',14,'bold'),text="Last Name:")
        lblsurname.grid(row=1,column=2)
        txtsurname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=lname,  width=20)
        txtsurname.grid(row=1,column=3)

        lbldoj=Label(DataFrame,font=('Times Roman',14,'bold'),text="Date of join:")
        lbldoj.grid(row=2,column=0)
        txtdoj =Entry(DataFrame, font=('arial',11,'bold'),textvariable=doj,  width=20)
        txtdoj.grid(row=2,column=1)

        lbldep=Label(DataFrame,font=('Times Roman',14,'bold'),text="Department:")
        lbldep.grid(row=2,column=2)
        txtdep =Entry(DataFrame, font=('arial',11,'bold'),textvariable=dep,  width=20)
        txtdep.grid(row=2,column=3)
        
        lblsal=Label(DataFrame,font=('Times Roman',14,'bold'),text="Salary:")
        lblsal.grid(row=3,column=0)
        txtsal =Entry(DataFrame, font=('arial',11,'bold'),textvariable=salary,  width=20)
        txtsal.grid(row=3,column=1)
        
        lblempid=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee Id:")
        lblempid.grid(row=3,column=2)
        txtempid=Entry(DataFrame, font=('arial',11,'bold'),textvariable=empid,  width=20)
        txtempid.grid(row=3,column=3)
        
        lblempn=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee no:")
        lblempn.grid(row=4,column=0)
        txtempn =Entry(DataFrame, font=('arial',11,'bold'),textvariable=enumber,  width=20)
        txtempn.grid(row=4,column=1)

        lblempemail=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee email:")
        lblempemail.grid(row=4,column=2)
        txtempemail=Entry(DataFrame, font=('arial',11,'bold'),textvariable=eemail,  width=20)
        txtempemail.grid(row=4,column=3)

        lblemppass=Label(DataFrame,font=('Times Roman',14,'bold'),text="Employee Password:")
        lblemppass.grid(row=5,column=0)
        txtemppass =Entry(DataFrame, font=('arial',11,'bold'),textvariable=epass, show="*", width=20)
        txtemppass.grid(row=5,column=1)

        btnsave=Button(DataFrame, font=('arial',14,'bold'), text="SAVE employee data",width=16,bg="indigo",fg="white",command=iadd)
        btnsave.grid(row=5,column=3)

        lblstu=Label(DataFrame,font=('Times Roman',14,'bold'),text="Student",fg="red")
        lblstu.grid(row=6,column=0)

        lblsname=Label(DataFrame,font=('Times Roman',14,'bold'),text="First Name:")
        lblsname.grid(row=7,column=0)
        txtsname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=stufname,  width=20)
        txtsname.grid(row=7,column=1)

        lblssurname=Label(DataFrame,font=('Times Roman',14,'bold'),text="Last Name:")
        lblssurname.grid(row=7,column=2)
        txtssurname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=stulname,  width=20)
        txtssurname.grid(row=7,column=3)

        lblyear=Label(DataFrame,font=('Times Roman',14,'bold'),text="DOB:")
        lblyear.grid(row=8,column=0)
        txtyear=Entry(DataFrame, font=('arial',11,'bold'),textvariable=year,  width=20)
        txtyear.grid(row=8,column=1)

        lbldep=Label(DataFrame,font=('Times Roman',14,'bold'),text="Department:")
        lbldep.grid(row=8,column=2)
        txtdep =Entry(DataFrame, font=('arial',11,'bold'),textvariable=depart,  width=20)
        txtdep.grid(row=8,column=3)
        
        lblstuid=Label(DataFrame,font=('Times Roman',14,'bold'),text="Student Id:")
        lblstuid.grid(row=9,column=0)
        txtstuid=Entry(DataFrame, font=('arial',11,'bold'),textvariable=studid,  width=20)
        txtstuid.grid(row=9,column=1)
        
        lblsnum=Label(DataFrame,font=('Times Roman',14,'bold'),text="Student no:")
        lblsnum.grid(row=9,column=2)
        txtsnum =Entry(DataFrame, font=('arial',11,'bold'),textvariable=snumber,  width=20)
        txtsnum.grid(row=9,column=3)

        lblssem=Label(DataFrame,font=('Times Roman',14,'bold'),text="Semester:")
        lblssem.grid(row=10,column=0)
        txtssem =Entry(DataFrame, font=('arial',11,'bold'),textvariable=ssem,  width=20)
        txtssem.grid(row=10,column=1)

        lblsec=Label(DataFrame,font=('Times Roman',14,'bold'),text="Section:")
        lblsec.grid(row=10,column=2)
        txtsec =Entry(DataFrame, font=('arial',11,'bold'),textvariable=section,  width=20)
        txtsec.grid(row=10,column=3)

        btnsave=Button(DataFrame, font=('arial',14,'bold'), text="SAVE student data",width=16,bg="orange",fg="white",command=isave)
        btnsave.grid(row=11,column=3)

        lblemp=Label(DataFrame,font=('Times Roman',14,'bold'),text="Add Course",fg="red")
        lblemp.grid(row=12,column=0)
        
        lblcourse=Label(DataFrame,font=('Times Roman',14,'bold'),text="Course:")
        lblcourse.grid(row=13,column=0)
        txtcourse=Entry(DataFrame, font=('arial',11,'bold'),textvariable=course,  width=20)
        txtcourse.grid(row=13,column=1)

        lblcode=Label(DataFrame,font=('Times Roman',14,'bold'),text="Course Code:")
        lblcode.grid(row=13,column=2)
        txtcode =Entry(DataFrame, font=('arial',11,'bold'),textvariable=code,  width=20)
        txtcode.grid(row=13,column=3)

        btnadd=Button(DataFrame, font=('arial',14,'bold'), text="ADD Course",width=10,bg="green",fg="white",command=isave2)
        btnadd.grid(row=14,column=3)
        btnexit=Button(DataFrame, font=('arial',11,'bold'), text="EXIT",width=5,bg="red",fg="white",command=iexit)
        btnexit.grid(row=14,column=0)

        btnextra=Button(DataFrame, font=('arial',11,'bold'), text="EXTRA",width=10,bg="blue",fg="white",command=extra)
        btnextra.place(x=590,y=-10)
        
        

root=Tk()
obj=department(root)
root.mainloop()
