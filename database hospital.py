import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import tkinter as tk
import sqlite3
conn=sqlite3.connect("Hospitaldata.db")
cur=conn.cursor()
conn2=sqlite3.connect("doctor.db")
cur2=conn2.cursor()
class homepage:
    def __init__(self,hp):
        self.hp=hp
        self.hp.geometry("1200x700+100+50")
        self.bg = ImageTk.PhotoImage(file="image2.jpg")
        self.bg_image = Label(self.hp, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.frame=Frame(self.hp,height=500,width=800,bg="lightyellow")
        self.frame.place(x=200,y=200)
        hpname = Label(self.frame, text="Miracle Hospital", bg="lightyellow", font=("times new roman", 40)).place(x=200, y=30)
        self.frame1 = Frame(self.frame, height=400, width=300, bg="lightblue")
        self.frame1.place(x=100,y=100)
        self.frame2 = Frame(self.frame, height=400, width=300, bg="lightgreen")
        self.frame2.place(x=400,y=100)
        self.but=Button(self.frame1,text="Book Appointment",font=("times new roman",15),bg="#d77337",bd=round(10),command=self.appoint)
        self.but.place(x=50,y=40,width=200,height=50)
        self.but1 = Button(self.frame1, text="Update", font=("times new roman", 15), bg="#d77337",bd=round(10), command=self.update)
        self.but1.place(x=50, y=100, width=200, height=50)
        Id=Label(self.frame1,text="ID",font=("times new roman",20),bg="lightblue").place(x=50,y=170)
        self.entry=Entry(self.frame1,bg="lightgrey",font=(15))
        self.entry.place(x=50,y=200,width=200,height=30)
        # b2 button to call function to show data with using primary key
        self.b2 = Button(self.frame1, text="Show ", font=(15), bg="#d55000", bd=round(10), command=self.datashow).place(x=50, y=240,width=200, height=50)
        # b3 button to delete appointment
        self.b3=Button(self.frame1,text="Delete",font=(15),bg="#d10000",bd=round(10),command=self.delete).place(x=50 , y=310 , width=200, height=50)
        self.box = Text(self.frame2,font=(15),bg="lightgrey",bd=round(5))
        self.box.place(x=0, y=0, width=300, height=400)
    def delete(self):
        self.ddata=self.entry.get()
        query="DELETE FROM Hospital_detail WHERE ID=?"
        cur.execute(query,[self.ddata])
        conn.commit()
        messagebox.showinfo("Delete","Your appointment deleted.")
    def datashow(self):
        self.data=self.entry.get()
        query = "SELECT * FROM Hospital_detail WHERE ID=? "
        cur.execute(query, [self.data])
        self.result = list(cur.fetchall())
        if self.result == []:
            self.box.insert(INSERT, "Invalid id :"+str(self.data))
            messagebox.showerror("Error", "Wrong ID :"+str(self.data))
        else:
            self.box.insert(INSERT, " Appointment id :" + str(self.result[0][0]))
            self.box.insert(INSERT, "\n Name :" + str(self.result[0][1]))
            self.box.insert(INSERT, "\n Age :" + str(self.result[0][2]))
            self.box.insert(INSERT, "\n Gender :" + str(self.result[0][3]))
            self.box.insert(INSERT, "\n location :" + str(self.result[0][4]))
            self.box.insert(INSERT, "\n Mobile No. :" + str(self.result[0][5]))
            self.box.insert(INSERT, "\n Shedule time  :" + str(self.result[0][6]))

    # Add details for booking of new appointment
    def appoint(self):
        self.hp= Toplevel(page)
        self.hp.geometry("1200x700+100+50")
        self.bg = ImageTk.PhotoImage(file="image2.jpg")
        self.bg_image = Label(self.hp, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # Frame used in scree----------------------------------------------------------------
        f1 = Frame(self.hp, bg="lightblue", height=700, width=800)
        f1.pack(side=LEFT)
        f2 = Frame(self.hp, bg="lightgreen", height=700, width=400)
        f2.pack(side=RIGHT)
        # detail and entry ------------------------------------------------------------------
        # id ------------------
        Id = Label(f1, text="ID", font=(20,), bg="lightblue").place(x=50, y=20)
        self.e1 = Entry(f1, font=(15), bg="Lightgrey")
        self.e1.place(x=50, y=50, height=30, width=200)
        # name ------------------
        name = Label(f1, text="Name", font=(20), bg="lightblue").place(x=50, y=90)
        self.e2 = Entry(f1, font=(15), bg="Lightgrey")
        self.e2.place(x=50, y=120, height=30, width=200)
        # Age------------------
        age = Label(f1, text="Age", font=(20), bg="lightblue").place(x=50, y=160)
        self.e3 = Entry(f1, font=(15), bg="Lightgrey")
        self.e3.place(x=50, y=190, height=30, width=200)
        # Gender  ------------------
        Gender = Label(f1, text="Gender", font=(20), bg="lightblue").place(x=50, y=230)
        self.e4 = Entry(f1, font=(15), bg="Lightgrey")
        self.e4.place(x=50, y=260, height=30, width=200)
        # Location ------------------
        loc = Label(f1, text="Location", font=(20), bg="lightblue").place(x=50, y=300)
        self.e5 = Entry(f1, font=(15), bg="Lightgrey")
        self.e5.place(x=50, y=330, height=30, width=200)
        # mobile Number  ------------------
        mob = Label(f1, text="Mobile No.", font=(20), bg="lightblue").place(x=50, y=370)
        self.e6 = Entry(f1, font=(15), bg="Lightgrey")
        self.e6.place(x=50, y=400, height=30, width=200)
        # Appoint shedule------------------
        she = Label(f1, text="Shedule Time", font=(20), bg="lightblue").place(x=50, y=440)
        self.e7 = Entry(f1, font=(15), bg="Lightgrey")
        self.e7.place(x=50, y=470, height=30, width=200)
        # b1 button to call function for entry of data
        b1 = Button(f1, text="Entry", font=(15), bg="#d77337", bd=round(10), command=self.DataEntry).place(x=50, y=510,width=200, height=50)
        self.box1=Text(f2,font=(15),bg="lightgrey",bd=round(5))
        self.box1.place(x=0,y=0,width=400,height=400)
        self.value=tkinter.StringVar()
        self.Doctor=["Dr. Arunendra Roy ","Dr. Raghvendra Pratap","Dr. ALok Singh","Dr. S Roy"]
        self.option=tkinter.OptionMenu(f1,self.value,*self.Doctor,command=self.choice)
        self.option.place(x=400,y=100,width=150,height=40)
    def choice(self,ch):
        self.ch=self.value.get()

    def update(self):
        self.up=Toplevel(page)
        self.up.geometry("1200x700+100+50")
        self.up.frame=Frame(self.up,bg="lightgreen", height=400, width=800)
        self.up.frame.place(x=200,y=300)
        self.up.id=Label(self.up.frame,text="Enter ID",font=("times new roman",20),bg="lightgreen").place(x=50,y=30)
        self.e11=Entry(self.up.frame,font=(20), bg="Lightgrey")
        self.e11.place(x=50,y=60,height=30)
        print=Label(self.up.frame,text="-------Add details to update-------",font=("times new roman",15),bg="lightgreen").place(x=200,y=100)
        # name ------------------
        name = Label(self.up.frame, text="Name", font=("times new roman",20),bg="lightgreen").place(x=50,y=120)
        self.e22 = Entry(self.up.frame, font=(15), bg="Lightgrey")
        self.e22.place(x=50, y=160, height=30, width=200)
        # Age------------------
        age = Label(self.up.frame, text="Age", font=("times new roman",20),bg="lightgreen").place(x=400, y=120)
        self.e33 = Entry(self.up.frame, font=(15), bg="Lightgrey")
        self.e33.place(x=400, y=160, height=30, width=200)
        # Gender  ------------------
        Gender = Label(self.up.frame, text="Gender", font=("times new roman",20),bg="lightgreen").place(x=50, y=200)
        self.e44 = Entry(self.up.frame, font=(15), bg="Lightgrey")
        self.e44.place(x=50, y=240, height=30, width=200)
        # Location ------------------
        loc = Label(self.up.frame, text="Location", font=("times new roman",20),bg="lightgreen").place(x=400, y=200)
        self.e55 = Entry(self.up.frame, font=(15), bg="Lightgrey")
        self.e55.place(x=400, y=240, height=30, width=200)
        # mobile Number  ------------------
        mob = Label(self.up.frame, text="Mobile No.",font=("times new roman",20),bg="lightgreen").place(x=50, y=280)
        self.e66 = Entry(self.up.frame, font=(15), bg="Lightgrey")
        self.e66.place(x=50, y=320, height=30, width=200)
        # Appoint shedule------------------
        she = Label(self.up.frame, text="Shedule Time", font=("times new roman",20),bg="lightgreen").place(x=400, y=280)
        self.e77 = Entry(self.up.frame, font=(15), bg="Lightgrey")
        self.e77.place(x=400, y=320, height=30, width=200)

        self.bb1 = Button(self.up.frame, text="Update", font=("times new roman", 15), bg="#d77337", bd=round(5),
                          command=self.updatedata)
        self.bb1.place(x=650, y=330,height=30, width=100)
        self.bb2= Button(self.up.frame, text="Reset", font=("times new roman", 15), bg="#d77337", bd=round(5),
                          command=self.resetdata)
        self.bb2.place(x=650, y=290,height=30, width=100)
    def resetdata(self):
        self.e22.delete("1.0","end")
        self.e33.delete("1.0","end")
        self.e44.delete("1.0","end")
        self.e55.delete("1.0","end")
        self.e66.delete("1.0","end")
        self.e77.delete("1.0","end")
        self.e11.delete("1.0","end")
    def updatedata(self):
        print(self.e22.get(),self.e33.get(),self.e44.get(),self.e55.get(),self.e66.get(),self.e77.get(),self.e11.get())
        query1="UPDATE Hospital_detail SET Name=?, Age=?, Gender=? , Location=?, Mobile_No=?, Shedule_time=? WHERE ID=?"
        data1=(self.e22.get(),self.e33.get(),self.e44.get(),self.e55.get(),self.e66.get(),self.e77.get(),self.e11.get())
        cur.execute(query1,data1)
        conn.commit()
    # called function after click entry button
    def DataEntry(self):
        self.d1 = self.e1.get()
        self.d2 = self.e2.get()
        self.d3 = self.e3.get()
        self.d4 = self.e4.get()
        self.d5 = self.e5.get()
        self.d6 = self.e6.get()
        self.d7 = self.e7.get()
        if self.d1 == "" or self.d2 == "" or self.d3 == "" or self.d3 == "" or self.d5 == "" or self.d6 == "" or self.d7 == "":
            messagebox.showerror("Error", "Please , Add all details")
        else:
            sql = "INSERT INTO 'Hospital_detail'( ID ,Name , Age, Gender , Location, Mobile_No, Shedule_time) Values(?,?,?,?,?,?,?)"
            data = (self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7)
            cur.execute(sql, data)
            conn.commit()
            self.box1.insert(INSERT,"Appointment fixed ")
            self.box1.insert(INSERT, "\nID :"+self.d1)
            self.box1.insert(INSERT, "\nName :"+self.d2)
            self.box1.insert(INSERT, "\nAge :"+self.d3)
            self.box1.insert(INSERT, "\nGender :"+self.d4)
            self.box1.insert(INSERT, "\nLocation :"+self.d5)
            self.box1.insert(INSERT, "\nMobile No. :"+self.d6)
            self.box1.insert(INSERT, "\nSchedule time :"+self.d7)
        self.query2="SELECT * FROM doctor WHERE doc_id=?"
        self.data2=self.ch
        cur2.execute(self.query2,(self.data2))
        self.result2=list(cur2.fetchall())
        print(self.result2)


page=Tk()
page.geometry("1200x700+100+100")
obj=homepage(page)
page.mainloop()
