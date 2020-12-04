from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from subprocess import call
import mysql.connector

class Student:

    def __init__(self,root):
        self.root=root
        self.root.title("Student Management")
        self.root.geometry("1200x560+50+50")
        self.root.resizable(False,False)
        self.logo_icon=PhotoImage(file="f://python/project/iconst.PNG")
        REG=StringVar()
        SEC=StringVar()
        SEM=StringVar()
        dob=StringVar()
        def login():
            u=REG.get()
            s=SEC.get()
            se=SEM.get()
            d=dob.get()
            if not (u and s and se and d):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mycursor=connection.cursor()
                        sql='Select registerno,section,semester,dob from student where registerno="{}" and section="{}" and semester="{}" and dob="{}"'.format(u,s,se,d)
                        mycursor.execute(sql)
                        wName=mycursor.fetchall()
                        if not wName:
                            tkinter.messagebox.showinfo("Fields Error", "Please enter all the fields correctly.")
                            REG.set("")
                            dob.set("")
                        else:
                            #login successful
                            root.destroy()
                            call(["python","studentmain.py"])
                        mycursor.close()
                    else:
                        print("Error in db connection")
                except Error as e:
                    print("Error while connecting to MySQL", e)
            
                
        def exitm():
            result=tkinter.messagebox.askyesno("STUDENT PAGE","Confirm if you want to exit")
            if (result==True):
                root.destroy()
                call(["python","front.py"])
            else:
                root.destroy()
                call(["python","student.py"])
            
            
        
        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label(TitleFrame,font=('Comic Sans MS',40,'bold'),text="\t\tSTUDENT PORTAL\t\t\t",foreground='black', background='orange')
        TitleFrame.pack(side= RIGHT)
        dataFrame= Frame(root)
        dataFrame.pack(side=TOP)
        dataFrame.pack(side=LEFT)
        lblname=Label(dataFrame,font=('Times Roman',16,'bold'),text="STUDY PORTAL - LOGIN\t\t\t\n_____________________________________________\n\n")
        lblname.grid(row=0,column=0)
        Image_label=Label(dataFrame,image=self.logo_icon).grid(row=0,column=1)
        lblbrief=Label(dataFrame,font=('Times Roman',12,'bold'),text="Please enter Semester and Section.\t\t\t\t\n Registration No. is the USN number\t\t\t\t", foreground="grey")
        lblbrief.grid(row=2,column=0)
        lblusn=Label(dataFrame,font=('Times Roman',12,'bold'),text="\t\t\t\tREGISTER NO.:")
        lblusn.grid(row=3,column=0)
        txtregister=Entry(dataFrame, font=('arial',12,'bold'),textvariable=REG, width=25)
        txtregister.grid(row=3,column=1)
        lbldob=Label(dataFrame,font=('Times Roman',12,'bold'),text="\t\t\t\t\t DOB:")
        lbldob.grid(row=4,column=0)
        txtdob=Entry(dataFrame, font=('arial',12,'bold'),textvariable=dob, width=25)
        txtdob.grid(row=4,column=1)
        lblsemester=Label(dataFrame,font=('Times Roman',12,'bold'),text="\t\t\t\t      SEMESTER:")
        lblsemester.grid(row=5,column=0)
        cbomember = ttk.Combobox(dataFrame, font=('arial',12,'bold'),textvariable=SEM, state='readonly',width=23)
        cbomember['value'] = ('1','2', '3','4','5','6','7','8')  
        cbomember.current(0)
        cbomember.grid(row=5,column=1)  
        lblsection=Label(dataFrame,font=('Times Roman',12,'bold'),text="\t\t\t\t          SECTION:")
        lblsection.grid(row=6,column=0)
        cbomember1 = ttk.Combobox(dataFrame, font=('arial',12,'bold'),textvariable=SEC, state='readonly',width=23)
        cbomember1['value'] = ('A','B', 'C','D')  
        cbomember1.current(0)
        cbomember1.grid(row=6,column=1)  
        btnlog=Button(dataFrame,font=('Arial',12,'bold'),text="LOGIN",bg="indigo",fg="white",command=login)
        btnlog.grid(row=8,column=1)
        btnexit=Button(dataFrame,font=('Arial',12,'bold'),text="EXIT",bg="indigo",fg="white",command=exitm)
        btnexit.grid(row=8,column=0)
               

        
        
        

root=Tk()
obj=Student(root)
root.mainloop()
