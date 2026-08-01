from tkinter import*
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
import re
from db_config import get_connection
from security import hash_password, is_hashed, verify_password
from hotel import HotelManagementSystem
import os
import theme
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")


def main():
    win = Tk()
    app = login_window(win)  # Pass the Tk instance to login_window
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Azure's Inn Login")
        theme.apply_theme(self.root)
        WIN_W,WIN_H=theme.fit_window(self.root,1150,720)

        bg_image = Image.open(os.path.join(IMG_DIR, "bkg1.jpg"))
        bg_image = bg_image.resize((WIN_W, WIN_H), Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(bg_image)

        lbl_bkg = Label(self.root, image=self.bg)
        lbl_bkg.place(x=0, y=0, relwidth=1, relheight=1)

        # the card is centred on the real window instead of a fixed 1550px one
        CARD_W,CARD_H=370,470
        card_x=(WIN_W-CARD_W)//2
        card_y=(WIN_H-CARD_H)//2
        PADX=35
        INNER=CARD_W-PADX*2

        frame=Frame(self.root,bg=theme.INK_DEEP)
        frame.place(x=card_x,y=card_y,width=CARD_W,height=CARD_H)

        img1=Image.open(os.path.join(IMG_DIR, "logo.png"))
        img1=img1.resize((200,84),Image.LANCZOS)

        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimg1,bg=theme.INK_DEEP,borderwidth=0)
        lblimg1.place(x=(CARD_W-200)//2,y=22,width=200,height=84)


        get_str=Label(frame,text="Get Started",font=theme.TITLE,fg=theme.GOLD,bg=theme.INK_DEEP)
        get_str.place(x=0,y=118,width=CARD_W)

#---------------------username-----------------
        img2=Image.open(os.path.join(IMG_DIR, "user.png"))
        img2=img2.resize((18,18),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        Label(frame,image=self.photoimg2,bg=theme.INK_DEEP,borderwidth=0).place(x=PADX,y=163,width=18,height=18)

        username_label=Label(frame,text="Username",font=theme.LABEL,fg="white",bg=theme.INK_DEEP)
        username_label.place(x=PADX+26,y=162)

        self.txtuser=ttk.Entry(frame,font=theme.ENTRY)
        self.txtuser.place(x=PADX,y=188,width=INNER,height=32)

#---------------------password-----------------
        img3=Image.open(os.path.join(IMG_DIR, "password.png"))
        img3=img3.resize((18,18),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        Label(frame,image=self.photoimg3,bg=theme.INK_DEEP,borderwidth=0).place(x=PADX,y=239,width=18,height=18)

        password_label=Label(frame,text="Password",font=theme.LABEL,fg="white",bg=theme.INK_DEEP)
        password_label.place(x=PADX+26,y=238)

        # masked from the start -- the old placeholder text was returned by get(),
        # so an untouched field counted as a filled-in password
        self.txtpass = ttk.Entry(frame,font=theme.ENTRY,show="*")
        self.txtpass.place(x=PADX,y=264,width=INNER,height=32)

        self.var_showpass=IntVar()

        def toggle_pass():
            self.txtpass.config(show="" if self.var_showpass.get() else "*")

        Checkbutton(frame,text="Show password",variable=self.var_showpass,command=toggle_pass,
                    font=theme.SMALL,fg="white",bg=theme.INK_DEEP,selectcolor=theme.INK_DEEP,
                    activebackground=theme.INK_DEEP,activeforeground="white",
                    borderwidth=0,highlightthickness=0,cursor="hand2").place(x=PADX-2,y=302)

            #login btn
        login_btn=Button(frame,text="Login",command=self.login,font=theme.BUTTON,bd=0,
                         relief=FLAT,fg=theme.INK_DEEP,bg=theme.GOLD,
                         activeforeground=theme.INK_DEEP,activebackground=theme.GOLD_BRIGHT,cursor="hand2")
        login_btn.place(x=PADX,y=338,width=INNER,height=38)

            #register btn
        register_btn=Button(frame,text="Register new user",command=self.register_window,font=theme.SMALL,
                            bd=0,relief=FLAT,fg=theme.GOLD,bg=theme.INK_DEEP,anchor="w",
                            activeforeground=theme.GOLD_BRIGHT,activebackground=theme.INK_DEEP,cursor="hand2")
        register_btn.place(x=PADX-2,y=392,width=160,height=24)

            #forget register
        forget_btn=Button(frame,text="Forgot password?",command=self.forgot_pass_window,font=theme.SMALL,
                          bd=0,relief=FLAT,fg=theme.GOLD,bg=theme.INK_DEEP,anchor="w",
                          activeforeground=theme.GOLD_BRIGHT,activebackground=theme.INK_DEEP,cursor="hand2")
        forget_btn.place(x=PADX-2,y=420,width=160,height=24)
 
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)

        else:
            conn=get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT password from register where email=%s",(self.txtuser.get(),))
            row=my_cursor.fetchone()

            if row==None or not verify_password(self.txtpass.get(),row[0]):
                messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
                conn.close()
                return

            #upgrade any leftover plaintext password to a hash on first login
            if not is_hashed(row[0]):
                my_cursor.execute("update register set password=%s where email=%s",(
                                    hash_password(self.txtpass.get()),
                                    self.txtuser.get()
                    ))
                conn.commit()
            conn.close()

            open_main=messagebox.askyesno("YesNo","Access only Admin",parent=self.root)
            if open_main:
                self.new_window = Toplevel(self.root)  # Correctly pass the root as the parent
                self.app = HotelManagementSystem(self.new_window)



#----------------------------reset pass button---------------------------

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question",parent=self.root2)
        elif self.txt_security_entry.get() == "":
            messagebox.showerror("Error", "Enter the answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Enter the new Password",parent=self.root2)
        else:
            conn = get_connection()
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Incorrect data. Please check your entries.",parent=self.root2)
            else:
                query1 = ("update register set password=%s where email=%s")
                value1 = (hash_password(self.txt_newpass.get()), self.txtuser.get())
                my_cursor.execute(query1, value1)
                conn.commit()
                messagebox.showinfo("Azure's Inn Hotel Management", "Your Password has been reset",parent=self.root2)
            
            conn.close()
            self.root2.destroy()

#=----------------------------forget pass window-------------------------------------------
    def forgot_pass_window(self):
        if self.txtuser.get() =="":
            messagebox.showerror("Error","Please Enter the Email Address To Reset Password",parent=self.root)
            return

        conn=get_connection()
        my_cursor = conn.cursor()
        query=("select * from register where email=%s")
        value=(self.txtuser.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        conn.close()

        # everything below used to run even on these two failures, which raised
        # NameError on `row` / AttributeError on self.root2
        if row==None:
            messagebox.showerror("Error","Enter the valid user name",parent=self.root)
            return

        self.root2=Toplevel(self.root)
        self.root2.title("Forgot Password")
        theme.apply_theme(self.root2)
        self.root2.configure(bg=theme.CARD)
        W2,H2=theme.fit_window(self.root2,380,410)

        PADX=50
        FIELD_W=W2-PADX*2

        l=Label(self.root2,text="Reset Password", font=theme.TITLE,fg=theme.INK,bg=theme.CARD)
        l.place(x=0,y=26,relwidth=1)
#--------------------secQ--------------------------
        security_Q=Label(self.root2,text="Select Security Question",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT)
        security_Q.place(x=PADX,y=86)

        self.combo_security_Q=ttk.Combobox(self.root2,font=theme.BODY,state="readonly")
        self.combo_security_Q["value"]=("Select","Name of your first pet","What is your favorite food","Name of your first crush")
        self.combo_security_Q.place(x=PADX,y=112,width=FIELD_W,height=32)
        self.combo_security_Q.current(0)

        security_A=Label(self.root2,text="Security Answer",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT)
        security_A.place(x=PADX,y=160)

        self.txt_security_entry=ttk.Entry(self.root2,font=theme.ENTRY)
        self.txt_security_entry.place(x=PADX,y=186,width=FIELD_W,height=32)


        new_password=Label(self.root2,text="New Password",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT)
        new_password.place(x=PADX,y=234)

        self.txt_newpass=ttk.Entry(self.root2,font=theme.ENTRY,show="*")
        self.txt_newpass.place(x=PADX,y=260,width=FIELD_W,height=32)

        btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=theme.BUTTON,
                   bd=0,relief=FLAT,fg=theme.GOLD,bg=theme.INK,
                   activeforeground=theme.GOLD_BRIGHT,activebackground=theme.INK_LIGHT,cursor="hand2")
        btn.place(x=PADX,y=318,width=FIELD_W,height=40)


           
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  #----------------------------------
  #                                  Register
  #                                          --------------------------------------------------------------------               

        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Register")
        theme.apply_theme(self.root)
        WIN_W,WIN_H=theme.fit_window(self.root,1180,700)


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
        bg_image = Image.open(os.path.join(IMG_DIR, "sky.jpg"))
        bg_image = bg_image.resize((WIN_W, WIN_H), Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(bg_image)

        lbl_bkg = Label(self.root, image=self.bg)
        lbl_bkg.place(x=0, y=0, relwidth=1, relheight=1)

#-----------left img--------------------

        bg_image1 = Image.open(os.path.join(IMG_DIR, "bkg2.jpg"))
        # panel sizes derived from the window so nothing hangs off the edge
        PANEL_Y=40
        PANEL_H=WIN_H-PANEL_Y*2
        SIDE_W=340
        SIDE_X=(WIN_W-(SIDE_W+700))//2
        bg_image1 = bg_image1.resize((SIDE_W, PANEL_H), Image.LANCZOS)

        self.bg1 = ImageTk.PhotoImage(bg_image1)

        lbl_bkg = Label(self.root, image=self.bg1, bd=0)
        lbl_bkg.place(x=SIDE_X, y=PANEL_Y, width=SIDE_W, height=PANEL_H)
#------------main frame----------------
        frame=Frame(self.root,bg=theme.CARD)
        frame.place(x=SIDE_X+SIDE_W,y=PANEL_Y,width=700,height=PANEL_H)

        register_label=Label(frame,text="REGISTER HERE",font=theme.DISPLAY,fg=theme.INK,bg=theme.CARD)
        register_label.place(x=50,y=30)
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
        fname = Label(frame, text="First Name", font=theme.LABEL, bg=theme.CARD)
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=theme.LABEL, 
                                validate="key", validatecommand=(validate_cmd, "%P"))
        fname_entry.place(x=50, y=130, width=250)

        #last name
        lname = Label(frame, text="Last Name", font=theme.LABEL, bg=theme.CARD)
        lname.place(x=380, y=100)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=theme.LABEL, 
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
        contact = Label(frame, text="Contact", font=theme.LABEL, bg=theme.CARD)
        contact.place(x=50, y=170)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=theme.LABEL,
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
        email = Label(frame, text="Email", font=theme.LABEL, bg=theme.CARD)
        email.place(x=380, y=170)

        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=theme.LABEL,
                                validate="focusout", validatecommand=(validate_cmd, "%P"))
        email_entry.place(x=380, y=200, width=250)
#row3

        security_Q=Label(frame,text="Select Security Question",font=theme.LABEL,bg=theme.CARD)
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=theme.LABEL,width=27,state="readonly")
        self.combo_security_Q["value"]=("Select","Name of your first pet","What is your favorite food","Name of your first crush")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=theme.LABEL,bg=theme.CARD)
        security_A.place(x=380,y=240)

        self.txt_security_entry=ttk.Entry(frame,textvariable=self.var_SecurityA,font=theme.BODY)
        self.txt_security_entry.place(x=380,y=270,width=250)

