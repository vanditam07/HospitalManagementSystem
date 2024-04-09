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

def pathist():
    f.destroy()
    import psearch
def dsearch():
    f.destroy()
    import dsearch
def logout():
    f.destroy()
    import login
def txtfile():
    t = open("Medhistory.txt" , 'w')
def refresh():
    f.destroy()
    import dsearch

#===================================SEARCH FUNCTIONS=====================================================

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("","end",values=i)


def docsearch():
    x = q.get()
    query = "SELECT d_id , d_name, d_mobile , d_dept, d_dob,d_special,d_degrees FROM DOCTORS WHERE D_NAME LIKE '%"+x+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)
def clear():
    query = "SELECT d_id , d_name, d_mobile , d_dept, d_dob,d_special,d_degrees FROM DOCTORS"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)


#========================MYSQL CONNECTIVITY==================================================

con = mysql.connect(host="localhost", user="root", password="krish10172003", database="clinic")
if con.is_connected():
    print("Success")
cursor = con.cursor()

#===========================MAIN WINDOW===========================================

f = tkinter.Tk()
f.title("Hospital Management Software")
f.geometry("1540x800+0+0")
l1 = tkinter.Label(f,bd=10,relief= "ridge" ,text="DOCTOR DETAILS", fg = "Black", bg = "White" , font =("Times New Roman",30,"bold") )
l1.pack(fill="x")

# ===============DATA FRAMES==============================================
pftop = tkinter.Frame(f, bd=20, relief="ridge")
pftop.place(x=0, y = 70 , width = 1530 , height = 200)
df = tkinter.Frame(f, bd=20, relief="ridge")
df.place(x=0, y=200, width=1530, height=400)
dfleft = tkinter.Frame(df,bd=10,relief = "ridge")
dfleft.place(x=0,y=0,width=1490,height=360)




#=================================TABLE======================================

scroll_x = ttk.Scrollbar(dfleft, orient='horizontal')
scroll_y = ttk.Scrollbar(dfleft, orient='vertical')

trv= ttk.Treeview(dfleft, column = ("d_id" , "d_name", "d_mobile" , "d_dept", "d_dob","d_special","d_degrees"),
                  xscrollcommand=scroll_y.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side='bottom', fill='x')
scroll_y.pack(side='bottom', fill='y')
scroll_x=ttk.Scrollbar(command = trv.xview)
scroll_y=ttk.Scrollbar(command = trv.yview)
trv.heading("d_id", text = "Doctor ID")
trv.heading("d_name", text = "Name")
trv.heading("d_mobile", text = "Mobile Number")
trv.heading("d_dept", text = "Department")
trv.heading("d_dob", text = "D.O.B")
trv.heading("d_special", text = "Specialty")
trv.heading("d_degrees", text = "Degrees")
trv["show"] = "headings"

trv.column("d_id", width = 25)
trv.column("d_name",width = 100)
trv.column("d_mobile", width = 100)
trv.column("d_dept",width = 110)
trv.column("d_dob", width = 10)
trv.column("d_special", width = 100)
trv.column("d_degrees", width = 100)
trv.place(x=5,y=35, width = 1450, height = 283)


query = "SELECT d_id , d_name, d_mobile , d_dept, d_dob,d_special,d_degrees FROM DOCTORS"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#SEARCH LABEL
q = tkinter.StringVar()
l2 = tkinter.Label(dfleft , relief = "ridge" , text = "ENTER DOCTOR NAME: " , font=("Times New Roman" , 15 , "bold") ,bd = 4)
l2.place(x=0,y=0)
l3= tkinter.Entry(dfleft, bd=3, textvariable= q )
l3.place(x=250,y=5,width = 150, height = 25)



#=========================PAGE HOPPER BUTTONS======================================
hp = tkinter.Button(pftop, text="HOME PAGE", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1 , command = homep , width = 21)
hp.grid(row=0, column=2)

np = tkinter.Button(pftop, text="NEW PATIENT", bg='white', font=("Arial", 12, "bold") , command = newp, padx=2, pady=6, height=1 , width = 21)
np.grid(row=0, column=3)

ph = tkinter.Button(pftop, text="PATIENT SEARCH", bg='white', font=("Arial", 12, "bold"),command = refresh, padx=2, pady=6, height=1, width = 21)
ph.grid(row=0, column=4)

dd = tkinter.Button(pftop, text="DOCTOR DETAIL", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21,command = refresh)
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
submit = tkinter.Button(f , bd = 4,text = "SEARCH",font=("Arial", 12, "bold"), relief = 'ridge', height = 2 , width = 14 , bg= 'white', command = docsearch )
submit.place(x=400, y = 602)
clear = tkinter.Button(f, bd = 4, text= "CLEAR",font=("Arial", 12, "bold"), relief = 'ridge', height = 2 , width = 14 , bg= 'white', command = clear)
clear.place(x=800 , y=602)
f.mainloop()
