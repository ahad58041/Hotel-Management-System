from tkinter import*
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import mysql.connector
from hotel import HotelManagementSystem


def main():
    win = Tk()
    app = login_window(win)  # Pass the Tk instance to login_window
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Azure's Inn Login")
        self.root.geometry("1550x800+0+0")

        bg_image = Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\bkg1.jpg")
        bg_image = bg_image.resize((1550, 800), Image.LANCZOS)  # Resize to fit the window

        self.bg = ImageTk.PhotoImage(bg_image)

        lbl_bkg = Label(self.root, image=self.bg)
        lbl_bkg.place(x=0, y=0, relwidth=1, relheight=1)


        frame=Frame(self.root,bg="black")
        frame.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\login2.png")
        img1=img1.resize((235,100),Image.LANCZOS)

        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=610,y=175,width=235,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=97,y=99)

        #lable for user name

        username_label=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_label.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        #password

        # Password entry field with placeholder logic
        self.txtpass = ttk.Entry(
            frame,
            font=("Times New Roman", 12),
        )
        self.txtpass.place(x=40, y=250, width=270)

        
        def on_focus_in(event):
            if self.txtpass.get() == "Enter your password":
                self.txtpass.delete(0, "end")
                self.txtpass.config(show="*")  # Mask the input

        # Function to handle focus-out event (add placeholder)
        def on_focus_out(event):
            if not self.txtpass.get():  # If the entry is empty
                self.txtpass.config(show="")  
                self.txtpass.insert(0, "Enter your password")

        self.txtpass.insert(0, "Enter your password")

        # Bind events to handle focus-in and focus-out
        self.txtpass.bind("<FocusIn>", on_focus_in)
        self.txtpass.bind("<FocusOut>", on_focus_out)





#---------------------icon images-----------------
        img2=Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\user.png")
        img2=img2.resize((25,25),Image.LANCZOS)

        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=600,y=325,width=25,height=25)


        img3=Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\password.png")
        img3=img3.resize((25,25),Image.LANCZOS)

        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=600,y=394,width=25,height=25)

            #login btn
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=0,borderwidth=0,relief=RIDGE,fg="black",bg="#AAD1E7",activeforeground="white",activebackground="#187194")
        login_btn.place(x=110,y=299,width=120,height=35)

            #register btn
        register_btn=Button(frame,text="Register new user",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_btn.place(x=15,y=350,width=160)

            #forget register
        forget_btn=Button(frame,text="Forget Password!",command=self.forgot_pass_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forget_btn.place(x=10,y=375,width=160)
 
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)

        elif self.txtuser.get()=="Ahad" and self.txtpass.get()=="123":
            messagebox.showinfo("Error","Welcome to Azzure Inn hotel Management system ",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * from register where email=%s and password=%s",(


                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin",parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root)  # Correctly pass the root as the parent
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()



#----------------------------reset pass button---------------------------

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question",parent=self.root2)
        elif self.txt_security_entry.get() == "":
            messagebox.showerror("Error", "Enter the answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Enter the new Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="bank_management"
            )
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Incorrect data. Please check your entries.",parent=self.root2)
            else:
                query1 = ("update register set password=%s where email=%s")
                value1 = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query1, value1)
                conn.commit()
                messagebox.showinfo("Azure's Inn Hotel Management", "Your Password has been reset",parent=self.root2)
            
            conn.close()
            self.root2.destroy()

#=----------------------------forget pass window-------------------------------------------
    def forgot_pass_window(self):
        if self.txtuser.get() =="":
            messagebox.showerror("Error","Please Enter the Email Address To Reset Password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
        if row==None:
            messagebox.showerror("Error","Enter the valid user name",parent=self.root)
        else:
            conn.close()
            self.root2=Toplevel(    )
            self.root2.title("Forgot Password")
            self.root2.geometry("342x452+561+170")

            l=Label(self.root2,text="Forget Password", font=("times new roman", 18, "bold"),fg="black")
            l.place(x=0,y=10,relwidth=1)
#--------------------secQ--------------------------
        security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"))
        security_Q.place(x=50,y=80)

        self.combo_security_Q=ttk.Combobox(self.root2,font=("arial",12,"bold"),width=27,state="readonly")
        self.combo_security_Q["value"]=("Select","Name of your first pet","What is your favorite food","Name of your first crush")
        self.combo_security_Q.place(x=50,y=110,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
        security_A.place(x=50,y=150)

        self.txt_security_entry=ttk.Entry(self.root2,font=("times new roman",15))
        self.txt_security_entry.place(x=50,y=180,width=250)


        new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
        new_password.place(x=50,y=220)

        self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
        self.txt_newpass.place(x=50,y=250,width=250)

        btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="black",bg="white")
        btn.place(x=100,y=290)


           
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  #----------------------------------
  #                                  Register
  #                                          --------------------------------------------------------------------               

        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Register")
        self.root.geometry("1550x800+0+0")


        #----------------data variables---------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



# bkg img----------------------------
        bg_image = Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\sky.jpg")
        bg_image = bg_image.resize((1550, 800), Image.LANCZOS)  # Resize to fit the window

        self.bg = ImageTk.PhotoImage(bg_image)

        lbl_bkg = Label(self.root, image=self.bg)
        lbl_bkg.place(x=0, y=0, relwidth=1, relheight=1)

#-----------left img--------------------

        bg_image1 = Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\bkg2.jpg")
        bg_image1 = bg_image1.resize((470, 550), Image.LANCZOS)  # Resize to fit the window

        self.bg1 = ImageTk.PhotoImage(bg_image1)

        lbl_bkg = Label(self.root, image=self.bg1)
        lbl_bkg.place(x=50, y=100, width=470, height=550)
#------------main frame----------------
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_label=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black")
        register_label.place(x=20,y=20)
#-------------lables and entry-------------------------------
#row1
        self.var_fname = StringVar()
        self.var_lname = StringVar()

        # Validation function
        def validate_name(input_str):
            if input_str.isalpha() or input_str == "":
                return True
            else:
                messagebox.showerror("Invalid Input", "Name should contain only alphabets!",parent=self.root)
                return False

        # Register validation function
        validate_cmd = root.register(validate_name)

        # First Name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"), 
                                validate="key", validatecommand=(validate_cmd, "%P"))
        fname_entry.place(x=50, y=130, width=250)

        #last name
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=380, y=100)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"), 
                                validate="key", validatecommand=(validate_cmd, "%P"))
        lname_entry.place(x=380, y=130, width=250)

