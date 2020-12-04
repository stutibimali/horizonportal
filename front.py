from tkinter import*
from tkinter import ttk
import random
from datetime import date
from datetime import timedelta
import tkinter.messagebox
import mysql.connector
from subprocess import call


class Front:
    def __init__(self,root):
        
        #==========================================================login function==========================================================================#
        def login():
            root.destroy()
            call(["python","student.py"])
            
            
    
        def tealogin():
            global username
            global password
            username=StringVar()
            password=StringVar()
            Teacherlogin=Toplevel(root)
            Teacherlogin.title("TEACHER LOGIN")
            Teacherlogin.geometry("400x390+10+10")
            Teacherlogin.resizable(False,False)
            Teacherlogin.bgtea=PhotoImage(file="F://python/project/login.png")
            Teacherlogin.bgtea_image=Label(Teacherlogin,image=Teacherlogin.bgtea).place(x=0,y=0,relwidth=1,relheight=1)
            Teacherlogin.logo_icon=PhotoImage(file="f://python/project/logo.PNG")
            TitleFrame2 =Frame(Teacherlogin)
            TitleFrame2.pack(side=TOP)
            TitleFrame2=Label(TitleFrame2,font=('Impact',16,'bold'),text="\t\tTEACHER PAGE \t\t",foreground='orange', background='brown')
            TitleFrame2.pack(side= LEFT)            
            dataframe =Frame(Teacherlogin)
            dataframe.pack(side=TOP)
            Image_label=Label(dataframe,image=Teacherlogin.logo_icon).grid(row=1,column=0)
            lblusername=Label(dataframe, font=('arial',12,'bold'), text="USERNAME",fg='indigo')
            lblusername.grid(row=2,column=0,sticky=W)
            txtusername=Entry(dataframe, font=('arial',12,'bold'),textvariable=username, width=23)
            txtusername.grid(row=3,column=0)
            lblpassword=Label(dataframe, font=('arial',12,'bold'), text="PASSWORD", fg='indigo')
            lblpassword.grid(row=4,column=0,sticky=W)
            txtpassword=Entry(dataframe, font=('arial',12,'bold'),textvariable=password,show='*', width=23)
            txtpassword.grid(row=5,column=0)
            btnlogin =Button(dataframe, font=('arial',12,'bold'), text="LOGIN",bg='indigo',fg='white',width=8,command=__teac__)
            btnlogin.grid(row=6,column=0)
            Teacherlogin.mainloop()

        def plaglogin():
            global username
            global password
            username=StringVar()
            password=StringVar()
            plag=Toplevel(root)
            plag.title("TEACHER LOGIN")
            plag.geometry("400x390+10+10")
            plag.resizable(False,False)
            plag.bgtea=PhotoImage(file="F://python/project/login.png")
            plag.bgtea_image=Label(plag,image=plag.bgtea).place(x=0,y=0,relwidth=1,relheight=1)
            plag.logo_icon=PhotoImage(file="f://python/project/logo.PNG")
            TitleFrame2 =Frame(plag)
            TitleFrame2.pack(side=TOP)
            TitleFrame2=Label(TitleFrame2,font=('Impact',16,'bold'),text="\t\tTEACHER PAGE \t\t",foreground='orange', background='brown')
            TitleFrame2.pack(side= LEFT)            
            dataframe =Frame(plag)
            dataframe.pack(side=TOP)
            Image_label=Label(dataframe,image=plag.logo_icon).grid(row=1,column=0)
            lblusername=Label(dataframe, font=('arial',12,'bold'), text="USERNAME",fg='indigo')
            lblusername.grid(row=2,column=0,sticky=W)
            txtusername=Entry(dataframe, font=('arial',12,'bold'),textvariable=username, width=23)
            txtusername.grid(row=3,column=0)
            lblpassword=Label(dataframe, font=('arial',12,'bold'), text="PASSWORD", fg='indigo')
            lblpassword.grid(row=4,column=0,sticky=W)
            txtpassword=Entry(dataframe, font=('arial',12,'bold'),textvariable=password,show='*', width=23)
            txtpassword.grid(row=5,column=0)
            btnlogin =Button(dataframe, font=('arial',12,'bold'), text="LOGIN",bg='indigo',fg='white',width=8,command=__plag__)
            btnlogin.grid(row=6,column=0)
            plag.mainloop()

        def liblogin():
            global username
            global password
            username=StringVar()
            password=StringVar()
            liblog=Toplevel(root)
            liblog.title("LIBRARY LOGIN")
            liblog.geometry("400x390+10+10")
            liblog.resizable(False,False)
            liblog.bglib=PhotoImage(file="F://python/project/login.png")
            liblog.bglib_image=Label(liblog,image=liblog.bglib).place(x=0,y=0,relwidth=1,relheight=1)
            liblog.logo_icon=PhotoImage(file="f://python/project/libicon.PNG")
            TitleFrame2 =Frame(liblog)
            TitleFrame2.pack(side=TOP)
            TitleFrame2=Label(TitleFrame2,font=('Impact',16,'bold'),text="\t\tLIBRARY PAGE \t\t",foreground='orange', background='brown')
            TitleFrame2.pack(side= LEFT)
            dataframe =Frame(liblog)
            dataframe.pack(side=TOP)
            Image_label=Label(dataframe,image=liblog.logo_icon).grid(row=1,column=0)
            lblusername=Label(dataframe, font=('arial',12,'bold'), text="USERNAME", fg='indigo')
            lblusername.grid(row=2,column=0,sticky=W)
            txtusername=Entry(dataframe, font=('arial',12,'bold'),textvariable=username, width=23)
            txtusername.grid(row=3,column=0)
            lblpassword=Label(dataframe, font=('arial',12,'bold'), text="PASSWORD", fg='indigo')
            lblpassword.grid(row=4,column=0,sticky=W)
            txtpassword=Entry(dataframe, font=('arial',12,'bold'),textvariable=password,show='*', width=23)
            txtpassword.grid(row=5,column=0)
            btnlogin =Button(dataframe, font=('arial',12,'bold'), text="LOGIN",bg='indigo',fg='white',width=8,command=__library__)
            btnlogin.grid(row=6,column=0)
            liblog.mainloop()

        def account():
            global username
            global password
            username=StringVar()
            password=StringVar()
            acco=Toplevel(root)
            acco.title("ACCOUNT LOGIN")
            acco.geometry("400x390+10+10")
            acco.resizable(False,False)
            acco.bgac=PhotoImage(file="F://python/project/login.png")
            acco.bgac_image=Label(acco,image=acco.bgac).place(x=0,y=0,relwidth=1,relheight=1)
            acco.logo_icon=PhotoImage(file="f://python/project/accoicon.PNG")
            TitleFrame2 =Frame(acco)
            TitleFrame2.pack(side=TOP)
            TitleFrame2=Label(TitleFrame2,font=('Impact',16,'bold'),text="\t\tACCOUNT PAGE \t\t",foreground='orange', background='brown')
            TitleFrame2.pack(side= LEFT)
            dataframe =Frame(acco)
            dataframe.pack(side=TOP)
            Image_label=Label(dataframe,image=acco.logo_icon).grid(row=1,column=0)
            lblusername=Label(dataframe, font=('arial',12,'bold'), text="USERNAME", fg='indigo')
            lblusername.grid(row=2,column=0,sticky=W)
            txtusername=Entry(dataframe, font=('arial',12,'bold'),textvariable=username, width=23)
            txtusername.grid(row=3,column=0)
            lblpassword=Label(dataframe, font=('arial',12,'bold'), text="PASSWORD", fg='indigo')
            lblpassword.grid(row=4,column=0,sticky=W)
            txtpassword=Entry(dataframe, font=('arial',12,'bold'),textvariable=password,show='*', width=23)
            txtpassword.grid(row=5,column=0)
            btnlogin =Button(dataframe, font=('arial',12,'bold'), text="LOGIN",bg='indigo',fg='white',width=8,command=__acco__)
            btnlogin.grid(row=6,column=0)
            acco.mainloop()

        def exam():
            global username
            global password
            username=StringVar()
            password=StringVar()
            examm=Toplevel(root)
            examm.title("EXAM LOGIN")
            examm.geometry("400x390+10+10")
            examm.resizable(False,False)
            examm.bgex=PhotoImage(file="F://python/project/login.png")
            examm.bgex_image=Label(examm,image=examm.bgex).place(x=0,y=0,relwidth=1,relheight=1)
            examm.logo_icon=PhotoImage(file="f://python/project/exam.PNG")
            TitleFrame2 =Frame(examm)
            TitleFrame2.pack(side=TOP)
            TitleFrame2=Label(TitleFrame2,font=('Impact',16,'bold'),text="\t\tEXAM PAGE \t\t",foreground='orange', background='brown')
            TitleFrame2.pack(side= LEFT)
            dataframe =Frame(examm)
            dataframe.pack(side=TOP)
            Image_label=Label(dataframe,image=examm.logo_icon).grid(row=1,column=0)
            lblusername=Label(dataframe, font=('arial',12,'bold'), text="USERNAME", fg='indigo')
            lblusername.grid(row=2,column=0,sticky=W)
            txtusername=Entry(dataframe, font=('arial',12,'bold'),textvariable=username, width=23)
            txtusername.grid(row=3,column=0)
            lblpassword=Label(dataframe, font=('arial',12,'bold'), text="PASSWORD", fg='indigo')
            lblpassword.grid(row=4,column=0,sticky=W)
            txtpassword=Entry(dataframe, font=('arial',12,'bold'),textvariable=password,show='*', width=23)
            txtpassword.grid(row=5,column=0)
            btnlogin =Button(dataframe, font=('arial',12,'bold'), text="LOGIN",bg='indigo',fg='white',width=8,command=__examv__)
            btnlogin.grid(row=6,column=0)
            examm.mainloop()

        def department():
            global username
            global password
            username=StringVar()
            password=StringVar()
            depart=Toplevel(root)
            depart.title("DEPARTMENT LOGIN")
            depart.geometry("400x390+10+10")
            depart.resizable(False,False)
            depart.bgdep=PhotoImage(file="F://python/project/login.png")
            depart.bgdep_image=Label(depart,image=depart.bgdep).place(x=0,y=0,relwidth=1,relheight=1)
            depart.logo_icon=PhotoImage(file="f://python/project/depicon.PNG")
            TitleFrame2 =Frame(depart)
            TitleFrame2.pack(side=TOP)
            TitleFrame2=Label(TitleFrame2,font=('Impact',16,'bold'),text="\t\tDEPARTMENT \t\t",foreground='orange', background='brown')
            TitleFrame2.pack(side= LEFT)
            dataframe =Frame(depart)
            dataframe.pack(side=TOP)
            Image_label=Label(dataframe,image=depart.logo_icon).grid(row=1,column=0)
            lblusername=Label(dataframe, font=('arial',12,'bold'), text="USERNAME", fg='indigo')
            lblusername.grid(row=2,column=0,sticky=W)
            txtusername=Entry(dataframe, font=('arial',12,'bold'),textvariable=username, width=23)
            txtusername.grid(row=3,column=0)
            lblpassword=Label(dataframe, font=('arial',12,'bold'), text="PASSWORD", fg='indigo')
            lblpassword.grid(row=4,column=0,sticky=W)
            txtpassword=Entry(dataframe, font=('arial',12,'bold'),textvariable=password,show='*', width=23)
            txtpassword.grid(row=5,column=0)
            btnlogin =Button(dataframe, font=('arial',12,'bold'), text="LOGIN",bg='indigo',fg='white',width=8,command=__dep__)
            btnlogin.grid(row=6,column=0)
            depart.mainloop()
            
        def __dep__():
            global loginname
            loginname=username.get()
            pass1=password.get()
            try:
                connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                if connection.is_connected():
                    mycursor=connection.cursor()
                    sql='Select name,password from admin where name="{}" and password="{}"'.format(loginname,pass1)
                    mycursor.execute(sql)
                    wName=mycursor.fetchall()
                    if not wName:
                        username.set("INVALID")
                        password.set("")
                    else:
                        #login successful
                        root.destroy()
                        call(["python","department.py"])
                    mycursor.close()
                else:
                    print("Error in db connection")
            except Error as e:
                print("Error while connecting to MySQL", e)
            

        def __library__():
            global loginname
            loginname=username.get()
            pass1=password.get()
            try:
                connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                if connection.is_connected():
                    mycursor=connection.cursor()
                    sql='Select emid,fname,password from librarymember where emid="{}" and password="{}"'.format(loginname,pass1)
                    mycursor.execute(sql)
                    wName=mycursor.fetchall()
                    if not wName:
                        username.set("INVALID")
                        password.set("")
                    else:
                        #login successful
                        root.destroy()
                        call(["python","libraryhome.py"])
                    mycursor.close()
                else:
                    print("Error in db connection")
            except Error as e:
                print("Error while connecting to MySQL", e)
            
            
        def __acco__():
            global loginname
            loginname=username.get()
            pass1=password.get()
            try:
                connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                if connection.is_connected():
                    mycursor=connection.cursor()
                    sql='Select empid,fname,password from accountmember where empid="{}" and password="{}"'.format(loginname,pass1)
                    mycursor.execute(sql)
                    wName=mycursor.fetchall()
                    if not wName:
                        username.set("INVALID")
                        password.set("")
                    else:
                        #login successful
                        root.destroy()
                        call(["python","account.py"])
                    mycursor.close()
                else:
                    print("Error in db connection")
            except Error as e:
                print("Error while connecting to MySQL", e)
            
            
        def __examv__():
            global loginname
            loginname=username.get()
            pass1=password.get()
            try:
                connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                if connection.is_connected():
                    mycursor=connection.cursor()
                    sql='Select empid,fname,password from exammember where empid="{}" and password="{}"'.format(loginname,pass1)
                    mycursor.execute(sql)
                    wName=mycursor.fetchall()
                    if not wName:
                        username.set("INVALID")
                        password.set("")
                    else:
                        #login successful
                        root.destroy()
                        call(["python","exam.py"])
                    mycursor.close()
                else:
                    print("Error in db connection")
            except Error as e:
                print("Error while connecting to MySQL", e)
            
            
        def __teac__():
            global loginname
            loginname=username.get()
            pass1=password.get()
            try:
                connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                if connection.is_connected():
                    mycursor=connection.cursor()
                    sql='Select empid,fname,password from department1 where empid="{}" and password="{}"'.format(loginname,pass1)
                    mycursor.execute(sql)
                    wName=mycursor.fetchall()
                    if not wName:
                        username.set("INVALID")
                        password.set("")
                    else:
                        #login successful
                        root.destroy()
                        call(["python","teacher.py"])
                    mycursor.close()
                else:
                    print("Error in db connection")
            except Error as e:
                print("Error while connecting to MySQL", e)
            
        def __plag__():
            global loginname
            loginname=username.get()
            pass1=password.get()
            try:
                connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                if connection.is_connected():
                    mycursor=connection.cursor()
                    sql='Select empid,fname,password from department1 where empid="{}" and password="{}"'.format(loginname,pass1)
                    mycursor.execute(sql)
                    wName=mycursor.fetchall()
                    if not wName:
                        username.set("INVALID")
                        password.set("")
                    else:
                        #login successful
                        root.destroy()
                        call(["python","plagarism.py"])
                    mycursor.close()
                else:
                    print("Error in db connection")
            except Error as e:
                print("Error while connecting to MySQL", e)
                
        #=====================================================================main page layout========================================================#

        self.root=root
        self.root.title("HORIZON OFFICIAL PORTAL")
        self.root.geometry("1360x560+50+50")
        self.root.resizable(False,False)
        self.bg=PhotoImage(file="F://python/project/wallpaper.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label(TitleFrame,font=('Comic Sans MS',40,'bold'),text="\t\t\tWELCOME HORIZONITES\t\t\t",foreground='grey', background='pink')
        TitleFrame.pack(side= RIGHT)
        ButtonFrame =Frame(root, width=1350, height=150)
        ButtonFrame.pack(side=TOP)

        btnLibrary =Button(ButtonFrame, font=('arial',12,'bold'), text="LIBRARY",width=15,bg="indigo",fg="white",command=liblogin)
        btnLibrary.grid(row=0,column=1)
        btnstudent =Button(ButtonFrame, font=('arial',12,'bold'), text="STUDENT",width=15,bg="indigo",fg="white",command=login)
        btnstudent.grid(row=0,column=2)
        btnteacher =Button(ButtonFrame, font=('arial',12,'bold'), text="TEACHER",width=15,bg="indigo",fg="white",command=tealogin)
        btnteacher.grid(row=0,column=3)
        btnaccount =Button(ButtonFrame, font=('arial',12,'bold'), text="ACCOUNT",width=15,bg="indigo",fg="white",command=account)
        btnaccount.grid(row=0,column=4)
        btnexam =Button(ButtonFrame, font=('arial',12,'bold'), text="EXAM",width=15,bg="indigo",fg="white",command=exam)
        btnexam.grid(row=0,column=5)
        btndepartment =Button(ButtonFrame, font=('arial',12,'bold'), text="DEPARTMENT",width=15,bg="indigo",fg="white",command=department)
        btndepartment.grid(row=0,column=6)
        btnPLAG =Button(ButtonFrame, font=('arial',12,'bold'), text="PLAGARISM",width=15,bg="indigo",fg="white",command=plaglogin)
        btnPLAG.grid(row=0,column=7)


root=Tk()
obj=Front(root)
root.mainloop()
