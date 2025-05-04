import tkinter

def button1_clicked():
    print("button1_clicked")

def button2_clicked():
    print("button2_clicked")

# Create a new window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons
button = tkinter.Button(text="Button", command=button1_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button2_clicked)
new_button.grid(column=2, row=0)

# Entry component
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()