from tkinter import *

# Create a new window

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold")) # font is a settings tuple
my_label.pack() # Automatically place and center the element on the screen (geometry_management mechanism) side="bottom", "left"/"right" expand ...
# Centered by default

my_label["text"] = "New text"
# OR
my_label.config(text="New Text")

# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{entry.get()}")

button = Button(text="Click Me", command=button_clicked) # Do an action whan clicked (Interactivity)
button.pack()

# Entry component

entry = Entry(width=10)
entry.pack()
entry.insert(END, string="Initial Text")

# Textbox

text = Text(height=5, width=30)
text.focus() # Put cursor in textbox.
text.insert(END, "Example of multi-line text entry.") # Add some text to begin with. #END is just an index
print(text.get("1.0", END)) # Get current value in textbox at line 1, character 0
text.pack()

# Spinbox

def spinbox_used():
    #gets the current value
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale

# Called with current scale value.
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton

def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton

def radio_used():
    print(radio_state.get())

#variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# mainloop that keeps the window on screen (This line need to be aét the end of the program)
window.mainloop()