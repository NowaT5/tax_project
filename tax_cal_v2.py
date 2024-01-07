import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#ล้างช่องข้อความ
def clear_box():
    price_input.delete(0, END)
    showprice1.delete(0, END)
    showprice2.delete(0, END)
    showprice3.delete(0, END)
    showprice4.delete(0, END)

#function ในการคำนวณ
def Vat_Cal():
    #ดึงค่า % มาเก็บไว้เตรียมคำนวณ
    pick = tax.get()
    try:
        if pick != 0 :

            Full_price = float(price_input.get()) #ดึงราคา(รวมVat)มา
            #การคำนวณ
            Price_non_tax = Full_price * 100 / 107 #หาราคาไม่รวม Vat
            Cus_tax = Price_non_tax * pick / 100 #หาราคาหักภาษี ตาม %
            Vat = Price_non_tax * 7 / 100 #หาราคาภาษีมูลค่าเพิ่ม (Vat)
            Pay_Price = Price_non_tax + Vat - Cus_tax #หาราคาที่ลูกค้าต้องชำระ

            #answer =  [Price_non_tax, Cus_tax, Vat, Pay_Price]
            #ลบผลลัพธ์ ก่อนหน้า
            showprice1.delete(0, END)
            showprice2.delete(0, END)
            showprice3.delete(0, END)
            showprice4.delete(0, END)
            #แสดงผลการคำนวณ
            showprice1.insert(0,'{:,.2f}'.format(Price_non_tax))
            showprice2.insert(0,'{:,.2f}'.format(Cus_tax))
            showprice3.insert(0,'{:,.2f}'.format(Vat))
            showprice4.insert(0,'{:,.2f}'.format(Pay_Price))

        else: #ถ้าไม่เลือก % ในการคำนวณ
            tk.messagebox.showinfo(title='Error',message='กรุณาลองใหม่อีกครั้ง')
    except:#ถ้าไม่ใส่ราคาเพื่อคำนวณ
        tk.messagebox.showinfo(title='Error',message='กรุณาลองใหม่อีกครั้ง')

#vat study window
def New_win():
        def what_tax_learn(): #แสดงรูป what tax % pic
                #show pic info
            pic = Image.open("pic\what_tax2.png")
            pic = pic.resize((int(pic.width * .6),int(pic.height *.6)))
            tx_img = ImageTk.PhotoImage(pic)
            image_label1 = Label(root,image=tx_img)
            image_label1.image=tx_img
            canvas.create_window(480,380,window=image_label1)

        def type_tax_learn():#แสดงรูป Tax %
            
            pic = Image.open("pic\\tpye_tax2.png")
            pic = pic.resize((int(pic.width * .6),int(pic.height *.6)))
            ty_img = ImageTk.PhotoImage(pic)
            image_label2 = Label(root,image=ty_img)
            image_label2.image=ty_img
                #return
            canvas.create_window(480,380,window=image_label2)
            
        def How_vat():#แสดงรูป การหา VAT
            pic = Image.open("pic\how_vat2.png")
            pic = pic.resize((int(pic.width * .6),int(pic.height *.6)))
            hv_img = ImageTk.PhotoImage(pic)
            image_label3 = Label(root,image=hv_img)
            image_label3.image=hv_img
            #return
            canvas.create_window(480,380,window=image_label3)

        def How_tax():#แสดงรูป การหาภาษีหัก ณ ที่จ่าย
            
            pic = Image.open("pic\how_tax2.png")
            pic = pic.resize((int(pic.width * .6),int(pic.height *.6)))
            ht_img = ImageTk.PhotoImage(pic)
            image_label4 = Label(root,image=ht_img)
            image_label4.image=ht_img
            #return
            canvas.create_window(480,380,window=image_label4)
        
        #หน้าต่างการเรียนรู้
        root = Toplevel()
        root.title('เรียนรู้เรื่องภาษีหัก ณ ที่จ่าย')
        #กำหนดขนาดด้วย canvas
        canvas = Canvas(root,width=960,height=640,bg='white')
        canvas.pack()

        #btn ภาษีหัก คือ
        whattax_learn = Button (root,text='ภาษีหัก ณ ที่จ่าย คือ ... ',font=('Arial',20,'bold'),command=what_tax_learn,bg='green',fg='white',width=20)
        canvas.create_window(195,50,window=whattax_learn)
        
        #btn % บุคคล
        tpyetax_learn = Button (root,text='อัตราหักภาษี ณ ที่จ่าย',font=('Arial',20,'bold'),command=type_tax_learn,bg='blue',fg='white',width=20)
        canvas.create_window(195,100,window=tpyetax_learn)

        #text  % ภาษี
        pro_name1 = Label(root,text='ขั้นตอนการคำนวณมีขั้นดังนี้ ',font=('Arial',20,'bold'),fg='black',bg='white')
        canvas.create_window(550,70,window=pro_name1)

        #btn การหา VAT
        how_vat = Button (root,text='1.การคำนวณภาษีมูลค่าเพิ่ม (VAT)',font=('Arial',14,'bold'),command=How_vat,bg='red',fg='white')
        canvas.create_window(530,108,window=how_vat)
        #btn การหาภาษีหัก ณ ที่จ่าย
        how_tax = Button (root,text='2.การคำนวณหักภาษี ณ ที่จ่าย',font=('Arial',14,'bold'),command=How_tax,bg='orange',fg='white')
        canvas.create_window(820,108,window=how_tax)