#row4

        paswd=Label(frame,text="Password",font=theme.LABEL,bg=theme.CARD)
        paswd.place(x=50,y=310)

        paswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=theme.LABEL)
        paswd_entry.place(x=50,y=340,width=250)

        cnfrm_paswd=Label(frame,text="Confirm Password",font=theme.LABEL,bg=theme.CARD)
        cnfrm_paswd.place(x=380,y=310)

        cnfrm_paswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=theme.LABEL)
        cnfrm_paswd_entry.place(x=380,y=340,width=250)

#---------------------chck btn---------------------
        self.var_check=IntVar()
        check_button=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=theme.LABEL,onvalue=1,offvalue=0,bg=theme.CARD,activebackground=theme.CARD)
        check_button.place(x=50,y=380)



#------------------btns------------------

        # plain buttons instead of two differently-styled clipart images
        reg_btn=Button(frame,text="REGISTER NOW",command=self.register_data,font=theme.BUTTON,
                       bd=0,relief=FLAT,fg=theme.GOLD,bg=theme.INK,
                       activeforeground=theme.GOLD_BRIGHT,activebackground=theme.INK_LIGHT,cursor="hand2")
        reg_btn.place(x=50,y=430,width=250,height=42)

        back_btn=Button(frame,text="Back to Login",command=self.return_login,font=theme.BUTTON,
                        bd=1,relief=SOLID,fg=theme.INK,bg=theme.CARD,
                        activeforeground=theme.INK,activebackground=theme.PAGE,cursor="hand2")
        back_btn.place(x=380,y=430,width=250,height=42)
#function declaration:

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
             messagebox.showerror("Error","Agree our Terms and Conditions",parent=self.root)
        else:
            conn=get_connection()
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
                                                        hash_password(self.var_pass.get())
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully ",parent=self.root)
           
           
    def return_login(self):
        self.root.destroy()           


if __name__ =="__main__":
        main()
