from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import pycountry
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkcalendar import Calendar

class room_booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Mannagement System ")
        self.root.geometry("1295x580+180+170")

#---------------------variables-----------------

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

# -----------------------Title--------------------------------------
        lbl_title=Label(self.root,text=" ROOMBOOKING DETAILS",font=("fantasy",18,"bold"),bg="black",fg="#C3B499",bd="4",relief=RIDGE )
        lbl_title.place(x=0,y=0,width=1295,height=60 )


#-------------------------- logo -------------------------------
        img2=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\logo.png")
        img2=img2.resize((100,60),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=4,y=1,width=100,height=60)


#------------------------lable frame ----------------------
        leftframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="ROOM BOOKING",padx=2,font=("fantasy",12,"bold"))
        leftframe.place(x=5,y=62,width=505,height=500 )


#------------------------Lables and Enteries-------------------------
        #Customer Contact
        customer_contact=Label(leftframe,text="Customer Contact",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        customer_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(leftframe,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)


        #fetch data btn

        fetchbtn=Button(leftframe,command=self.fetch_contact,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="#FFFFFF",width=8,padx=1,pady=3)
        fetchbtn.place(x=350,y=4)
#-------------------check in ------------------------

        # Check-in Date Label
        checkin_date = Label(leftframe, text="Check in date:", bd=4, font=("arial", 12, "bold"), padx=2, pady=6)
        checkin_date.grid(row=1, column=0, sticky=W)

        # Function to show the calendar popup
        def open_calendar():
            def select_date():
                selected_date = cal.get_date() 
                # Format date in d/m/y
                day, month, year = selected_date.split('/')
                formatted_date = f"{day}/{month}/{year}"
                self.var_checkin.set(formatted_date) 
                cal_window.destroy()  # Close the calendar window
            
            cal_window = Toplevel(leftframe)
            cal_window.title("Select Check-in Date")
            
            # Create the calendar widget
            cal = Calendar(cal_window, selectmode="day", date_pattern="d/m/y")
            cal.pack(padx=20, pady=20)
            
            # Button to confirm the date selection
            btn_select = Button(cal_window, text="Select Date", command=select_date)
            btn_select.pack(pady=10)

        # Check-in Entry with lock
        txt_checkin = ttk.Entry(leftframe, textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"), state="readonly")
        txt_checkin.grid(row=1, column=1)

        # Add a button to open the calendar
        btn_calendar = Button(leftframe, text="Select Date", command=open_calendar, font=("arial", 10, "bold"))
        btn_calendar.grid(row=1, column=1,sticky=E)


 
        #Check Out-date
    

        # Check-out Date Label
        Check_out = Label(leftframe, text="Check out date:", bd=4, font=("arial", 12, "bold"), padx=2, pady=6)
        Check_out.grid(row=2, column=0, sticky=W)

        def open_checkout_calendar():
            def select_date():
                selected_date = cal.get_date() 
                day, month, year = selected_date.split('/')
                formatted_date = f"{day}/{month}/{year}"
                self.var_checkout.set(formatted_date)  # Set the selected date to the entry field
                cal_window.destroy()  # Close the calendar window
            
            # Create a new window for the calendar
            cal_window = Toplevel(leftframe)
            cal_window.title("Select Check-out Date")
            
            # Create the calendar widget
            cal = Calendar(cal_window, selectmode="day", date_pattern="d/m/y")
            cal.pack(padx=20, pady=20)
            
            # Button to confirm the date selection
            btn_select = Button(cal_window, text="Select Date", command=select_date)
            btn_select.pack(pady=10)

        # Check-out Entry with lock
        txt_checkout = ttk.Entry(leftframe, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"), state="readonly")
        txt_checkout.grid(row=2, column=1)

        btn_checkout_calendar = Button(leftframe, text="Select Date", command=open_checkout_calendar, font=("arial", 10, "bold"))
        btn_checkout_calendar.grid(row=2, column=1,sticky=E)



















        #Room type
        lable_roomtype=Label(leftframe,text="Room Type:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lable_roomtype.grid(row=3,column=0,sticky=W)

            #connect with sql
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        avail_rooms_type=my_cursor.fetchall()


        roomtype_combo=ttk.Combobox(leftframe,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27)
        roomtype_combo["value"]=avail_rooms_type
        roomtype_combo.current(0)
        roomtype_combo.grid(row=3,column=1)

        #Available room
        lblRoomAvailability=Label(leftframe,text="Available Rooms:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailability.grid(row=4,column=0,sticky=W)
            #connect with sql 
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        avail_rooms_data=my_cursor.fetchall()


        room_no_combo=ttk.Combobox(leftframe,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27)
        room_no_combo["value"]=avail_rooms_data
        room_no_combo.current(0)
        room_no_combo.grid(row=4,column=1)

        #meal
        lblmeal=Label(leftframe,text="Meal: ",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(leftframe,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtmeal.grid(row=5,column=1)

        # No of Dys
        lblNoOfDays=Label(leftframe,text="No of Days:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid tax

        lblNoOfDays=Label(leftframe,text="Paid Tax:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)


        # Sub Total

        lblNoOfDays=Label(leftframe,text="Sub Total:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)


        # Total Cost
        
        lblNoOfDays=Label(leftframe,text="Total Cost:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=9,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=9,column=1)

        # Bill btn
        billbtn=Button(leftframe,text="Billing",command=self.total,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        billbtn.grid(row=10,column=0,padx=1,sticky=W)



#------------------btns-----------------------------
        btn_frame=Frame(leftframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=430,width=413,height=40)

        addbtn=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addbtn.grid(row=0,column=0)

        addupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addupdate.grid(row=0,column=1)

        adddelete=Button(btn_frame,text="Delete",command=self.fDelete,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        adddelete.grid(row=0,column=2)

        addreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addreset.grid(row=0,column=3)


#------------------Right side image-----------------------------

        img3=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\room1.jpg")
        img3=img3.resize((520,300),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,relief=RIDGE)
        lblimg.place(x=760,y=65,width=520,height=300)



#------------------table frame & search syst em-------------------------------

        customer_table_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="View Details & Search System",padx=2,font=("fantasy",12,"bold"))
        customer_table_frame.place(x=515,y=280,width=780,height=260  )

        lblSearch=Label(customer_table_frame,text="Search By:",bd=4,font=("arial",12,"bold"),bg="#767374",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        Search_combo=ttk.Combobox(customer_table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state=READABLE)
        Search_combo["value"]=("Contact","Room")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(customer_table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        searchbtn=Button(customer_table_frame,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        searchbtn.grid(row=0,column=3)

        showallbtn=Button(customer_table_frame,command=self.fetch_data,text="Show All",font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        showallbtn.grid(row=0,column=4)

#-------------------------Data Table--------------------------
        detail_table=Frame(customer_table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=771,height=180)

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(detail_table,column=("contact","checkin","checkout","roomtype","roomavailability","meal","noOfdays"),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailability",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No Of Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailability",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


#----------------adding data---------------------
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", " sari fields fill kro<<<<lazy peoplee 😒",parent=self.root)
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
                    "insert into room values (%s, %s, %s, %s, %s, %s, %s)",
                    (
                                self.var_contact.get(),
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomavailable.get(),
                                self.var_meal.get(),
                                self.var_noofdays.get()                                


                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked,Now enjoy the bed",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}",parent=self.root)
                    
# fetchinggggg-------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
#--------------get cursor event------------------
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])                                
#------------update-----------------------

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Enter Your mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomavailable.get(),
                                self.var_meal.get(),
                                self.var_noofdays.get(),
                                self.var_contact.get()
                              
       ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Details has been updated",parent=self.root)

#--------------delete function---------------------


    def fDelete(self):
        fDelete=messagebox.askyesno("Azure's Inn Hotel Mannagement System","Do you want to delete this customer!!!",parent=self.root)
        if fDelete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)

        else:
            if not fDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


#------------------------reset----------------------------

    def reset(self):
        
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

                              


        x=random.randint(1000,9999)
        self.var_contact.set(str(x))

#----------------right side search system------------

    def search(self):
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor() 
            query = f"SELECT * FROM room WHERE {self.search_var.get()} LIKE %s"
            my_cursor.execute(query, (f"%{self.txt_search.get()}%",))
            rows=my_cursor.fetchall()    
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()




#-------------billing button of taxex--------------
    def total(self):

        in_date = self.var_checkin.get()
        out_date = self.var_checkout.get()

        in_date = datetime.strptime(in_date, "%d/%m/%Y")
        out_date = datetime.strptime(out_date, "%d/%m/%Y")

        
        no_of_days = abs((out_date - in_date).days)
        self.var_noofdays.set(no_of_days)

        #  meal and room type costs
        meal_costs = {"breakfast": 450, "lunch": 700, "dinner":50 }

        room_costs = { "luxury": 2500,  "double": 2000,  "single": 1500, "Duplex":3500 }

        selected_meal = self.var_meal.get().strip().lower() #strip & lower for handling any kind of data input like all caps or toggle
        selected_room = self.var_roomtype.get().strip().lower()           

        meal_cost = meal_costs.get(selected_meal, 0)
        room_cost = room_costs.get(selected_room, 0)

        # Calculate subtotal, tax, and total
        subtotal = (meal_cost + room_cost) * no_of_days
        tax = subtotal * 0.09
        total = subtotal + tax

        self.var_paidtax.set(f"Rs: {tax:.2f}")
        self.var_actualtotal.set(f"Rs: {subtotal:.2f}")
        self.var_total.set(f"Rs: {total:.2f}")
        message = (
                f"Selected Meal: {selected_meal.capitalize()}\n"
                f"Selected Room: {selected_room.capitalize()}\n"
                f"Paid Tax: {self.var_paidtax.get()}\n"
                f"Actual Total: {self.var_actualtotal.get()}\n"
                f"Total Amount (including tax): {self.var_total.get()}\n\n"
                "Thank you!"
            )

        messagebox.showinfo(" Azure's Inn Hotel Billing Summary", message, parent=self.root)


#------------------All data fetch from SQL-----------------------
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)

        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","User not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdata_frame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdata_frame.place(x=510,y=70,width=250,height=190)

                lblname=Label(showdata_frame,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)

                lbl_fromsql=Label(showdata_frame,text=row,font=("arial",12,"bold"))
                lbl_fromsql.place(x=90,y=0)

                #gender
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
                my_cursor = conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showdata_frame,text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl_fromsql2=Label(showdata_frame,text=row,font=("arial",12,"bold"))
                lbl_fromsql2.place(x=90,y=30)

#---------------------email
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
                my_cursor = conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showdata_frame,text="E-mail:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl_fromsql3=Label(showdata_frame,text=row,font=("arial",12,"bold"))
                lbl_fromsql3.place(x=90,y=60)
#---------------------------------nationality
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
                my_cursor = conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_Nationality=Label(showdata_frame,text="Nationality:",font=("arial",12,"bold"))
                lbl_Nationality.place(x=0,y=90)

                lbl_fromsql4=Label(showdata_frame,text=row,font=("arial",12,"bold"))
                lbl_fromsql4.place(x=90,y=90)

#-------------Address---------------------
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
                my_cursor = conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_address=Label(showdata_frame,text="Address:",font=("arial",12,"bold"))
                lbl_address.place(x=0,y=120)

                lbl_fromsql5=Label(showdata_frame,text=row,font=("arial",12,"bold"))
                lbl_fromsql5.place(x=90,y=120)

# ***************************************************************************************************************************************************************************************************

if __name__ == "__main__":
    root = Tk()
    obj = room_booking(root)
    root.mainloop()
