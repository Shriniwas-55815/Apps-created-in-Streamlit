from tkinter import *
from tkinter import messagebox

# Configuration
root = Tk()
root.title("Count App")
root.configure(bg="blue")
root.geometry("500x300")
root.resizable(False, False)

# Counter variable
counter = IntVar(value=0)  # Initialize counter with a default value of 0

# Functions
def increment():
    counter.set(counter.get() + 1)

def decrement():
    counter.set(counter.get() - 1)
    
def reset():
    counter.set(0)

# Labeling
Label(
    root, 
    text="VEHICLE COUNTING SYSTEM", 
    font=("arial 25 bold"), 
    fg="white", 
    bg="blue", 
    border=2
).grid(row=0, column=0, columnspan=3, pady=20)

Label(
    root, 
    text="@This App is Build by Shriniwas Uttarkar", 
    font=("arial 10 bold"), 
    fg="black", 
    bg="blue", 
    border=2
).grid(row=10, column=0, columnspan=3, pady=10)

# Entry Widget for Display
Entry(
    root, 
    textvariable=counter, 
    fg="green",
    font=("arial 25 bold"), 
    justify="center", 
    state="readonly"
).grid(row=2, column=0, columnspan=3, pady=20)

# Buttons
Button(
    root, 
    text="Increment +1", 
    font=("Comic Sans MS", 15, "bold"), 
    fg="white", 
    bg="black", 
    border=2, 
    command=increment
).grid(row=4, column=0, padx=10)

Button(
    root, 
    text="RESET", 
    font=("Comic Sans MS", 10, "bold"), 
    fg="white", 
    bg="black", 
    border=2, 
    command=reset
).grid(row=4, column=1, padx=10)

Button(
    root, 
    text="Decrement -1", 
    font=("Comic Sans MS", 15, "bold"), 
    fg="white", 
    bg="black", 
    border=2, 
    command=decrement
).grid(row=4, column=2, padx=10)

# Main View
root.mainloop()
