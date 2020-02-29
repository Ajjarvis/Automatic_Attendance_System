#import module from tkinter for UI
from tkinter import *
#from playsound import playsound
import os
from datetime import datetime;

#creating instance of TK
root=Tk()
root.configure(background="Powderblue")

#root.geometry("300x300")

def function1():
    
    os.system("py Create_dataset.py")
    
def function2():
    
    os.system("py Train_model.py")

def function3():

    os.system("py Face_Recognization.py")
    playsound('sound.mp3')

def function5():    
   os.startfile(os.getcwd()+"/developers/diet1frame1first.html");
   
def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#stting title for the window
root.title("Automatic Attendance System")

#creating a text label
Label(root, text="Fase Recognision based Attendance System",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Collect Sample",font=("lucida",18),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("lucida",18),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize & Attendance",font=('lucida',18),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('lucida',18),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating Exit button
Button(root,text="Exit",font=('lucida',18),bg="#0D47A2",fg="white",command=function6).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Developed by : Ajay Chaudhari.",font=("lucida",8),fg="black",bg="Powderblue",height=1).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
