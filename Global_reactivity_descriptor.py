#********************************************************************************************************
#------------This code is based on the theory of 
#------------Theoretical Aspects of Chemical Reactivity by Alejandro Toro-Labbe, 1st Ed. Nov 14, 2006).----
#********************************************************************************************************
import math
from math import*
import pandas as pd

from tkinter import *
window = Tk()
window.title("Calculation of global reactivity parameters")
window.geometry("600x650")
#window.config(bg='#9A9ACD')

label5 = Label(window, text = "Global reactivity parameters",fg='#000080',font=("Times New Roman",18)).place(x = 35,y = 10)
label7 = Label(window, text = "Results",fg='#000080',font=("Times New Roman",18)).place(x = 35,y = 150)
#label5.grid(padx=5,pady=10)
#------------------------------------------text1-------------------------------
label1 = Label(window, text = "Enter value of HOMO energy", fg='blue',font=("Times New Roman",14)).place(x = 35,y = 50)
#label1.grid(padx=5,pady=35)
label8 = Label(window, text = "in Hartree", fg='blue',font=("Times New Roman",14)).place(x = 460,y = 50)
label8 = Label(window, text = "in Hartree", fg='blue',font=("Times New Roman",14)).place(x = 460,y = 90)

label2 = Label(window, text = "Enter value of LUMO energy", fg='blue',font=("Times New Roman",14)).place(x = 35,y = 90)
#label2.grid(padx=5,pady=20)

data=StringVar()    #IntVar(), DoubleVar()
data1=StringVar()
data2=StringVar() 

textbox1=Entry(window,textvariable=data,fg='black',font=("Times New Roman",14)).place(x = 265,y = 50)
#textbox1.grid(padx=5,pady=35)

textbox2=Entry(window,textvariable=data1,fg='black',font=("Times New Roman",14)).place(x = 265,y = 90)
#textbox2.grid(padx=5,pady=20)
#------------------------------------code-----------------------------------------------------------------

import math

def myfunction():
    HOMO = data.get()
    LUMO = data1.get()
    HOMO1 = float(HOMO)
    LUMO1 = float(LUMO) 

#homo1 = float(input("\n Enter homo energy: "))
#lumo1 = float(input("\n Enter lumo energy: "))
#homo = -7.0994
#lumo = -1.3660

#in electonvolt
    homo=HOMO1*27.2114
    lumo=LUMO1*27.2114
    BG1=homo-lumo
    BG=-BG1
#print(homo)
#print(lumo)
    IP=homo
    EA=lumo
    CP=0.5*(IP+EA)
    Eta=0.5*(EA-IP)

    SIG=1/(2*Eta)

    OMEGA=CP**2*SIG

    KI=-CP

#print(CP, Eta, SIG, OMEGA)
#--------------------------------------------------output--------------------------------------------------
    emptylabel3.config(text="Homo energy of Molecule E_{HOMO}: %.2f"" eV\r\n" % homo)
    emptylabel4.config(text="Lumo energy of Molecule E_{LUMO}: %.2f"" eV\r\n" % lumo)
    emptylabel2.config(text="Energy band gap E_{HOMO-LUMO}: %.2f"" eV\r\n" % BG)
    emptylabel5.config(text="Chemical potential of Molecule (\u03BC): %.4f"" eV\r\n" % CP)
    emptylabel6.config(text="Chemical hardness of Molecule (\u03B7): %.4f"" eV\r\n" % Eta)
    emptylabel7.config(text="Chemical Softness of Molecule (\u03C3): %.4f"" eV\r\n" % SIG)
    emptylabel8.config(text="Electrophilicity of Molecule (\u03A9): %.4f"" eV\r\n" % OMEGA)
    emptylabel9.config(text="Elctronegativity of Molecule (\u03C7): %.4f"" eV\r\n" % KI)

emptylabel3=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel3.place(x = 35,y = 190)

emptylabel4=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel4.place(x = 35,y = 220)

emptylabel2=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel2.place(x = 35,y = 250)


emptylabel5=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel5.place(x = 35,y = 280)

emptylabel6=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel6.place(x = 35,y = 310)

emptylabel7=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel7.place(x = 35,y = 340)

emptylabel8=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel8.place(x = 35,y = 370)

emptylabel9=Label(window,fg='green',font=("Times New Roman",14))
#emptylabel2.grid(row=8,column=1,sticky=W,pady=10)
emptylabel9.place(x = 35,y = 400)


def close():
    window.destroy()

button1=Button(window,command=myfunction,text="Submit",fg='blue',font=("Times New Roman",14)).place(x = 130,y = 450)
#button3=Button(window,command=cleartext,text="Clear",fg='blue',font=("Times New Roman",14)).place(x = 180,y = 360)
button4=Button(window,command=close,text="Exit",fg='blue',font=("Times New Roman",14)).place(x = 350,y = 450)
#button1.grid(row=9,column=1,sticky=W)

label7 = Label(window, text = "*************************************************",fg='#000080',font=("Times New Roman",18)).place(x = 5,y = 490)


label6 = Label(window, text = "The properties of interest are usually response functions with respect to \n perturbations as per the Koopmans’ approximation.",fg='#2F2F4F',font=("Times New Roman",14)).place(x = 10,y = 510)
label11 = Label(window, text = " For ex. chemical potential and the hardness are represented by derivatives of electronic properties.",fg='#2F2F4F',font=("Times New Roman",10)).place(x = 10,y = 560)
#button2=Button(window,text="click here",fg='blue',font=("Times New Roman",14)).place(x = 30,y = 470)
label10 = Label(window, text = "-------Theoretical Aspects of Chemical Reactivity by Alejandro Toro-Labbe, \n 1st Ed. Nov 14, 2006)-------", fg='#4A4A70',font=("Times New Roman",12)).place(x = 50,y = 600)


window.mainloop()
#********************************************************************************************************************************************************************
