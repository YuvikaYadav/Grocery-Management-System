# import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("C:\\Users\yuviy\OneDrive\Desktop\store\store management software\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]
class Database:
    def __init__(self, master, *args, **kwargs):
        
        self.master = master
        self.heading = Label(master, text="Add to the database", font=('arial 40 bold'), fg='steelblue') 
        self.heading.place(x=450, y=0)
        
        # labels for the window
        self.product_name_l = Label(master, text="Enter Product Name", font=('arial 18 bold'))
        self.product_name_l.place(x=0, y=80) 
        
        self.stock_l = Label(master, text="Enter Stocks", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=130) 
        
        self.cp_l = Label(master, text="Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=180) 
        
        self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=230) 
        
        self.vendor_l = Label(master, text="Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=280) 
        
        self.vendor_contact_l = Label(master, text="Enter Vendor Contact", font=('arial 18 bold'))
        self.vendor_contact_l.place(x=0, y=330)
        
        self.id_l = Label(master, text="Enter ID", font=('arial 18 bold'))
        self.id_l.place(x=0, y=380)
        
        # entries for the labels
        self.product_name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.product_name_e.place(x=350, y=80) 
        
        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=350, y=130) 
        
        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=350, y=180) 
        
        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=350, y=230) 
        
        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=350, y=280)
        
        self.vendor_contact_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_contact_e.place(x=350, y=330) 
        
        self.id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.id_e.place(x=350, y=380)
        
        # button to add to the database
        self.btn_add = Button(master, text="Add To Database", width=25, height=2, bg='steelblue', fg='white', command=self.get_items)
        self.btn_add.place(x=495, y=430)
        
        self.btn_clear = Button(master, text="Clear All Fields", width=18, height=2, bg='lightgreen', fg='white', command=self.clear_all)
        self.btn_clear.place(x=340, y=430)
                
        #text box for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "ID has reached upto: " + str(id))
        
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)
    def get_items(self, *args, **kwargs):
        # get from entries
        self.product_name = self.product_name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_contact = self.vendor_contact_e.get()
                
        # dynamic entries
        self.totalcp = float(self.cp)*float(self.stock)
        self.totalsp = float(self.sp)*float(self.stock)
        self.profit_assumed = float(self.totalsp - self.totalcp)
        
        if self.product_name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
        else:
            sql = "INSERT INTO inventory (product_name, stock, cp, sp, totalcp, totalsp, profit_assumed, vendor, vendor_contact) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.product_name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.profit_assumed, self.vendor, self.vendor_contact))
            conn.commit()
            # textbox insert 
            self.tBox.insert(END, "\n\nInseted " + str(self.product_name) + " into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")
    def clear_all(self, *args, **kwargs):
        self.product_name_e.delete(0, END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_contact_e.delete(0,END)   
root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()