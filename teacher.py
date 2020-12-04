from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from subprocess import call
import mysql.connector

class teacher:

    def __init__(self,root):
        #absent
        fname=StringVar()
        lname=StringVar()
        usn=StringVar()
        sem=StringVar()
        sec=StringVar()
        dep=StringVar()
        code=StringVar()
        dateee=StringVar()
        teac=StringVar()
        period=StringVar()
        remark=StringVar()
        #assign
        reg=StringVar()
        sub=StringVar()
        assign=StringVar()
        sc=StringVar()
        #quiz
        regnn=StringVar()
        subj=StringVar()
        quiz=StringVar()
        score=StringVar()
        #cie
        usnreg=StringVar()
        subject=StringVar()
        cie=StringVar()
        scored=StringVar()
        
        self.root=root
        self.root.title("Teacher Page")
        self.root.geometry("1200x570+50+50")
        self.root.resizable(False,False)
        self.bg=PhotoImage(file="F://python/project/st2.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        def isave():
            fn=fname.get()
            ln=lname.get()
            u=usn.get()
            s=sem.get()
            se=sec.get()
            de=dep.get()
            c=code.get()
            da=dateee.get()
            t=teac.get()
            p=period.get()
            r=remark.get()
            if not (fn and ln and u and s and se and de and c and da and t and p and r):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO teacherabsent VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(u, fn, ln, s, se, de, c, da, t, p, r)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    
        def iass():
            re=reg.get()
            subj=sub.get()
            ass=assign.get()
            scc=sc.get()
            e=teac.get()
            if not (re and subj and ass and e and scc):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields. Dont forget to enter teacher id.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO assignmentmarks VALUES ("{}","{}","{}","{}","{}")' \
                                      .format(e,re,ass,scc,subj)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    
        def iquiz():
            ren=regnn.get()
            su=subj.get()
            q=quiz.get()
            sco=score.get()
            e=teac.get()
            if not (ren and su and q and e and sco):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields. Dont forget to enter teacher id.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO quizmarks VALUES ("{}","{}","{}","{}","{}")' \
                                      .format(e,ren,su,q,sco)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    
        def icie():
            us=usnreg.get()
            js=subject.get()
            ci=cie.get()
            e=teac.get()
            scoe=scored.get()
            if not (us and js and ci and e and scoe):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields. Dont forget to enter teacher id.")
            else:
                ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO ciemarks VALUES ("{}","{}","{}","{}","{}")' \
                                      .format(e,us,ci,js,scoe)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                    else:
                        tkinter.messagebox.showwarning("Fields error", "Please check the fields.")
                
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    
        def iexit():
            result=tkinter.messagebox.askyesno("TEACHER PAGE","Confirm if you want to exit")
            if (result==True):
                root.destroy()
                call(["python","front.py"])
            else:
                root.destroy()
                call(["python","teacher.py"])
            
        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label (TitleFrame,font=('Comic Sans MS',40,'bold'),text="\t\tCLASSROOM DETAIL\t\t",foreground='orange', background='black')
        TitleFrame.pack(side=RIGHT)
        
        
        
        
        DataFrame=Frame(root)
        DataFrame.pack(side=TOP)
        DataFrameleft =LabelFrame(DataFrame,fg="red", font=('arial',14,'bold'),bd=9, text="Add Absent details:")
        DataFrameleft.pack(side=LEFT)
        DataFrameright=LabelFrame(DataFrame,fg="red", font=('arial',16,'bold'),bd=9, text="Assignment and Quiz:")
        DataFrameright.pack(side=RIGHT)
        buttomFrame=Frame(root,bd=13)
        buttomFrame.pack(side=TOP)

        
        

        #absentees
        lblname=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="First Name:")
        lblname.grid(row=2,column=0)
        txtname =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=fname,  width=20)
        txtname.grid(row=2,column=1)

        lbllname=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Last Name:")
        lbllname.grid(row=3,column=0)
        txtlname =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=lname,  width=20)
        txtlname.grid(row=3,column=1)
        
        lblusn=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="USN:")
        lblusn.grid(row=4,column=0)
        txtusn =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=usn,  width=20)
        txtusn.grid(row=4,column=1)

        lblsem=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Semester:")
        lblsem.grid(row=5,column=0)
        txtsem =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=sem,  width=20)
        txtsem.grid(row=5,column=1)

        lblsec=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Section:")
        lblsec.grid(row=6,column=0)
        txtsec=Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=sec,  width=20)
        txtsec.grid(row=6,column=1)

        lbldep=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Department:")
        lbldep.grid(row=7,column=0)
        txtdep =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=dep,  width=20)
        txtdep.grid(row=7,column=1)

        lblsub=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Subject code:")
        lblsub.grid(row=8,column=0)
        txtsub =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=code,  width=20)
        txtsub.grid(row=8,column=1)

        lbldate=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Date:")
        lbldate.grid(row=9,column=0)
        txtdate =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=dateee,  width=20)
        txtdate.grid(row=9,column=1)

        lblteac=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Teacher Name:")
        lblteac.grid(row=10,column=0)
        txtteac =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=teac,  width=20)
        txtteac.grid(row=10,column=1)

        lblpe=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Period:")
        lblpe.grid(row=11,column=0)
        txtpe =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=period,  width=20)
        txtpe.grid(row=11,column=1)

        lblre=Label(DataFrameleft,font=('Times Roman',11,'bold'),text="Remark:")
        lblre.grid(row=12,column=0)
        txtre =Entry(DataFrameleft, font=('arial',11,'bold'),textvariable=remark,  width=20)
        txtre.grid(row=12,column=1)

        btndisplay=Button(DataFrameleft, font=('arial',11,'bold'), text="Absent",width=15,bg="orange",fg="white",command=isave)
        btndisplay.grid(row=13,column=1)

        #assignment

        lblinfo=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Assignment total score= 25;",fg='blue')
        lblinfo.grid(row=1,column=0)

        lblinfo2=Label(DataFrameright,font=('Times Roman',11,'bold'),text=" Quiz total score= 15(5 each);",fg='blue')
        lblinfo2.grid(row=1,column=1)

        lblinfo3=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Not submitted= 0",fg='blue')
        lblinfo3.grid(row=1,column=2)

        lblcl=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Usn:")
        lblcl.grid(row=2,column=0)
        txtcl =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=reg,  width=20)
        txtcl.grid(row=2,column=1)

        lblsub=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Subject:")
        lblsub.grid(row=3,column=0)
        txtsub =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=sub,  width=20)
        txtsub.grid(row=3,column=1)
        

        lblass=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Assignment No:")
        lblass.grid(row=4,column=0)
        txtass =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=assign,  width=20)
        txtass.grid(row=4,column=1)

        lblsc=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Score:")
        lblsc.grid(row=5,column=0)
        txtsc =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=sc,  width=20)
        txtsc.grid(row=5,column=1)

        btndisplay=Button(DataFrameright, font=('arial',11,'bold'), text="Assignment score",width=15,bg="blue",fg="white",command=iass)
        btndisplay.grid(row=6,column=1)


        #quiz

        lblclas=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Usn:")
        lblclas.grid(row=7,column=1)
        txtclas =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=regnn,  width=20)
        txtclas.grid(row=7,column=2)

        lblsubj=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Subject:")
        lblsubj.grid(row=8,column=1)
        txtsubj =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=subj,  width=20)
        txtsubj.grid(row=8,column=2)
        

        lblquiz=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Quiz No:")
        lblquiz.grid(row=9,column=1)
        txtquiz =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=quiz,  width=20)
        txtquiz.grid(row=9,column=2)

        lblscore=Label(DataFrameright,font=('Times Roman',11,'bold'),text="Score:")
        lblscore.grid(row=10,column=1)
        txtscore =Entry(DataFrameright, font=('arial',11,'bold'),textvariable=score,  width=20)
        txtscore.grid(row=10,column=2)

        btndisplay=Button(DataFrameright, font=('arial',11,'bold'), text="Quiz score",width=15,bg="indigo",fg="white",command=iquiz)
        btndisplay.grid(row=11,column=2)

        #cie
        lblin=Label(buttomFrame,font=('Times Roman',14,'bold'),text="CIE SCORE",fg='red')
        lblin.grid(row=0,column=0)

        lblusnreg=Label(buttomFrame,font=('Times Roman',11,'bold'),text="Usn:")
        lblusnreg.grid(row=1,column=0)
        txtusnreg=Entry(buttomFrame, font=('arial',11,'bold'),textvariable=usnreg,  width=18)
        txtusnreg.grid(row=1,column=1)

        lblsubject=Label(buttomFrame,font=('Times Roman',11,'bold'),text="Subject:")
        lblsubject.grid(row=1,column=2)
        txtsubject =Entry(buttomFrame, font=('arial',11,'bold'),textvariable=subject,  width=18)
        txtsubject.grid(row=1,column=3)

        lblcie=Label(buttomFrame,font=('Times Roman',11,'bold'),text="CIE:")
        lblcie.grid(row=1,column=4)
        txtcie =Entry(buttomFrame, font=('arial',11,'bold'),textvariable=cie,  width=18)
        txtcie.grid(row=1,column=5)

        lblscored=Label(buttomFrame,font=('Times Roman',11,'bold'),text="Score:")
        lblscored.grid(row=1,column=6)
        txtscored =Entry(buttomFrame, font=('arial',11,'bold'),textvariable=scored,  width=19)
        txtscored.grid(row=1,column=7)

        btndisplay=Button(buttomFrame, font=('arial',11,'bold'), text="CIE score",width=15,bg="green",fg="white",command=icie)
        btndisplay.grid(row=2,column=7)
        btniexit=Button(buttomFrame, font=('arial',11,'bold'), text="Exit",width=10,bg="red",fg="white",command=iexit)
        btniexit.grid(row=2,column=0)

        
        




root=Tk()
obj=teacher(root)
root.mainloop()
