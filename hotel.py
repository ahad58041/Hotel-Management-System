from tkinter import*
from PIL import Image,ImageTk
from customer import customer_win
from room import room_booking
from details import details_room
import re
import os
import theme
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure's Inn Hotel Management System")
        theme.apply_theme(self.root)
        WIN_W,WIN_H=theme.fit_window(self.root,1400,780)

        BANNER_H=132
        TITLE_H=58
        SIDEBAR_W=248
        body_y=BANNER_H+TITLE_H

#-------------------------- banner + logo -------------------------------
        img1=Image.open(os.path.join(IMG_DIR, "hotell.jpg"))
        img1=img1.resize((WIN_W,BANNER_H),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=0)
        lblimg.place(x=0,y=0,width=WIN_W,height=BANNER_H)

        img2=Image.open(os.path.join(IMG_DIR, "logo.png"))
        img2=img2.resize((SIDEBAR_W,BANNER_H),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbllogo=Label(self.root,image=self.photoimg2,bd=0,bg=theme.INK)
        lbllogo.place(x=0,y=0,width=SIDEBAR_W,height=BANNER_H)

# -----------------------Title--------------------------------------
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=theme.DISPLAY,
                        bg=theme.INK,fg=theme.GOLD)
        lbl_title.place(x=0,y=BANNER_H,width=WIN_W,height=TITLE_H)

#-------------------menu sidebar------------------------------------
        sidebar=Frame(self.root,bg=theme.INK)
        sidebar.place(x=0,y=body_y,width=SIDEBAR_W,height=WIN_H-body_y)

        lbl_menu=Label(sidebar,text="MENU",font=theme.TITLE,bg=theme.INK_LIGHT,fg=theme.GOLD)
        lbl_menu.place(x=0,y=0,width=SIDEBAR_W,height=40)

        menu_items=[("ADD CUSTOMER",self.cust_details),
                    ("ROOMS DETAILS",self.roombooking),
                    ("ADD NEW ROOM",self.details_room),
                    ("LOGOUT",self.logout)]

        for i,(label,cmd) in enumerate(menu_items):
            b=Button(sidebar,text=label,command=cmd,font=theme.BUTTON,
                     bg=theme.INK,fg=theme.GOLD,activebackground=theme.INK_LIGHT,
                     activeforeground=theme.GOLD_BRIGHT,relief=FLAT,bd=0,
                     anchor="w",padx=22,cursor="hand2")
            b.place(x=0,y=52+i*44,width=SIDEBAR_W,height=40)

#--------------------sidebar thumbnails-----------------------
        thumb_y=52+len(menu_items)*44+theme.PAD
        thumb_h=max(90,(WIN_H-body_y-thumb_y-theme.PAD*2)//2)

        img4=Image.open(os.path.join(IMG_DIR, "food.jpg"))
        img4=img4.resize((SIDEBAR_W-theme.PAD*2,thumb_h),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        Label(sidebar,image=self.photoimg4,bd=0).place(
            x=theme.PAD,y=thumb_y,width=SIDEBAR_W-theme.PAD*2,height=thumb_h)

        img5=Image.open(os.path.join(IMG_DIR, "peeps.jpg"))
        img5=img5.resize((SIDEBAR_W-theme.PAD*2,thumb_h),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        Label(sidebar,image=self.photoimg5,bd=0).place(
            x=theme.PAD,y=thumb_y+thumb_h+theme.PAD,width=SIDEBAR_W-theme.PAD*2,height=thumb_h)

#--------------------Right side Image-----------------------
        main_w=WIN_W-SIDEBAR_W
        main_h=WIN_H-body_y
        img3=Image.open(os.path.join(IMG_DIR, "rightside.jpg"))
        img3=img3.resize((main_w,main_h),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,bd=0)
        lblimg1.place(x=SIDEBAR_W,y=body_y,width=main_w,height=main_h)

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
