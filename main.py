#=========================IMPORTING MODULES========================================
import tkinter
from PIL import ImageTk, Image

#=========================PAGE HOPPER FUNCTIONS======================================

def homep():
    f.destroy()
    import main
def newpat():
    f.destroy()
    import npatient
def newdoc():
    f.destroy()
    import ndoctor
def pathist():
    f.destroy()
    import psearch
def refresh():
    f.destroy()
    import main
def logout():
    f.destroy()
    import login
def dsearch():
    f.destroy()
    import dsearch


#===========================HOME WINDOW===========================================

f = tkinter.Tk()
f.title("Hospital Management Software")
f.geometry("1540x800+0+0")
l = tkinter.Label(f,bd=20,relief= "ridge" ,text="CHECKUP CLINIC", fg = "Black", bg = "Grey" , font =("Times New Roman",35,"bold") )
l.pack(fill = 'x')

#==========================DATA FRAMES============================================

dftop = tkinter.Frame(f, bd=15, relief="ridge")
dftop.place(x=0, y=93, width=1530, height=200)

df = tkinter.Frame(f, bd=20, relief="ridge")
df.place(x=0, y=200, width=1530, height=400)
dfleft = tkinter.Frame(df,bd=10,relief = "ridge")
l2 = tkinter.Label(dfleft , relief = "ridge" , text = "WELCOME" , font=("Times New Roman" , 30 , "bold")).pack(fill = 'x')
dfleft.place(x=0,y=5,width=750,height=350)

#ADDING INTRODUCTRY TEXT
txt = tkinter.Text(dfleft , bd = 4, height = 12, width = 65, font = ("Arial" , 14) ,relief = 'ridge'  )
txt.insert('2.0','Welcome USER \n \n')
txt.insert('3.0','This software was was made using tkitner module in Python along with a database    made in MySQL \n')
txt.insert('4.0','Its purpose is to manage and organize the data used in a hospital \n')
txt.insert('7.0','Btech CSE Core \n')
txt.insert('8.0','A1 Section \n')
txt.insert('9.0','Made by: Vandita Maloo')

txt.place(y = 50 , x = 0)


dfright = tkinter.Frame(df ,bd = 5 ,relief = "ridge")
dfright.place(x=750, y=7, width=730, height=350)
load= Image.open("C:\Krish Mehta\SRM SEM 1\PPS\python shit\hospitalimage.jpg")
render = ImageTk.PhotoImage(load)
img = tkinter.Label(dfright, image=render)
img.pack()


#=========================PAGE HOPPER BUTTONS======================================


hp = tkinter.Button(dftop, text="HOME PAGE", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1 , command = homep , width = 21)
hp.grid(row=0, column=2)

np = tkinter.Button(dftop, text="NEW PATIENT", bg='white', font=("Arial", 12, "bold") , command = newpat, padx=2, pady=6, height=1 , width = 21)
np.grid(row=0, column=3)

ph = tkinter.Button(dftop, text="PATIENT SEARCH", bg='white', font=("Arial", 12, "bold"),command = pathist, padx=2, pady=6, height=1, width = 21)
ph.grid(row=0, column=4)

dd = tkinter.Button(dftop, text="DOCTOR DETAIL", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21, command = dsearch)
dd.grid(row=0, column=5)

nd = tkinter.Button(dftop, text="NEW DOCTOR", bg='white', font=("Arial", 12, "bold"), command = newdoc , padx=2, pady=6, height=1, width = 21)
nd.grid(row=0, column=6)

pb = tkinter.Button(dftop, text="LOGOUT", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=1, width = 21, command = logout)
pb.grid(row=0, column=7)

rf = tkinter.Button(dftop, text="REFRESH", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=2, command = refresh,width = 21)
rf.grid(row=1, column=4)

ex = tkinter.Button(dftop, text="EXIT", bg='white', font=("Arial", 12, "bold"), padx=2, pady=6, height=2, command = exit,width = 21)
ex.grid(row=1, column=5)




#MAILOOP IS USED TO EXECUTE AND RUN THE GUI

f.mainloop()