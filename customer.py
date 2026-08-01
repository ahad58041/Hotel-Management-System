from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import pycountry
import random
from db_config import get_connection
from tkinter import messagebox
import re
import os
import theme
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

class customer_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Management System")
        theme.apply_theme(self.root)
        WIN_W,WIN_H=theme.fit_window(self.root,1360,768)
        HEAD=58



# -----------------------------variables for sql ---------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_customer_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

 # -----------------------Title--------------------------------------
        img2=Image.open(os.path.join(IMG_DIR, "logo.png"))
        img2=img2.resize((88,50),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        theme.header(self.root,"ADD CUSTOMER DETAILS",WIN_W,self.photoimg2,HEAD)

#------------------------lable frame ----------------------
        LEFT_W=520
        body_y=HEAD+theme.PAD
        body_h=WIN_H-body_y-theme.PAD

        leftframe=theme.panel(self.root,"Customer Details")
        leftframe.place(x=theme.PAD,y=body_y,width=LEFT_W,height=body_h)


#------------------------Lables and Enteries-------------------------
        #Customer Refernce
        customer_ref=Label(leftframe,text="Customer Refrence",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        customer_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(leftframe,width=29,state="readonly",textvariable=self.var_ref,font=theme.ENTRY)
        entry_ref.grid(row=0, column=1, pady=2, sticky=W)

        #Customer Name
        cust_name=Label(leftframe,text="Customer Name:",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        cust_name.grid(row=1,column=0,sticky=W)

        txtname=ttk.Entry(leftframe,width=29,textvariable=self.var_customer_name,font=theme.ENTRY)
        txtname.grid(row=1, column=1, pady=2, sticky=W)

        #Mother Name
        moth_name=Label(leftframe,text="Mother Name:",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        moth_name.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(leftframe,width=29,textvariable=self.var_mother,font=theme.ENTRY)
        txtmname.grid(row=2, column=1, pady=2, sticky=W)

        #Gender- combobox
        lable_gender=Label(leftframe,text="Gender:",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lable_gender.grid(row=3,column=0,sticky=W)

        gender_combo=ttk.Combobox(leftframe,textvariable=self.var_gender,font=theme.LABEL,width=27,state="readonly")
        gender_combo["value"]=("Male","Female","Rather not say","Custom")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1, pady=2, sticky=W)

        #Post code
        lblpostcode = Label(leftframe, text="PostCode:", bd=4, font=theme.LABEL, padx=2, pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblpostcode.grid(row=4, column=0, sticky=W)

        txtpostcode = ttk.Entry(leftframe, textvariable=self.var_post, width=29, font=theme.ENTRY)
        txtpostcode.grid(row=4, column=1, pady=2, sticky=W)

        def validate_postcode():
            postcode = self.var_post.get()
            if not postcode.isdigit(): 
                messagebox.showerror("Invalid Postcode", "Please enter a valid postcode containing only numbers.")

        btn_validate = Button(leftframe, text="Verify", command=validate_postcode, font=theme.SMALL)
        btn_validate.grid(row=4, column=2, sticky=W, padx=(6,0))

        #mobile number
        lblmobile=Label(leftframe,text="Mobile: ",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(leftframe,textvariable=self.var_mobile,width=29,font=theme.ENTRY)
        txtmobile.grid(row=5, column=1, pady=2, sticky=W)

        def validate_mobileno():
            mobile = self.var_mobile.get()
            if not mobile.isdigit():  
                messagebox.showerror("Invalid Mobile Number", "Please enter a valid mobile number containing only numbers.")
            elif len(mobile) != 11:  
                messagebox.showerror("Invalid Mobile Number", "Please enter a mobile number with exactly 11 digits.")

        btn_validate = Button(leftframe, text="Verify", command=validate_mobileno, font=theme.SMALL)
        btn_validate.grid(row=5, column=2, sticky=W, padx=(6,0))


        # Email Label
        lblemail = Label(leftframe, text="Email:", bd=4, font=theme.LABEL, padx=2, pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblemail.grid(row=6, column=0, sticky=W)

        
        txtemail = ttk.Entry(leftframe, textvariable=self.var_email, font=theme.ENTRY, width=29)
        txtemail.grid(row=6, column=1,sticky=W)

        def validate_email():
            email = self.var_email.get()
            if not (email.endswith("@gmail.com") or email.endswith("@yahoo.com")):
                messagebox.showerror("Invalid Email", "Please enter a valid email address with '@gmail.com' or '@yahoo.com'.")

        
        btn_validate = Button(leftframe, text="Verify", command=validate_email, font=theme.SMALL)
        btn_validate.grid(row=6, column=2, sticky=W, padx=(6,0))


        #nationality

        lblnationality = Label(leftframe, text="Nationality:", bd=4, font=theme.LABEL, padx=2, pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblnationality.grid(row=7, column=0, sticky=W)

        nationalities = [country.name for country in pycountry.countries]
        nationality_combo = ttk.Combobox(leftframe, textvariable=self.var_nationality,font=theme.LABEL, width=27, state="readonly")
        nationality_combo["value"] = nationalities
        nationality_combo.current(0)
        nationality_combo.grid(row=7, column=1, pady=2, sticky=W)


        #id proof
        lblidproof=Label(leftframe,text="Id Proof Type:",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblidproof.grid(row=8,column=0,sticky=W)

        id_proof=ttk.Combobox(leftframe,textvariable=self.var_id_proof,font=theme.LABEL,width=27,state=READABLE)
        id_proof["value"]=("CNIC or B-Form","Passport No","Driving Licence",)
        id_proof.current(0)
        id_proof.grid(row=8, column=1, pady=2, sticky=W)


        #Id number
        lblId=Label(leftframe,text="Id Number:",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblId.grid(row=9,column=0,sticky=W)

        txtid=ttk.Entry(leftframe,textvariable=self.var_id_number,width=29,font=theme.ENTRY)
        txtid.grid(row=9, column=1, pady=2, sticky=W)

        def validate_idnumber():
            postcode = self.var_post.get()
            if not postcode.isdigit(): 
                messagebox.showerror("Invalid Postcode", "Please enter a valid id number containing only numbers.")

        btn_validate = Button(leftframe, text="Verify", command=validate_idnumber, font=theme.SMALL)
        btn_validate.grid(row=9, column=2, sticky=W, padx=(6,0))



        #address
        lbladdress=Label(leftframe,text="Address:",bd=4,font=theme.LABEL,padx=2,pady=2,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lbladdress.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(leftframe,textvariable=self.var_address,width=29,font=theme.ENTRY)
        txtaddress.grid(row=10, column=1, pady=2, sticky=W)




#------------------btns-----------------------------
        # gridded after the last field so it can never overlap the form
        btn_frame=Frame(leftframe,bg=theme.CARD)
        btn_frame.grid(row=11,column=0,columnspan=3,sticky=W,pady=(18,4))

        for i,(label,cmd) in enumerate([("Add",self.add_data),("Update",self.update),
                                        ("Delete",self.mDelete),("Reset",self.reset)]):
            theme.primary_button(btn_frame,label,cmd,width=10).grid(row=0,column=i,padx=(0,6))


#------------------table frame & search systrem-------------------------------

        customer_table_frame=theme.panel(self.root,"View Details & Search System")
        customer_table_frame.place(x=LEFT_W+theme.PAD*2,y=body_y,
                                   width=WIN_W-LEFT_W-theme.PAD*3,height=body_h)

        # search row packs across the top; the table then fills whatever is left
        search_row=Frame(customer_table_frame,bg=theme.CARD)
        search_row.pack(fill=X,pady=(4,10))
        search_row.columnconfigure(2,weight=1)   # entry absorbs the slack so buttons always fit

        lblSearch=Label(search_row,text="Search By:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT)
        lblSearch.grid(row=0,column=0,sticky=W,padx=(0,8))

        self.search_var=StringVar()
        Search_combo=ttk.Combobox(search_row,textvariable=self.search_var,font=theme.BODY,width=12,state="readonly")
        Search_combo["value"]=("Mobile","Ref")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=(0,8))

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(search_row,textvariable=self.txt_search,width=10,font=theme.ENTRY)
        txtsearch.grid(row=0,column=2,padx=(0,8),sticky="ew")

        theme.primary_button(search_row,"Search",self.search,width=10).grid(row=0,column=3,padx=(0,6))
        theme.primary_button(search_row,"Show All",self.fetch_data,width=10).grid(row=0,column=4)


#-------------------------Data Table--------------------------
        detail_table=Frame(customer_table_frame,bd=1,relief=SOLID)
        detail_table.pack(fill=BOTH,expand=1,pady=(0,4))

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.customer_detail_table=ttk.Treeview(detail_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","id number","address" ),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.customer_detail_table.xview)
        scroll_y.config(command=self.customer_detail_table.yview)

        self.customer_detail_table.heading("ref",text="Refer No")
        self.customer_detail_table.heading("name",text="Name")
        self.customer_detail_table.heading("mother",text="Mother Name")
        self.customer_detail_table.heading("gender",text="Gender")
        self.customer_detail_table.heading("post",text="Post Code")
        self.customer_detail_table.heading("mobile",text="Mobile No")
        self.customer_detail_table.heading("email",text="Email")
        self.customer_detail_table.heading("nationality",text="Nationality")
        self.customer_detail_table.heading("idproof",text="ID Proof")
        self.customer_detail_table.heading("id number",text="ID No")
        self.customer_detail_table.heading("address",text="Address")


        self.customer_detail_table["show"]="headings"
        # widths sized to the content rather than a uniform 100px
        for col,wdt,anc in (("ref",70,"center"),("name",120,"w"),("mother",120,"w"),
                            ("gender",90,"center"),("post",80,"center"),("mobile",110,"center"),
                            ("email",180,"w"),("nationality",120,"w"),("idproof",130,"w"),
                            ("id number",110,"center"),("address",180,"w")):
            self.customer_detail_table.column(col,width=wdt,anchor=anc,stretch=False)


        self.customer_detail_table.pack(fill=BOTH,expand=1)
        self.customer_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "ankheye kharab hain kya <<< sari fields fill kro 😒",parent=self.root)
        else:
            try:
                conn = get_connection()
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into customer values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_ref.get(),
                        self.var_customer_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get()


                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}",parent=self.root)

    def fetch_data(self):
        conn = get_connection()
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.customer_detail_table.delete(*self.customer_detail_table.get_children())
            for i in rows:
                self.customer_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def get_cursor(self,event=""):
        cursor_row=self.customer_detail_table.focus()
        content=self.customer_detail_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_customer_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

#-----------------update function---------------------------
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Enter Your mobile number",parent=self.root)
        else:
            conn = get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                        self.var_customer_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get(),
                        self.var_ref.get()
             ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Details has been updated",parent=self.root)


#-------------------delete function------------------------------
    def mDelete(self):
        mDelete=messagebox.askyesno("Azure's Inn Hotel Mannagement System","Do you want to delete this customer!!!",parent=self.root)
        if mDelete>0:
            conn = get_connection()
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

#-----------------------reset function-------------------------------
    def reset(self):
        #self.var_ref.set("")
        self.var_customer_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))




    def search(self):
            conn = get_connection()
            my_cursor = conn.cursor() 
            query = f"SELECT * FROM customer WHERE {self.search_var.get()} LIKE %s"
            my_cursor.execute(query, (f"%{self.txt_search.get()}%",))
            rows=my_cursor.fetchall()    
            if len(rows)!=0:
                self.customer_detail_table.delete(*self.customer_detail_table.get_children())
            for i in rows:
                self.customer_detail_table.insert("",END,values=i)
            conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = customer_win(root)
    root.mainloop()
