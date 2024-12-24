from tkinter import*
from PIL import Image,ImageTk
from customer import customer_win
from room import room_booking
from details import details_room
import re
 
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Mannagement System ")
        self.root.geometry("1550x800+0+0")
#-------------------------- 1st img -------------------------------
        img1=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\hotell.jpg")
        img1=img1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)


#-------------------------- logo -------------------------------
        img2=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\logo.png")
        img2=img2.resize((230,160),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


# -----------------------Title--------------------------------------
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("fantasy",40,"bold"),bg="black",fg="#C3B499",bd="4",relief=RIDGE )
        lbl_title.place(x=0,y=140,width=1550,height=60 )


#-------------------main frame------------------------------------
        frame=Frame(self.root,bd=4,relief=RIDGE)
        frame.place(x=0,y=190,width=1550,height=620 )

        # ----------------- menu --------------------------
        lbl_menu=Label(frame,text="MENU",font=("fantasy",20,"bold"),bg="black",fg="#C3B499",bd="4",relief=RIDGE )
        lbl_menu.place(x=0,y=0,width=230 )

#-------------------btn frame------------------------------------
        btn_frame=Frame(frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=155 )

        cust_btn = Button(btn_frame, text="ADD CUSTOMER", command=self.cust_details, width=22, font=("fantasy", 14, "bold"), bg="black", fg="#C3B499", bd=0, cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOMS DETAILS",command=self.roombooking,width=22,font=("fantasy",14,"bold"),bg="black",fg="#C3B499",bd=0, cursor="hand2" )
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="ADD NEW ROOM",command=self.details_room,width=22,font=("fantasy",14,"bold"),bg="black",fg="#C3B499",bd=0, cursor="hand2" )
        details_btn.grid(row=2,column=0,pady=1)
        
        logout_btn=Button(btn_frame,command=self.logout,text="LOGOUT",width=22,font=("fantasy",14,"bold"),bg="black",fg="#C3B499",bd=0, cursor="hand2" )
        logout_btn.grid(row=3,column=0,pady=1)


#--------------------Right side Image-----------------------
        img3=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\rightside.jpg")
        img3=img3.resize((1310,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=580)

#----------------------downimages-----------------------
        
        img4=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\food.jpg")
        img4=img4.resize((227,230),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=190,width=227,height=230 )

        img5=Image.open(r"C:\Users\PMLS\Desktop\Github\Hotel Management system\images\peeps.jpg")
        img5=img5.resize((227,190),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=400,width=227,height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = customer_win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = room_booking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = details_room(self.new_window)


    def logout(self):
        self.root.destroy()





if __name__ =="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()