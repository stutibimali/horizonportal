from tkinter import*
from tkinter import ttk
from datetime import date
from datetime import timedelta
import tkinter.messagebox
import mysql.connector
from subprocess import call

class exam:
    
    def __init__(self,root):
        fname=StringVar()
        lname=StringVar()
        usn=StringVar()
        sem=StringVar()
        sec=StringVar()
        dep=StringVar()
        cgpa=StringVar()
        sgpa=StringVar()
        year=StringVar()
        edited=StringVar()
        self.root=root
        self.root.title("EXAMINATION")
        self.root.geometry("1200x500+20+20")
        self.root.resizable(False,False)
        self.bg=PhotoImage(file="F://python/project/bd.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        

        def isave():
            f=fname.get()
            l=lname.get()
            u=usn.get()
            s=sem.get()
            se=sec.get()
            d=dep.get()
            c=cgpa.get()
            sg=sgpa.get()
            y=year.get()
            ed=edited.get()
            if not (f and l and u and s and se and d and c and sg and y and ed ):
                tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
                
            else:
                        ###Database COMMAND 
                try:
                    connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                    if connection.is_connected():
                        mysql_insert= 'INSERT INTO exam VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(u,f,l,s,se,d,c,sg,y,ed)
                        cursor = connection.cursor()
                        cursor.execute(mysql_insert)
                        connection.commit()
                        
                        tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                                        
                except Error as e:
                    print("Error while connecting to MySQL", e)

        def ireset():
            f=fname.set("")
            l=lname.set("")
            u=usn.set("")
            s=sem.set("")
            se=sec.set("")
            d=dep.set("")
            c=cgpa.set("")
            sg=sgpa.set("")
            y=year.set("")
            ed=edited.set("")
            
        def iexit():
            result=tkinter.messagebox.askyesno("Exam","Confirm if you want to exit")
            if (result==True):
                root.destroy()
                call(["python","front.py"])
            else:
                root.destroy()
                call(["python","exam.py"])
                
        TitleFrame =Frame(root)
        TitleFrame.pack(side=TOP)
        TitleFrame=Label (TitleFrame,font=('Comic Sans MS',40,'bold'),text="EXAM DETAILS",foreground='orange',bg='black')
        TitleFrame.pack(side=RIGHT)
        DataFrame=Frame(root)
        DataFrame.pack(side=TOP)
        DataFrame=LabelFrame(DataFrame, bd=9, width=800, height=380,background="grey",fg="black",padx=11, relief=RIDGE, font=('arial',16,'bold'), text="EXAM REPORT:")
        DataFrame.pack(side=LEFT)

        lblname=Label(DataFrame,font=('Times Roman',16,'bold'),text="First Name:",background="grey",fg="black")
        lblname.grid(row=0,column=0)
        txtname =Entry(DataFrame, font=('arial',11,'bold'),textvariable=fname,  width=25)
        txtname.grid(row=0,column=1)
        
        lblsur=Label(DataFrame,font=('Times Roman',16,'bold'),text="Last Name:",background="grey",fg="black")
        lblsur.grid(row=1,column=0)
        txtsur =Entry(DataFrame, font=('arial',11,'bold'),textvariable=lname,  width=25)
        txtsur.grid(row=1,column=1)
        
        lblUsn=Label(DataFrame,font=('Times Roman',16,'bold'),text="USN:",background="grey",fg="black")
        lblUsn.grid(row=2,column=0)
        txtusn =Entry(DataFrame, font=('arial',11,'bold'),textvariable=usn,  width=25)
        txtusn.grid(row=2,column=1)
        
        lblsemester=Label(DataFrame,font=('Times Roman',16,'bold'),text="Semester:",background="grey",fg="black")
        lblsemester.grid(row=3,column=0)
        txtsem =Entry(DataFrame, font=('arial',11,'bold'),textvariable=sem,  width=25)
        txtsem.grid(row=3,column=1)

        lblsection=Label(DataFrame,font=('Times Roman',16,'bold'),text="Section:",background="grey",fg="black")
        lblsection.grid(row=4,column=0)
        txtsection =Entry(DataFrame, font=('arial',11,'bold'),textvariable=sec,  width=25)
        txtsection.grid(row=4,column=1)
        
        lbldep=Label(DataFrame,font=('Times Roman',16,'bold'),text="Department:",background="grey",fg="black")
        lbldep.grid(row=5,column=0)
        txtdep =Entry(DataFrame, font=('arial',11,'bold'),textvariable=dep,  width=25)
        txtdep.grid(row=5,column=1)
        
        lblcgpa=Label(DataFrame,font=('Times Roman',16,'bold'),text="CGPA:",background="grey",fg="black")
        lblcgpa.grid(row=6,column=0)
        txtcgpa=Entry(DataFrame, font=('arial',11,'bold'),textvariable=cgpa,  width=25)
        txtcgpa.grid(row=6,column=1)

        lblsgpa=Label(DataFrame,font=('Times Roman',16,'bold'),text="SGPA:",background="grey",fg="black")
        lblsgpa.grid(row=7,column=0)
        txtsgpa=Entry(DataFrame, font=('arial',11,'bold'),textvariable=sgpa,  width=25)
        txtsgpa.grid(row=7,column=1)

        lblyear=Label(DataFrame,font=('Times Roman',16,'bold'),text="Year:",background="grey",fg="black")
        lblyear.grid(row=8,column=0)
        txtyear=Entry(DataFrame, font=('arial',11,'bold'),textvariable=year,  width=25)
        txtyear.grid(row=8,column=1)

        lbledited=Label(DataFrame,font=('Times Roman',16,'bold'),text="Edited By:",background="grey",fg="black")
        lbledited.grid(row=9,column=0)
        txtedited=Entry(DataFrame, font=('arial',11,'bold'),textvariable=edited,  width=25)
        txtedited.grid(row=9,column=1)

        ButtonFrame=Frame(root)
        ButtonFrame.pack(side=TOP)
        btnsave=Button(ButtonFrame, font=('arial',16,'bold'), text="SAVE",width=15,bg="green",fg="white",command=isave)
        btnsave.grid(row=1,column=0)
        btnexit=Button(ButtonFrame, font=('arial',16,'bold'), text="EXIT",width=15,bg="red",fg="white",command=iexit)
        btnexit.grid(row=1,column=2)
        btnreset=Button(ButtonFrame, font=('arial',16,'bold'), text="RESET",width=15,bg="indigo",fg="white",command=ireset)
        btnreset.grid(row=1,column=1)

root=Tk()
obj=exam(root)
root.mainloop()
        
