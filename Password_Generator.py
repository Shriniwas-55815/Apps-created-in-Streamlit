from tkinter import *
from tkinter import messagebox
import random, string
import pyperclip

root = Tk()
root.configure(bg="lightblue")  # Set background color
root.geometry("400x400")
root.resizable(0,0)
root.title("PYTHON PROJECT - PASSWORD GENERATOR")


def generator():
    try:
        leng = int(pass_len.get())
        if leng < 8:
            messagebox.WARNING("Please Set your Password Lentht Between 8 to 22")
        messagebox.Message("Password Generated Sucessfully!!")
        characters = string.ascii_letters + string.digits + string.punctuation
        pass_str = ''.join(random.choice(characters) for _ in range(leng))

        pasw.delete(0, END)
        pasw.insert(0, pass_str)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")
        
            
def Copy_password():
    pyperclip.copy(pass_str.get())
    pasw.delete(0, END)
    

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold',bg="lightblue").pack()
Label(root, text='Python', font='arial 10').pack(side=BOTTOM)


pass_label = Label(root, text='SELECT YOUR PASSWORD LENGTH', font='arial 10 bold',bg="lightblue").pack()
pass_len = IntVar()
length = Spinbox(root, from_=8 , to_=22, textvariable=pass_len, width=25,bg="white").pack(pady=20)

pass_str = StringVar()

Button(root, text= "Generate Password", command=generator,bg="lightgreen",width=15, height=2).pack(pady=10)
pasw =Entry(root, textvariable=pass_str)
pasw.pack()
Button(root, text= "Copy Password to Clipboard", command=Copy_password,bg="lightgreen").pack(pady=10)





# Main Window
root.mainloop()