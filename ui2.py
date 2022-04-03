import tkinter as tk
from tkinter import ttk
import keras
from keras.models import load_model
import numpy as np
model=load_model('model1.h5')

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
bg = PhotoImage(file = "img2.png")

# Create Canvas
canvas1 = Canvas( root, width = 800,
				height = 800)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

canvas1.create_text( 430, 50, text = "AI Police",font=('times', 50, ' bold '))
canvas1.create_text( 490, 120, text = "Enter the following information to get the idea of",font=('times', 20, ' bold '))
canvas1.create_text( 490, 145, text = "the index of difficulty in arresting.",font=('times', 20, ' bold '))
canvas1.create_text( 490, 176, text = "Latitude: Any value between 41 and 42.",font=('times', 15, ' bold ')) 
canvas1.create_text( 490, 193, text = "Longitude: Any value between -88 and -87",font=('times', 15, ' bold '))
canvas1.create_text( 490, 212, text = "Month of the year: Numbers from 1 to 12",font=('times', 15, ' bold '))
canvas1.create_text( 490, 231, text = "Day of the month: Numbers from 0 to 31",font=('times', 15, ' bold '))
canvas1.create_text( 490, 250, text = "Hour of the day: Numbers from 0 to 23",font=('times', 15, ' bold '))
canvas1.create_text( 490, 269, text = "Type of crime: Numbers from 1 to 31",font=('times', 15, ' bold '))
canvas1.create_text( 150, 300, text = "1-BATTERY\n2-OTHER OFFENSE\n3-ROBBERY\n4-NARCOTICS\n5-CRIMINAL DAMAGE\n6-WEAPONS VIOLATION\n7-THEFT\n8-BURGLARY\n9-MOTOR VEHICLE THEFT\n10-PUBLIC PEACE VIOLATION\n11-ASSAULT\n12-CRIMINAL TRESPASS\n13-CRIM SEXUAL ASSAULT\n14-INTERFERENCE WITH PUBLIC OFFICER\n15-ARSON\n16-DECEPTIVE PRACTICE\n17-LIQUOR LAW VIOLATION\n18-KIDNAPPING\n19-SEX OFFENSE\n20-OFFENSE INVOLVING CHILDREN\n21-PROSTITUTION\n22-GAMBLING\n23-INTIMIDATION\n24-STALKING\n25-OBSCENITY\n26-PUBLIC INDECENCY\n27-HUMAN TRAFFICKING\n28-CONCEALED CARRY LICENSE VIOLATION\n29-OTHER NARCOTIC VIOLATION\n30-HOMICIDE\n31-NON-CRIMINAL",font=('times', 10, 'bold'))

entry1 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(490, 300, window=entry1)
canvas1.create_text( 370, 300, text = "Latitude:",font=('times', 15, ' bold ')) 
entry2 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(490, 335, window=entry2)
canvas1.create_text( 370, 335, text = "Longitude:",font=('times', 15, ' bold '))
entry3 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(490, 370, window=entry3)
canvas1.create_text( 370, 370, text = "Month",font=('times', 15, ' bold ')) 
entry4= tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(490, 405, window=entry4)
canvas1.create_text( 370, 405, text = "Day:",font=('times', 15, ' bold ')) 
entry5 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(490, 440, window=entry5)
canvas1.create_text( 370, 440, text = "Hour:",font=('times', 15, ' bold '))
entry6 = tk.Entry (root,width=10,bg="white" ,fg="black",font=('times', 15, ' bold ')) 
canvas1.create_window(490, 475, window=entry6)
canvas1.create_text( 370, 475, text = "Crime Number:",font=('times', 15, ' bold '))


def getSquareRoot ():  
    x1 = entry1.get()
    x2= entry2.get()
    x3= entry3.get()
    x4= entry4.get()
    x5= entry5.get()
    x6=entry6.get()
    a=np.array([float(x1),float(x2),float(x4),float(x5),float(x3),float(x6)])
    data = a.reshape(-1,6)
    result=model.predict(data)
    result1=result[0][0]

    crim=['1-BATTERY','2-OTHER OFFENSE','3-ROBBERY','4-NARCOTICS','5-CRIMINAL DAMAGE','6-WEAPONS VIOLATION','7-THEFT','8-BURGLARY','9-MOTOR VEHICLE THEFT','10-PUBLIC PEACE VIOLATION','11-ASSAULT','12-CRIMINAL TRESPASS','13-CRIM SEXUAL ASSAULT','14-INTERFERENCE WITH PUBLIC OFFICER','15-ARSON','16-DECEPTIVE PRACTICE','17-LIQUOR LAW VIOLATION','18-KIDNAPPING','19-SEX OFFENSE','20-OFFENSE INVOLVING CHILDREN','21-PROSTITUTION','22-GAMBLING','23-INTIMIDATION','24-STALKING','25-OBSCENITY','26-PUBLIC INDECENCY','27-HUMAN TRAFFICKING','28-CONCEALED CARRY LICENSE VIOLATION','29-OTHER NARCOTIC VIOLATION','30-HOMICIDE','31-NON-CRIMINAL']
    label1 = tk.Label(root, text=result1,font=("Arial", 35),width=30,height=1)
    label1.configure(foreground="red",background="black")
    canvas1.create_window(450, 630, window=label1)
    
button1 = tk.Button(text='Check Arrest Difficulty Index',fg=fgcolor  ,bg=bgcolor,activebackground = "#CD5C5C" ,font=('times', 20, ' bold '), command=getSquareRoot)
canvas1.create_window(450, 550, window=button1)


# Execute tkinter
root.mainloop()