import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os   #to genrate bill number randomly
from tkinter import messagebox as mb
import tempfile
from time import strftime

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='komal2402',
        database='billing_system',
        port=3306
    )


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title("BillEase")
        self.root.state('zoomed')
        self.root.resizable(FALSE,FALSE)

        #Variables
        self.c_name=StringVar()
        self.c_mobile=StringVar()
        self.c_email=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()     #intvar because we need to perform calculation with this
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        #product category list
        self.Category=["Select an Option","Clothing","Lifestyle","Mobiles"]

        #subcategory clothing
        self.subcatclothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=700
        self.price_spykar=8000

        self.tshirt = ["Polo", "Roadster", "Jack&Jones"]
        self.price_polo = 1500
        self.price_roadster = 1800
        self.price_jack = 1700

        self.shirt = ["Peter England", "Louis Phillipe", "Park Avenue"]
        self.price_peter = 2100
        self.price_louis = 2700
        self.price_park = 1740

        #subcategory lifestyle
        self.subcatlifestyle=["Bath Soap","Face Cream","Hair Oil"]
        self.bathsoap=["Life Boy","Lux","Santoor","Pearl"]
        self.price_life=20
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=20

        self.facecream = ["Fair & Lovely", "Ponds", "Olay", "Garnier"]
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay = 20
        self.price_garnier = 30

        self.hairoil = ["Parachute", "Jasmine", "Bajaj"]
        self.price_para =25
        self.price_jas = 22
        self.price_bajaj = 30

        #sub category mobile
        self.subcatmobile=["Iphone","Samsung","Xiome","RealMe","OnePlus"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_x=40000
        self.price_11=60000
        self.price_12=85000

        self.Samsung=["Samsung M16","Samsung M12","Samsung M21"]
        self.price_m16=16000
        self.price_m12=12000
        self.price_m21=18000

        self.Xiome = ["Redmi 11", "Redmi 12", "Redmi 12 Pro"]
        self.price_r11 = 11000
        self.price_r12 = 12000
        self.price_rpro = 20000

        self.Realme = ["RealMe 12", "RealMe 13", "RealMe Pro"]
        self.price_re12 = 25000
        self.price_re13 = 22000
        self.price_repro = 30000

        self.Oneplus = ["OnePlus 13", "OnePlus Ace 5 Pro", "OnePlus Open 2","OnePlus Nord 4"]
        self.price_o13 = 70000
        self.price_o5 = 55000
        self.price_o3 = 150000
        self.price_o4 = 30000

        #IMAGE1
        img = Image.open("images/b1.jpg")
        img = img.resize((500,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #IMAGE2
        img1 = Image.open("images/girls.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl1_img = Label(self.root, image=self.photoimg1)
        lbl1_img.place(x=500, y=0, width=500, height=130)

        #IMAGE3
        img2 = Image.open("images/girl1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl2_img = Label(self.root, image=self.photoimg2)
        lbl2_img.place(x=1000, y=0, width=500, height=130)

        lbl_title = Label(self.root,text="BILL EASE",font=("times new roman",30,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1408,height=30)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=("times new roman",16,"bold"),bg='white',fg='blue')
        lbl.place(x=0,y=-7,width=120,height=40)
        time()

        main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        main_frame.place(x=0,y=160,width=1408,height=620)

        #customer label frame
        cust_label_frame=LabelFrame(main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_label_frame.place(x=0,y=2,width=340,height=120)

        self.lbl_mobile=Label(cust_label_frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mobile.grid(row=0,column=0,stick=W,padx=3,pady=2)

        self.entry_mob=Entry(cust_label_frame,textvariable=self.c_mobile,font=("times new roman",12,"bold"),width=25)
        self.entry_mob.grid(row=0,column=1)

        self.lbl_name = Label(cust_label_frame, text="Customer Name", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_name.grid(row=1, column=0, stick=W, padx=3, pady=2)

        self.entry_name = Entry(cust_label_frame, textvariable=self.c_name,font=("times new roman", 12, "bold"), width=25)
        self.entry_name.grid(row=1, column=1)

        self.lbl_email = Label(cust_label_frame, text="Email", font=("times new roman", 12, "bold"),bg="white")
        self.lbl_email.grid(row=2, column=0, stick=W, padx=3, pady=2)

        self.entry_email = Entry(cust_label_frame,textvariable=self.c_email, font=("times new roman", 12, "bold"), width=25)
        self.entry_email.grid(row=2, column=1)

        #Product label frame
        product_label_frame = LabelFrame(main_frame, text="Product", font=("times new roman", 12, "bold"), bg="white",fg="red")
        product_label_frame.place(x=370, y=2, width=600, height=120)

        #category
        self.lbl_category = Label(product_label_frame, text="Select Category", font=("times new roman", 12, "bold"), bd=4, bg="white")
        self.lbl_category.grid(row=0, column=0, stick=W, padx=3, pady=2)

        self.combo_category=ttk.Combobox(product_label_frame,value=self.Category,font=("times new roman", 10, "bold"),width=24,state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=3,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.categories)


        #subcategory
        self.lbl_subcategory = Label(product_label_frame, text="Subcateory", font=("times new roman", 12, "bold"),bd=4, bg="white")
        self.lbl_subcategory.grid(row=1, column=0, stick=W, padx=3, pady=2)

        self.combo_subcategory = ttk.Combobox(product_label_frame,value=[""], font=("times new roman", 10, "bold"), width=24,state="readonly")
        self.combo_subcategory.grid(row=1, column=1, sticky=W, padx=3, pady=2)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product name
        self.lbl_product = Label(product_label_frame, text="Product Name", font=("times new roman", 12, "bold"),bd=4, bg="white")
        self.lbl_product.grid(row=2, column=0, stick=W, padx=3, pady=2)

        self.combo_product = ttk.Combobox(product_label_frame,textvariable=self.product, font=("times new roman", 10, "bold"), width=24,state="readonly")
        self.combo_product.grid(row=2, column=1, sticky=W, padx=3, pady=2)
        self.combo_product.bind("<<ComboboxSelected>>",self.price)

        #price
        self.lbl_price = Label(product_label_frame, text="Price", font=("times new roman", 12, "bold"),bd=4, bg="white")
        self.lbl_price.grid(row=0, column=2, stick=W, padx=3, pady=2)

        self.combo_price = ttk.Combobox(product_label_frame, textvariable=self.prices,font=("times new roman", 10, "bold"), width=24,state="readonly")
        self.combo_price.grid(row=0, column=3, sticky=W, padx=3, pady=2)

        #Quantity
        self.lbl_Qty= Label(product_label_frame, text="Quantity", font=("times new roman", 12, "bold"),bd=4, bg="white")
        self.lbl_Qty.grid(row=1, column=2, stick=W, padx=3, pady=2)

        self.entry_Qty = Entry(product_label_frame,textvariable=self.qty, font=("times new roman", 10, "bold"), width=24)
        self.entry_Qty.grid(row=1, column=3, sticky=W, padx=3, pady=2)

        #Middle frame
        middle_frame=Frame(main_frame,bd=10)
        middle_frame.place(x=0,y=130,width=968,height=350)

        # IMAGE4
        img3 = Image.open("images/good.jpg")
        img3= img3.resize((490, 350), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(middle_frame, image=self.photoimg3)
        lbl_img3.grid(row=0,column=0,padx=0,pady=0,sticky='nsew')

        # IMAGE5
        img4 = Image.open("images/mall.jpg")
        img4 = img4.resize((495, 350), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl1_img4 = Label(middle_frame, image=self.photoimg4)
        lbl1_img4.grid(row=0,column=1,padx=0,pady=0,sticky='nsew')


        #Search
        Search_frame = Frame(main_frame, bg="white", bd=2)
        Search_frame.place(x=975, y=10,width=412,height=40)

        #bill number label
        self.lbl_billno = Label(Search_frame, text="Bill Number", font=("arial", 12, "bold"), bd=4,bg="red",fg="white")
        self.lbl_billno.grid(row=0, column=0, stick=W, padx=1)

        self.entry_billno = Entry(Search_frame,textvariable=self.search_bill, font=("arial", 12, "bold"), width=17)
        self.entry_billno.grid(row=0, column=1, sticky=W, padx=4)

        self.btnsearch = Button(Search_frame, command=self.search, text="Search", font=("arial", 12, "bold"), bg="orangered",fg="white",width=15, cursor="hand2")
        self.btnsearch.grid(row=0, column=2)

        #Rightframe Bill Area
        rightlabelframe=LabelFrame(main_frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        rightlabelframe.place(x=975,y=45,width=420,height=435)

        scroll_y=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #bill counter label frame
        bottom_label_frame = LabelFrame(main_frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white",fg="red")
        bottom_label_frame.place(x=0, y=480, width=1400, height=130)

        #Subtotal
        self.lbl_subtotal = Label(bottom_label_frame, text="Sub Total", font=("arial", 12, "bold"), bd=4,bg="white")
        self.lbl_subtotal.grid(row=0, column=0, stick=W, padx=3, pady=2)

        self.entry_subtotal = Entry(bottom_label_frame,textvariable=self.sub_total, font=("arial", 10, "bold"), width=24)
        self.entry_subtotal.grid(row=0, column=1, sticky=W, padx=3, pady=2)

        #tax
        self.lbl_tax = Label(bottom_label_frame, text="Gov Tax", font=("arial", 12, "bold"), bd=4, bg="white")
        self.lbl_tax.grid(row=1, column=0, stick=W, padx=3, pady=2)

        self.entry_tax = Entry(bottom_label_frame,textvariable=self.tax_input, font=("arial", 10, "bold"), width=24)
        self.entry_tax.grid(row=1, column=1, sticky=W, padx=3, pady=2)

        #total amount
        self.lbl_amounttotal = Label(bottom_label_frame, text="Total", font=("arial", 12, "bold"), bd=4, bg="white")
        self.lbl_amounttotal.grid(row=2, column=0, stick=W, padx=3, pady=2)

        self.entry_amounttotal = Entry(bottom_label_frame,textvariable=self.total, font=("arial", 10, "bold"), width=24)
        self.entry_amounttotal.grid(row=2, column=1, sticky=W, padx=3, pady=2)

        #button frame
        Button_frame=Frame(bottom_label_frame,bg="white",bd=2)
        Button_frame.place(x=320,y=0)

        #add to cart button
        self.btnAddtocart=Button(Button_frame,command=self.Addtocart, text="Add To Cart",font=("arial",17,"bold"),bg="orangered",fg="white",width=11,cursor="hand2")
        self.btnAddtocart.grid(row=0,column=0,padx=3)

        #generate bill button
        self.btngeneratebill = Button(Button_frame,command=self.Generatebill, text="Generate Bill", font=("arial", 17, "bold"), bg="orangered",fg="white",width=11,cursor="hand2")
        self.btngeneratebill.grid(row=0, column=1,padx=3)

        #save bill button
        self.btnsavebill = Button(Button_frame, text="Save Bill",command=self.Savebill, font=("arial", 17, "bold"), bg="orangered",fg="white",width=11,cursor="hand2")
        self.btnsavebill.grid(row=0, column=2,padx=3)

        #print button
        self.btnprint = Button(Button_frame, text="Print",command=self.iprint, font=("arial", 17, "bold"), bg="orangered",fg="white",width=11,cursor="hand2")
        self.btnprint.grid(row=0, column=3,padx=3)

        #clear button
        self.btnclear = Button(Button_frame,command=self.clear, text="Clear", font=("arial", 17, "bold"), bg="orangered",fg="white",width=11,cursor="hand2")
        self.btnclear.grid(row=0, column=4,padx=3)

        #exit button
        self.btnexit = Button(Button_frame,command=self.root.destroy, text="Exit", font=("arial", 17, "bold"), bg="orangered", fg="white",width=11,cursor="hand2")
        self.btnexit.grid(row=0, column=5,padx=3)
        self.welcome()

        self.l=[]
    # =====================function declarations===================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,("WELCOME TO APNA BAZAR").center(70))
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Mobile Number:{self.c_mobile.get()}")
        self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END, f"\n Products\t\t\tQTY\t\tPrice")
        self.textarea.insert(END, "\n===========================================\n")

    def Addtocart(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            mb.showerror("Error","Please Enter Mobile Number and Select the Product Name")
        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")

            #calculate sub total
            subtotal=sum(self.l)
            self.sub_total.set(f"Rs.{subtotal:.2f}")

            #calculate tex
            tax_amount=(subtotal*1)/100
            self.tax_input.set(f"Rs.{tax_amount:.2f}")

            #calculate total with tax
            total_amount=subtotal+tax_amount
            self.total.set(f"Rs.{total_amount:.2f}")

    def Generatebill(self):
        if self.product.get()=="":
            mb.showerror("Error","Please Add To Cart a Product")
        else:
            text=self.textarea.get(9.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=========================================")
            self.textarea.insert(END,f"\n Sub Total:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.total.get()}")

    def Savebill(self):
        op = mb.askyesno("Save", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO bills (bill_no, customer_name, mobile, email, bill_data) VALUES (%s, %s, %s, %s, %s)",
                    (self.bill_no.get(), self.c_name.get(), self.c_mobile.get(), self.c_email.get(), self.bill_data))
                conn.commit()
                conn.close()
                mb.showinfo("Saved", f"Bill No:{self.bill_no.get()} saved successfully.")
            except Error as e:
                mb.showerror("Database Error", str(e))

    def iprint(self):
        q=self.textarea.get(1.0,END)
        filename=tempfile.mktemp('.txt')
        open(filename,"w").write(q)
        os.startfile(filename,"print")

    def search(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT bill_data FROM bills WHERE bill_no = %s", (self.search_bill.get(),))
            result = cursor.fetchone()
            conn.close()

            if result:
                self.textarea.delete(1.0, END)
                self.textarea.insert(END, result[0])
            else:
                mb.showerror("Error", "Invalid Bill Number")
        except Error as e:
            mb.showerror("Database Error", str(e))

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_mobile.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()



    def categories(self,event=""):
        if self.combo_category.get()=="Clothing":
            self.combo_subcategory.config(value=self.subcatclothing)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=="Lifestyle":
            self.combo_subcategory.config(value=self.subcatlifestyle)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=="Mobiles":
            self.combo_subcategory.config(value=self.subcatmobile)
            self.combo_subcategory.current(0)

    def Product_add(self,event=""):
        #clothing
        if self.combo_subcategory.get()=="Pant":
            self.combo_product.config(value=self.pant)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="T-Shirt":
            self.combo_product.config(value=self.tshirt)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Shirt":
            self.combo_product.config(value=self.shirt)
            self.combo_product.current(0)

        #lifestyle
        if self.combo_subcategory.get()=="Bath Soap":
            self.combo_product.config(value=self.bathsoap)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Face Cream":
            self.combo_product.config(value=self.facecream)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Hair Oil":
            self.combo_product.config(value=self.hairoil)
            self.combo_product.current(0)

        #Mobile
        if self.combo_subcategory.get()=="Iphone":
            self.combo_product.config(value=self.Iphone)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Samsung":
            self.combo_product.config(value=self.Samsung)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Xiome":
            self.combo_product.config(value=self.Xiome)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="RealMe":
            self.combo_product.config(value=self.Realme)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="OnePlus":
            self.combo_product.config(value=self.Oneplus)
            self.combo_product.current(0)

    def price(self,event):
        #Pant
        if self.combo_product.get()=="Levis":
            self.combo_price.config(value=self.price_levis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Mufti":
            self.combo_price.config(value=self.price_mufti)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Spykar":
            self.combo_price.config(value=self.price_spykar)
            self.combo_price.current(0)
            self.qty.set(1)

        #Tshirt
        if self.combo_product.get()=="Polo":
            self.combo_price.config(value=self.price_polo)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Roadster":
            self.combo_price.config(value=self.price_roadster)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Jack&Jones":
            self.combo_price.config(value=self.price_jack)
            self.combo_price.current(0)
            self.qty.set(1)

        #Shirts
        if self.combo_product.get()=="Peter England":
            self.combo_price.config(value=self.price_peter)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Louis Phillipe":
            self.combo_price.config(value=self.price_louis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Park Avenue":
            self.combo_price.config(value=self.price_park)
            self.combo_price.current(0)
            self.qty.set(1)

        #bathsoap
        if self.combo_product.get()=="Life Boy":
            self.combo_price.config(value=self.price_life)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Lux":
            self.combo_price.config(value=self.price_lux)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Santoor":
            self.combo_price.config(value=self.price_santoor)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Pearl":
            self.combo_price.config(value=self.price_pearl)
            self.combo_price.current(0)
            self.qty.set(1)

        #Facecream
        if self.combo_product.get()=="Fair & Lovely":
            self.combo_price.config(value=self.price_fair)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Ponds":
            self.combo_price.config(value=self.price_ponds)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Olay":
            self.combo_price.config(value=self.price_olay)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Garnier":
            self.combo_price.config(value=self.price_garnier)
            self.combo_price.current(0)
            self.qty.set(1)

        #hairoil
        if self.combo_product.get()=="Parachute":
            self.combo_price.config(value=self.price_para)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Jasmine":
            self.combo_price.config(value=self.price_jas)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Bajaj":
            self.combo_price.config(value=self.price_bajaj)
            self.combo_price.current(0)
            self.qty.set(1)

        #iphone
        if self.combo_product.get()=="Iphone_X":
            self.combo_price.config(value=self.price_x)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Iphone_11":
            self.combo_price.config(value=self.price_11)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Iphone_12":
            self.combo_price.config(value=self.price_12)
            self.combo_price.current(0)
            self.qty.set(1)

        #Samsung
        if self.combo_product.get()=="Samsung M16":
            self.combo_price.config(value=self.price_m16)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Samsung M12":
            self.combo_price.config(value=self.price_m12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Samsung M21":
            self.combo_price.config(value=self.price_m21)
            self.combo_price.current(0)
            self.qty.set(1)

        #xiome
        if self.combo_product.get()=="Redmi 11":
            self.combo_price.config(value=self.price_r11)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Redmi 12":
            self.combo_price.config(value=self.price_r12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Redmi 12 Pro":
            self.combo_price.config(value=self.price_rpro)
            self.combo_price.current(0)
            self.qty.set(1)

        #Realme
        if self.combo_product.get()=="RealMe 12":
            self.combo_price.config(value=self.price_re12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="RealMe 13":
            self.combo_price.config(value=self.price_re13)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="RealMe Pro":
            self.combo_price.config(value=self.price_repro)
            self.combo_price.current(0)
            self.qty.set(1)

        #One Plus
        if self.combo_product.get()=="OnePlus 13":
            self.combo_price.config(value=self.price_o13)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="OnePlus Ace 5 Pro":
            self.combo_price.config(value=self.price_o5)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="OnePlus Open 2":
            self.combo_price.config(value=self.price_o2)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="OnePlus Nord 4":
            self.combo_price.config(value=self.price_o4)
            self.combo_price.current(0)
            self.qty.set(1)

if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()