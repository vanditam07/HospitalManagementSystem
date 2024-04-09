#=========================IMPORTING MODULES========================================

import tkinter
import mysql.connector as mysql
from tkinter import messagebox
from tkinter import ttk

#=========================PAGE HOPPER FUNCTIONS======================================

def homep():
        f.destroy()
        import main
def newdoc():
        f.destroy()
        import ndoctor
def newp():
    f.destroy()
    import npatient
def logout():
    f.destroy()
    import login
def pathist():
    f.destroy()
    import psearch
def dsearch():
    f.destroy()
    import dsearch
def refresh():
    f.destroy()
    import npatient

#======================================MYSQL-CONNECTIVITY===============================================
def insert():
    patid = p_ide.get()
    pname = p_nme.get()
    pmob = p_mbe.get()
    pland = p_lde.get()
    pdob = p_dobe.get()
    pfa = p_fae.get()
    pmo = p_mae.get()
    pbt = p_bte.get()
    pem = p_eme.get()
    pmed = p_hie.get(1.0)

    if (patid=="" or pname == "" or pmob == "" or pdob == "" or pbt == "" or pem == "") :
        tkinter.messagebox.showinfo("Insert Status" , "All Fields Neccessary")
    else:
        con = mysql.connect(host = "localhost" , user = "root" , password = "krish10172003" , database="clinic")
        if con.is_connected():
            print("Success")
        cursor = con.cursor()
        query = "insert into p_details values({} , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}')"\
            .format( patid , pname , pmob ,pland ,pdob ,pfa ,pmo , pbt ,pem , pmed)

        cursor.execute(query)
        con.commit()
        tkinter.messagebox.showinfo("Insert Status:", "Inserted Succesfully")
        con.close();

#===========================PAGE WINDOW===========================================

f = tkinter.Tk()
f.title("Hospital Management Software")
f.geometry("1540x800+0+0")
l1 = tkinter.Label(f,bd=10,relief= "ridge" ,text="ADD PATIENT", fg = "Black", bg = "White" , font =("Times New Roman",30,"bold") )
l1.pack(fill="x")

# ========================================DATA FRAMES=======================================================

pftop = tkinter.Frame(f, bd=20, relief="ridge")
pftop.place(x=0, y = 70 , width = 1530 , height = 200)
df = tkinter.Frame(f, bd=20, relief="ridge")
df.place(x=0, y=200, width=1530, height=400)

dfleft = tkinter.Frame(df,bd=10,relief = "ridge")
l2 = tkinter.Label(dfleft , relief = "ridge" , text = "Input Details: " , font=("Times New Roman" , 15 , "bold") ,bd = 4)
l2.grid(row=0,column=0)
dfleft.place(x=0,y=3,width=1000,height=355)

dfright = tkinter.Frame(df,bd=10,relief = "ridge")
dfright.place(x=750, y=3, width=735, height=355)



#==========================================DOCTOR ADDING===============================================

p_id = tkinter.Label(dfleft , text = "Patient ID: " , font = ("Arial" , 12) ,padx=2,pady=6 , height = 1)
p_id.grid(row=1,column=0)
p_ide = tkinter.Entry(dfleft , width = 30)
p_ide.grid(row = 1 , column =1)
p_nm = tkinter.Label(dfleft, text="Patient Name: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_nm.grid(row=2, column=0)
p_nme = tkinter.Entry(dfleft, width=30)
p_nme.grid(row=2, column=1)

p_mb = tkinter.Label(dfleft, text="Patient Mobile: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_mb.grid(row=3, column=0)
p_mbe = tkinter.Entry(dfleft, width=30)
p_mbe.grid(row=3, column=1)
p_ld = tkinter.Label(dfleft, text="Patient Landline: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_ld.grid(row=4, column=0)
p_lde = tkinter.Entry(dfleft, width=30)
p_lde.grid(row=4, column=1)
p_dob = tkinter.Label(dfleft, text="Patient DOB: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_dob.grid(row=5, column=0)
p_dobe = tkinter.Entry(dfleft, width=30)

p_dobe.grid(row=5, column=1)
p_fa = tkinter.Label(dfleft, text="Patient Father: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_fa.grid(row=6, column=0)
p_fae = tkinter.Entry(dfleft, width=30)
p_fae.grid(row=6, column=1)

p_ma = tkinter.Label(dfleft, text="Patient Mother: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_ma.grid(row=7, column=0)
p_mae = tkinter.Entry(dfleft, width=30)
p_mae.grid(row=7, column=1)
p_bt = tkinter.Label(dfleft, text="Blood Type: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_bt.grid(row=8, column=0)
p_bte = ttk.Combobox(dfleft, width=30)
p_bte["values"]=( "A+" , "A-" , "B-" , "B+" , "O-" , "O+" , "AB" , "AB-" )
p_bte.grid(row=8, column=1)
p_em = tkinter.Label(dfleft, text="Patient Email: ", font=("Arial", 12), padx=2, pady=6, height=1)
p_em.grid(row=1, column=2)
p_eme = tkinter.Entry(dfleft, width=30)
p_eme.grid(row=1, column=3)

p_hi = tkinter.Label(dfright, bd = 4,text="Patient History: ", font=("Times New Roman", 15 , 'bold') , relief = 'ridge' , height = 1)
p_hi.place(x=0, y =0)
p_hie = tkinter.Text(dfright , width = 66 , height = 17)
p_hie.place(x = 6 , y = 45)

#=========================PAGE HOPPER BUTTONS======================================
hp = tkinter.Button(pftop, text="HOME PAGE", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1 , command = homep , width = 21)
hp.grid(row=0, column=2)

np = tkinter.Button(pftop, text="NEW PATIENT", bg='white', font=("Arial", 12, "bold") , command = refresh, padx=2, pady=6, height=1 , width = 21)
np.grid(row=0, column=3)

ph = tkinter.Button(pftop, text="PATIENT SEARCH", bg='white', font=("Arial", 12, "bold"),command = pathist, padx=2, pady=6, height=1, width = 21)
ph.grid(row=0, column=4)

dd = tkinter.Button(pftop, text="DOCTOR DETAIL", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21, command = dsearch)
dd.grid(row=0, column=5)

nd = tkinter.Button(pftop, text="NEW DOCTOR", bg='white', font=("Arial", 12, "bold"), command = newdoc , padx=2, pady=6, height=1, width = 21)
nd.grid(row=0, column=6)

pb = tkinter.Button(pftop, text="LOGOUT", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21, command = logout)
pb.grid(row=0, column=7)

rf = tkinter.Button(pftop, text="REFRESH", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=2, command = refresh,width = 21)
rf.grid(row=1, column=4)

ex = tkinter.Button(pftop, text="EXIT", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=2, command = exit,width = 21)
ex.grid(row=1, column=5)


pfbot = tkinter.Frame(f,height = 55,width = 1360,  relief = 'ridge' ).place(x=0,y=600)
submit = tkinter.Button(f , bd = 4,text = "SUBMIT",font=("Arial", 12, "bold"), relief = 'ridge', height = 2 , width = 14 , bg= 'white', command = insert )
submit.place(x=590, y = 602)

f.mainloop()