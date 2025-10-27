from tkinter import *
from datetime import date

def calculate_age():
    name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))

    result_label.config(text=f"Hi {name}! You are {age} years old.")

window = Tk()
window.title("Age Calculator App")
window.geometry("400x400")

title_label = Label(window, text="Enter your details below:")
title_label.pack(pady=10)

name_label = Label(window, text="Name:")
name_label.pack()

name_entry = Entry(window)
name_entry.pack(pady=5)


day_label = Label(window, text="Date (DD):")
day_label.pack()

day_entry = Entry(window)
day_entry.pack(pady=5)


month_label = Label(window, text="Month (MM):")
month_label.pack()

month_entry = Entry(window)
month_entry.pack(pady=5)


year_label = Label(window, text="Year (YYYY):")
year_label.pack()

year_entry = Entry(window)
year_entry.pack(pady=5)


calc_button = Button(window, text="Calculate Age", command=calculate_age, bg="#4CAF50", fg="white", width=20)
calc_button.pack(pady=15)

result_label = Label(window)
result_label.pack(pady=10)

window.mainloop()