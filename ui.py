import tkinter as tk
from tkinter import ttk
import keras
from keras.models import load_model
import numpy as np
model=load_model('model.h5')

bgcolor="#F08080"
fgcolor="black"
# Import module 
# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("900x700")

# Add image file
bg = PhotoImage(file = "img.png")

# Create Canvas
canvas1 = Canvas( root, width = 800,
				height = 800)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

canvas1.create_text( 430, 50, text = "AI Police",font=('times', 50, ' bold '))
canvas1.create_text( 450, 120, text = "Enter the following information to get the idea of",font=('times', 20, ' bold '))
canvas1.create_text( 450, 145, text = "the type of crime that probably took place.",font=('times', 20, ' bold '))
canvas1.create_text( 450, 176, text = "Latitude: Any value between 41 and 42.",font=('times', 15, ' bold ')) 
canvas1.create_text( 450, 193, text = "Longitude: Any value between -88 and -87",font=('times', 15, ' bold '))
canvas1.create_text( 450, 212, text = "Month of the year: Numbers from 1 to 12",font=('times', 15, ' bold '))
canvas1.create_text( 450, 231, text = "Day of the month: Numbers from 0 to 31",font=('times', 15, ' bold '))
canvas1.create_text( 450, 250, text = "Hour of the day: Numbers from 0 to 23",font=('times', 15, ' bold '))

entry1 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(450, 300, window=entry1)
canvas1.create_text( 330, 300, text = "Latitude:",font=('times', 15, ' bold ')) 
entry2 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(450, 335, window=entry2)
canvas1.create_text( 330, 335, text = "Longitude:",font=('times', 15, ' bold '))
entry3 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(450, 370, window=entry3)
canvas1.create_text( 330, 370, text = "Month",font=('times', 15, ' bold ')) 
entry4= tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(450, 405, window=entry4)
canvas1.create_text( 330, 405, text = "Day:",font=('times', 15, ' bold ')) 
entry5 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(450, 440, window=entry5)
canvas1.create_text( 330, 440, text = "Hour:",font=('times', 15, ' bold '))

def getSquareRoot ():  
    x1 = entry1.get()
    x2= entry2.get()
    x3= entry3.get()
    x4= entry4.get()
    x5= entry5.get()
    a=np.array([float(x1),float(x2),float(x4),float(x5),float(x3)])
    data = a.reshape(-1,5)
    result=model.predict(data)
    result1=result[0][0]
    ans=(result1-6)*10
    ans=round(ans)
    crim=['BATTERY','OTHER OFFENSE','ROBBERY','NARCOTICS','CRIMINAL DAMAGE','WEAPONS VIOLATION','THEFT','BURGLARY','MOTOR VEHICLE THEFT','PUBLIC PEACE VIOLATION','ASSAULT','CRIMINAL TRESPASS','CRIM SEXUAL ASSAULT','INTERFERENCE WITH PUBLIC OFFICER','ARSON','DECEPTIVE PRACTICE','LIQUOR LAW VIOLATION','KIDNAPPING','SEX OFFENSE','OFFENSE INVOLVING CHILDREN','PROSTITUTION','GAMBLING','INTIMIDATION','STALKING','OBSCENITY','PUBLIC INDECENCY','HUMAN TRAFFICKING','CONCEALED CARRY LICENSE VIOLATION','OTHER NARCOTIC VIOLATION','HOMICIDE','NON-CRIMINAL']
    label1 = tk.Label(root, text=crim[ans],font=("Arial", 35),width=30,height=1)
    label1.configure(foreground="red",background="black")
    canvas1.create_window(450, 600, window=label1)
    
button1 = tk.Button(text='Which crime could it be at this location and time?',fg=fgcolor  ,bg=bgcolor,activebackground = "#CD5C5C" ,font=('times', 20, ' bold '), command=getSquareRoot)
canvas1.create_window(450, 500, window=button1)


# Execute tkinter
root.mainloop()
