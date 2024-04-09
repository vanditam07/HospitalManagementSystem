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
def newdoc():
        f.destroy()
        import ndoctor
def newp():
    f.destroy()
    import npatient
def dsearch():
    f.destroy()
    import dsearch
def pathist():
    f.destroy()
    import psearch
def refresh():
    f.destroy()
    import psearch

#======================================MYSQL-CONNECTIVITY===============================================

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("","end",values=i)
def patsearch():
    x = q.get()
    query = "SELECT * FROM P_DETAILS WHERE P_NAME LIKE '%"+x+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)
def clear():
    query = "SELECT * FROM P_DETAILS"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)
con = mysql.connect(host="localhost", user="root", password="krish10172003", database="clinic")
if con.is_connected():
    print("Success")
cursor = con.cursor()


#===========================HOME WINDOW===========================================

f = tkinter.Tk()
f.title("Hospital Management Software")
f.geometry("1540x800+0+0")
l1 = tkinter.Label(f,bd=10,relief= "ridge" ,text="PATIENT SEARCH", fg = "Black", bg = "White" , font =("Times New Roman",30,"bold") )
l1.pack(fill="x")

#==========================DATA FRAMES==============================================

pftop = tkinter.Frame(f, bd=20, relief="ridge")
pftop.place(x=0, y = 70 , width = 1530 , height = 200)
df = tkinter.Frame(f, bd=20, relief="ridge")
df.place(x=0, y=200, width=1530, height=400)
dfleft = tkinter.Frame(df,bd=10,relief = "ridge")
dfleft.place(x=0,y=0,width=1485,height=360)
pfbot = tkinter.Frame(f,height = 55,width = 1360,  relief = 'ridge' ).place(x=0,y=600)

#==========================TABLE==============================================


scroll_x = ttk.Scrollbar(dfleft, orient='horizontal')
scroll_y = ttk.Scrollbar(dfleft, orient='vertical')
trv= ttk.Treeview(dfleft, column = ("p_id" , "p_name", "p_mobile" , "p_land", "p_dob","p_father","p_mother"),
                  xscrollcommand=scroll_y.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side='bottom', fill='x')
scroll_y.pack(side='bottom', fill='y')
scroll_x=ttk.Scrollbar(command = trv.xview)
scroll_y=ttk.Scrollbar(command = trv.yview)

trv.heading("p_id", text = "Patient ID")
trv.heading("p_name", text = "Name")
trv.heading("p_mobile", text = "Mobile Number")
trv.heading("p_land", text = "Landline")
trv.heading("p_dob", text = "D.O.B")
trv.heading("p_father", text = "Father")
trv.heading("p_mother", text = "Mother")
trv["show"] = "headings"

trv.column("p_id", width = 25)
trv.column("p_name",width = 100)
trv.column("p_mobile", width = 100)
trv.column("p_land",width = 110)
trv.column("p_dob", width = 10)
trv.column("p_father", width = 100)
trv.column("p_mother", width = 100)

trv.place(x=5,y=35, width = 1450, height = 283)


query = "SELECT * FROM P_DETAILS"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

q = tkinter.StringVar()
l2 = tkinter.Label(dfleft , relief = "ridge" , text = "ENTER PATIENT NAME: " , font=("Times New Roman" , 15 , "bold") ,bd = 4)
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

#SEARCH & CLEAR BUTTON
submit = tkinter.Button(f , bd = 4,text = "SEARCH",font=("Arial", 12, "bold"), relief = 'ridge', height = 2 , width = 14 , bg= 'white', command = patsearch )
submit.place(x=400, y = 602)
clear = tkinter.Button(f, bd = 4, text= "CLEAR",font=("Arial", 12, "bold"), relief = 'ridge', height = 2 , width = 14 , bg= 'white', command = clear)
clear.place(x=800 , y=602)


f.mainloop()
