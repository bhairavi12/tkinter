import os
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import pyodbc

class Login:   
    def __init__(self,root):  #default constructor,pass window
        self.root=root
        self.root.title("V-Cafeteria")
        self.root.geometry("1000x1000+100+0")
        
        #==BG Image====
        self.bg_icon=ImageTk.PhotoImage(file="D:\Bhairavi\PROJECT/VitCanteenn.jpg",)  
        #self.bg_image=Label(self.root,image=self.bg_icon).place(x=0,y=0,relwidth=1,relheight=2)
        bg_lbl = Label(self.root,image=self.bg_icon).pack()
        self.root.resizable(False,False)
        
        title=Label(self.root,text="V-CAFETERIA",font=("times new roman",40,"bold"),bg="white",fg="darkblue",relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        

        #====Login frame===
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=250,y=250,height=350,width=500)
        

        title=Label(Frame_login,text="V-LOGIN",font=("CopperplGoth Bd BT",30,"bold"),bg="white",fg="green").place(x=180,y=5)
        des=Label(Frame_login,text="Login and start ordering food!!!! ",font=("Lucida Handwriting",10,"bold"),bg="blue",fg="yellow").place(x=120,y=80)

                        #pngvalaimage
        self.bg_Vitlogo=PhotoImage(file="D:\Bhairavi\PROJECT\Vit_logooo.png")
        #self.bg_image=Label(self.root,image=self.bg_Vitlogo).place(x=100,y=0,relwidth=1,relheight=2)
        #logolbl=Label(Frame_login,image=self.bg_Vitlogo).grid(row=100,column=5,pady=10)
        logolbl=Label(self.root,image=self.bg_Vitlogo).place(x=585,y=390)
        
                    #User,Password,forgotpassword
        self.rno=StringVar()
        self.pass_=StringVar()
        User=Label(Frame_login,text="Username",font=("GoudyOLSt BT",15,"bold"),fg="brown").place(x=100,y=120)
        self.txt_User =Entry(Frame_login,textvariable=self.rno,font=("times new roman",15),bg="lightgray").place(x=100,y=160,height=35)

        Pass=Label(Frame_login,text="Password",font=("GoudyOLSt BT",15,"bold"),fg="brown").place(x=100,y=220)
        self.txt_Pass =Entry(Frame_login,textvariable=self.pass_,show="*",font=("times new roman",15),bg="lightgray").place(x=100,y=260,height=35)

        forgot_btn=Button(Frame_login,command=self.forgot_PasswordWindow,text="Forget Password ?",bg="white",fg="brown",bd=0,font=("GoudyOLSt BT",10)).place(x=100,y=310,height=35)
        register_btn=Button(self.root,command=self.register_window,text="Click Here to Register",bg="white",fg="brown",bd=0,font=("GoudyOLSt BT",10)).place(x=500,y=560,height=35)
        
        login_btn=Button(self.root,command=self.login_function,text="LOGIN ",bg="green",fg="white",font=("GoudyOLSt BT",15,"bold")).place(x=600,y=530,height=35)
    


    def forgot_Password(self):
        print( self.rno.get(),self.sq.get(),self.sa.get(),self.new.get())
    #For Forgotcall
    def forgot_PasswordWindow(self):
        
        if self.rno.get() == "" :
           messagebox.showerror("Error","Please Enter the  Rollno to Reset Password",parent=self.root)
        else:
            try:
                conn = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DIKSHA-PC\SQLEXPRESS;'
                                       'Database=BHAIRAVI;'
                                       'Trusted_Connection=yes;')

                cur =conn.cursor()
                Querey=("SELECT * FROM REGISTER"
                            " WHERE ROLLNO= ? ")
                Values = [self.rno.get()]


                cur.execute(Querey,Values)
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter the vaild Rollno to Reset Password",parent=self.root)
        
                    
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("340x350+320+270") #width,height,x,y
                    self.root.config(bg="white")# to remove background colour of Forgot password
                    self.root2.focus_force() # blur the back Screen
                    self.root2.grab_set()
                    
                    self.sq =StringVar()
                    self.sa =StringVar()
                    self.new =StringVar()

                    titleof_forgot=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="brown").place(x=0,y=10,relwidth=1)
                    #Forgotwindow
                    SecurityQuestion=Label(self.root2,text="Security Question",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=50)
                    self.txt_sq =ttk.Combobox(self.root2,textvariable=self.sq,font=("times new roman",15),state='readonly',justify=CENTER)
                    self.txt_sq['values']=("Select","Your First Pet Name","Your Favrorite Actor","Your Birth Place")
                    self.txt_sq.place(x=50,y=80,height=30)
                    self.txt_sq.current(0) #first element display on top tox
                    SecurityAnswer=Label(self.root2,text="Security Answer",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=130)
                    self.txt_sa =Entry(self.root2,textvariable=self.sa,font=("times new roman",15),bg="white").place(x=50,y=160,height=30)
                    SecurityAnswer=Label(self.root2,text="New Password",font=("GoudyOLSt BT",15,"bold"),fg="black").place(x=50,y=210)
                    self.newvala =Entry(self.root2,textvariable=self.new,font=("times new roman",15),bg="white").place(x=50,y=240,height=30)

                    changePassword=Button(self.root2,text="Change Password",command=self.forgot_Password,bg="green",fg="white",bd=3,font=("GoudyOLSt BT",15,"bold")).place(x=50,y=300,height=30)
             
                

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
       

            
    #For registrationCall
        
    def register_window(self):
        self.root.destroy()
        import register

    def login_function(self):
        if self.rno.get() == "" or self.pass_.get() =="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DIKSHA-PC\SQLEXPRESS;'
                                       'Database=BHAIRAVI;'
                                       'Trusted_Connection=yes;')

                cur =conn.cursor()
                Querey=("SELECT * FROM REGISTER"
                            " WHERE ROLLNO= ? AND PASSWORD=?")
                Values = [self.rno.get(),self.pass_.get()]


                cur.execute(Querey,Values)
                row=cur.fetchone()
                if row==None:
                    messagebox.showwarning("Error","Invalid Username or Password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Sucessful",f"WELCOME!  {self.rno.get()}")
                    

                #conn.commit()

                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
    #GET DATA EG    BHAIRAVI 123456
    '''
    def login_function(self):
        print(self.uname.get(),self.pass_.get())
    '''  
    
         



root = Tk()   #constructor of tkinter module
obj = Login(root)
root.mainloop()
