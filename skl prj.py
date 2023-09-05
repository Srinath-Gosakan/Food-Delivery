#importing modules

from tkinter import *
from tkinter.ttk import Combobox
import random
import datetime
import time
from datetime import date
import pyscreenshot as ImageGrab
from PIL import ImageTk,Image
import mysql.connector as sql
from plyer import notification
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import num2word as nw

####file savinggg #######

mc=sql.connect(host="localhost",user="root",passwd="srinath")
cur=mc.cursor()

#####Creating Tables######
#cur.execute("create database efood")
#cur.execute("create table users(cname varchar(20),password varchar(15),address varchar(100),pincode int(8),phonenumber numeric(11),date date)")
#cur.execute("create table hotels(hid varchar(8),hotel varchar(30),address varchar(100),pincode int(8),phonenumber numeric(11),date date)")
#cur.execute("create table foods(hid varchar(8),item varchar(50),itemcode int(6),category varchar(30),price int(5))")
#cur.execute("create table admin(name varchar(20),password varchar(20))")
#cur.execute("create table orders(cname varchar(20),hotel varchar(30),items varchar(50),quantity int(2),price int(4),date date)")


#######Selecting Database########

cur.execute("use efood")

#intro screen

def main():
    global mainwin
    mainwin=Tk()
    mainwin.title("WELCOME")
    image=Image.open(r'D:\Srinath\csc proj\2.0000.png')
    photo=ImageTk.PhotoImage(image)
    background_label = Label(mainwin, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    b1=Button(mainwin,text="CLICK TO ENTER!",bg='black',fg='white',font=("Times New Roman",19,'bold'),command=secwin)
    b1.place(x=550,y=550,relwidth=0.2,relheight=0.05)
    mainwin.geometry('1920x1080')
    mainloop()
    
def secwin():
    global sec
    mainwin.destroy()
    sec=Tk()
    sec.title("Efood Cart")
    image1=Image.open(r'D:\Srinath\csc proj\3.0000.png')
    photo1=ImageTk.PhotoImage(image1)
    background_label1 = Label(sec, image=photo1)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    b1=Button(sec,text="CREATE ACCOUNT",bg='white',fg='black',font=("Times New Roman",9,'bold'),command=register)
    b1.place(x=20,y=520,relwidth=0.1,relheight=0.05)
    b2=Button(sec,text="VIEW PARTNERS",bg='white',fg='black',font=("Times New Roman",19,'bold'),command=viewhotels)
    b2.place(x=0,y=320,relwidth=0.17,relheight=0.05)
    b3=Button(sec,text="LOGIN",bg='white',fg='black',font=("Times New Roman",19,'bold'),command=login)
    b3.place(x=20,y=420,relwidth=0.1,relheight=0.05)
    sec.geometry('1920x1080')
    mainloop()
    
#registration screen
    
def register():
    global urs
    urs=Toplevel(sec)
    urs.title("USER REGISTRATION")
    urs.geometry("500x350+400+200")
    global username
    global password
    global address
    global phno
    global passwd
    global pin
    global userentry
    global pwdentry
    global pwdentry2
    global addentry
    global phentry
    global pinentry
    username=StringVar()
    password=StringVar()
    passwd=StringVar()
    address=StringVar()
    phno=IntVar()
    pin=IntVar()
    Label(urs,text="PLEASE ENTER THE DETAILS BELOW",fg="white",bg="black").pack()
    Label(urs,text="").pack()
    Label(urs,text="USERNAME").pack()
    userentry=Entry(urs,textvariable=username)
    userentry.pack()
    Label(urs,text="PASSWORD").pack()
    pwdentry=Entry(urs,textvariable=password,show="*")
    pwdentry.pack()
    Label(urs,text="CONFIRM PASSWORD").pack()
    pwdentry2=Entry(urs,textvariable=passwd,show="*")
    pwdentry2.pack()
    Label(urs,text="ADDRESS").pack()
    addentry=Entry(urs,textvariable=address)
    addentry.pack()
    Label(urs,text="PINCODDE").pack()
    pinentry=Entry(urs,textvariable=pin)
    pinentry.pack()
    Label(urs,text="PHONE NUMBER").pack()
    phentry=Entry(urs,textvariable=phno)
    phentry.pack()
    Button(urs,text="REGISTER",width=10,height=1,command=reg_user).pack()
    Button(urs,text="BACK",command=del_urs).pack()

def del_urs():
    urs.destroy()

#login screen
    
def login():
    global ls
    ls=Toplevel(sec)
    ls.title("LOGIN")
    ls.geometry("300x250+500+200")
    Label(ls,text="LOGIN AS").pack()
    Button(ls,text="USER",command=ulog).pack()
    Button(ls,text="ADMIN",command=adlog).pack()
    Button(ls,text="DON'T HAVE AN ACCOUNT REGISTER",relief=FLAT,command=register,fg="red").pack()
    Button(ls,text="BACK",command=del_ls).pack()

def del_ls():
    ls.destroy()

#user login screen
    
def ulog():
    global uls
    uls=Toplevel(sec)
    uls.title("USER LOGIN")
    uls.geometry("300x250+500+200")
    global user_verify
    global pwd_verify
    user_verify = StringVar()
    pwd_verify = StringVar()
    global user_log_entry
    global pwd_log_entry
    Label(uls,text="USERNAME").pack()
    user_log_entry=Entry(uls,textvariable=user_verify)
    user_log_entry.pack()
    Label(uls,text="PASSWORD").pack()
    pwd_log_entry=Entry(uls,textvariable=pwd_verify,show="*")
    pwd_log_entry.pack()
    Button(uls,text="LOGIN",width=10,height=1,command=ulog_verify).pack()

#admin login screen
    
def adlog():
    global als
    global admin_verify
    global apwd_verify
    admin_verify=StringVar()
    apwd_verify=StringVar()
    als=Toplevel(sec)
    als.geometry("300x250+500+200")
    Label(als,text="ADMIN NAME").pack()
    Entry(als,textvariable=admin_verify).pack()
    Label(als,text="PASSWORD").pack()
    Entry(als,textvariable=apwd_verify,show="*").pack()
    Button(als,text="LOGIN",command=adlog_verify).pack()


#user registration screen
    
def reg_user():
    global user_info
    global pwd_info
    global add_info
    global ph_info
    global pin_info
    user_info=username.get()
    pwd_info=password.get()
    pwd1_info=passwd.get()
    add_info=address.get()
    pin_info=pin.get()
    ph_info=phno.get()
    cur.execute("select phonenumber from users")
    a=cur.fetchall()
    cur.execute("select cname from users")
    us=cur.fetchall()
    if pwd_info==pwd1_info and (ph_info,) not in a and (user_info,) not in us and len(pwd_info)>=8:
        reg_success()
    elif (ph_info,) in a:
        global pe
        pe=Toplevel(sec)
        pe.geometry("+500+200")
        pe.title("PHONE NUMBER ALREADY EXISTS")
        Label(pe,text="PHONE NUMBER ALREADY EXISTS \n DO YOU WANT TO LOGIN").pack()
        Button(pe,text="LOGIN",command=del_pe).pack()
        Button(pe,text="BACK",command=del_pe).pack()
    elif (user_info,) in us:
        global ue
        ue=Toplevel(sec)
        ue.geometry("+500+200")
        ue.title("USER NAME TAKEN")
        Label(ue,text="USERNAME ALREADY EXISTS \n LOG IN").pack()
        Button(ue,text="LOGIN",command=del_ue).pack()
        Button(ue,text="TRY AGAIN",command=del_ue).pack()
    elif len(pwd_info)<8:
        global pl
        pl=Toplevel(sec)
        pl.geometry("+500+200")
        pl.title("PASSWORD ERROR SCREEN")
        Label(pl,text="PASSWORD IS TOO WEAK TRY AGAIN WITH PASSWORD LENGHT MORE THAN 8").pack()
        Button(pl,text="TRY AGAIN",command=del_pl).pack()
    elif len(str(ph_info))<10 or len(str(ph_info))>10:
        global phl
        phl=Toplevel(sec)
        phl.geometry("+500+200")
        phl.title("PHONE NUMBER LENGHT ERROR")
        Label(phl,text="PLEASE ENTER YOUR PHONE NUMBER CORRECTLY").pack()
        Button(phl,text="TRY AGAIN",command=del_phl).pack()
    elif len(str(pin_info))<6 or len(str(pin_info))>6:
        global pie
        pie=Toplevel(sec)
        pie.geometry("+500+200")
        Label(pie,text="PLEASE CHECK YOUR PIN CODE").pack()
        Button(pie,text="TRY AGAIN",command=del_pie).pack()
    else:
        reg_not_success()
    
def del_pe():
    pe.destroy()

def del_phl():
    phl.destroy()

def del_pie():
    pie.destroy()
    
def del_ue():
    ue.destroy()

def del_pl():
    pl.destroy()
    
def reg_success():
    urs.destroy()
    global rgss
    rgss=Toplevel(sec)
    rgss.geometry("+500+200")
    rgss.title("REGISTRATION SUCCESS")
    cur.execute("select curdate()")
    da=cur.fetchall()
    cur.execute("insert into users(cname,password,address,pincode,phonenumber,date) values('{}','{}','{}',{},{},'{}')".format(user_info,pwd_info,add_info,pin_info,ph_info,da[0][0]))
    mc.commit()
    Label(rgss,text="SUCCESSFULLY REGISTERED").pack()
    Button(rgss,text="BACK",command=del_rgss).pack()

def del_rgss():
    rgss.destroy()

def reg_not_success():
    global reg
    reg=Toplevel(sec)
    reg.geometry("+500+200")
    reg.title("NOT REGISTERED")
    Label(reg,text="YOUR PASSWORD DOESN'T MATCH PLEASE TRY AGAIN").pack()
    Button(reg,text="TRY AGAIN",command=del_reg).pack()

def del_reg():
    reg.destroy()

#user login verify commands
    
def ulog_verify():
    global username1
    global password1
    cur.execute("select cname from users")
    details=cur.fetchall()
    username1=user_verify.get()
    password1=pwd_verify.get()
    cur.execute("select password from users")
    details1=cur.fetchall()
    if (username1,) in details and (password1,) in details1:
        ulog_suc()
    elif (username1,) in details and (password1,) not in details1:
        global pnrs
        pnrs=Toplevel(sec)
        pnrs.title("PASSWORD NOT RECOGNISED")
        Label(pnrs,text="YOUR PASSWORD IS INCORRECT").pack()
        Button(pnrs,text="TRY AGAIN",command=del_pnrs).pack()
    elif (username1,) not in details and (password1,) in details1:
        global unrs
        unrs=Toplevel(sec)
        unrs.title("USER NOT RECOGNISED")
        Label(unrs,text="USERNAME NOT FOUND").pack()
        Button(unrs,text="TRY AGAIN",command=del_unrs).pack()
    else:
        global insc
        insc=Toplevel(sec)
        insc.title("INVALID")
        Label(insc,text="USERNAME AND PASSWORD ARE INVALID").pack()
        Button(insc,text="TRY AGAIN",command=del_insc).pack()
        
def del_pnrs():
    pnrs.destroy()

def del_unrs():
    unrs.destroy()

def del_insc():
    insc.destroy()

#admin login verify commands
    
def adlog_verify():
    global lvs
    cur.execute("select name from admin" )
    ad=cur.fetchall()
    cur.execute("select pwd from admin")
    adpass=cur.fetchall()
    if (admin_verify.get(),) in ad and (apwd_verify.get(),) in adpass:
        adlog_suc()
    elif (admin_verify.get(),) not in ad and (apwd_verify.get(),) in adpass:
        lvs=Toplevel(sec)
        Label(lvs,text="ADMIN NAME INVALID").pack()
        Button(lvs,text="TRY AGAIN",command=del_lvs).pack()
    elif (admin_verify.get(),) in ad and (apwd_verify.get(),) not in adpass:
        lvs=Toplevel(sec)
        Label(lvs,text="PASSWORD INVALID").pack()
        Button(lvs,text="TRY AGAIN",command=del_lvs).pack()
    else:
        lvs=Toplevel(sec)
        Label(lvs,text="ADMIN NAME AND PASSWORD INVALID").pack()
        Button(lvs,text="TRY AGAIN",command=del_lvs).pack()

def del_lvs():
    lvs.destroy()

#admin main screen
    
def adlog_suc():
    global ads
    global hp
    global sp
    global adh
    global adi
    als.destroy()
    ls.destroy()
    ads=Toplevel(sec)
    ads.title("ADMIN SCREEN")
    ads.geometry("2000x2500")
    Label(ads,text="eFOOD CART",font=("Forte",22),fg="red",bg="green").pack(fill=X)
    pho=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp=pho.subsample(6)
    pho4=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp=pho4.subsample(15)
    b1=Button(ads,image=sp,bg="green",relief=FLAT,command=setad)
    b1.image=sp
    b1.place(x=1240,y=0)
    b2=Button(ads,image=hp,bg="green",relief=FLAT,)
    b2.image=hp
    b2.place(x=0,y=0)
    pho2=PhotoImage(file=r"D:\Srinath\csc proj\adhotel.png")
    adh=pho2.subsample(2,2)
    Label(ads,text="MODIFY",font=("Times",22,"bold"),bg="white").place(x=585,y=200)
    b2=Button(ads,text=" HOTELS ",image=adh,compound=LEFT,command=hs,height=200,width=470,bg="white",font=("Verdana",17),relief=FLAT)
    b2.image=adh
    b2.place(x=100,y=300)
    pho3=PhotoImage(file=r"D:\Srinath\csc proj\aditems.png")
    adi=pho3.subsample(4,2)
    b3=Button(ads,text=" ITEMS ",image=adi,compound=LEFT,height=200,width=430,font=("Verdana",17),bg="white",command=Is,relief=FLAT)
    b3.image=adi
    b3.place(x=700,y=300)
    ads.config(bg="white")

def setad():
    global adsets
    adsets=Toplevel(sec)
    adsets.geometry("350x260+920+0")
    adsets.title("settings")
    Button(adsets,text="VIEW APP STATS",command=sh_stat,height=5,width=100).pack()
    Button(adsets,text="CHANGE PASSWORD",height=5,width=100,command=ch_pass).pack()
    Button(adsets,text="LOG OUT",command=log_out,height=5,width=100).pack()

def sh_stat():
    global shs
    global fig
    shs=Toplevel(sec)
    statlst=[]
    labels =["Total orders","Recent orders","Total users","New users","Total partners","New partners"]
    cur.execute("select count(items) from orders")
    l=cur.fetchall()
    statlst.append(l[0][0])
    cur.execute("select month(curdate())")
    d=cur.fetchall()
    cur.execute("select count(items) from orders where month(date)=%s",d[0])
    l1=cur.fetchall()
    statlst.append(l1[0][0])
    cur.execute("select count(cname) from users")
    l2=cur.fetchall()
    statlst.append(l2[0][0])
    cur.execute("select count(cname) from users where month(date)=%s",d[0])
    l3=cur.fetchall()
    statlst.append(l3[0][0])
    cur.execute("select count(hid) from hotels")
    l4=cur.fetchall()
    statlst.append(l4[0][0])
    cur.execute("select count(hid) from hotels where month(date)=%s",d[0])
    l5=cur.fetchall()
    statlst.append(l5[0][0])
    fig1, ax1 = plt.subplots()
    ax1.pie(statlst, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    fig = matplotlib.figure.Figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.pie(statlst)
    ax.legend(statlst)
    circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
    ax.add_artist(circle) 
    canvas = FigureCanvasTkAgg(fig1, master=shs)
    canvas.get_tk_widget().pack()
    canvas.draw()
   


def hs():
    global adhp
    global hs
    global mp
    global hp
    global sp
    global rmhp
    ads.destroy()
    hs=Toplevel(sec)
    hs.geometry("1920x1080")
    ig4=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp=ig4.subsample(9)
    ig5=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp=ig5.subsample(15)
    Label(hs,text="eFOOD CART",font=("Forte",22),fg="red",bg="white").pack()
    Button(hs,image=sp,bg="white",relief=FLAT).place(x=1240,y=0)
    Button(hs,image=hp,bg="white",relief=FLAT).place(x=0,y=0)
    hs.title("HOTEL MODIFY SCREEN")
    ig=PhotoImage(file=r"D:\Srinath\csc proj\add hotel.png")
    adhp=ig.subsample(12)
    ig2=PhotoImage(file=r"D:\Srinath\csc proj\mod.png")
    mp=ig2.subsample(2)
    ig3=PhotoImage(file=r"D:\Srinath\csc proj\remove hotel.png")
    rmhp=ig3.subsample(1)
    Button(hs,text="VIEW HOTELS",height=3,width=15,command=viewhotels,bg="white").place(x=100,y=20)
    Button(hs,text="ADD A HOTEL",image=adhp,compound=LEFT,font=("Verdana",22),bg="white",command=addhotel).place(x=0,y=300)
    Button(hs,text="UPDATE A HOTEL",image=mp,compound=LEFT,height=170,font=("Verdana",22),bg="white",command=updatehotel).place(x=420,y=300)
    Button(hs,text="REMOVE HOTEL",image=rmhp,compound=LEFT,height=170,font=("Verdana",22),command=del_hotel,bg="white").place(x=800,y=300)
    hs.config(bg="white")


def addhotel():
    adhs=Toplevel(sec)
    global hn_var
    global pass_var
    global hpin_var
    global hadd_var
    global cpass_var
    global hph_var
    hn_var=StringVar()
    pass_var=StringVar()
    hpin_var=IntVar()
    cpass_var=StringVar()
    hadd_var=StringVar()
    hph_var=IntVar()
    adhs.title("ADD HOTELS SCREEN")
    adhs.geometry("400x350+20+200")
    Label(adhs,text="HOTEL NAME").place(x=170,y=20)
    Entry(adhs,textvariable=hn_var).place(x=150,y=40)
    Label(adhs,text="ADDRESS").place(x=180,y=60)
    Entry(adhs,textvariable=hadd_var).place(x=150,y=80)
    Label(adhs,text="PIN CODE").place(x=180,y=100)
    Entry(adhs,textvariable=hpin_var).place(x=150,y=120)
    Label(adhs,text="PHONE NUMBER").place(x=155,y=140)
    Entry(adhs,textvariable=hph_var).place(x=150,y=160)
    Button(adhs,text="REGISTER",command=reg_hotel).place(x=200,y=200)
    Button(adhs,text="BACK",command=lambda:adhs.destroy()).place(x=200,y=230)

def reg_hotel():
    global rhs
    rhs=Toplevel(sec)
    rhs.title("REGISTATION SUCCESSFUL")
    rhs.geometry("400x350")
    hn_get=hn_var.get()
    pass_get=pass_var.get()
    hpin_get=hpin_var.get()
    hadd_get=hadd_var.get()
    hph_get=hph_var.get()
    cpass_get=cpass_var.get()
    hid=""
    for i in range(0,2):
        hid+=hn_get[i].upper()
    hid+=str(random.randint(100,999))
    cur.execute("select curdate()")
    da=cur.fetchall()
    cur.execute("insert into hotels(hid,hotel,address,pincode,phonenumber,date) values('{}','{}','{}',{},{},'{}')".format(hid,hn_get,hadd_get,hpin_get,hph_get,da[0][0]))
    mc.commit()
    Label(rhs,text=hid,bg="yellow").place(x=200,y=40)
    Label(rhs,text="THIS IS THE HOTELS'S ID").place(x=130,y=70)
    Button(rhs,text="BACK",command=lambda:rhs.destroy()).place(x=150,y=100)

def updatehotel():
    global uhs
    global change_var
    uhs=Toplevel(sec)
    uhs.title("UPDATE INFORMATION")
    uhs.geometry("400x350+420+200")
    global change_var
    change_var=IntVar()
    Label(uhs,text="CHOOSE WHAT DO YOU WANT TO UPDATE").place(x=110,y=20)
    Radiobutton(uhs,text="HOTEL NAME",variable=change_var,command=divert_screen,value=1).place(x=150,y=100)
    Radiobutton(uhs,text="ADDRESS",variable=change_var,command=divert_screen,value=2).place(x=150,y=150)
    Radiobutton(uhs,text="PINCODE",variable=change_var,command=divert_screen,value=3).place(x=150,y=200)
    Radiobutton(uhs,text="PHONE NUMBER",variable=change_var,command=divert_screen,value=4).place(x=150,y=250)
    Button(uhs,text="BACK",command=lambda:uhs.destroy()).place(x=200,y=280)

def divert_screen():
    uhs.destroy()
    global hncs
    global pics
    global phcs
    global apcs
    global hnn_change
    global hne_var
    global hne_var1
    global hno_change
    global phno_change
    global phn_change
    global pincode_change
    global pino_change
    global address_change
    global addo_change
    hne_var=StringVar()
    hne_var1=StringVar()
    hnn_change=StringVar()
    hno_change=StringVar()
    address_change=StringVar()
    addo_change=StringVar()
    phn_change=IntVar()
    hno_change=StringVar()
    pino_change=IntVar()
    pincode_change=IntVar()
    if change_var.get()==1:
        hncs=Toplevel(sec)
        hncs.title("HOTEL NAME CHANGE")
        hncs.geometry("500x450")
        Label(hncs,text="ENTER OLD HOTEL NAME").place(x=110,y=40)
        Entry(hncs,textvariable=hno_change).place(x=110,y=60)
        Label(hncs,text="ENTER NEW HOTEL NAME").place(x=110,y=120)
        Entry(hncs,textvariable=hnn_change).place(x=110,y=140)
        Button(hncs,text="CHANGE",command=change).place(x=150,y=190)
        Button(hncs,text="BACK",command=lambda:hncs.destroy().place(x=250,y=210))
    elif change_var.get()==4:
        phno_change=IntVar()
        phcs=Toplevel(sec)
        phcs.title("PHONE NUMBER UPDATE")
        phcs.geometry("500x450")
        Label(phcs,text="ENTER OLD PHONE NUMBER").  place(x=150,y=20)
        Entry(phcs,textvariable=phn_change).place(x=110,y=40)
        Label(phcs,text="ENTER NEW PHONE NUMBER").place(x=150,y=60)
        Entry(phcs,textvariable=phno_change).place(x=110,y=80)
        Button(phcs,text="CHANGE",command=change4).place(x=200,y=120)
        Button(phcs,text="BACK",command=lambda:phcs.destroy()).place(x=250,y=150)
    elif change_var.get()==2:
        address_change=StringVar()
        apcs=Toplevel(sec)
        apcs.title("ADDRESS UPDATE")
        apcs.geometry("400x350")
        Label(apcs,text="ENTER YOUR HID").place(x=150,y=20)
        Entry(apcs,textvariable=hne_var).place(x=110,y=40)
        Label(apcs,text="YOUR OLD ADDRESS").place(x=110,y=60)
        Label(apcs,text="ENTER YOUR NEW ADDRESS").place(x=150,y=80)
        Entry(apcs,textvariable=address_change).place(x=110,y=100)    
        Button(apcs,text="CHANGE",command=change2).place(x=200,y=180)
        Button(apcs,text="BACK",command=lambda:apcs.destroy()).place(x=250,y=210)
    elif change_var.get()==3:
        pincode_change=IntVar()
        pics=Toplevel(sec)
        pics.title("PINCODE UPDATE")
        pics.geometry("400x350")
        Label(pics,text="ENTER YOUR HID").place(x=120,y=20)
        Entry(pics,textvariable=hne_var1).place(x=110,y=40)
        Label(pics,text="ENTER YOUR NEW PIN CODE").place(x=150,y=60)
        Entry(pics,textvariable=pincode_change).place(x=110,y=80)
        Button(pics,text="CHANGE",command=change3).place(x=150,y=150)
        Button(pics,text="BACK",command=lambda:pics.destroy()).place(x=250,y=180)

def change():
    global cs
    cur.execute("select hotel from hotels")
    a=cur.fetchall()
    hg=hno_change.get()
    if (hg,) in a:               
        cur.execute("update hotels set hotel='{}' where hotel='{}'".format(hnn_change.get(),hno_change.get()))
        mc.commit()
        hidn=""
        for i in range(0,2):
            hidn+=hnn_change.get()[i].upper()
        hidn+=str(random.randint(100,999))
        cur.execute("update hotels set hid='{}' where hotel='{}'".format(hidn,hnn_change.get()))
        mc.commit()
        cs=Toplevel(sec)
        cs.title("UPDATE SUCCESS")
        Label(cs,text="UPDATED SUCCESSFULLY").pack()
        Label(cs,text="YOUR NEW HOTEL ID IS").pack()
        Label(cs,text=hidn,bg="yellow").pack()
        Button(cs,text="EXIT",command=del_cs).pack()
    else:
        cs=Toplevel(sec)
        cs.title("UPDATE NOT SUCCESS")
        Label(cs,text="NOT UPDATED SUCCESSFULLY").pack()
        Button(cs,text="TRY AGAIN",command=del_cs_1).pack()

def del_cs():
    cs.destroy()
    hncs.destroy()

def del_cs_1():
    cs.destroy()
    
def change3():
    global cs3
    cur.execute("select hid from hotels")
    c=cur.fetchall()
    i=(hne_var1.get(),)
    if i in c:
        cs3=Toplevel(sec)
        cs3.geometry("400x350")
        cur.execute("update hotels set pincode={} where hid='{}'".format(pincode_change.get(),hne_var1.get()))
        mc.commit()
        Label(cs3,text="UPDATED SUCCESFULLY").pack()
        Button(cs3,text="EXIT",command=del_cs3).pack()
    else:
        cs3=Toplevel(sec)
        cs3.geometry("400x350")
        Label(cs3,text="PIN CODE NOT FOUND").pack()
        Button(cs3,text="TRY AGAIN",command=del_cs3_1).pack()

def del_cs3():
    cs3.destroy()
    pics.destroy()
    
def del_cs3_1():
    cs3.destroy()        
            
def change2():
    global cs2
    cur.execute("select hid from hotels")
    g=cur.fetchall()
    h=(hne_var.get(),)
    if h in g:
        cs2=Toplevel(sec)
        cs2.geometry("400x350")
        cur.execute("update hotels set address='{}' where hid='{}'".format(address_change.get(),hne_var.get()))
        mc.commit()
        Label(cs2,text="UPDATED SUCCESFULLY").pack()
        Button(cs2,text="EXIT",command=del_cs2).pack()
    else:
        cs2=Toplevel(sec)
        cs2.geometry("400x350")
        Label(cs2,text="ADDRESS NOT FOUND").pack()
        Button(cs2,text="TRY AGAIN",command=del_cs2_1).pack()

def del_cs2():
    cs2.destroy()
    apcs.destroy()

def del_cs2_1():
    cs2.destroy()
        
        
def change4():
    global cs4
    cur.execute("select phno from hotels")
    e=cur.fetchall()
    d=(phn_change.get(),)
    if d in e:
        cs4=Toplevel(sec)
        cs4.geometry("400x350")
        cur.execute("update hotels set phno={} where phno={}".format(phno_change.get(),phn_change.get()))
        mc.commit()
        Label(cs4,text="UPDATED SUCCESFULLY").pack()
        Button(cs4,text="EXIT",command=del_cs4).pack()
    else:
        cs4=Toplevel(sec)
        cs4.geometry("400x350")
        Label(cs4,text="PHONE NUMBER NOT FOUND").pack()
        Button(cs4,text="TRY AGAIN",command=del_cs4_1).pack()

def del_cs4():
    cs4.destroy()
    phcs.destroy()
    
def del_cs4_1():
    cs4.destroy()

def del_hotel():
    global dls
    dls=Toplevel(sec)
    global delhotel
    delhotel=IntVar()
    dls.title("REMOVE SCREEN")
    cur.execute("select hotel from hotels")
    dh=cur.fetchall()
    dhc=1
    for i in dh:
        Radiobutton(dls,text=i[0],variable=delhotel,value=dhc,command=rem).pack()
        dhc+=1
    Button(dls,text="BACK",command=lambda:dls.destroy()).pack()

def rem():
    global rms
    rms=Toplevel(sec)
    rms.geometry("400x350")
    rms.title("GOODBYE SCREEN")
    cur.execute("select hotel from hotels")
    hona1=cur.fetchall()
    for i in hona1:
        if hona1.index(i)==delhotel.get()-1:
            cur.execute("delete from hotels where hotel=%s",i)
            mc.commit()
    Label(rms,text="YOUR HOTEL HAS BEEN REMOVED SUCCESSFULLY").pack()
    Button(rms,text="EXIT",command=del_rms1).pack()
   

def del_rms():
    rms.destroy()

def del_rms1():
    rms.destroy()
    dls.destroy()

def Is():
    global Is
    global adit
    global mop
    global rmip
    global hp
    global sp
    ads.destroy()
    Is1=Toplevel(sec)
    Is1.geometry("1920x1080")
    Is1.title("ITEMS MODIFICATION")
    im4=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp=im4.subsample(9)
    im5=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp=im5.subsample(15)
    Button(Is1,image=sp,bg="white",relief=FLAT).place(x=1240,y=0)
    Button(Is1,image=hp,bg="white",relief=FLAT).place(x=0,y=0)
    im=PhotoImage(file=r"D:\Srinath\csc proj\add item.png")
    adit=im.subsample(5)
    im2=PhotoImage(file=r"D:\Srinath\csc proj\mod.png")
    mop=im2.subsample(2)
    im3=PhotoImage(file=r"D:\Srinath\csc proj\remove hotel.png")
    rmip=im3.subsample(1)
    Label(Is1,text="eFOOD CART",font=("Forte",22),fg="red",bg="white").pack()
    #Button(Is,text="VIEW ITEMS IN HOTEL",height=3,width=15,command=view_items).place(x=100,y=20)
    Button(Is1,text="ADD AN ITEM",image=adit,compound=LEFT,font=("Verdana",22),bg="white",height=170,command=additem).place(x=0,y=300)
    Button(Is1,text="UPDATE AN ITEM",image=mop,compound=LEFT,height=170,font=("Verdana",22),bg="white",command=updateitem).place(x=420,y=300)
    Button(Is1,text="REMOVE A ITEM",image=rmip,compound=LEFT,height=170,font=("Verdana",22),command=del_item,bg="white").place(x=800,y=300)
    Is1.config(bg="white")

def additem():
    global adis
    adis=Toplevel(sec)
    global hid_var
    global item_var
    global cat_var
    global pr_var
    hid_var=StringVar()
    item_var=StringVar()
    cat_var=StringVar()
    pr_var=IntVar()
    Label(adis,text="eFOOD CART",font=("Forte",22),fg="red").pack()
    adis.title("ADD ITEMS SCREEN")
    adis.geometry("400x350+20+200")
    Label(adis,text="HOTEL ID").pack()
    Entry(adis,textvariable=hid_var).pack()
    Label(adis,text="ITEM").pack()
    Entry(adis,textvariable=item_var).pack()
    Label(adis,text="CATEGORY").pack()
    catchoosen=Combobox(adis,width=20,textvariable=cat_var)
    catchoosen['values']=("breakfast","lunch","dinner","chats","drinks","dessert","conti")
    catchoosen.pack()
    catchoosen.current()
    Label(adis,text="PRICE").pack()     
    Entry(adis,textvariable=pr_var).pack()
    Button(adis,text="ADD",command=add_item).pack()
    Button(adis,text="VIEW HOTEL ID's",command=view_ids).place(x=5,y=10)
    Button(adis,text="BACK",command=lambda:adis.destroy()).pack()

def add_item():
    global ias
    ias=Toplevel(sec)
    ias.title("ITEM SUCCESSFUL")
    ias.geometry("400x350")
    hid_get=hid_var.get()
    item_get=item_var.get()
    Label(ias,text="eFOOD CART",font=("Forte",22),fg="red").pack(fill=X)
    cat_get=cat_var.get()
    pr_get=pr_var.get()
    cur.execute("select itemcode from foods where hid=%s",(hid_get,))
    itc=cur.fetchall()
    try:
        reitc=itc[-1][-1]
        if reitc%100<10:
            itc_c=reitc%100+1
            itc_var=hid_get[2:]+str(0)+str(itc_c)
        else:
            itc_c=reitc%100+1
            itc_var=hid_get[2:]+str(itc_c)
    except:
        itc_var=hid_get[2:]+"01"        
    Label(ias,text="Your Added Item Code is:").place(x=160,y=40)
    Label(ias,text=itc_var).place(x=160,y=60)
    cur.execute("insert into foods(hid,item,itemcode,category,price) values('{}','{}',{},'{}',{})".format(hid_get,item_get,itc_var,cat_get,pr_get))
    mc.commit()
    Button(ias,text="BACK",command=del_ias).place(x=150,y=100)
    


def view_ids():
    global shids
    cur.execute("select hid,hotel from hotels")
    honaid=cur.fetchall()
    shids=Toplevel(sec)
    shids.geometry("350x300")
    Label(shids,text="eFOOD CART",font=("Forte",22),fg="red").pack()
    Label(shids,text="HID:").place(x=40,y=60)
    Label(shids,text="HOTELNAME:").place(x=100,y=60)
    x=40
    x1=100
    y=80
    for i  in honaid:
        Label(shids,text=i[0]).place(x=x,y=y)
        Label(shids,text=i[1]).place(x=x1,y=y)
        y+=20
    Button(shids,text="BACK",command=del_shids).place(x=150,y=y+30)

def del_shids():
    shids.destroy()


def del_ias():
    adis.destroy()
    ias.destroy()

def updateitem():
    global uis
    global change_var
    uis=Toplevel(sec)
    uis.title("UPDATE INFORMATION")
    uis.geometry("400x350+380+200")
    change_var=IntVar()
    Label(uis,text="CHOOSE WHAT DO YOU WANT TO UPDATE").place(x=110,y=20)
    Radiobutton(uis,text="ITEM NAME",variable=change_var,command=update_screen,value=1).place(x=150,y=100)
    Radiobutton(uis,text="CATEGORY",variable=change_var,command=update_screen,value=2).place(x=150,y=200)
    Radiobutton(uis,text="PRICE",variable=change_var,command=update_screen,value=3).place(x=150,y=250)
    Button(uis,text="BACK",command=lambda:uis.destroy()).place(x=200,y=280)

def update_screen():
    uis.destroy()
    global incs
    global iccs
    global prcs
    global ctcs
    global inn_change
    global ino_change
    global ico_change
    global icn_change
    global cato_change
    global catn_change
    global prn_change
    global pro_change
    global itc_var
    global itc_var2
    global itc_var3
    itc_var3=IntVar()
    itc_var2=IntVar()
    itc_var=IntVar()
    inn_change=StringVar()
    ino_change=StringVar()
    pro_change=IntVar()
    prn_change=IntVar()
    icn_change=IntVar()
    ico_change=IntVar()
    cato_change=StringVar()
    catn_change=StringVar()
    if change_var.get()==1:
        incs=Toplevel(sec)
        incs.title("ITEM NAME CHANGE")
        incs.geometry("500x450")
        Label(incs,text="ENTER ITEMCODE").place(x=150,y=20)
        Entry(incs,textvariable=itc_var3).place(x=110,y=40)
        Label(incs,text="ENTER OLD ITEM NAME").place(x=110,y=60)
        Entry(incs,textvariable=ino_change).place(x=110,y=80)
        Label(incs,text="ENTER NEW ITEM NAME").place(x=110,y=100)
        Entry(incs,textvariable=inn_change).place(x=110,y=120)
        Button(incs,text="CHANGE",command=change5).place(x=150,y=190)
        Button(incs,text="BACK",command=lambda:incs.destroy()).place(x=200,y=220)
    elif change_var.get()==3:
        prcs=Toplevel(sec)
        prcs.title("PRICE UPDATE")
        Label(prcs,text="ENTER ITEMCODE").place(x=150,y=20)
        Entry(prcs,textvariable=itc_var).place(x=110,y=40)
        Label(prcs,text="ENTER OLD PRICE").place(x=150,y=60)
        Entry(prcs,textvariable=pro_change).place(x=110,y=80)
        Label(prcs,text="ENTER NEW PRICE").place(x=150,y=100)
        Entry(prcs,textvariable=prn_change).place(x=110,y=120)
        Button(prcs,text="CHANGE",command=change8).place(x=200,y=160)
        Button(prcs,text="BACK",command=lambda:prcs.destroy()).place(x=200,y=190)
    elif change_var.get()==2:
        ctcs=Toplevel(sec)
        ctcs.title("CATEGORY UPDATE")
        ctcs.geometry("400x350")
        Label(ctcs,text="ENTER YOUR ITEM CODE").place(x=150,y=20)
        Entry(ctcs,textvariable=itc_var2).place(x=110,y=40)
        Label(ctcs,text="ENTER YOUR OLD CATEGORY").place(x=150,y=60)
        Entry(ctcs,textvariable=cato_change).place(x=110,y=80)
        Label(ctcs,text="ENTER YOUR NEW CATEGORY").place(x=150,y=100)
        Entry(ctcs,textvariable=catn_change).place(x=110,y=120)
        Button(ctcs,text="CHANGE",command=change7).place(x=150,y=160)
        Button(ctcs,text="BACK",command=lambda:ctcs.destroy()).place(x=200,y=190)

def change5():
    global change
    cur.execute("select itemcode from foods")
    a=cur.fetchall()
    if (itc_var3.get(),) in a:               
        cur.execute("update foods set item=%s where itemcode=%s",(inn_change.get(),itc_var3.get()))
        mc.commit()
        change=Toplevel(sec)
        change.title("UPDATE SUCCESS")
        Label(change,text="UPDATED SUCCESSFULLY").pack()
        Button(change,text="EXIT",command=del_change).pack()
    else:
        change=Toplevel(sec)
        change.title("UPDATE NOT SUCCESS")
        Label(change,text="NOT UPDATED SUCCESSFULLY").pack()
        Button(change,text="TRY AGAIN",command=del_change_1).pack()

def del_change():
    change.destroy()
    incs.destroy()

def del_change_1():
    change.destroy()
    
def change7():
    global cs7
    cur.execute("select itemcode from foods")
    k=cur.fetchall()
    if (itc_var2.get(),) in k:
        cs7=Toplevel(sec)
        cs7.geometry("400x350")
        cur.execute("update foods set category=%s where itemcode=%s",(catn_change.get(),itc_var2.get()))
        mc.commit()
        Label(cs3,text="UPDATED SUCCESFULLY").pack()
        Button(cs3,text="EXIT",command=del_cs7).pack()
    else:
        cs7=Toplevel(sec)
        cs7.geometry("400x350")
        Label(cs7,text="ITEM CODE NOT FOUND").pack()
        Button(cs7,text="TRY AGAIN",command=del_cs7_1).pack()

def del_cs7():
    cs7.destroy()
    ctcs.destroy()
    
def del_cs7_1():
    cs7.destroy()                
        
def change8():
    global cs8
    cur.execute("select itemcode from foods")
    m=cur.fetchall()
    if (itc_var.get(),) in m:
        cs8=Toplevel(sec)
        cs8.geometry("400x350")
        Label(cs8,text="after commit11").pack() 
        cur.execute("update foods set price=%s where itemcode=%s",(prn_change.get(),itc_var.get()))
        mc.commit()
        Label(cs8,text="UPDATED SUCCESFULLY").pack()
        Button(cs8,text="EXIT",command=del_cs8).pack()
    else:
        cs8=Toplevel(sec)
        cs8.geometry("400x350")
        Label(cs8,text="ITEM CODE NOT FOUND").pack()
        Label(cs8,text=itc_var.get()).pack()
        Label(cs8,text=len(itc_var.get())).pack()
        Button(cs8,text="TRY AGAIN",command=del_cs8_1).pack()

def del_cs8():
    cs8.destroy()
    prcs.destroy()
    
def del_cs8_1():
    cs8.destroy()

def del_item():
    global dis
    dis=Toplevel(sec)
    global sel_hotel
    sel_hotel=IntVar()
    dis.title("REMOVE SCREEN")
    cur.execute("select hotel from hotels")
    hona1=cur.fetchall()    
    Label(dis,text="SELECT THE HOTEL FROM WHICH YOU WANT TO REMOVE ITEM").pack()
    selhc=1
    for i in hona1:
        Radiobutton(dis,text=i[0],variable=sel_hotel,value=selhc,command=remove_item).pack()
        selhc+=1


def remove_item():
    global itemslst
    dis.destroy()
    global ris
    global del_item
    del_item=IntVar()
    ris=Toplevel(sec)
    cur.execute("select hotel from hotels")
    hona1=cur.fetchall()  
    for j in hona1:
        if hona1.index(j)==sel_hotel.get()-1:
            cur.execute("select hid from hotels where hotel=%s",j)
            hidlst=cur.fetchall()
            cur.execute("select item from foods where hid=%s",(hidlst[0]))
            itemslst=cur.fetchall()
            dic=1
            for k in itemslst:
                Radiobutton(ris,text=k[0],variable=del_item,value=dic,command=remove_item1).pack()            
                dic+=1
    Button(ris,text="BACK",command=lambda:ris.destroy()).pack()



def remove_item1():
    global rmi
    rmi=Toplevel(sec)
    rmi.geometry("400x350")
    rmi.title("GOODBYE SCREEN")
    for i in itemslst:
        if itemslst.index(i)==del_item.get()-1:
            cur.execute("delete from foods where itemcode=%s",i)
            mc.commit()
    Label(rmi,text="YOUR ITEM HAS BEEN REMOVED SUCCESSFULLY").pack()
    Button(rmi,text="EXIT",command=del_rmi1).pack()
   

def del_rmi():
    rmi.destroy()

def del_rmi1():
    rmi.destroy()
    dis.destroy()

def view_items():
    global vis
    cur.execute("select item from foods")
    p=cur.fetchall()
    vis=Toplevel(sec)
    vis.title("view hotels")
    for q in p:
        Label(vis,text=q).pack()
    Button(vis,text="BACK",command=del_vis).pack()

def del_vis():
    vis.destroy()

#main screen view hotels
    
def viewhotels():
    global vhs
    vhs=Toplevel(sec)
    vhs.geometry("400x250")
    vhs.title("VIEW HOTELS")
    cur.execute("select hotel from hotels")
    h=cur.fetchall()
    for k in h:
        Label(vhs,text=k[0]).pack()
    Button(vhs,text="BACK",command=del_vhs).pack()

def del_vhs():
    vhs.destroy()

#user setting screen
def settings():
    global sets
    sets=Toplevel(sec)
    sets.geometry("350x350+920+0")
    sets.title("settings")
    #give commands
    Button(sets,text="CHANGE USERNAME",command=ch_name,height=5,width=100).pack()
    Button(sets,text="CHANGE ADDRESS",command=ch_add,height=5,width=100).pack()
    Button(sets,text="CHANGE PASSWORD",height=5,width=100,command=ch_pass).pack()
    Button(sets,text="LOG OUT",command=log_out,height=5,width=100).pack()

"""def log_out():
    try:
        myord.destroy()
        sets.destroy()
        cs.destroy()
        ulss.destroy()
    except:
        try:
            bfs.destroy()
            sets.destroy()
            cs.destroy()
            ulss.destroy()
        except:
            try:
                lus.destroy()
                sets.destroy()
                cs.destroy()
                ulss.destroy()
            except:
                try:
                    dis1.destroy()
                    sets.destroy()
                    cs.destroy()
                    ulss.destroy()
                except:
                    try:
                        chs.destroy()
                        sets.destroy()
                        cs.destroy()
                        ulss.destroy()
                    except:
                        try:
                            bes.destroy()
                            sets.destroy()
                            cs.destroy()
                            ulss.destroy()
                        except:
                            try:
                                dess.destroy()
                                sets.destroy()
                                cs.destroy()
                                ulss.destroy()
                            except:
                                try:
                                    conts.destroy()
                                    sets.destroy()
                                    cs.destroy()
                                    ulss.destroy()
                                except:
                                    try:
                                        carts.destroy()
                                        sets.destroy()
                                        cs.destroy()
                                        ulss.destroy()
                                    except:
                                        try:
                                            sets.destroy()
                                            ulss.destroy()
                                        except:
                                            try:
                                                adsets.destroy()
                                                ads.destroy()
                                            except:
                                                try:
                                                    adsets.destroy()
                                                    hs.destroy()
                                                    ads.destroy()
                                                except:
                                                    try:
                                                        adsets.destroy()
                                                        Is1.destroy()
                                                        ads.destroy()
                                                    except:
                                                        cs.destroy()
                                                        sets.destroy()
                                                        ulss.destroy()
                                                        
"""

def ch_name():
    global chna
    global new_name
    new_name=StringVar()
    chna=Toplevel(sec)
    chna.geometry("300x250+500+200")
    Label(chna,text="YOUR CURRENT USERNAME").place(x=105,y=20)
    Label(chna,text=username1,relief="ridge").place(x=90,y=40)
    Label(chna,text="ENTER YOUR NEW USERNAME").place(x=90,y=60)
    Entry(chna,textvariable=new_name).place(x=95,y=80)
    Button(chna,text="BACK",command=del_chna).place(x=135,y=220)
    Button(chna,text="CHANGE",command=change11).place(x=130,y=180)    

def ch_add():
    global chad
    global new_uad
    new_uad=StringVar()
    chad=Toplevel(sec)
    chad.geometry("300x250+500+200")
    Label(chad,text="YOUR CURRENT ADDRESS").place(x=105,y=20)
    cur.execute("select address from users where cname=%s",(username1,))
    uad=cur.fetchall()
    Label(chad,text=uad[0][0],relief="ridge").place(x=85,y=60)
    Label(chad,text="ENTER YOUR NEW ADDRESS").place(x=90,y=100)
    Entry(chad,textvariable=new_uad).place(x=95,y=140)
    Button(chad,text="CHANGE",command=change9).place(x=130,y=180)
    Button(chad,text="BACK",command=del_chad).place(x=135,y=220)

def ch_pass():
    global chps
    global new_key
    global old_key
    new_key=StringVar()
    old_key=StringVar()
    chps=Toplevel(sec)
    chps.geometry("300x250+500+200")
    Label(chps,text="ENTER YOUR OLD PASSWORD").place(x=90,y=20)
    Entry(chps,textvariable=old_key,show="*").place(x=95,y=60)
    Label(chps,text="ENTER YOUR NEW PASSWORD").place(x=90,y=100)
    Entry(chps,textvariable=new_key,show="*").place(x=95,y=140)
    Button(chps,text="CHANGE",command=change10).place(x=130,y=180)
    Button(chps,text="BACK",command=del_chps).place(x=135,y=220)

def change9():
    cur.execute("update users set address=%s where cname=%s",(new_uad.get(),username1))
    mc.commit()
    global cs9
    cs9=Toplevel(sec)
    cs9.geometry("+500+100")
    Label(cs9,text="SUCCESSFULLY UPDATED").pack()

def change11():
    cur.execute("update users set cname=%s where cname=%s",(new_name,username1))
    mc.commit()
    global cs11
    cs11=Toplevel(sec)
    cs11.geometry("+500+100")
    Label(cs11,text="SUCCESSFULLY UPDATED").pack()

def del_chna():
    chna.destroy()


def del_chad():
    chad.destroy()  

def del_chps():
    chps.destroy()

def change10():
    global cs10
    cs10=Toplevel(sec)
    cs10.geometry("+500+100")
    try:
        cur.execute("select password from users where cname=%s",(username1,))
        ukey=cur.fetchall()
        if old_key.get() == ukey[0][0]:
            cur.execute("update users set password=%s where cname=%s",(new_key.get(),username1))
            mc.commit()
            Label(cs10,text="SUCCESSFULLY UPDATED").pack()
            Button(cs10,text="BACK",command=del_cs10_0).pack()
        else:
            Label(cs10,text="YOUR OLD PASSWORD IS WRONG PLEASE TRY AGAIN").pack()
            Button(cs10,text="TRY AGAIN",command=del_cs10).pack()
    except:
        cur.execute("select password from admin where adminname=%s",(admin_verify.get(),))
        akey=cur.fetchall()
        if old_key.get() == akey[0][0]:
            cur.execute("update admin set password=%s where adminname=%s",(new_key.get(),admin_verify.get()))
            mc.commit()
            Label(cs10,text="SUCCESSFULLY UPDATED").pack()
            Button(cs10,text="BACK",command=del_cs10_0).pack()
        else:
            Label(cs10,text="YOUR OLD PASSWORD IS WRONG PLEASE TRY AGAIN").pack()
            Button(cs10,text="TRY AGAIN",command=del_cs10).pack()

def del_cs10():
    cs10.destroy()

def del_cs10_0():
    cs10.destroy()
    chps.destroy()
    
def bfast():
    global bfs
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global cp2
    global hp2
    global sp2
    global hotelname
    bfs=Toplevel(sec)
    bfs.geometry("2000x2500")
    Label(bfs,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp2=imge.subsample(6)
    Button(bfs,image=hp2,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp2=imge1.subsample(15)
    Button(bfs,image=sp2,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp2=imge2.subsample(8)
    Button(bfs,image=cp2,bg="green",activebackground="red",relief=FLAT,command=cartpage).place(x=1185,y=2)
    Label(bfs,text="ITEM",bg="white",font=("Verdana",22)).place(x=20,y=60)
    Label(bfs,text="QUANTITY",bg="white",font=("Verdana",22)).place(x=180,y=60)
    Label(bfs,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=380,y=60)
    Button(bfs,text="BACK PAGE",font=("Verdana",19),command=lambda:bfs.destroy()).place(x=15,y=630)
    bfs.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()==hona.index(j)+1:
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where category='{}' and hid='{}'".format("breakfast",hotelid[0][0]))
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(bfs,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(bfs,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=180,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"breakfast"))
            items1=cur.fetchall()
            for k in items1:
                Label(bfs,text="Rs."+str(k[0]),bg="white",font=("Verdana",22)).place(x=380,y=yaxis1)
                yaxis1+=45
    Button(bfs,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)


def des():
    global dess
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global cp7
    global hp7
    global sp7
    global hotelname
    dess=Toplevel(sec)
    dess.geometry("2000x2500")
    Label(dess,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp7=imge.subsample(6)
    Button(dess,image=hp7,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp7=imge1.subsample(15)
    Button(dess,image=sp7,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp7=imge2.subsample(8)
    Button(dess,image=cp7,bg="green",activebackground="red",command=cartpage,relief=FLAT).place(x=1185,y=2)
    Label(dess,text="ITEM",bg="white",font=("Verdana",22)).place(x=20,y=60)
    Label(dess,text="QUANTITY",bg="white",font=("Verdana",22)).place(x=300,y=60)
    Label(dess,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=500,y=60)
    Button(dess,text="BACK PAGE",font=("Verdana",19),command=lambda:dess.destroy()).place(x=15,y=630)
    dess.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()-1==hona.index(j):
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where category='{}' and hid='{}'".format("dessert",hotelid[0][0]))
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(dess,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(dess,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=300,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"dessert"))
            items1=cur.fetchall()
            for k in items1:
                Label(dess,text="Rs."+str(k[0]),bg="white",font=("Verdana",22)).place(x=500,y=yaxis1)
                yaxis1+=45
    Button(dess,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)

def cart():
    global cartlst
    global price
    try:
        cartlst,price
    except:
        cartlst={}
        price=0
    for v in chckval.keys():
        if chckval[v].get()==True and v in chckval2.keys() and  chckval1[v].get()>0:
            var=items1[items.index(v)]
            for smtg in var:
                price+=smtg*chckval1[v].get()
            cartlst[v[0]]=[chckval1[v].get(),smtg,hotelname]
            notification.notify(title='FOOD DELIVER APP',message='ADDED TO CART SUCCESSFULLY',app_icon=r'D:\Srinath\csc proj\mohan works\download.ico',timeout=10)
    
def cartpage():
    global carts
    global hp8
    global sp8
    try:
        price
    except:
        price=150
    carts=Toplevel(sec)
    carts.geometry("2000x2500")
    carts.title("CART")
    ige=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp8=ige.subsample(6)
    ige2=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp8=ige2.subsample(15)
    Label(carts,text="eFOOD CART",font=("Forte",22),fg="red",bg="green").pack(fill=X)
    Button(carts,image=sp8,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=0)
    Button(carts,image=hp8,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    Button(carts,text="BACK PAGE",font=("Verdana",19),command=lambda:carts.destroy()).place(x=15,y=630)
    yin=160
    price3=price+price*(15/100)
    
    try:
        if cartlst!={}:
            Label(carts,text="YOUR ITEMS :",font=("Verdana",22),bg="white").place(x=400,y=100)
            Label(carts,text="QTY :",font=("Verdana",22),bg="white").place(x=850,y=100)
            Label(carts,text="RATE :",font=("Verdana",22),bg="white").place(x=1000,y=100)
            Label(carts,text="HOTELNAME :",font=("Verdana",22),bg="white").place(x=15,y=100)
            for i in cartlst.keys():
                Label(carts,text=cartlst[i][2],font=("Verdana",22),bg="white").place(x=15,y=yin)
                Label(carts,text=i,font=("Verdana",22),bg="white").place(x=400,y=yin+7)
                Label(carts,text=cartlst[i][0],font=("Verdana",22),bg="white").place(x=850,y=yin)
                Label(carts,text="Rs."+str(cartlst[i][1]),font=("Verdana",22),bg="white").place(x=1000,y=yin)
                yin+=50
            Label(carts,text="TOTAL PRICE:",font=("Verdana",22),bg="white").place(x=770,y=yin+60)    
            Label(carts,text="Rs."+str(price3),font=("Verdana",22),bg="white").place(x=1000,y=yin+60)
            Label(carts,text="(**Including GST)",font=("Times",19),bg="white").place(x=1000,y=yin+100)  
            Button(carts,text="CLEAR CART",font=("Verdana",15),command=edit).place(x=90,y=yin+60)
            Button(carts,text="PROCEED TO BUY",font=("Verdana",22),command=place_ord1).place(x=200,y=600)
        else:
            pass
    except:
        Label(carts,text="NO ITEMS IN CART",font=("Verdana",22),bg="white").place(x=20,y=100)

    carts.config(bg="white")

def edit():
    global cartlst
    if cartlst=={}:
        pass
    else:
        but=carts.place_slaves()
        for i in but:
            i.destroy()
        Button(carts,image=sp8,bg="white",activebackground="red",relief=FLAT).place(x=1230,y=0)
        Button(carts,image=hp8,bg="white",activebackground="red",relief=FLAT).place(x=0,y=0)
        Label(carts,text="YOUR CART HAS BEEN CLEARED!!",font=("Verdana",22),bg="white").place(x=20,y=100)
        cartlst={}
        price=0
    
def place_ord1():
    global pos
    pos=Toplevel(sec)
    pos.geometry("300x250+500+180")
    cur.execute("select address from users where cname=%s",(username1,))
    ad=cur.fetchall()
    cur.execute("select phonenumber from users where cname=%s",(username1,))
    pn=cur.fetchall()
    Label(pos,text="eFOOD CART",font=("Forte",22),fg="red").pack()
    Label(pos,text=username1,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
    Label(pos,text=ad[0][0],font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
    Label(pos,text=pn,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
    Button(pos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
    Button(pos,text="EDIT",width=12,command=editord).place(x=100,y=230)
    Button(pos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
       
def del_pos():
    pos.destroy()

def editord():
    global eds
    global edna_var
    global edad_var
    global edph_var
    edna_var=IntVar()
    edad_var=IntVar()
    edph_var=IntVar()
    eds=Toplevel(sec)
    eds.geometry("300x250+500+180")
    Label(eds,text="eFOODCART",font=("Forte",22),fg="red").pack()
    Label(eds,text="CHANGE:",font=("Verdana",19)).pack()
    Checkbutton(eds,text="NAME",variable=edna_var).pack()
    Checkbutton(eds,text="ADDRESS",variable=edad_var).pack()
    Checkbutton(eds,text="PHONE NUMBER",variable=edph_var).pack()
    Button(eds,text="EDIT",command=editproc).pack()

def editproc():
    global eps
    global ename
    global eadd
    global ephno
    ename=StringVar()
    eadd=StringVar()
    ephno=IntVar()
    eps=Toplevel(sec)
    eps.geometry("300x250+500+180")
    Label(eps,text="eFOODCART",font=("Forte",22),fg="red").pack()
    if edna_var.get()==1 and edad_var.get()==1 and edph_var.get()==1:
        Label(eps,text="ENTER NEW NAME:").pack()
        Entry(eps,textvariable=ename).pack()
        Label(eps,text="ENTER NEW ADDRESS:").pack()
        Entry(eps,textvariable=eadd).pack()
        Label(eps,text="ENTER NEWPHONE NUMBER:").pack()
        Entry(eps,textvariable=ephno).pack()
        Button(eps,text="CHANGE",command=echange).pack()
    elif edph_var.get()==1 and edad_var.get()==1:
        Label(eps,text="ENTER NEW ADDRESS:").pack()
        Entry(eps,textvariable=eadd).pack()
        Label(eps,text="ENTER NEWPHONE NUMBER:").pack()
        Entry(eps,textvariable=ephno).pack()
        Button(eps,text="CHANGE",command=echange).pack()
    elif edna_var.get()==1 and edph_var.get()==1:
        Label(eps,text="ENTER NEW NAME:").pack()
        Entry(eps,textvariable=ename).pack()
        Label(eps,text="ENTER NEWPHONE NUMBER:").pack()
        Entry(eps,textvariable=ephno).pack()
        Button(eps,text="CHANGE",command=echange).pack()
    elif edna_var.get()==1 and edad_var.get()==1:
        Label(eps,text="ENTER NEW NAME:").pack()
        Entry(eps,textvariable=ename).pack()
        Label(eps,text="ENTER NEW ADDRESS:").pack()
        Entry(eps,textvariable=eadd).pack()
        Button(eps,text="CHANGE",command=echange).pack()
    elif edna_var.get()==1:
        Label(eps,text="ENTER NEW NAME:").pack()
        Entry(eps,textvariable=ename).pack()
        Button(eps,text="CHANGE",command=echange).pack()
    elif edad_var.get()==1:
        Label(eps,text="ENTER NEW ADDRESS:").pack()
        Entry(eps,textvariable=eadd).pack()
        Button(eps,text="CHANGE",command=echange).pack()
    elif edph_var.get()==1:
        Label(eps,text="ENTER NEWPHONE NUMBER:").pack()
        Entry(eps,textvariable=ephno).pack()
        Button(eps,text="CHANGE",command=echange).pack()    
    else:
        eps.destroy()

def echange():
    eds.destroy()
    eps.destroy()
    pos.destroy()
    global npos
    cur.execute("select address from users where cname=%s",(username1,))
    ad=cur.fetchall()
    cur.execute("select phonenumber from users where cname=%s",(username1,))
    pn=cur.fetchall()
    npos=Toplevel(sec)
    npos.geometry("300x250+500+180")
    Label(npos,text="eFOODCART",font=("Forte",22),fg="red").pack()
    if edna_var.get()==1 and edph_var.get()==1 and edad_var.get()==1:
        Label(npos,text=ename.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=eadd.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ephno.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
    elif edad_var.get()==1 and edna_var.get()==1:
        Label(npos,text=ename.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=eadd.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=pn,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
    elif edph_var.get()==1 and edad_var.get()==1:
        Label(npos,text=username1,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=eadd.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ephno.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
    elif edna_var.get()==1 and edph_var.get()==1:
        Label(npos,text=ename.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ad[0][0],font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ephno.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
    elif edna_var.get()==1:
        Label(npos,text=ename.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ad[0][0],font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=pn,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
    elif edad_var.get()==1:
        Label(npos,text=username1,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=eadd.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=pn,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)
    else:
        Label(npos,text=username1,font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ad[0][0],font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Label(npos,text=ephno.get(),font=("Times"),bg="yellow",relief=SUNKEN).pack(fill=X)
        Button(npos,text="BACK",width=12,command=del_pos).place(x=0,y=230)
        Button(npos,text="EDIT",width=12,command=editord).place(x=100,y=230)
        Button(npos,text="PROCEED",width=12,command=mode).place(x=203,y=230)



def mode():
    global mos
    mos=Toplevel(sec)
    global mode_var
    pos.destroy()
    mos.geometry("300x250+500+180")
    mode_var=IntVar()
    Label(mos,text="eFOOD CART",font=("Forte",22),fg="red").pack()
    Radiobutton(mos,text="CREDIT/DEBIT CARD",variable=mode_var,value=1,command=modechck).place(x=70,y=60)
    Radiobutton(mos,text="CASH",variable=mode_var,value=2,command=modechck).place(x=70,y=80)
    Radiobutton(mos,text="PAYTM/PHONEPE/GPAY",variable=mode_var,value=4,command=modechck).place(x=70,y=100)
    Button(mos,text="BACK",command=del_mos,width=15).place(x=1,y=230)

def del_mos():
    mos.destroy() 
      
def modechck():
    mos.destroy()
    global cos
    global progress
    if mode_var.get()==1:
        global credit_info
        global val_info
        global cvv_info
        cos=Toplevel(sec)
        cos.geometry("300x250+500+180")
        credit_info=IntVar()
        val_info=StringVar()
        cvv_info=IntVar()
        Label(cos,text="eFOOD CART",fg="red",font=("Forte",22)).pack()
        Label(cos,text="CREDIT CARD NO").place(x=110,y=80)
        Entry(cos,textvariable=credit_info).place(x=90,y=100)
        Label(cos,text="VALIDITY PERIOD").place(x=110,y=120)
        Entry(cos,textvariable=val_info).place(x=90,y=140)
        Label(cos,text="* NOTE DATE FORMAT=DD/MM/YYYY").place(x=75,y=160)
        Label(cos,text="CVV").place(x=120,y=180)
        Entry(cos,textvariable=cvv_info).place(x=90,y=200)
        Button(cos,text="BACK",command=del_cos,width=12).place(x=1,y=230)
        Button(cos,text="PROCEED",width=12,command=place_ord_suc()).place(x=215,y=230)

    elif mode_var.get()==2:
        place_ord_suc()
        
    else:
        global qrimage
        cos=Toplevel(sec)
        cos.geometry("300x250+500+180")
        image=PhotoImage(file=r"D:\Srinath\csc proj\combined works\qrcode.png")
        qrimage=image.subsample(10)
        Label(cos,text='eFOOD CART',font=("Forte",22),fg="red").pack()
        Label(cos,image=qrimage).place(x=90,y=80)
        Label(cos,text="Scan this QRCode to pay via paytm/gpay/phonpe").place(x=20,y=200)
        Button(cos,text="PROCEED",width=12,command=place_ord_suc()).place(x=215,y=230)
        Button(cos,text="BACK",width=12,command=del_cos).place(x=1,y=230)
    
def del_cos():
    cos.destroy()
    mode()

        
def place_ord_suc():
    global pos2
    global fb
    cur.execute("select address from users where cname=%s",(username1,))
    ad0=cur.fetchall()
    ad1=ad0[0][0]
    cur.execute("select phonenumber from users where cname =%s",(username1,))
    ph0=cur.fetchall()
    ph1=ph0[0][0]
    if mode_var.get()==True:
        if  len(str(credit_info))==19 and type(cvv_info)==int and len(str(cvv_info))==3:  
            pos2=Toplevel(sec)          
            Label(pos2,text="YOUR ORDER HAS BEEN SUCCESSFULLY PLACED").pack()
            fb=open(r'C:\Users\Srinath\Downloads\Bill.txt','w+')
            fb.write('\n\n+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+\n')
            cur.execute("select curdate()")
            date=cur.fetchall()
            d_date = datetime.datetime.now()
            filedatetime=d_date.strftime("  %d-%m-%Y\t\t\t\t\t\t\t  EFood Cart Order Invoice\t\t\t\t\t\t  %I:%M:%S %p")
            fb.write(filedatetime)
            fb.write('\n+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+\n\n')
            fb.write("\t NAME:"+username1+"\t\t\t ADDRESS:"+ad1 + "\t\t\t CONTACT:{0}".format(ph1))
            fb.write('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n')
            fb.write('\t\t\tHotelname\t\t\tItemname\t\t\t\t'+'Rate\t'+'Qty\t'+'Amount\n')
            for i in cartlst.keys():
                a=cartlst[i][0];b=cartlst[i][1];fb.write('\n\t\t\t{0}\t\t\t{1}\t\t\t\t\t{2}\t{3}\t{4}'.format(cartlst[i][2],i,"Rs."+str(cartlst[i][1]),cartlst[i][0],"Rs."+str(a*b)))
            fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            fb.write('\n\t\t\t\t\t\t\t\tTotal amount:\t\t\t\t\t{0} Rs.'.format(price))
            fb.write("\n\t\t\t\t\t\t\t\tGST:\t\t\t\t\t\t{0} Rs. (10%) ".format(price*(10/100)))
            fb.write("\n\t\t\t\t\t\t\t\tService Tax:\t\t\t\t\t{0} Rs. (5%)".format(price*(5/100)))
            price1=int(price+price*(15/100))
            fb.write("\n\t\t\t\t\t\t\t\tGrand Total:\t\t\t\t\t{0} Rs.".format(price1))
            fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            fb.write("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t{0} Rupees Only/-".format(nw.word(price1)))
            fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            fb.write("\n->No Return")
            fb.write("\n->No Tips")
            fb.write("\n->No Cancellation After Bill Generation")
            fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            fb.write("\n\t\t\t\t\t\t\tThank You For Using Our App Visit Again!!")
            fb.write("\n\t\t\t\t\t\t\t\t\t HAVE A GOOD DAY!!!")
            fb.close()
            for i in cartlst.keys():
                cur.execute("insert into orders(cname,hotel,items,quantity,price,date) values('{}','{}','{}',{},{},'{}')".format(username1,cartlst[i][2],i,cartlst[i][0],price,date[0][0]))
                mc.commit()
            Button(pos2,text="DOWNLOAD BILL",command=download).pack()
            Button(pos2,text="SCREENSHOT",command=ss).pack()

        elif len(str(credit_info))<19:
            pos2=Toplevel(sec)
            pos2.title("CREDIT INFO WRONG")
            Label(pos2,text="CHECK YOUR CREDIT CARD NUMBER").pack()
        elif len(val_info)!=10:
            pos2=Toplevel(sec)
            pos2.title("DATE WRONG")
            Label(pos2,text="CHECK YOUR VALIDITY DATE").pack()
        elif len(str(cvv_info))!=3 or type(cvv_info)!=int:
            pos2=Toplevel(sec)
            pos2.title("CVV WRONG")
            Label(pos2,text="CHECK YOUR CVV NUMBER").pack()
    else:
        pos2=Toplevel(sec)          
        Label(pos2,text="YOUR ORDER HAS BEEN SUCCESSFULLY PLACED").pack()
        fb=open(r'C:\Users\Srinath\Downloads\Bill.txt','w+')
        fb.write('\n\n+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+\n')
        cur.execute("select curdate()")
        date=cur.fetchall()
        d_date = datetime.datetime.now()
        filedatetime=d_date.strftime("  %d-%m-%Y\t\t\t\t\t\t\t  EFood Cart Order Invoice\t\t\t\t\t\t\t %I:%M:%S %p")
        fb.write(filedatetime)
        fb.write('\n+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+\n\n')
        fb.write("\t NAME:"+username1+"\t\t\t ADDRESS:"+ad1 + "\t\t\t CONTACT:{0}".format(ph1))
        fb.write('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n')
        fb.write('\t\t\tHotelname\t\t\tItemname\t\t\t\t'+'Rate\t'+'Qty\t'+'Amount\n')
        for i in cartlst.keys():
            a=cartlst[i][0];b=cartlst[i][1];fb.write('\n\t\t\t{0}\t\t\t{1}\t\t\t\t\t{2}\t{3}\t{4}'.format(cartlst[i][2],i,"Rs."+str(cartlst[i][1]),cartlst[i][0],"Rs."+str(a*b)))
        fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        fb.write('\n\t\t\t\t\t\t\t\tTotal amount:\t\t\t\t\t{0} Rs.'.format(price))
        fb.write("\n\t\t\t\t\t\t\t\tGST:\t\t\t\t\t\t{0} Rs. (10%) ".format(price*(10/100)))
        fb.write("\n\t\t\t\t\t\t\t\tService Tax:\t\t\t\t\t{0} Rs. (5%)".format(price*(5/100)))
        price1=int(price+price*(15/100))
        fb.write("\n\t\t\t\t\t\t\t\tGrand Total:\t\t\t\t\t{0} Rs.".format(price1))
        fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        fb.write("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t{0} Rupees Only/-".format(nw.word(price1)))
        fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        fb.write("\n->No Return")
        fb.write("\n->No Tips")
        fb.write("\n->No Cancellation After Bill Generation")
        fb.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        fb.write("\n\t\t\t\t\t\t\tThank You For Using Our App Visit Again!!")
        fb.write("\n\t\t\t\t\t\t\t\t HAVE A GOOD DAY!!!")
        fb.close()
        for i in cartlst.keys():
            cur.execute("insert into orders(cname,hotel,items,quantity,price,date) values('{}','{}','{}',{},{},'{}')".format(username1,cartlst[i][2],i,cartlst[i][0],price,date[0][0]))
            mc.commit()
        Button(pos2,text="DOWNLOAD BILL",command=download).pack()
        Button(pos2,text="SCREENSHOT",command=ss).pack()

def lu():
    global lus
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global cp3
    global sp3
    global hp3
    global hotelname
    lus=Toplevel(sec)
    lus.geometry("2000x2500")
    Label(lus,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp3=imge.subsample(6)
    Button(lus,image=hp3,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp3=imge1.subsample(15)
    Button(lus,image=sp3,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp3=imge2.subsample(8)
    Button(lus,image=cp3,bg="green",activebackground="red",relief=FLAT,command=cartpage).place(x=1185,y=2)
    Label(lus,text="ITEM",bg="white",font=("Verdana",22)).place(x=20,y=60)
    Label(lus,text="QUANTITY",bg="white",font=("Verdana",22)).place(x=260,y=60)
    Label(lus,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=460,y=60)
    Button(lus,text="BACK PAGE",font=("Verdana",19),command=lambda:lus.destroy()).place(x=15,y=630)
    lus.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()==hona.index(j)+1:
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where hid='{}' and category='{}'".format(hotelid[0][0],"lunch")) 
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(lus,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(lus,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=260,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"lunch"))
            items1=cur.fetchall()
            for k in items1:
                Label(lus,text="Rs."+(k[0]),bg="white",font=("Verdana",22)).place(x=460,y=yaxis1)
                yaxis1+=45
    Button(lus,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)
    
def ch():
    global chs
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global cp4
    global hp4
    global sp4
    global hotelname
    chs=Toplevel(sec)
    chs.geometry("2000x2500")
    Label(chs,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp4=imge.subsample(6)
    Button(chs,image=hp4,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp4=imge1.subsample(15)
    Button(chs,image=sp4,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp4=imge2.subsample(8)
    Button(chs,image=cp4,bg="green",activebackground="red",relief=FLAT,command=cartpage).place(x=1185,y=2)
    Label(chs,text="ITEM",bg="white",font=("Verdana",22)).place(x=20,y=60)
    Label(chs,text="QUANTITY",bg="white",font=("Verdana",22)).place(x=300,y=60)
    Label(chs,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=500,y=60)
    Button(chs,text="BACK PAGE",font=("Verdana",19),command=lambda:chs.destroy()).place(x=15,y=630)
    chs.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()==hona.index(j)+1:
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where hid='{}' and category='{}'".format(hotelid[0][0],"chats")) 
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(chs,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(chs,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=300,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"chats"))
            items1=cur.fetchall()
            for k in items1:
                Label(chs,text="Rs."+str(k[0]),bg="white",font=("Verdana",22)).place(x=500,y=yaxis1)
                yaxis1+=45
    Button(chs,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)

def bev():
    global bes
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global hp5
    global sp5
    global cp5
    global hotelname
    bes=Toplevel(sec)
    bes.geometry("2000x2500")
    Label(bes,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp5=imge.subsample(6)
    Button(bes,image=hp5,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp5=imge1.subsample(15)
    Button(bes,image=sp5,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp5=imge2.subsample(8)
    Button(bes,image=cp5,bg="green",activebackground="red",relief=FLAT,command=cartpage).place(x=1185,y=2)
    Label(bes,text="ITEM",bg="white",font=("Verdana",22)).place(x=20,y=60)
    Label(bes,text="QUANTITY",bg="white",font=("Verdana",22)).place(x=300,y=60)
    Label(bes,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=500,y=60)
    Button(bes,text="BACK PAGE",font=("Verdana",19),command=lambda:bes.destroy()).place(x=15,y=630)
    bes.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()==hona.index(j)+1:
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where hid='{}' and category='{}'".format(hotelid[0][0],"drinks")) 
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(bes,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(bes,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=300,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"drinks"))
            items1=cur.fetchall()
            for k in items1:
                Label(bes,text="Rs."+str(k[0]),bg="white",font=("Verdana",22)).place(x=500,y=yaxis1)
                yaxis1+=45
    Button(bes,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)
    
def din():
    global dis1
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global cp6
    global sp6
    global hp6
    global hotelname
    dis1=Toplevel(sec)
    dis1.geometry("2000x2500")
    Label(dis1,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp6=imge.subsample(6)
    Button(dis1,image=hp6,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp6=imge1.subsample(15)
    Button(dis1,image=sp6,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp6=imge2.subsample(8)
    Button(dis1,image=cp6,bg="green",activebackground="red",relief=FLAT,command=cartpage).place(x=1185,y=2)
    Label(dis1,text="ITEM",bg="white",font=("Verdana",22)).place(x=20,y=60)
    Label(dis1,text="QUANTITY",bg="white",font=("Verdana",22)).place(x=300,y=60)
    Label(dis1,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=500,y=60)
    Button(dis1,text="BACK PAGE",font=("Verdana",19),command=lambda:dis1.destroy()).place(x=15,y=630)
    dis1.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()==hona.index(j)+1:
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where hid='{}' and category='{}'".format(hotelid[0][0],"dinner")) 
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(dis1,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(dis1,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=300,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"dinner"))
            items1=cur.fetchall()
            for k in items1:
                Label(dis1,text="Rs."+str(k[0]),bg="white",font=("Verdana",22)).place(x=500,y=yaxis1)
                yaxis1+=45
    Button(dis1,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)

def cont():
    global conts
    global items
    global items1
    global chckval
    global chckval1
    global chckval2
    global hp9
    global cp9
    global sp9
    global hotelname
    conts=Toplevel(sec)
    conts.geometry("2000x2050")
    Label(conts,text="eFOOD CART",font=("Forte",32),bg="green",fg="red").pack(fill=X)
    imge=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp9=imge.subsample(6)
    Button(conts,image=hp9,bg="green",activebackground="red",relief=FLAT).place(x=0,y=0)
    imge1=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp9=imge1.subsample(15)
    Button(conts,image=sp9,bg="green",activebackground="red",relief=FLAT,command=settings).place(x=1230,y=2)
    imge2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp9=imge2.subsample(8)
    Button(conts,image=cp9,bg="green",activebackground="red",relief=FLAT,command=cartpage).place(x=1185,y=2)
    Label(conts,text="ITEM",bg="white",font=("Versdana",22)).place(x=20,y=60)
    Label(conts,text="QUANTITY",bg="white",font=("Versdana",22)).place(x=400,y=60)
    Label(conts,text="PRICE/ITEM",bg="white",font=("Verdana",22)).place(x=600,y=60)
    Button(conts,text="BACK PAGE",font=("Verdana",19),command=conts.destroy()).place(x=15,y=650)
    conts.config(bg="white")
    yaxis=yaxis1=120
    for j in hona:
        if sel_var.get()==hona.index(j)+1:
            try:
                hotelname=j[0][0]
                if len(hotelname)==1:
                    hotelname=j[0]
                else:
                    break
            except:
                hotelname=j[0]
            cur.execute("select hid from hotels where hotel=%s",j)
            hotelid=cur.fetchall()
            cur.execute("select item from foods where hid='{}' and category='{}'".format(hotelid[0][0],"conti")) 
            items=cur.fetchall()
            chckval={}
            chckval1=dict(chckval)
            chckval2=dict()
            itemsdup=list(items)
            count=0
            for l in items:
                chckval[l]=IntVar()
                chckval1[l]=IntVar()
                chckval2[l]="food"
                Checkbutton(conts,text=itemsdup[count][0],variable=chckval[l],bg="white",font=("Verdana",22)).place(x=20,y=yaxis)
                Spinbox(conts,from_=0,to_=25,textvariable=chckval1[l],bg="white").place(x=400,y=yaxis+15)
                yaxis+=40
                count+=1
            cur.execute("select price from foods where hid='{}' and category='{}'".format(hotelid[0][0],"conti"))
            items1=cur.fetchall()
            for k in items1:
                Label(conts,text="Rs."+str(k[0]),bg="white",font=("Verdana",22)).place(x=600,y=yaxis1)
                yaxis1+=45
    Button(conts,text="ADD TO CART",font=("Verdana",19),command=cart).place(x=800,y=600)

def ulog_suc():
    uls.destroy()
    ls.destroy()
    global length
    global ulss
    global length2
    global pd
    global pageno
    global shres
    global h
    global hona
    hona=[]
    ulss=Toplevel(sec)
    ulss.geometry("2000x2500")
    Label(ulss,text="eFOOD CART",font=("Forte",33),bg="green",fg="red").pack(fill=X)
    h=0
    pd={}
    cur.execute("select hotel from hotels")
    shres=cur.fetchall()
    for i in shres:
        hona.append(i)
    length=len(shres)
    c=4
    if length%4==0:
        pageno=length/4
        ulog_suc2()
    else:
        if length>4 and length<8:
            pageno=2
        elif length>8:
            length2=int(length%4)
            pageno=int((length-length2)/4) +1
        elif length<4:
            pageno=1
    #length2=int(length%4)
    a1=0
    b1=4
    for  i in range(1,pageno+1):
        pd[i]=[a1,b1]
        a1=b1
        b1+=4
    ulog_suc2()

def ulog_suc2():   
    global hp
    global cp
    global sp
    global np
    global bp
    global ulss
    global h1
    global g1
    global ya
    global xa
    global xa1
    ya=125
    xa=xa1=50
    bph=PhotoImage(file=r"D:\Srinath\csc proj\back.png")
    bp=bph.subsample(2)
    hph=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp=hph.subsample(6)
    cph=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp=cph.subsample(7)
    sph=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp=sph.subsample(15)
    nph=PhotoImage(file=r"D:\Srinath\csc proj\nxt.png")
    np=nph.subsample(2)
    ulog_suc3()

def ulog_suc3():
    global xa
    global xa1
    global ya
    global count
    global pgno
    global sel_var
    global imgph
    global imgph1
    global hp
    global cp
    global sp
    global np
    global bpf
    global photok1
    sel_var=IntVar()
    Button(ulss,image=hp,relief="flat",activebackground="red",bg="green").place(x=0,y=0)
    Button(ulss,image=cp,relief="flat",activebackground="red",bg="green",command=cartpage).place(x=1185,y=2)
    Button(ulss,image=sp,relief="flat",activebackground="red",bg="green",command=settings).place(x=1230,y=2)    
    Button(ulss,text="MY ORDERS",relief="flat",height=2,activebackground="red",bg="green",command=view_myord).place(x=1110,y=4)
    if h==0:
        pgno=1
    if pgno+1==pageno:
        Button(ulss,image=np,command=next1,relief=FLAT).place(x=1230,y=350)
    elif pageno==pgno:
        Button(ulss,image=bp,command=back1,relief=FLAT).place(x=5,y=350)
    elif pageno>1:
        Button(ulss,image=np,command=next1,relief=FLAT).place(x=1230,y=350)
        Button(ulss,image=bp,command=back1,relief=FLAT).place(x=5,y=350)
    c=4
    count=1
    try:
        h1=pd[pgno][0]
        g1=pd[pgno][1]
    except:
        pass
    for k in shres[h1:g1]:
        while c==4:
            for i in shres[h1:int(g1/2)]:
                imgph=PhotoImage(file=r"D:/Srinath/csc proj/combined works/"+str(random.randint(1,3))+".png").subsample(3)
                rb=Radiobutton(ulss,text=i[0],height=170,variable=sel_var,bg="white",value=hona.index(i)+1,image=imgph,compound=LEFT,command=catscreen,font=("Verdana",22))
                rb.image=imgph
                rb.place(x=xa,y=ya)
                count+=1
                xa+=600
                c-=1
            ya+=200
            for j in shres[int(g1/2):g1]:
                imgph1=PhotoImage(file=r"D:/Srinath/csc proj/combined works/"+str(random.randint(4,7))+".png").subsample(3)
                rb1=Radiobutton(ulss,text=j[0],height=170,image=imgph1,bg="white",compound=LEFT,variable=sel_var,value=hona.index(j)+1,command=catscreen,font=("Verdana",22))
                rb1.image=imgph1
                rb1.place(x=xa1,y=ya)
                xa1+=600
                count+=1
            xa=0
            xa1=0
            c-=1
    ulss.config(bg="white")
    
    
def next1():
    global h
    global count
    global ya
    global xa
    global xa1
    xa1=0
    xa=0
    ya=0
    count=count
    h+=1
    global pgno
    pgno=pgno+1   
    global q2
    q2=1
    lst=ulss.place_slaves()
    for i in lst:
        i.destroy() 
    ulog_suc3()

def back1():
    global h
    global count
    count=count
    h=1
    global pgno
    pgno=pgno-1  
    
    global q2
    q2=1
    lst=ulss.place_slaves()
    for i in lst:
        i.destroy()
    ulog_suc3()

def catscreen():
    global bf
    global bfp
    global l
    global lp
    global di
    global dip
    global sn
    global snp
    global be
    global bep
    global de
    global dep
    global con
    global conp
    global photo
    global hp1
    global photo1
    global cp1
    global photo2
    global sp1
    global cs
    global background_label
    global photok
    cs=Toplevel(sec)
    cs.geometry("2000x2500")
    Label(cs,text="eFOOD CART",font=("Forte",33),bg="green",fg="red").pack(fill=X)
    bf=PhotoImage(file=r"D:/Srinath/csc proj/combined works/breakfast.png")
    bfp=bf.subsample(3,4)
    Button(cs,image=bfp,compound=LEFT,text=" BREAKFAST ",font=("Verdana",22),height=170,bg="white",activebackground="red",command=bfast).place(x=0,y=100)
    l=PhotoImage(file=r"D:/Srinath/csc proj/combined works/lunch.png")
    lp=l.subsample(3,2)
    Button(cs,text=" LUNCH  ",image=lp,compound=LEFT,font=("Verdana",22),height=170,bg="white",activebackground="red",command=lu).place(x=400,y=100)
    di=PhotoImage(file=r"D:/Srinath/csc proj/combined works/dinner.png")
    dip=di.subsample(3,3)
    Button(cs,text=" DINNER    ",image=dip,compound=LEFT,font=("Verdana",19),height=170,activebackground="red",bg="white",command=din).place(x=800,y=100)
    sn=PhotoImage(file=r"D:/Srinath/csc proj/combined works/snacks.png")
    snp=sn.subsample(5,3)
    Button(cs,image=snp,text=" SNACKS/CHATS ",compound=LEFT,font=("Verdana",22),height=170,bg="white",activebackground="red",command=ch).place(x=0,y=300)
    be=PhotoImage(file=r"D:/Srinath/csc proj/combined works/beverages.png")
    bep=be.subsample(3,3)
    Button(cs,text=" BEVERAGES ",image=bep,compound=LEFT,font=("Verdana,22"),height=170,bg="white",activebackground="red",command=bev).place(x=400,y=300)
    de=PhotoImage(file=r"D:/Srinath/csc proj/combined works/dessert.png")
    dep=de.subsample(3,3)
    Button(cs,text="DESSERT ",image=dep,compound=LEFT,font=("Verdana",22),height=170,bg="white",activebackground="red",command=des).place(x=800,y=300)
    con=PhotoImage(file=r"D:/Srinath/csc proj/combined works/continental.png")
    conp=con.subsample(3,2)
    Button(cs,text="CONTINENTALS",image=conp,compound=LEFT,font=("Verdana",22),height=170,bg="white",activebackground="red",command=cont).place(x=340,y=500)
    photo=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    hp1=photo.subsample(6)
    photo1=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    cp1=photo1.subsample(7)
    photo2=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    sp1=photo2.subsample(15)
    Button(cs,image=hp1,relief="flat",activebackground="red",bg="green").place(x=0,y=0)
    Button(cs,image=cp1,relief="flat",bg="green",activebackground="red",command=cartpage).place(x=1185,y=2)
    Button(cs,image=sp1,relief="flat",bg="green",activebackground="red",command=settings).place(x=1230,y=2)
    Button(cs,text="BACK PAGE",font=("Verdana",19),bg="white",command=lambda:cs.destroy()).place(x=15,y=600)
    cs.config(bg="white")

def view_myord():
    global myord
    global  hp10
    global cp10
    global sp10
    image=PhotoImage(file=r"D:\Srinath\csc proj\home.png")
    image2=PhotoImage(file=r"D:\Srinath\csc proj\cart.png")
    image3=PhotoImage(file=r"D:\Srinath\csc proj\settings.png")
    hp10=image.subsample(6)
    cp10=image2.subsample(8)
    sp10=image3.subsample(15)
    myord=Toplevel(sec)
    myord.geometry("2000x2500")
    Label(myord,text="eFOOD CART",fg="red",bg="green",font=("Forte",)).pack(fill=X)
    Button(myord,image=hp10,activebackground="red").place(x=0,y=0)
    Button(myord,image=cp10,activebackground="red",command=cartpage).place(x=1185,y=0)
    Button(myord,image=sp10,activebackground="red",command=settings).place(x=1230,y=0)
    Label(myord,text="HOTELNAME",font=("Verdana",22)).place(x=15,y=40)
    Label(myord,text="ITEM",font=("Verdana",22)).place(x=350,y=40)
    Label(myord,text="DATE",font=("Verdana",22)).place(x=700,y=40)
    cur.execute("select distinct hotel from orders where cname=%s",(username1,))
    hotel=cur.fetchall() 
    l=[];m=[]
    y1=100  
    for i in hotel:
        cur.execute("select distinct date from orders where hotel='{}' and cname='{}'".format(i[0],username1))
        l.append(cur.fetchall())
    c=0
    for j in hotel:
        cur.execute("select items from orders where hotel='{}' and cname='{}' and date='{}'".format(j[0],username1,l[c][0][0]))
        c+=1
        m.append(cur.fetchall())
    for k in hotel:
        Label(myord,text=k[0],font=("Verdana",15)).place(x=15,y=y1)
        y1+=60
    y=100
    for j in range(len(l)):        
        Label(myord,text=m[1],font=("Verdana",15)).place(x=350,y=y)
        Label(myord,text=l[j],font=("Verdana",15)).place(x=700,y=y)
        y+=60
    
    Button(myord,text="BACK",command=lambda:myord.destroy()).place(x=600,y=720)
                                   

def download():
    notification.notify(title='FOOD DELIVER APP', 
    message='Bill Downloaded \nCheck It Out In The Downloads!!', 
    app_icon=r'D:\Srinath\csc proj\mohan works\download.ico',   
    timeout=10,  
    )
    
def ss():
    im = ImageGrab.grab()
    im.save(r'C:\Users\Srinath\Downloads\fullscreen.png')
    notification.notify(
    title='FOOD DELIVER APP', #title
    message='ScreenShot Taken \nCheck It Out In The Downloads!!', #msg
    app_icon=r'D:\Srinath\csc proj\mohan works\download.ico',  #img loc 
    timeout=10,  #sec
    )
#toplevel statements    
main()



 




    

