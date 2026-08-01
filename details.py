from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import pycountry
import random
from time import strftime
from datetime import datetime
from db_config import get_connection
from tkinter import messagebox
import os
import theme
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

class details_room:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Management System")
        theme.apply_theme(self.root)
        WIN_W,WIN_H=theme.fit_window(self.root,1180,620)
        HEAD=58

# -----------------------Title--------------------------------------
        img2=Image.open(os.path.join(IMG_DIR, "logo.png"))
        img2=img2.resize((88,50),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        theme.header(self.root,"ADD NEW ROOM",WIN_W,self.photoimg2,HEAD)


#------------------------lable frame ----------------------
        LEFT_W=470
        body_y=HEAD+theme.PAD
        body_h=WIN_H-body_y-theme.PAD

        leftframe=theme.panel(self.root,"Add New Room")
        leftframe.place(x=theme.PAD,y=body_y,width=LEFT_W,height=body_h)



#------------------------Lables and Enteries-------------------------

        #Floor
        lbl_floor=Label(leftframe,text="Floor:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        floor=ttk.Entry(leftframe,textvariable=self.var_floor,width=20,font=theme.ENTRY)
        floor.grid(row=0,column=1,sticky=W)


        #Room No
        lbl_room_no=Label(leftframe,text="Room No:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lbl_room_no.grid(row=1,column=0,sticky=W)

        self.var_room_no=StringVar()


        room_no=ttk.Entry(leftframe,textvariable=self.var_room_no,width=20,font=theme.ENTRY)
        room_no.grid(row=1,column=1,sticky=W)

        #Room type
        lbl_RoomType=Label(leftframe,text="Room Type:",bd=4,font=theme.LABEL,padx=2,pady=6,bg=theme.CARD,fg=theme.TEXT,anchor="w")
        lbl_RoomType.grid(row=2,column=0,sticky=W)


        self.var_room_type=StringVar()

        roomtype_combo=ttk.Combobox(leftframe,textvariable=self.var_room_type,font=theme.LABEL,width=20)
        roomtype_combo["value"]=("Single","Double","Luxury","Duplex")
        roomtype_combo.current(0)
        roomtype_combo.grid(row=2,column=1,sticky=W)

        

#------------------btns-----------------------------
        # gridded after the last field so it can never overlap the form
        btn_frame=Frame(leftframe,bg=theme.CARD)
        btn_frame.grid(row=3,column=0,columnspan=2,sticky=W,pady=(18,4))

        for i,(label,cmd) in enumerate([("Add",self.add_data),("Update",self.update),
                                        ("Delete",self.fDelete),("Reset",self.reset)]):
            theme.primary_button(btn_frame,label,cmd,width=9).grid(row=0,column=i,padx=(0,6))

#------------------table frame & search syst em-------------------------------

        room_detail_frame=theme.panel(self.root,"Show Room Details")
        room_detail_frame.place(x=LEFT_W+theme.PAD*2,y=body_y,
                                width=WIN_W-LEFT_W-theme.PAD*3,height=body_h)

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

        for col,wdt in (("floor",180),("roomno",180),("roomtype",200)):
            self.room_table.column(col,width=wdt,anchor="center")

        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)


#-------------add data------------------------------
    def add_data(self):
        if self.var_floor.get() == "" or self.var_room_type.get() == "" or self.var_room_no.get() == "":
            messagebox.showerror("Error", " sari fields fill kro<<<<lazy peoplee 😒",parent=self.root)
        else:
            try:
                conn = get_connection()
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
        conn = get_connection()
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
            conn = get_connection()
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
            conn = get_connection()
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
