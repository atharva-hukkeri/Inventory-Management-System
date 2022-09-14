from tkinter import*
from tkinter import ttk
from tkinter import messagebox

class BillClass:
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

        #Product Frame#
        self.var_search=StringVar()

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Producs", font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=4,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Prodcut | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
        lbl_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=135,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=288,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=288,y=10,width=100,height=25)

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview) 
        scrolly.config(command=self.product_Table.yview)
        
        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")

        self.product_Table["show"]="headings"
        self.product_Table.column("pid",width=90)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
        
        self.product_Table.pack(fill=BOTH,expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",11),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)


if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()