from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import pycountry
import random
from time import strftime
from datetime import datetime
from db_config import get_connection
from tkinter import messagebox
from tkcalendar import Calendar
import os
import theme
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

class room_booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Management System")
        theme.apply_theme(self.root)
        WIN_W,WIN_H=theme.fit_window(self.root,1360,768)
        HEAD=58

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
        img2=Image.open(os.path.join(IMG_DIR, "logo.png"))
        img2=img2.resize((88,50),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        theme.header(self.root,"ROOM BOOKING DETAILS",WIN_W,self.photoimg2,HEAD)


#------------------------lable frame ----------------------
        LEFT_W=520
        body_y=HEAD+theme.PAD
        body_h=WIN_H-body_y-theme.PAD
        RIGHT_X=LEFT_W+theme.PAD*2
        RIGHT_W=WIN_W-LEFT_W-theme.PAD*3

        leftframe=theme.panel(self.root,"Room Booking")
        leftframe.place(x=theme.PAD,y=body_y,width=LEFT_W,height=body_h)


#------------------------Lables and Enteries-------------------------
        #Customer Contact
        customer_contact=Label(leftframe,text="Customer Contact",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        customer_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(leftframe,textvariable=self.var_contact,width=20,font=theme.ENTRY)
        entry_contact.grid(row=0,column=1,sticky=W)


        #fetch data btn

        fetchbtn=theme.primary_button(leftframe,"Fetch Data",self.fetch_contact,width=10)
        fetchbtn.grid(row=0,column=2,sticky=W,padx=(6,0))
#-------------------check in ------------------------

        # Check-in Date Label
        checkin_date = Label(leftframe, text="Check in date:", bd=4, font=theme.LABEL, padx=2, pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
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
        txt_checkin = ttk.Entry(leftframe, textvariable=self.var_checkin, width=29, font=theme.ENTRY, state="readonly")
        txt_checkin.grid(row=1, column=1, pady=4, sticky=W)

        # Add a button to open the calendar
        btn_calendar = Button(leftframe, text="Select Date", command=open_calendar, font=theme.SMALL)
        btn_calendar.grid(row=1, column=2, sticky=W, padx=(6,0))


 
        #Check Out-date
    

        # Check-out Date Label
        Check_out = Label(leftframe, text="Check out date:", bd=4, font=theme.LABEL, padx=2, pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
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
        txt_checkout = ttk.Entry(leftframe, textvariable=self.var_checkout, width=29, font=theme.ENTRY, state="readonly")
        txt_checkout.grid(row=2, column=1, pady=4, sticky=W)

        btn_checkout_calendar = Button(leftframe, text="Select Date", command=open_checkout_calendar, font=theme.SMALL)
        btn_checkout_calendar.grid(row=2, column=2, sticky=W, padx=(6,0))



















        #Room type
        lable_roomtype=Label(leftframe,text="Room Type:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lable_roomtype.grid(row=3,column=0,sticky=W)

            #connect with sql
        conn = get_connection()
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        avail_rooms_type=my_cursor.fetchall()


        roomtype_combo=ttk.Combobox(leftframe,textvariable=self.var_roomavailable,font=theme.LABEL,width=27)
        roomtype_combo["value"]=avail_rooms_type
        roomtype_combo.current(0)
        roomtype_combo.grid(row=3, column=1, pady=4, sticky=W)

        #Available room
        lblRoomAvailability=Label(leftframe,text="Available Rooms:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblRoomAvailability.grid(row=4,column=0,sticky=W)
            #connect with sql 
        conn = get_connection()
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        avail_rooms_data=my_cursor.fetchall()


        room_no_combo=ttk.Combobox(leftframe,textvariable=self.var_roomtype,font=theme.LABEL,width=27)
        room_no_combo["value"]=avail_rooms_data
        room_no_combo.current(0)
        room_no_combo.grid(row=4, column=1, pady=4, sticky=W)

        #meal
        lblmeal=Label(leftframe,text="Meal: ",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblmeal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(leftframe,textvariable=self.var_meal,width=29,font=theme.ENTRY)
        txtmeal.grid(row=5, column=1, pady=4, sticky=W)

        # No of Dys
        lblNoOfDays=Label(leftframe,text="No of Days:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_noofdays,font=theme.ENTRY,width=29)
        txtNoOfDays.grid(row=6, column=1, pady=4, sticky=W)

        #Paid tax

        lblNoOfDays=Label(leftframe,text="Paid Tax:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_paidtax,font=theme.ENTRY,width=29)
        txtNoOfDays.grid(row=7, column=1, pady=4, sticky=W)


        # Sub Total

        lblNoOfDays=Label(leftframe,text="Sub Total:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblNoOfDays.grid(row=8,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_actualtotal,font=theme.ENTRY,width=29)
        txtNoOfDays.grid(row=8, column=1, pady=4, sticky=W)


        # Total Cost
        
        lblNoOfDays=Label(leftframe,text="Total Cost:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lblNoOfDays.grid(row=9,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(leftframe,textvariable=self.var_total,font=theme.ENTRY,width=29)
        txtNoOfDays.grid(row=9, column=1, pady=4, sticky=W)

        # Bill btn
        billbtn=theme.primary_button(leftframe,"Billing",self.total,width=10)
        billbtn.grid(row=10,column=1,sticky=W,pady=(8,0))



#------------------btns-----------------------------
        # gridded after the last field so it can never overlap the form
        btn_frame=Frame(leftframe,bg=theme.CARD)
        btn_frame.grid(row=11,column=0,columnspan=3,sticky=W,pady=(16,4))

        for i,(label,cmd) in enumerate([("Add",self.add_data),("Update",self.update),
                                        ("Delete",self.fDelete),("Reset",self.reset)]):
            theme.primary_button(btn_frame,label,cmd,width=10).grid(row=0,column=i,padx=(0,6))


#------------------Right side image-----------------------------

        IMG_H=250
        INFO_W=260
        IMG_W=RIGHT_W-INFO_W-theme.PAD
        # remembered so fetch_contact() can drop its info card beside the photo
        self.info_x=RIGHT_X+IMG_W+theme.PAD
        self.info_y=body_y
        self.info_w=INFO_W
        self.info_h=IMG_H

        img3=Image.open(os.path.join(IMG_DIR, "room1.jpg"))
        img3=img3.resize((IMG_W,IMG_H),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0)
        lblimg.place(x=RIGHT_X,y=body_y,width=IMG_W,height=IMG_H)



#------------------table frame & search syst em-------------------------------

        # sits below the photo instead of underneath it
        table_y=body_y+IMG_H+theme.PAD
        customer_table_frame=theme.panel(self.root,"View Details & Search System")
        customer_table_frame.place(x=RIGHT_X,y=table_y,width=RIGHT_W,
                                   height=WIN_H-table_y-theme.PAD)

        search_row=Frame(customer_table_frame,bg=theme.CARD)
        search_row.pack(fill=X,pady=(4,10))
        search_row.columnconfigure(2,weight=1)

        lblSearch=Label(search_row,text="Search By:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT)
        lblSearch.grid(row=0,column=0,sticky=W,padx=(0,8))

        self.search_var=StringVar()
        Search_combo=ttk.Combobox(search_row,textvariable=self.search_var,font=theme.BODY,width=12,state="readonly")
        Search_combo["value"]=("Contact","Room")
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

        for col,wdt in (("contact",120),("checkin",110),("checkout",110),
                        ("roomtype",120),("roomavailability",130),("meal",110),("noOfdays",100)):
            self.room_table.column(col,width=wdt,anchor="center")
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


#----------------adding data---------------------
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", " sari fields fill kro<<<<lazy peoplee 😒",parent=self.root)
        else:
            try:
                conn = get_connection()
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
        conn = get_connection()
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
            conn = get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where Contact=%s",(
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
            conn = get_connection()
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
            conn = get_connection()
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
            conn = get_connection()
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

                showdata_frame=Frame(self.root,bd=1,relief=SOLID,padx=10,pady=8,bg=theme.CARD)
                showdata_frame.place(x=self.info_x,y=self.info_y,
                                     width=self.info_w,height=self.info_h)

                lblname=Label(showdata_frame,text="Name:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lblname.place(x=0,y=0)

                lbl_fromsql=Label(showdata_frame,text=(row[0] if row else ""),font=theme.BODY,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_fromsql.place(x=90,y=0)

                #gender
                conn = get_connection()
                my_cursor = conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showdata_frame,text="Gender:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lblgender.place(x=0,y=30)

                lbl_fromsql2=Label(showdata_frame,text=(row[0] if row else ""),font=theme.BODY,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_fromsql2.place(x=90,y=30)

#---------------------email
                conn = get_connection()
                my_cursor = conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showdata_frame,text="E-mail:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lblemail.place(x=0,y=60)

                lbl_fromsql3=Label(showdata_frame,text=(row[0] if row else ""),font=theme.BODY,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_fromsql3.place(x=90,y=60)
#---------------------------------nationality
                conn = get_connection()
                my_cursor = conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_Nationality=Label(showdata_frame,text="Nationality:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_Nationality.place(x=0,y=90)

                lbl_fromsql4=Label(showdata_frame,text=(row[0] if row else ""),font=theme.BODY,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_fromsql4.place(x=90,y=90)

#-------------Address---------------------
                conn = get_connection()
                my_cursor = conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_address=Label(showdata_frame,text="Address:",font=theme.LABEL,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_address.place(x=0,y=120)

                lbl_fromsql5=Label(showdata_frame,text=(row[0] if row else ""),font=theme.BODY,bg=theme.CARD,fg=theme.TEXT,anchor="w")
                lbl_fromsql5.place(x=90,y=120)

# ***************************************************************************************************************************************************************************************************

if __name__ == "__main__":
    root = Tk()
    obj = room_booking(root)
    root.mainloop()
