from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Login_Page:
    def __init__(self,root):
        self.root=root
        self.root.title("Face_Recognition_Based_Attendance_System Login")
        self.root.geometry("1600x900+0+0")

        self.bg=ImageTk.PhotoImage(file=r"E:\Final yr pr. doc\slazzer-edit-image.png")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=800,y=170,width=380,height=450)

        img1=Image.open(r"E:\Final yr pr. doc\516-5167304_transparent-background-white-user-icon-png-png-download.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,borderwidth=0)
        lblimg1.place(x=950,y=180,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",16,"bold"),fg="black",bg="white")
        get_str.place(x=144,y=120)


        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="black")
        username.place(x=30,y=160)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=192,width=308)


        password=lbl=Label(frame,font=("times new roman",12,"bold"),fg="white",bg="black")
        password.place(x=30,y=235)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=30,y=266,width=308)

        #login button

        loginb=Button(frame,command=self.login,text="Login",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginb.place(x=120,y=320,width=120,height=35)

        #creat new acc button
        creatb=Button(frame,text="New User? Register",font=("times new roman",12,"bold"),bd=0,fg="white",bg="black")
        creatb.place(x=5,y=380,width=180,height=35)

        #forgot pass button
        passb=Button(frame,text="Forgot password?",font=("times new roman",12,"bold"),bd=0,fg="white",bg="black")
        passb.place(x=210,y=380,width=140,height=35)


    def login(self):
        if self.txtuser.get( )==" " or self.txtpass.get( )==" ":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get( )=="sayo" and self.txtpass.get( )=="smile":
            messagebox.showinfo("Success","Welcome to Face Recognition Based Attendance System")
        else:
            messagebox.showerror("Invalid","Invalid username & password")




if __name__ == "__main__":
    root=Tk()
    web=Login_Page(root)
    root.mainloop()