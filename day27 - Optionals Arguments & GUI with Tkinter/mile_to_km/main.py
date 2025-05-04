from tkinter import *

def button_clicked():
    result_km = convert_to_km(miles_entry.get())
    km_result_label.config(text=f"{result_km}") 

def convert_to_km(miles_input):
    miles = float(miles_input)
    return miles * 1.609

# Create a new window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=30)
window.config(padx=20,pady=20)

#Entry
miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)
miles_entry.insert(END, string="")

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

is_equal_label = Label(text=f"is equal to ")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Button
button_calculate = Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row=3)

window.mainloop()