import builtins
from tkinter import*
from employee import employeeClass
from suppliers import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from stock import stockClass

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #TITLE#
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM", font=("times new roman",40,"bold"), bg="black", fg="white",anchor="w",padx=40).place(x=0,y=0,relwidth=1,height=70)

        #LOGOUT#
        butn_logout=Button(self.root,text="LOGOUT",font=("times new roman",15,"bold"),bg="#00ffff",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #CLOCK#
        self.lbl_clock=Label(self.root,text="WELCOME TO INVENTORY MANAGEMENT SYSTEM\t\t DATE: DD-MM-YYYY\t\t TIME: HH:MM:SS", font=("times new roman",15,), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #LEFT MENU#
        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200,height=570)

        label_menu=Label(leftmenu,text="MENU",font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X)
        
        butn_employee=Button(leftmenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X)
        butn_suppliers=Button(leftmenu,text="Suppliers",command=self.suppliers,font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X)
        butn_customers=Button(leftmenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X)
        butn_product=Button(leftmenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X)
        butn_sales=Button(leftmenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X)
        butn_stocks=Button(leftmenu,text="Stocks",command=self.stock,font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X) 
        butn_exit=Button(leftmenu,text="Exit",font=("times new roman",20,"bold"),bg="white",cursor="hand2").pack(side=TOP,fill=X)

        #CONTENT#
        self.lbl_employee = Label(self.root,text="Total Employee\n [ 0 ]",bd=5,relief=RIDGE ,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_suppliers = Label(self.root,text="Total Suppliers\n [ 0 ]",bd=5,relief=RIDGE ,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_suppliers.place(x=650,y=120,height=150,width=300)

        self.lbl_customers = Label(self.root,text="Total Customers\n [ 0 ]",bd=5,relief=RIDGE ,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_customers.place(x=1000,y=120,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product\n [ 0 ]",bd=5,relief=RIDGE ,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales\n [ 0 ]",bd=5,relief=RIDGE ,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        self.lbl_stocks = Label(self.root,text="Total Stocks\n [ 0 ]",bd=5,relief=RIDGE ,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_stocks.place(x=1000,y=300,height=150,width=300)

        #FOOTER#
        lbl_footer=Label(self.root,text="IMS - Inventory Management System\t\t", font=("times new roman",15,), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def suppliers(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def stock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=stockClass(self.new_win)





if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()