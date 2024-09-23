from tkinter import * # Here we import everything from tkinter
from time import * # Here we import everything from the time module

def update(): # We make a function called update
    time_string = strftime("%I:%M:%S %p") # WE make time into a string these ketter represent hour minute second and its its pm or am
    time_label.config(text=time_string) # Here we configure our variable to have the time strings variable as our text


    day_string = strftime("%A") # Variable for our day down below
    day_label.config(text=day_string) # Puts it within our label

    date_string = strftime("%B %d, %Y") # variable for our Month Day and Year
    date_label.config(text=date_string) # Puts it within our label using config

    window.after(1000,update) # We want it to update every 1000 milliseconds

window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black") # Here we make our background font and letters colors
time_label.pack()

day_label = Label(window,font=("Ink Free",25),fg="#000000",bg="#EFEEEE")
day_label.pack()

date_label = Label(window,font=("Ink Free",25),fg="#000000",bg="#EFEEEE")
date_label.pack() # we pack it so it all shows at once necessary!

update()

window.mainloop() # We need this to actually open a window