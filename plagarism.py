from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import filedialog
from subprocess import call

class plagarism:
    
    def __init__(self,root):
       file1=StringVar()
       file2=StringVar()
       file1text=StringVar()
       file2text=StringVar()
       self.root=root
       self.root.title("HORIZON OFFICIAL PORTAL")
       self.root.geometry("1340x650+30+30")
       self.root.resizable(False,False)
       self.btnc= PhotoImage(file='f:\python\project\searchbtn.png')
       self.btnplag=PhotoImage(file='f:\python\project\pla.png')

       def exitm():
           result=tkinter.messagebox.askyesno("PLAGARISM ","Confirm if you want to exit")
           if (result==True):
               root.destroy()
               call(["python","front.py"])
           else:
               root.destroy()  
               call(["python","plagarism.py"])

       def searchh():
           fname = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a directory',filetypes = (("Text File","*.txt"), ("All files", "*")))
           file1.set(fname)
          

       def search1():
           fname2 = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a directory',filetypes = (("Text File","*.txt"), ("All files", "*")))
           file2.set(fname2)
           
           
       def plag():
                     
           fname=file1.get()
           f = open(fname, "r")
           text1=f.readlines()
           str1=''.join(text1)
           sent_text1=str1.split('.')
           a=len(str1)
           fname2=file2.get()
           g= open(fname2,"r")
           text2=g.readlines()
           str2=''.join(text2)
           sent_text2=str2.split('.')
           b=len(str2)
           
           final_list=[]
           for z in sent_text1:
               for y in sent_text2:
                   if z==y:
                       final_list.append(z)
                   
           str3=''.join(final_list)
           c=len(str3)
           if(c==0):
               txtdisplay1.insert(END, "NO MATCHING TEXT FOUND")
               txtdisplay2.insert(END, "NO MATCHING TEXT FOUND")
           else: 
               txtdisplay1.insert(END, final_list)
               txtdisplay2.insert(END, final_list)
           percent=(c/(a+b))*100
           txtper.insert(END, percent)
      

       MainFrame = Frame(root)
       MainFrame.grid()
    
       TitleFrame=Frame(MainFrame, bd=9, width=1300)
       TitleFrame.pack(side=TOP)
       TitleFrame=Label(TitleFrame, font=('Comic Sans MS',40,'bold'),text="       CHECK PLAGARISM OF TWO REPORT      ", fg='white',bg='grey',bd=10, relief=RAISED)
       TitleFrame.pack()
       
       DataFrame=Frame(MainFrame, bd=9, width=1320,height=700)
       DataFrame.pack(side=TOP)

       lblchooose=Label(DataFrame,font=('Arial',16,'bold italic'),text="Choose file 1",fg="blue")
       lblchooose.pack() 
       lblchooose.place(x=10,y=10)

       txtchooose=Entry(DataFrame,font=('arial',12,'bold'),textvariable=file1,width=40)
       txtchooose.pack()
       txtchooose.place(x=200,y=14)
       
       btnchoose1=Button(DataFrame,image=self.btnc,command=searchh)
       btnchoose1.place(x=580,y=0)
       

       lblchoose=Label(DataFrame,font=('Arial',16,'bold italic'),text="Choose file 2",fg="blue")
       lblchoose.pack() 
       lblchoose.place(x=650,y=10)

       txtchoose=Entry(DataFrame,font=('Arial',12,'bold italic'),textvariable=file2,width=40)
       txtchoose.pack()
       txtchoose.place(x=840,y=14)

       btnchoose2=Button(DataFrame,image=self.btnc,command=search1)
       btnchoose2.place(x=1220,y=0)

       btnplaga=Button(DataFrame,image=self.btnplag,command=plag)
       btnplaga.place(x=520,y=70)

       lblfile=Label(DataFrame,font=('Arial',16,'bold italic'),text="File One :",fg="purple")
       lblfile.pack() 
       lblfile.place(x=10,y=60)

       
       txtdisplay1=Text(DataFrame,font=('arial',12,'bold'),bd=5,width=55,height=10,relief=RAISED)
       txtdisplay1.place(x=0,y=90)
       

       lblfile2=Label(DataFrame,font=('Arial',16,'bold italic'),text="File Two :",fg="purple")
       lblfile2.pack() 
       lblfile2.place(x=770,y=60)

       
     
       txtdisplay2=Text(DataFrame,font=('arial',12,'bold'),width=57,bd=5,height=10,relief=RAISED)
       txtdisplay2.place(x=770,y=90)
      

       lblper=Label(DataFrame,font=('Arial',16,'bold italic'),text="PLAGARISM \nPERCENTAGE",fg="green")
       lblper.pack() 
       lblper.place(x=570,y=180)


       txtper=Text(DataFrame,font=('arial',12,'bold'),width=20,height=1,bd=3,relief=RIDGE)
       txtper.place(x=550,y=240)

       lblinfo=Label(MainFrame,font=('Arial',16,'bold italic'),text="NOTE :\t\t\t\t\t\t\t\t\t\t\n  Both the files should be in .txt format.\t\t\t\t\t\t\n  Plagarism is checked in sentence wise rather than paragraph.\t\t\t\t\n",fg="red")
       lblinfo.pack() 
       lblinfo.place(x=10,y=420)

       lblinfo2=Label(MainFrame,font=('Arial',16,'bold'),text="What is plagarism?\nPlagiarism is presenting someone else’s work or ideas as your own, with or without their consent, by incorporating it into your work  \n without full acknowledgement. All published and unpublished material, whether in manuscript, printed or electronic form, is\t\t\ncovered under this definition. Plagiarism may be intentional or reckless, or unintentional. Under the regulations for examinations,      \n intentional or reckless plagiarism is a disciplinary offence.\t\t\t\t\t\t\t\t",fg="white",bg="blue")
       lblinfo2.pack() 
       lblinfo2.place(x=0,y=500)

       btnexit=Button(MainFrame,font=('arial',11,'bold'),text="EXIT",bg='red',fg='white',width=5,command=exitm)
       btnexit.place(x=1200,y=450)


      
root=Tk()
obj=plagarism(root)
root.mainloop()


