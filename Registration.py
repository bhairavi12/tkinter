import os
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import pyodbc

class Register:   
    def __init__(self,root):  #default constructor,pass window
        self.root=root
        self.root.title("V-Cafeteria")
        self.root.geometry("1000x1000+100+0")
        #==BG Image====
        self.bg_icon=ImageTk.PhotoImage(file="D:\Bhairavi\PROJECT\Login/VITclgg.jpg",)#backgroundpg
        #self.bg_image=Label(self.root,image=self.bg_icon).place(x=0,y=0,relwidth=1,relheight=2)
        bg_lbl = Label(self.root,image=self.bg_icon).pack()
        self.root.resizable(False,False)
        
        title=Label(self.root,text="V-CAFETERIA",font=("times new roman",40,"bold"),bg="white",fg="darkblue",relief=GROOVE) 
        title.place(x=0,y=0,relwidth=1)

        #====Login frame===
        Frame_login=Frame(self.root,bg="lightyellow")   #login window
        Frame_login.place(x=200,y=150,height=500,width=550)
        

        title=Label(Frame_login,text="V-REGISTER",font=("CopperplGoth Bd BT",30,"bold"),bg="lightyellow",fg="green").place(x=160,y=5)
        
                            #User,Password,forgotpassword

        self.fname =StringVar()
        self.lname =StringVar()
        self.email =StringVar()
        self.contact =StringVar()
        self.rno =StringVar()
        self.sq =StringVar()
        self.sa =StringVar()
        self.pass_=StringVar()
        self.Conpass_=StringVar()
        self.chkbox=IntVar()
        #UI OF REGISTRATIONWINDOW
        FirstName=Label(Frame_login,text="First Name",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=80)
        self.txt_fname =Entry(Frame_login,textvariable=self.fname,font=("times new roman",15),bg="white").place(x=50,y=120,height=30)
        LastName=Label(Frame_login,text="Last Name",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=300,y=80)
        self.txt_lname =Entry(Frame_login,textvariable=self.lname,font=("times new roman",15),bg="white").place(x=300,y=120,height=30)

        Email=Label(Frame_login,text="Email",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=150)
        self.txt_email =Entry(Frame_login,textvariable=self.email,font=("times new roman",15),bg="white").place(x=50,y=190,height=30)
        Contact=Label(Frame_login,text="Contact",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=300,y=150)
        self.txt_contact =Entry(Frame_login,textvariable=self.contact,font=("times new roman",15),bg="white").place(x=300,y=190,height=30)

        RollNo=Label(Frame_login,text="Roll No",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=360)
        self.txt_rno =Entry(Frame_login,textvariable=self.rno,font=("times new roman",15),bg="white").place(x=50,y=390,height=30)
        #Security Question
        SecurityQuestion=Label(Frame_login,text="Security Question",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=220)
        self.txt_sq =ttk.Combobox(Frame_login,textvariable=self.sq,font=("times new roman",15),state='readonly',justify=CENTER)
        self.txt_sq['values']=("Select","Your First Pet Name","Your Favrorite Actor","Your Birth Place")
        self.txt_sq.place(x=50,y=260,height=30)
        self.txt_sq.current(0) #first element display on top tox
        SecurityAnswer=Label(Frame_login,text="Security Answer",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=300,y=220)
        self.txt_sa =Entry(Frame_login,textvariable=self.sa,font=("times new roman",15),bg="white").place(x=300,y=260,height=30)

        Password=Label(Frame_login,text="Password",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=290)
        self.txt_pass =Entry(Frame_login,textvariable=self.pass_,font=("times new roman",15),bg="white").place(x=50,y=320,height=30)
        ConfirmPassword=Label(Frame_login,text="Confirm Password",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=300,y=290)
        self.txt_Conpass =Entry(Frame_login,textvariable=self.Conpass_,show="*",font=("times new roman",15),bg="white").place(x=300,y=320,height=30)
        #registerbtn and Agree Condition
        Register_btn=Button(self.root,command=self.register_data,text="Register Here",bg="green",fg="white",bd=3,font=("GoudyOLSt BT",15,"bold")).place(x=320,y=600,height=35,width=300)
        login_btn=Button(self.root,command=self.loginwindow_call,text="Go to login",bg="blue",fg="white",bd=3,font=("GoudyOLSt BT",15,"bold")).place(x=500,y=550,height=35,width=200)
        
        chk=Checkbutton(Frame_login,variable=self.chkbox,text="I Agree The Terms & Conditions",font=("GoudyOLSt BT",10,"bold"),fg="black").place(x=300,y=360)
                                    #CLEAR function                         
    '''
    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0,END)  
        self.email.delete(0,END)  
        #self.contact.delete(0,END) 
        self.contact.dele 
        self.sq.current(0) 
        self.sa.delete(0,END)   
        self.rno.delete(0,END)  
        self.pass_.delete(0,END)
        self.Conpass_.delete(0,END)  
    '''
    def loginwindow_call(self):
        self.root.destroy()
        import REGISTERANDLOGIN

                                   
                                   
                                    #registration function
    def register_data(self):
        '''# TO GET ALL DETAILS PRINT
        print(self.fname.get())
        print(self.lname.get()) 
        print(self.email.get())
        print(self.contact.get())
        print(self.rno.get())
        print(self.sq.get()) 
        print(self.sa.get()) 
        print(self.pass_.get())
        print(self.Conpass_.get())
        '''
    
        if self.fname.get()==""  or  self.email.get()=="" or  self.contact.get()=="" or self.sq.get()=="Select" or self.sa.get()=="" or self.pass_.get=="" or self.Conpass_.get()=="" or  self.rno.get()=="" :
            messagebox.showerror("Error","All field are required")
        elif self.chkbox.get()==0:
            messagebox.showerror("Error"," Please Agree The Terms & Conditions")
        elif self.pass_.get() !=  self.Conpass_.get():
            messagebox.showerror("Error","Password & ConfirmPassword is Incorrect")
        else:
            try:       #   Database Conectivity
                conn = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DIKSHA-PC\SQLEXPRESS;'
                                       'Database=BHAIRAVI;'
                                       'Trusted_Connection=yes;')

                cur =conn.cursor()
                #SQL query
                cur.execute("SELECT * FROM REGISTER  WHERE EMAIL= ?" ,self.email.get())
                row=cur.fetchone()
                #print(row)
                if row != None:
                    messagebox.showwarning("Sorry","User Already Exist",parent=self.root)
                else:
                    
                    QuereyofRegister=("INSERT INTO REGISTER (FIRSTNAME, LASTNAME, EMAIL, CONTACTNO, QUESTION, ANSWER, PASSWORD,ROLLNO )  VALUES (?,?,?,?,?,?,?,?) ")
                
                    Values =[(self.fname.get()),
                            (self.lname.get()),
                            (self.email.get()),
                            (self.contact.get()),
                            (self.sq.get()) ,
                            (self.sa.get()) ,
                            (self.pass_.get()),
                            (self.rno.get())]

                    


                    cur.execute(QuereyofRegister,Values)
                
                

                    
                    messagebox.showinfo("Sucessful",f"WELCOME!  {self.fname.get()}")
                    #self.clear()
                    conn.commit()

                    conn.close()
                    

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}")
         

        
    
root = Tk()   #constructor of tkinter module
obj = Register(root)
root.mainloop()
        

        
