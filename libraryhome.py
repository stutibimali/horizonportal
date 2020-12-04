from tkinter import*
from tkinter import ttk
import random
from datetime import date
from datetime import timedelta
import tkinter.messagebox
from subprocess import call

class libraryhome():
    def __init__(self,root):        
       
        #============================================================frame setting======================================================================
        self.root=root
        self.root.title("HORIZON OFFICIAL PORTAL")
        self.root.geometry("1100x570+40+50")
        self.root.resizable(False,False)
        
        self.bg=PhotoImage(file="librarybg.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

         #========================================================button function========================================================================
        def ibook():
            root.destroy()
            call(["python","book.py"])
            
            
        def ireturn():
            root.destroy()
            call(["python","returnbook.py"])
             
        def iexit():
            result=tkinter.messagebox.askyesno("HORIZON OFFICIAL PORTAL","Confirm if you want to exit")
            if (result==True):
                root.destroy()
                call(["python","front.py"])
            else:
                root.destroy()
                call(["python","libraryhome.py"])

        self.bookDbBtn = PhotoImage(file='booknow.png')
        self.bookDbBtnLbl = Button(self.root, image=self.bookDbBtn,command=ibook)
        self.bookDbBtnLbl.pack()
        self.bookDbBtnLbl.place(x=250, y=150)
        
        self.bookDbBtn2 = PhotoImage(file='returnbook.png')
        self.bookDbBtnLb2 = Button(self.root, image=self.bookDbBtn2,command=ireturn)
        self.bookDbBtnLb2.pack()
        self.bookDbBtnLb2.place(x=565, y=150)

    
        self.bookDbBtnLb3 = Button(self.root,text="EXIT",fg="white",bg="indigo",font=('Arial',15,'bold'),command=iexit)
        self.bookDbBtnLb3.pack()
        self.bookDbBtnLb3.place(x=1000, y=500)

root= Tk()
obj=libraryhome(root)
root.mainloop()

    


