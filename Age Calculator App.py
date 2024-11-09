
from tkinter import *
import datetime

# Create Window
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

# Frame
frame = Frame(master = root , height = 200 , width = 360 , bg = "#D2DCE6")

# Add labels
lbl1 = Label(frame , text = "Name" , bg = "#72383D" , fg = "#F2F2EB" , width = 12)
lbl2 = Label(frame , text = "Year" , bg = "#72383D" , fg = "#F2F2EB" , width = 12)
lbl3 = Label(frame , text = "Month" , bg = "#72383D" , fg = "#F2F2EB" , width = 12)
lbl4 = Label(frame , text = "Date" , bg = "#72383D" , fg = "#F2F2EB" , width = 12)

# Create text box for user to enter details
name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)

# Display the message
def calulate():
    name = name_entry.get()
    year = int(year_entry.get())
    today = datetime.date.today()
    age = today.year - year
    greet = f"Hi {name}!!"
    message = f"\nBcz of you being so dumb, i will tell you your age.\nYou are {age} years old stoopeed person"
    
    textbox.insert(END , greet)
    textbox.insert(END , message)
    
# Textbox to display mssg
textbox = Text(bg = "#9CABB4" , fg = "#401B1B")

# Add button
btn = Button(text = "Calculate" , command = calulate , bg = "#AB644B" , fg = "#401B1B")

# Arrange Everything
frame.place(x = 20 , y = 0)
lbl1.place(x = 20 , y = 20)
name_entry.place(x = 150 , y = 20)
lbl2.place(x = 20 , y = 50)
year_entry.place(x = 150 , y = 50)
lbl3.place(x = 20 , y = 80)
month_entry.place(x = 150 , y = 80)
lbl4.place(x = 20 , y = 110)
date_entry.place(x = 150 , y = 110)
btn.place(x = 140 , y = 210)
textbox.place(y = 250)

root.mainloop()