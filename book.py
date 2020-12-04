from tkinter import*
from tkinter import ttk
import random
from datetime import date
from datetime import timedelta
import tkinter.messagebox
import mysql.connector
from subprocess import call

class book():
    def __init__(self,root):
            self.root=root
            self.root.title("LIBRARY")
            self.root.geometry("1200x580+150+50")
            self.root.resizable(False,False)
            self.bg=PhotoImage(file="librarybg.png")
            
            Member=StringVar()
            BookTitle=StringVar()
            BookID=StringVar()
            Ref=StringVar()
            Author=StringVar()
            FirstName=StringVar()
            Surname=StringVar()
            Usn=StringVar()
            DateBorrowed=StringVar()
            DateDue=StringVar()
            Mobileno=StringVar()
            Department=StringVar()
            Semester=StringVar()
            IssuedBy=StringVar()
            
            def iReset():
                Member.set("")
                BookTitle.set("")
                BookID.set("")
                Ref.set("")
                Author.set("")
                FirstName.set("")
                Surname.set("")
                Usn.set("")
                DateBorrowed.set("")
                DateDue.set("")
                Mobileno.set("")
                Department.set("")
                Semester.set("")
                IssuedBy.set("")
                txtDisplayR.delete("1.0",END)
            

            def iExit():
                result=tkinter.messagebox.askyesno("Library","Confirm if you want to exit")
                if (result==True):
                   root.destroy()
                   call(["python","libraryhome.py"])
                else:
                   root.destroy()  
                   call(["python","book.py"])
                
        

            def iSave():
                
                m=Member.get()
                bo=BookTitle.get()
                ib=BookID.get()
                r=Ref.get()
                a=Author.get()
                fn=FirstName.get()
                sn=Surname.get()
                u=Usn.get()
                mo=Mobileno.get()
                dab=DateBorrowed.get()
                dad=DateDue.get()
                d=Department.get()
                s=Semester.get()
                i=IssuedBy.get()
                if not (m and bo and ib and r and a and fn and sn and u and mo and dab and dad and d and s and i):
                    tkinter.messagebox.showwarning("Fields Empty", "Please enter all the fields.")
                else:
                    txtDisplayR.insert(END,'Member:\t\t'+ Member.get()+"\n")
                    txtDisplayR.insert(END,'Book Title:\t\t'+ BookTitle.get()+"\n")
                    txtDisplayR.insert(END,'Book ID:\t\t'+ BookID.get()+"\n")
                    txtDisplayR.insert(END,'Ref No:\t\t'+ Ref.get()+"\n")
                    txtDisplayR.insert(END,'Author:\t\t'+ Author.get()+"\n")
                    txtDisplayR.insert(END,'First Name:\t\t'+ FirstName.get()+"\n")
                    txtDisplayR.insert(END,'Surname:\t\t'+ Surname.get()+"\n")
                    txtDisplayR.insert(END,'ID:\t\t'+ Usn.get()+"\n")
                    txtDisplayR.insert(END,'Mobile no:\t\t'+ Mobileno.get()+"\n")
                    txtDisplayR.insert(END,'Date Borrowed:\t\t'+ DateBorrowed.get()+"\n")
                    txtDisplayR.insert(END,'Date Due:\t\t'+ DateDue.get()+"\n")
                    txtDisplayR.insert(END,'Late return fine:\t\t'+ Department.get()+"\n")
                    txtDisplayR.insert(END,'Semester:\t\t'+ Semester.get()+"\n")
                    txtDisplayR.insert(END,'Issued By:\t\t'+ IssuedBy.get()+"\n")
                        ###Database COMMAND 
                    try:
                        connection = mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
                        if connection.is_connected():
                            mysql_insert= 'INSERT INTO library VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                                      .format(m, ib, a, dab, dad, u, d, bo, r, fn, sn, mo, s, i)
                            cursor = connection.cursor()
                            cursor.execute(mysql_insert)
                            connection.commit()
                        
                            tkinter.messagebox.showinfo("Data Saved", "The data was successfully saved!")
                                        
                    except Error as e:
                        print("Error while connecting to MySQL", e)
               
          #==========================Frame===============================
            MainFrame = Frame(root)
            MainFrame.grid()
            
            TitleFrame =Frame(MainFrame)
            TitleFrame.pack(side=TOP)
            TitleFrame=Label(TitleFrame,font=('Comic Sans MS',40,'bold'),width=38,text="LIBRARY",foreground="orange",bg="black")
            TitleFrame.pack()
            
            
            DataFrame =Frame(MainFrame, bd=9, width=1030, bg="black",height=500, padx=9, relief=RIDGE)
            DataFrame.pack()
            self.bg_image=Label(DataFrame,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
            DataFrameLEFT =LabelFrame(DataFrame, bd=9, width=1200, height=600, padx=9, relief=RIDGE, font=('arial',12,'bold'),foreground="red", text="Library Info:")
            DataFrameLEFT.pack()
            DataFrameLEFT.place(x=50, y=20)
            DataFrameRIGHT =LabelFrame(DataFrame, bd=9, width=1200, height=600, padx=9, relief=RIDGE, font=('arial',12,'bold'),foreground="red", text="Recent Book Details:")
            DataFrameRIGHT.pack()
            DataFrameRIGHT.place(x=440, y=50)
            ButtonFrame =Frame(MainFrame, width=1200, height=50)
            ButtonFrame.pack()
            ButtonFrame.place(x=130, y=520)

        #==========================Widget==============================
            lblmember =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Member:",padx=2,pady=2)
            lblmember.grid(row=0,column=0,sticky=W)
            cbomember = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'), textvariable=Member, state='readonly',width=18)
            cbomember['value'] = ('','Student', 'Lecturer')  
            cbomember.current(0)
            cbomember.grid(row=0,column=1)
            
            lblBookTitle =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Book Title:",padx=2,pady=2)
            lblBookTitle.grid(row=1,column=0,sticky=W)
            txtBookTitle=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=BookTitle, width=20)
            txtBookTitle.grid(row=1,column=1)
            
            lblBookID =Label(DataFrameLEFT, font=('arial',12,'bold'),text="Book ID:",padx=2,pady=2)
            lblBookID.grid(row=2,column=0,sticky=W)
            txtBookID =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=BookID,  width=20)
            txtBookID.grid(row=2,column=1)
            
            lblRef =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Reference No:",padx=2,pady=2)
            lblRef.grid(row=3,column=0,sticky=W)
            txtRef =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Ref, width=20)
            txtRef.grid(row=3,column=1)
            
            lblAuthor =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Author:",padx=2,pady=2)
            lblAuthor.grid(row=4,column=0,sticky=W)
            txtAuthor=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Author, width=20)
            txtAuthor.grid(row=4,column=1)
            
            lblFirstName =Label(DataFrameLEFT, font=('arial',12,'bold'), text="First Name:",padx=2,pady=2)
            lblFirstName.grid(row=5,column=0,sticky=W)
            txtFirstName=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=FirstName, width=20)
            txtFirstName.grid(row=5,column=1)
            
            lblDateBorrowed =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Date Borrowed:",padx=2,pady=2)
            lblDateBorrowed.grid(row=6,column=0,sticky=W)
            txtDateBorrowed=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=DateBorrowed, width=20)
            txtDateBorrowed.grid(row=6,column=1)
            
            lblSurname =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Surname:",padx=2,pady=2)
            lblSurname.grid(row=7,column=0,sticky=W)
            txtSurname =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Surname, width=20)
            txtSurname.grid(row=7,column=1)
            
            lblDateDue =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Date Due:",padx=2,pady=2)
            lblDateDue.grid(row=8,column=0,sticky=W)
            txtDateDue=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=DateDue, width=20)
            txtDateDue.grid(row=8,column=1)
            
            lblMobileno =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Mobile no:",padx=2,pady=2)
            lblMobileno.grid(row=9,column=0,sticky=W)
            txtMobileno =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Mobileno, width=20)
            txtMobileno.grid(row=9,column=1)
            
            lblUsn =Label(DataFrameLEFT, font=('arial',12,'bold'), text="USN:",padx=2,pady=2)
            lblUsn.grid(row=10,column=0,sticky=W)
            txtUsn =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Usn , width=20)
            txtUsn.grid(row=10,column=1)
            
            lblDepartment =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Department:",padx=2,pady=2)
            lblDepartment.grid(row=11,column=0,sticky=W)
            txtDepartment =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Department, width=20)
            txtDepartment.grid(row=11,column=1)
            
            lblSemester =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Semester:",padx=2,pady=2)
            lblSemester.grid(row=12,column=0,sticky=W)
            txtSemester =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Semester, width=20)
            txtSemester.grid(row=12,column=1)
            
            lblIssuedby =Label(DataFrameLEFT, font=('arial',12,'bold'),text="Issued By:",padx=2,pady=2)
            lblIssuedby.grid(row=13,column=0,sticky=W)
            txtIssuedby =Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=IssuedBy,  width=20)
            txtIssuedby.grid(row=13,column=1)
        #======================================Widget================
            txtDisplayR=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=32,height=13,padx=8,pady=20)
            txtDisplayR.grid(row=0,column=2)
        #======================================Listbox================
            scrollbar=Scrollbar(DataFrameRIGHT)
            scrollbar.grid(row=0,column=1,sticky='ns')
            ListOfBooks=['ada','math','dbms','facd','ci','c programming','unix','chemistry','physics','electronic','python','qbasic','co','dmgt','math2','os','ads','caed','projects','math3']
            booklist=Listbox(DataFrameRIGHT,font=('arial',12,'bold'),width=15,height=12)
            
            def SelectedBook(evnt):
                values = str(booklist.get(booklist.curselection()))
                w=values
                if(w=='ada'):
                    BookID.set("ISBN 567896545678")
                    BookTitle.set("Analysis and design algorithm")
                    Author.set("ramalal")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='math'):
                    BookID.set("ISBN 09876458765")
                    BookTitle.set("mathematics part1")
                    Author.set("saam")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                
                
                elif(w=='dbms'):
                    BookID.set("ISBN 98547734658")
                    BookTitle.set("Database Management System")
                    Author.set("tinu")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='facd'):
                    BookID.set("ISBN 567896545678")
                    BookTitle.set("Finite Automata")
                    Author.set("rama")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='ci'):
                    BookID.set("ISBN 46738920448")
                    BookTitle.set("computational intelligence")
                    Author.set("adwin")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='c programming'):
                    BookID.set("ISBN 876543567543")
                    BookTitle.set("c programming")
                    Author.set("sita")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='unix'):
                    BookID.set("ISBN 7686768696")
                    BookTitle.set("Unix")
                    Author.set("fred")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='chemistry'):
                    BookID.set("ISBN 676767676768")
                    BookTitle.set("chemistry")
                    Author.set("om")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='physics'):
                    BookID.set("ISBN 34535463564 ")
                    BookTitle.set("physics")
                    Author.set("ramprakash")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='electronic'):
                    BookID.set("ISBN 123456543455")
                    BookTitle.set("Electronics")
                    Author.set("william")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='python'):
                    BookID.set("ISBN 655675656543")
                    BookTitle.set("Python")
                    Author.set("reesma")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                
                elif(w=='qbasic'):
                    BookID.set("ISBN 567896545678")
                    BookTitle.set("Analysis and design algorithm")
                    Author.set("ramalal")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='co'):
                    BookID.set("ISBN 45678987689")
                    BookTitle.set("computer organization")
                    Author.set("yukta")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='dmgt'):
                    BookID.set("ISBN 876546784456")
                    BookTitle.set("Discrete mathematics")
                    Author.set("govinda")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='math2'):
                    BookID.set("ISBN 0987123456432")
                    BookTitle.set("Mathematics part2")
                    Author.set("aaradhya")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='os'):
                    BookID.set("ISBN 34567898767")
                    BookTitle.set("operating system")
                    Author.set("ramalal")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    return
                
                elif(w=='ads'):
                    BookID.set("ISBN 987678987678")
                    BookTitle.set("Advanced data structure")
                    Author.set("shobha")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                    
                elif(w=='caed'):
                    BookID.set("ISBN 765456765456")
                    BookTitle.set("CAED")
                    Author.set("gopal")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='projects'):
                    BookID.set("ISBN 543456545665")
                    BookTitle.set("Miniproject sample")
                    Author.set("Various")
                    
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
                
                elif(w=='math3'):
                    BookID.set("ISBN 2345678989")
                    BookTitle.set("Mathematics part3")
                    Author.set("krishna")
                    today=date.today()
                    d1=today.strftime("%Y-%m-%d")
                    d2=today+timedelta(days=15)
                    DateBorrowed.set(d1)
                    DateDue.set(d2)
                    
            booklist.bind('<<ListboxSelect>>',SelectedBook)  
            booklist.grid(row=0,column=0,padx=8)
            scrollbar.config(command=booklist.yview)

            for items in ListOfBooks:
                booklist.insert(END,items)
    
        #==========================Button==============================
            btnSaveData =Button(ButtonFrame, font=('arial',12,'bold'), text="Save Data",width=25,bg="indigo",fg="white",command=iSave)
            btnSaveData.grid(row=0,column=1)
            
            btnReset =Button(ButtonFrame, font=('arial',12,'bold'), text="Reset",width=25,bg="indigo",fg="white", command=iReset)
            btnReset.grid(row=0,column=4)
            btnExit =Button(ButtonFrame, font=('arial',12,'bold'), text="Exit",width=25,bg="indigo",fg="white", command=iExit)
            btnExit.grid(row=0,column=6)





root=Tk()
obj=book(root)
root.mainloop()
 
