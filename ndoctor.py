#=========================IMPORTING MODULES========================================

import tkinter
import mysql.connector as mysql
from tkinter import messagebox
from tkinter import ttk

#=========================PAGE HOPPER FUNCTIONS======================================

def homep():
    f.destroy()
    import main

def logout():
    f.destroy()
    import login

def pathist():
    f.destroy()
    import psearch
def newp():
    f.destroy()
    import npatient
def refresh():
    f.destroy()
    import ndoctor
def dsearch():
    f.destroy()
    import dsearch

#=========================MYSQL CONNECTIVITY======================================

def insert():
    docid = d_ide.get()
    dname = d_nme.get()
    dmob = d_mbe.get()
    dland = d_lde.get()
    ddob = d_dobe.get()
    dsp = d_spe.get()
    dadr = d_ade.get()
    ddpt = d_dpe.get()
    dem = d_eme.get()
    ddeg =d_dge.get()

    if (docid=="" or dname == "" or dmob == "" or ddob == "" or ddpt == "" or dem == "") :
        tkinter.messagebox.showinfo("Insert Status" , "All Fields Necessary")
    else:
        con = mysql.connect(host = "localhost" , user = "root" , password = "krish10172003" , database="clinic")
        if con.is_connected():
            print("Success")
        cursor = con.cursor()
        query = "insert into doctors(D_ID , D_NAME , D_MOBILE, D_LANDLINE , D_DOB , D_SPECIAL , D_ADRESS , D_DEPT , D_EMAIL , D_DEGREES) " \
                "values({} , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}')"\
            .format( docid , dname , dmob ,dland ,ddob ,dsp ,dadr , ddpt ,dem , ddeg)
        cursor.execute(query)
        con.commit()
        tkinter.messagebox.showinfo("Insert Status:", "Inserted Succesfully")
        con.close( );


#===========================PAGE WINDOW===========================================

f = tkinter.Tk()
f.title("Hospital Management Software")
f.geometry("1540x800+0+0" )

l1 = tkinter.Label(f,bd=10,relief= "ridge" ,text="ADD DOCTOR", fg = "Black", bg = "White" , font =("Times New Roman",30,"bold") )
l1.pack(fill="x")

#========================================DATA FRAMES=======================================================

dftop = tkinter.Frame(f, bd=20, relief="ridge")
dftop.place(x=0, y = 70 , width = 1530 , height = 200)
df = tkinter.Frame(f, bd=20, relief="ridge")
df.place(x=0, y=200, width=1530, height=400)


dfleft = tkinter.Frame(df,bd=10,relief = "ridge")
l2 = tkinter.Label(dfleft , relief = "ridge" , text = "Input Details: " , font=("Times New Roman" , 12 , "bold"))
l2.grid(row=0,column=0)
dfleft.place(x=0,y=3,width=1490,height=355)



#==========================================ADDING DOCTORS===================================
d_id = tkinter.Label(dfleft , text = "Doctor ID: " , font = ("Arial" , 12) ,padx=2,pady=6 , height = 1)
d_id.grid(row=1,column=0)
d_ide = tkinter.Entry(dfleft , width = 30)
d_ide.grid(row = 1 , column =1)

d_nm = tkinter.Label(dfleft, text="Doctor Name: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_nm.grid(row=2, column=0)
d_nme = tkinter.Entry(dfleft, width=30)
d_nme.grid(row=2, column=1)

d_mb = tkinter.Label(dfleft, text="Doctor Mobile: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_mb.grid(row=3, column=0)
d_mbe = tkinter.Entry(dfleft, width=30)
d_mbe.grid(row=3, column=1)

d_ld = tkinter.Label(dfleft, text="Doctor Landline: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_ld.grid(row=4, column=0)
d_lde = tkinter.Entry(dfleft, width=30)
d_lde.grid(row=4, column=1)

d_dob = tkinter.Label(dfleft, text="Doctor DOB: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_dob.grid(row=5, column=0)
d_dobe = tkinter.Entry(dfleft, width=30)
d_dobe.grid(row=5, column=1)

d_sp = tkinter.Label(dfleft, text="Speciality: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_sp.grid(row=6, column=0)
d_spe = tkinter.Entry(dfleft, width=30)
d_spe.grid(row=6, column=1)

d_ad = tkinter.Label(dfleft, text="Doctor Address: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_ad.grid(row=7, column=0)
d_ade = tkinter.Entry(dfleft, width=30)
d_ade.grid(row=7, column=1)

d_dp = tkinter.Label(dfleft, text="Doctor Dept: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_dp.grid(row=8, column=0)
d_dpe = ttk.Combobox(dfleft, width=30)
d_dpe["values"]=("General" , "Neurologist" , "Cardiologist" , "Pediatrician" , "Dentist")
d_dpe.grid(row=8, column=1)

d_em = tkinter.Label(dfleft, text="Doctor Email: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_em.grid(row=1, column=2)
d_eme = tkinter.Entry(dfleft, width=30)
d_eme.grid(row=1, column=3)

d_dg = tkinter.Label(dfleft, text="Degrees: ", font=("Arial", 12), padx=2, pady=6, height=1)
d_dg.grid(row=2, column=2)
d_dge = tkinter.Entry(dfleft, width = 30)
d_dge.grid(row=2, column=3)



#=========================PAGE HOPPER BUTTONS======================================

hp = tkinter.Button(dftop, text="HOME PAGE", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1 , command = homep , width = 21)
hp.grid(row=0, column=2)

np = tkinter.Button(dftop, text="NEW PATIENT", bg='white', font=("Arial", 12, "bold") , command = newp, padx=2, pady=6, height=1 , width = 21)
np.grid(row=0, column=3)

ph = tkinter.Button(dftop, text="PATIENT SEARCH", bg='white', font=("Arial", 12, "bold"),command = pathist, padx=2, pady=6, height=1, width = 21)
ph.grid(row=0, column=4)

dd = tkinter.Button(dftop, text="DOCTOR DETAIL", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21, command = dsearch)
dd.grid(row=0, column=5)

nd = tkinter.Button(dftop, text="NEW DOCTOR", bg='white', font=("Arial", 12, "bold"), command = refresh , padx=2, pady=6, height=1, width = 21)
nd.grid(row=0, column=6)

pb = tkinter.Button(dftop, text="LOGOUT", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21, command = logout)
pb.grid(row=0, column=7)

rf = tkinter.Button(dftop, text="REFRESH", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=2, command = refresh,width = 21)
rf.grid(row=1, column=4)

ex = tkinter.Button(dftop, text="EXIT", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=2, command = exit,width = 21)
ex.grid(row=1, column=5)

#SUBMIT BUTTON
dfbot = tkinter.Frame(f,height = 55,width = 1360,  relief = 'ridge' ).place(x=0,y=600)
submit = tkinter.Button(f , bd = 4,text = "SUBMIT",font=("Arial", 12, "bold"), command = insert , relief = 'ridge', height = 2 , width = 14 , bg= 'white')
submit.place(x=590, y = 602)


#MAILOOP IS USED TO EXECUTE AND RUN THE GUI

f.mainloop()