#row2
        
        self.var_contact = StringVar()
        self.var_email = StringVar()

        # Validation function for contact
        def validate_contact(input_str):
            if input_str.isdigit() or input_str == "":
                return True
            else:
                messagebox.showerror("Invalid Input", "Contact should contain only numeric digits!",parent=self.root)
                return False

        # Register validation function
        validate_cmd = root.register(validate_contact)

        # Contact Label and Entry
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"),
                                  validate="key", validatecommand=(validate_cmd, "%P"))
        contact_entry.place(x=50, y=200, width=250)

        def validate_email(input_str):
            # Regular expression for email validation with specific domains (gmail.com or outlook.com)
            email_pattern = r"^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com|yahoo\.com|icloud\.com)$"
            if re.match(email_pattern, input_str) or input_str == "":  # Allow empty input
                return True
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid email address with @gmail.com or @outlook.com or @yahoo.com or @icloud.com", parent=self.root)
                return False

        # Register validation function
        validate_cmd = root.register(validate_email)

        # Email Label and Entry
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=380, y=170)

        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"),
                                validate="focusout", validatecommand=(validate_cmd, "%P"))
        email_entry.place(x=380, y=200, width=250)
#row3

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("arial",12,"bold"),width=27,state="readonly")
        self.combo_security_Q["value"]=("Select","Name of your first pet","What is your favorite food","Name of your first crush")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security_entry=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security_entry.place(x=380,y=270,width=250)

#row4

        paswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        paswd.place(x=50,y=310)

        paswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        paswd_entry.place(x=50,y=340,width=250)

        cnfrm_paswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        cnfrm_paswd.place(x=370,y=310)

        cnfrm_paswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        cnfrm_paswd_entry.place(x=370,y=340,width=250)

#---------------------chck btn---------------------
        self.var_check=IntVar()
        check_button=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        check_button.place(x=50,y=380)



#------------------btns------------------

        img3=Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\reg.png")
        img3=img3.resize((200,140),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        b1=Button(frame,command=self.register_data,image=self.photoimage3,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=405,width=300)


        img4=Image.open(r"C:\Users\PMLS\Desktop\Ict lab projet\Hotel Management system\images\logbtn.png")
        img4=img4.resize((150,40),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage4,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=420,width=300)
#function declaration:

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
             messagebox.showerror("Error","Agree our Terms and Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Try with another email",parent=self.root)
            else:
                my_cursor.execute(" insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                
                                                        self.var_fname.get(),
                                                        self.var_lname.get(),
                                                        self.var_contact.get(),
                                                        self.var_email.get(),
                                                        self.var_securityQ.get(),
                                                        self.var_SecurityA.get(),
                                                        self.var_pass.get() 
                ))                        
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully ",parent=self.root)
           
           
    def return_login(self):
        self.root.destroy()           


if __name__ =="__main__":
        main()
