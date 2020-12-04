from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from subprocess import call
import mysql.connector

class Studentmain:
    
    def __init__(self,root):
       self.root=root
       self.root.title("New Horizon College of Engineering")
       self.root.geometry("1280x730+10+10")
       self.root.resizable(False,False)
       self.calenderevent=PhotoImage(file="f://python/project/calandarevent.PNG")

       def exam():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1400x720+20+20")
           connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
           if connection.is_connected():
               mycur=connection.cursor()
               sql='Select * from exam'
               mycur.execute(sql)
               rows=mycur.fetchall()
               
               
           qframe=Frame(sub,bd=1,relief=RIDGE)

           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1280,height=80)
           q.pack()
           for i in range(100):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\t\tEXAM MARKS\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           txtframe.pack(side=TOP)
           textw=ttk.Treeview(txtframe, columns=(1,2,3,4,5,6,7),show="headings",height=15)
           textw.pack()
           textw.heading(1, text="USN")
           textw.heading(2, text="NAME")
           textw.heading(3, text="SURNAME")
           textw.heading(4, text="SEMESTER")
           textw.heading(5, text="SECTION")
           textw.heading(6, text="DEPARTMENT")
           textw.heading(7, text="CGPA")
          
           for i in rows:
               textw.insert('','end',values=i)
           sub.mainloop() 
                      

           
       def fee():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1400x720+20+20")
           connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
           if connection.is_connected():
               mycur=connection.cursor()
               sql='Select regno, fname,surname, semester, department, due from account'
               mycur.execute(sql)
               rows=mycur.fetchall()
           qframe=Frame(sub,bd=1,relief=RIDGE)

           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1280,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\t\t\tFEE INFORMATION\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text=Text(txtframe, height=25, width=185)
           txtframe.pack(side=TOP)
           textw=ttk.Treeview(txtframe, columns=(1,2,3,4,5,6),show="headings",height=15)
           textw.pack()
           textw.heading(1, text="USN")
           textw.heading(2, text="NAME")
           textw.heading(3, text="SURNAME")
           textw.heading(4, text="SEMESTER")
           textw.heading(5, text="DEPARTMENT")
           textw.heading(6, text="DUE")
          
           for i in rows:
               textw.insert('','end',values=i)

           sub.mainloop()
    #####################################################################button functions###################################################################################
       def mentor():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1200x720+20+20")
           qframe=Frame(sub,bd=1,relief=RIDGE)

           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1280,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\t\tMiniproject Reviewer\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text=Text(txtframe, height=25, width=185)
           txtEmbed=open('F:/python/project/mentor.txt')
           lines=txtEmbed.read()
           txtEmbed.close()
           text.insert(END,lines)
           text.pack(side=LEFT,fill=X,padx=5)
           sb=Scrollbar(txtframe,orient=VERTICAL,command=text.yview)
           sb.pack(side=RIGHT,fill=Y)
           text.configure(yscrollcommand=sb.set)
           txtframe.pack(expand=1,fill=X,pady=10,padx=5)
           sub.mainloop()

       def examt():
           tkinter.messagebox.showinfo("ALERT", "NOT YET DECIDED.\nTHE DATES OF EXAM WILL BE DISPLAYED 2 WEEKS PRIOR THE EXAM *-*")
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1400x720+20+20")
           connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
           if connection.is_connected():
               mycur=connection.cursor()
               sql='Select DATES, Day, morning_shift, evening_shift, afternoon_shift from examtable'
               mycur.execute(sql)
               rows=mycur.fetchall()
           qframe=Frame(sub,bd=1,relief=RIDGE)

           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1280,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\t\t\tEXAM TIMETABLE\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text=Text(txtframe, height=25, width=185)
           txtframe.pack(side=TOP)
           textw=ttk.Treeview(txtframe, columns=(1,2,3,4,5),show="headings",height=15)
           textw.pack()
           textw.heading(1, text="DATES")
           textw.heading(2, text="DAY")
           textw.heading(3, text="MORNING SHIFT")
           textw.heading(5, text="EVENING SHIFT")
           textw.heading(4, text="AFTERNOON SHIFT")
          
          
           for i in rows:
               textw.insert('','end',values=i)

           sub.mainloop()
           

       def logical():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1200x720+20+20")
           qframe=Frame(sub,bd=1,relief=RIDGE)
           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1580,height=80)
           q.pack()
           for i in range(85):
                   q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\t\tLogical Reasoning\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text2=Text(txtframe, height=25, width=185)
           txtEmbed=open('F:/python/project/logical.txt')
           lines=txtEmbed.read()
           txtEmbed.close()
           text2.insert(END,lines)
           text2.pack(side=LEFT,fill=X,padx=5)
           sb=Scrollbar(txtframe,orient=VERTICAL,command=text2.yview)
           sb.pack(side=RIGHT,fill=Y)
           text2.configure(yscrollcommand=sb.set)
           txtframe.pack(expand=1,fill=X,pady=10,padx=5)
           sub.mainloop()
           
       def quants():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1200x720+20+20")
           qframe=Frame(sub,bd=1,relief=RIDGE)

           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1580,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(600,50,text='\t\tQuantitative\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text=Text(txtframe, height=25, width=185)
           txtEmbed=open('F:/python/project/quant.txt')
           lines=txtEmbed.read()
           txtEmbed.close()
           text.insert(END,lines)
           text.pack(side=LEFT,fill=X,padx=5)
           sb=Scrollbar(txtframe,orient=VERTICAL,command=text.yview)
           sb.pack(side=RIGHT,fill=Y)
           text.configure(yscrollcommand=sb.set)
           txtframe.pack(expand=1,fill=X,pady=10,padx=5)
           sub.mainloop()
           
       def classt():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1300x500+20+20")
           sub.resizable(False,False)
           sub.icon=PhotoImage(file="f://python/project/time.PNG")
           qframe=Frame(sub,bd=1,relief=RIDGE)
           t=StringVar()
           q=Canvas(qframe,bg='Navajo White',width=1350,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(400,50,text='\t\t\tClass timetable\t\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           dataframe=Frame(qframe)
           dataframe.pack()
           Image_label=Label(dataframe,image=sub.icon,bg='black',width=1350).grid(row=0,column=1)
           sub.mainloop()
           
       def intre():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1200x720+20+20")
           qframe=Frame(sub,bd=1,relief=RIDGE)
           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t\tNew Horizon College of Engineering\t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1580,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\t\tData Interpretation\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text=Text(txtframe, height=25, width=185)
           txtEmbed=open('F:/python/project/data.txt')
           lines=txtEmbed.read()
           txtEmbed.close()
           text.insert(END,lines)
           text.pack(side=LEFT,fill=X,padx=5)
           sb=Scrollbar(txtframe,orient=VERTICAL,command=text.yview)
           sb.pack(side=RIGHT,fill=Y)
           text.configure(yscrollcommand=sb.set)
           txtframe.pack(expand=1,fill=X,pady=10,padx=5)
           sub.mainloop()
           
       def pseudo():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1200x720+20+20")
           qframe=Frame(sub,bd=1,relief=RIDGE)
           titleframe=Frame(sub,bd=2,relief=RIDGE)
           Label(titleframe,text='\t New Horizon College of Engineering \t',fg='red', font=('arial',30,'bold')).pack(side=LEFT,padx=5)
           t=StringVar()
           titleframe.pack(expand=1,fill=X,pady=10,padx=5)
           q=Canvas(qframe,bg='Navajo White',width=1580,height=80)
           q.pack()
           for i in range(65):
               q.create_oval(20+(20*i),20+(9*i),(320*i)+90,(i)+690,fill='Bisque')
           q.create_text(500,50,text='\tPseudocode\t',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           txtframe=Frame(sub,bd=2,relief=RAISED)
           text=Text(txtframe, height=25, width=185)
           txtEmbed=open('F:/python/project/pseudo.txt')
           lines=txtEmbed.read()
           txtEmbed.close()
           text.insert(END,lines)
           text.pack(side=LEFT,fill=X,padx=5)
           sb=Scrollbar(txtframe,orient=VERTICAL,command=text.yview)
           sb.pack(side=RIGHT,fill=Y)
           text.configure(yscrollcommand=sb.set)
           txtframe.pack(expand=1,fill=X,pady=10,padx=5)
           sub.mainloop()
           
       def csesy():
           sub=Toplevel(root)
           sub.title("New Horizon College of Engineering")
           sub.geometry("1100x720+20+20")
           sub.resizable(False,False)
           sub.icon=PhotoImage(file="f://python/project/scheme.PNG")
           qframe=Frame(sub,bd=1,relief=RIDGE,bg="black")
           t=StringVar()
           q=Canvas(qframe,bg='Navajo White',width=1200,height=80)
           q.pack()
           dataframe=Frame(qframe)
           dataframe.pack()
           for i in range(65):
               q.create_oval(10+(10*i),10+(9*i),(120*i)+90,(i)+190,fill='Bisque')
           q.create_text(370,50,text='\t\tScheme of subject',font=('arial',40,'bold'))
           qframe.pack(expand=1,fill=X,pady=10,padx=5)
           Image_label=Label(dataframe,image=sub.icon,bg='grey',width=800).grid(row=0,column=1)
           sub.mainloop()
                
       def exitm():
           result=tkinter.messagebox.askyesno("STUDENT PAGE","Confirm if you want to exit")
           if (result==True):
               root.destroy()
               call(["python","front.py"])
           else:
               root.destroy()  
               call(["python","studentmain.py"])
          ############################################################################### frame setting ################################################################### 

       MainFrame = Frame(root)
       MainFrame.grid()

       TitleFrame =Frame(MainFrame)
       TitleFrame.pack(side=TOP)
       TitleFrame=Label(TitleFrame,font=('Comic Sans MS',40,'bold'),text="\tEVENTS AND INFORMATIONS\t",foreground='black', background='orange')
       TitleFrame.pack(side= RIGHT)
       
       DataFrame =Frame(MainFrame, bd=9, width=1170,height=650, padx=9, relief=RIDGE)
       DataFrame.pack()
       DataFrameLEFT=LabelFrame(DataFrame,font=('Comic Sans MS',12,'bold'), text="CALANDER OF EVENTS",fg="red",padx=10,pady=10,bd=5,width=20, height=40)
       DataFrameLEFT.pack()
       DataFrameLEFT.place(x=0, y=5)
       DataFrameRIGHT=LabelFrame(DataFrame,font=('Comic Sans MS',12,'bold'), text=" IMPORTANT ",fg="red",padx=10,pady=10,bd=5,width=340, height=620)
       DataFrameRIGHT.pack()
       DataFrameRIGHT.place(x=800, y=5)
       
       Image_label=Label(DataFrameLEFT,image=self.calenderevent).grid(row=0,column=0)

       btnexam=Button(DataFrameRIGHT, font=('Arial',12,'bold'),text="EXAM RESULT",bg="indigo", fg="white",command=exam)
       btnexam.place(x=0, y=0)
       btnfee=Button(DataFrameRIGHT,font=('Arial',12,'bold'),text="FEE INFORMATION",bg="indigo",fg="white",command=fee)
       btnfee.place(x=150, y=0)
       
       lblaptitude=Label(DataFrameRIGHT,font=('Arial',12,'bold italic'),text="APTITUDE NOTES",fg="green")
       lblaptitude.place(x=80, y=40)
       
       btnlogical=Button(DataFrameRIGHT, font=('Arial',12,'bold'), text="LOGICAL REASONING",bg="red", fg="white",command=logical)
       btnlogical.place(x=0, y=80)
       
       btnquants=Button(DataFrameRIGHT, font=('Arial',12,'bold'), text="QUANTITATIVE APTITUDE ",bg="red", fg="white",command=quants)
       btnquants.place(x=0, y=120)
       
       btnintre=Button(DataFrameRIGHT, font=('Arial',12,'bold '), text="DATA INTERPRETATION",bg="red", fg="white",command=intre)
       btnintre.place(x=0, y=160)

       btnpseudo=Button(DataFrameRIGHT, font=('Arial',12,'bold '), text="PSEUDOCODE ",bg="red", fg="white",command=pseudo)
       btnpseudo.place(x=0, y=200)


       lblacad=Label(DataFrameRIGHT,font=('Arial',12,'bold italic'),text="ACADEMIC",fg="blue")
       lblacad.place(x=90, y=240)


       btnreviewer=Button(DataFrameRIGHT, font=('Arial',12,'bold '), text="REVIEWER LIST ",bg="grey", fg="white",command=mentor)
       btnreviewer.place(x=0, y=280)

       btnexamtimetable=Button(DataFrameRIGHT, font=('Arial',12,'bold '), text="EXAM TIMETABLE",bg="grey", fg="white",command=examt)
       btnexamtimetable.place(x=0, y=320)

       btncseclasstable=Button(DataFrameRIGHT, font=('Arial',12,'bold '), text="CSE CLASS TIMETABLE",bg="grey", fg="white",command=classt)
       btncseclasstable.place(x=0, y=360)

       btncsesy=Button(DataFrameRIGHT, font=('Arial',12,'bold '), text="SCHEME OF SYLLABUS",bg="grey", fg="white",command=csesy)
       btncsesy.place(x=0, y=400)

       lblinfor=Label(DataFrameRIGHT,font=('Arial',10,'bold italic'),text="Each Subject notes are in respective classroom \n Please check the classroom code from the \n respective subject teachers",fg="purple")
       lblinfor.place(x=0, y=440)

       btnexit=Button(DataFrameRIGHT, font=('Arial',12,'bold'), text="EXIT",bg="indigo", fg="white",command=exitm)
       btnexit.place(x=250, y=535)
             


root=Tk()
obj=Studentmain(root)
root.mainloop()        