#Titlebar n size
window = tk.Tk()
window.title('โปรแกรมคำนวณภาษีหัก ณ ที่จ่าย')
window.geometry('440x350+300+200')

#input price box
title_label = tk.Label(master=window, text= 'กรอกราคา (รวม Vat)',font=30,bg='Black',fg='White').grid(row=0,column=0,pady=10)


#input
price_input = tk.Entry(master=window,font=20,width=30,justify="center")
price_input.grid(row=0,column=1)

#เลือก % ที่ต้องการหา
tax = IntVar()
Radiobutton(text='1%',variable=tax,value=1,font=10).grid(row=1,column=0)
Radiobutton(text='2%',variable=tax,value=2,font=10).grid(row=1,column=1)
Radiobutton(text='3%',variable=tax,value=3,font=10).grid(row=2,column=0)
Radiobutton(text='5%',variable=tax,value=4,font=10).grid(row=2,column=1)

#Calculate button
go_button1 = tk.Button(master=window, text='คำนวณ',font=20, command= Vat_Cal,width=10,bg='Green',fg='White').grid(row=3,column=1,pady=10)

#clear button
clear = Button(text='ล้างค่า',font=10,command=clear_box,width=10,bg='Red',fg='White').grid(row=3,column=0,padx=5)

#output_on_screen
#ราคาไม่รวม ภาษีมูลค่าเพิ่ม
pricenontax = Label(master=window, text= 'ราคาไม่รวมภาษี',font=(80),bg='Black',fg='White').grid(
    row=4,column=0,padx=5,sticky=W)
showprice1 = Entry(font=20,width=30,justify="center")
showprice1.grid(row=4,column=1,pady=5,sticky=E)
#ราคาภาษีหัก ณ ที่จ่าย
taxprice = Label(master=window, text= 'ราคาภาษี',font=(80),bg='Black',fg='White').grid(
    row=6,column=0,padx=5,sticky=W)
showprice2 = Entry(font=20,width=30,justify="center")
showprice2.grid(row=6,column=1,pady=5,sticky=E)
#ราคาภาษีมูลค่าเพิ่ม (VAT)
vatprice = Label(master=window, text= 'ภาษีมูลค่าเพิ่ม',font=(80),bg='Black',fg='White').grid(
    row=5,column=0,padx=5,sticky=W)
showprice3 = Entry(font=20,width=30,justify="center")
showprice3.grid(row=5,column=1,pady=5,sticky=E)
#ราคาที่ลูกค้าต้องชำระหลักหักภาษี ณ ที่จ่าย 
payprice = Label(master=window, text= 'ราคาที่ลูกค้าต้องชำระ',font=(80),bg='Black',fg='White').grid(
    row=7,column=0,padx=5,sticky=W)
showprice4 = Entry(font=20,width=30,justify="center")
showprice4.grid(row=7,column=1,pady=5,sticky=E)

#learn btn
learn_button1 = tk.Button(master=window, text='เรียนรู้เรื่องภาษีหัก ณ ที่จ่าย',font=20,command=New_win,width=20,bg='Orange',fg='White')
learn_button1.grid(row=8,column=1,pady=10)

window.mainloop()