from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import pycountry
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class details_room:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Mannagement System ")
        self.root.geometry("1295x580+180+170")

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
        leftframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="ADD NEW ROOM",padx=2,font=("times new roman",12,"bold"))
        leftframe.place(x=5,y=62,width=625,height=350 )



#------------------------Lables and Enteries-------------------------

        #Floor
        lbl_floor=Label(leftframe,text="Floor:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        floor=ttk.Entry(leftframe,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        floor.grid(row=0,column=1,sticky=W)


        #Room No
        lbl_room_no=Label(leftframe,text="Room No:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lbl_room_no.grid(row=1,column=0,sticky=W)

        self.var_room_no=StringVar()


        room_no=ttk.Entry(leftframe,textvariable=self.var_room_no,width=20,font=("arial",13,"bold"))
        room_no.grid(row=1,column=1,sticky=W)

        #Room type
        lbl_RoomType=Label(leftframe,text="Room Type:",bd=4,font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)


        self.var_room_type=StringVar()

        roomtype_combo=ttk.Combobox(leftframe,textvariable=self.var_room_type,font=("arial",12,"bold"),width=20)
        roomtype_combo["value"]=("Single","Double","Luxury","Duplex")
        roomtype_combo.current(0)
        roomtype_combo.grid(row=2,column=1,sticky=W)

        

#------------------btns-----------------------------
        btn_frame=Frame(leftframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=445,height=40)

        addbtn=Button(btn_frame,command=self.add_data,text="Add",font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addbtn.grid(row=3,column=0)

        addupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        addupdate.grid(row=3,column=1)

        adddelete=Button(btn_frame,text="Delete",command=self.fDelete,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=1,pady=3)
        adddelete.grid(row=3,column=2)

        addreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="#C3B499",width=10,padx=5,pady=3)
        addreset.grid(row=3,column=3)

#------------------table frame & search syst em-------------------------------

        room_detail_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Show Room Details",padx=2,font=("fantasy",12,"bold"))
        room_detail_frame.place(x=650,y=62,width=600,height=360  )

        scroll_x=ttk.Scrollbar(room_detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(room_detail_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(room_detail_frame,column=("floor","roomno","roomtype"),
                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room no")
        self.room_table.heading("roomtype",text="Room type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100) 

        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)


#-------------add data------------------------------
    def add_data(self):
        if self.var_floor.get() == "" or self.var_room_type.get() == "" or self.var_room_no.get() == "":
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
                    "insert into details values (%s, %s, %s)",
                    (
                                self.var_floor.get(),
                                self.var_room_no.get(),
                                self.var_room_type.get()
                               

                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New room added successfully!",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}",parent=self.root)



        
                    

# fetchinggggg-------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0])
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])
    
#------------update-----------------------

    def update(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="" or self.var_room_no.get()=="":
            messagebox.showerror("Error","Enter Correct Information",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                self.var_floor.get(),
                                self.var_room_type.get(),
                                self.var_room_no.get(),
                               
                              
       ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Details has been updated",parent=self.root)


#--------------delete function---------------------


    def fDelete(self):
        fDelete=messagebox.askyesno("Azure's Inn Hotel Mannagement System","Do you want to delete this Room details!!!",parent=self.root)
        if fDelete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="bank_management")
            my_cursor = conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)

        else:
            if not fDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

#------------------------reset----------------------------

    def reset(self):
        
        self.var_floor.set("")
        self.var_room_no.set("")
        self.var_room_type.set("")


if __name__ == "__main__":
    root = Tk()
    obj = details_room(root)
    root.mainloop()
