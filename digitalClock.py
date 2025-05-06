from tkinter import Label,Tk
import time 

appWindow = Tk()
appWindow.title("Digital Clock")
appWindow.geometry("160x120")
appWindow.resizable(1,1)
appWindow.configure(bg="black")

bg="black"
fg="white"
border_widht=20

#color ticket
label=Label(appWindow,font=("Boulder",18,),bg=bg,fg=fg)
label.grid(row=0,column=1,padx=10,pady=10)

#date ticket
dateLabel=Label(appWindow,font=("Boulder",18,),bg=bg,fg=fg)
dateLabel.grid(row=1,column=1,padx=10,pady=10)


def DigitalClock():
    #Clock
    timeLive=time.strftime("%H:%M:%S")
    label.config(text=timeLive)
    #Date
    dateInfo=time.strftime("%d %B %Y")
    dateLabel.config(text=dateInfo)
    label.after(200,DigitalClock)
    dateLabel.after(200,DigitalClock)
    
DigitalClock()

appWindow.mainloop()