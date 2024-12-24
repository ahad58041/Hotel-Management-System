from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import pycountry
import random
import mysql.connector
from tkinter import messagebox
import re

class customer_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Mannagement System ")
        self.root.geometry("1295x580+180+170")
        


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
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("fantasy",18,"bold"),bg="black",fg="#C3B499",bd="4",relief=RIDGE )
        lbl_title.place(x=0,y=0,width=1295,height=60 )


#-------------------------- logo -------------------------------
        img2=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\logo.png")
        img2=img2.resize((100,60),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=4,y=1,width=100,height=60)

#------------------------lable frame ----------------------
        leftframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="Customer Details",padx=2,font=("fantasy",12,"bold"))
        leftframe.place(x=5,y=58,width=505,height=590 )


#------------------------Lables and Enteries-------------------------
        #Customer Refernce
        customer_ref=Label(leftframe,text="Customer Refrence",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        customer_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(leftframe,width=29,state="readonly",textvariable=self.var_ref,font=("arial",13,"bold"))
        entry_ref.grid(row=0,column=1)

        #Customer Name
        cust_name=Label(leftframe,text="Customer Name:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        txtname=ttk.Entry(leftframe,width=29,textvariable=self.var_customer_name,font=("arial",13,"bold"))
        txtname.grid(row=1,column=1)

        #Mother Name
        moth_name=Label(leftframe,text="Mother Name:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        moth_name.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(leftframe,width=29,textvariable=self.var_mother,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)

        #Gender- combobox
        lable_gender=Label(leftframe,text="Gender:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lable_gender.grid(row=3,column=0,sticky=W)

        gender_combo=ttk.Combobox(leftframe,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        gender_combo["value"]=("Male","Female","Rather not say","Custom")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1)

        #Post code
        lblpostcode = Label(leftframe, text="PostCode:", bd=4, font=("arial", 12, "bold"), padx=2, pady=6)
        lblpostcode.grid(row=4, column=0, sticky=W)

        txtpostcode = ttk.Entry(leftframe, textvariable=self.var_post, width=29, font=("arial", 13, "bold"))
        txtpostcode.grid(row=4, column=1)

        def validate_postcode():
            postcode = self.var_post.get()
            if not postcode.isdigit(): 
                messagebox.showerror("Invalid Postcode", "Please enter a valid postcode containing only numbers.")

        btn_validate = Button(leftframe, text="Verify", command=validate_postcode, font=("arial", 10, "bold"))
        btn_validate.grid(row=4, column=1,sticky=E)

        #mobile number
        lblmobile=Label(leftframe,text="Mobile: ",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(leftframe,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1)

        def validate_mobileno():
            mobile = self.var_mobile.get()
            if not mobile.isdigit():  
                messagebox.showerror("Invalid Mobile Number", "Please enter a valid mobile number containing only numbers.")
            elif len(mobile) != 11:  
                messagebox.showerror("Invalid Mobile Number", "Please enter a mobile number with exactly 11 digits.")

        btn_validate = Button(leftframe, text="Verify", command=validate_mobileno, font=("arial", 10, "bold"))
        btn_validate.grid(row=5, column=1, sticky=E)


        # Email Label
        lblemail = Label(leftframe, text="Email:", bd=4, font=("arial", 12, "bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)

        
        txtemail = ttk.Entry(leftframe, textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtemail.grid(row=6, column=1,sticky=W)

        def validate_email():
            email = self.var_email.get()
            if not (email.endswith("@gmail.com") or email.endswith("@yahoo.com")):
                messagebox.showerror("Invalid Email", "Please enter a valid email address with '@gmail.com' or '@yahoo.com'.")

        
        btn_validate = Button(leftframe, text="Verify", command=validate_email, font=("arial", 10, "bold"))
        btn_validate.grid(row=6, column=1, sticky=E)


        #nationality

        lblnationality = Label(leftframe, text="Nationality:", bd=4, font=("arial", 12, "bold"), padx=2, pady=6)
        lblnationality.grid(row=7, column=0, sticky=W)

        nationalities = [country.name for country in pycountry.countries]
        nationality_combo = ttk.Combobox(leftframe, textvariable=self.var_nationality,font=("arial", 12, "bold"), width=27, state="readonly")
        nationality_combo["value"] = nationalities
        nationality_combo.current(0)
        nationality_combo.grid(row=7, column=1)


        #id proof
        lblidproof=Label(leftframe,text="Id Proof Type:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)

        id_proof=ttk.Combobox(leftframe,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state=READABLE)
        id_proof["value"]=("CNIC or B-Form","Passport No","Driving Licence",)
        id_proof.current(0)
        id_proof.grid(row=8,column=1)


        #Id number
        lblId=Label(leftframe,text="Id Number:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblId.grid(row=9,column=0,sticky=W)

        txtid=ttk.Entry(leftframe,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtid.grid(row=9,column=1)

        def validate_idnumber():
            postcode = self.var_post.get()
            if not postcode.isdigit(): 
                messagebox.showerror("Invalid Postcode", "Please enter a valid id number containing only numbers.")

        btn_validate = Button(leftframe, text="Verify", command=validate_idnumber, font=("arial", 10, "bold"))
        btn_validate.grid(row=9, column=1,sticky=E)



        #address
        lbladdress=Label(leftframe,text="Address:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(leftframe,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)




#------------------btns-----------------------------
        btn_frame=Frame(leftframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=423,width=413,height=40)

        addbtn=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addbtn.grid(row=0,column=0)

        addupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addupdate.grid(row=0,column=1)

        adddelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        adddelete.grid(row=0,column=2)

        addreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addreset.grid(row=0,column=3)


#------------------table frame & search systrem-------------------------------

        customer_table_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="View Details & Search System",padx=2,font=("fantasy",12,"bold"))
        customer_table_frame.place(x=515,y=57,width=780,height=592 )

        lblSearch=Label(customer_table_frame,text="Search By:",bd=4,font=("arial",12,"bold"),bg="#767374",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        Search_combo=ttk.Combobox(customer_table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state=READABLE)
        Search_combo["value"]=("Mobile","Ref")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(customer_table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        searchbtn=Button(customer_table_frame,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        searchbtn.grid(row=0,column=3)

        showallbtn=Button(customer_table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        showallbtn.grid(row=0,column=4)


#-------------------------Data Table--------------------------
        detail_table=Frame(customer_table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=771,height=350)

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
        self.customer_detail_table.column("ref",width=100)
        self.customer_detail_table.column("name",width=100)
        self.customer_detail_table.column("mother",width=100)
        self.customer_detail_table.column("gender",width=100)
        self.customer_detail_table.column("post",width=100)
        self.customer_detail_table.column("mobile",width=100)
        self.customer_detail_table.column("email",width=100)
        self.customer_detail_table.column("nationality",width=100)
        self.customer_detail_table.column("idproof",width=100)
        self.customer_detail_table.column("id number",width=100)
        self.customer_detail_table.column("address",width=100)


        self.customer_detail_table.pack(fill=BOTH,expand=1)
        self.customer_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "ankheye kharab hain kya <<< sari fields fill kro 😒",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="bank_management"
                )
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
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
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
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
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
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
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
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
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
