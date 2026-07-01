from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
     password_list = []
     
     password_letter=[(choice(letters)) for char in range(randint(8, 10))]
     password_symbols=[choice(symbols) for char in range(randint(2, 4))]
     password_numbers=[choice(numbers) for char in range(randint(2, 4))]
     password_list= password_letter + password_symbols + password_numbers
     shuffle(password_list)
     
     password="".join(password_list)
     pass_entry.insert(0,password)

     pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
        if (len(web_entry.get())==0) or (len(mail_entry.get())==0) or (len(pass_entry.get())==0):
              messagebox.showinfo(title="Warning", message="Please fill the all details")

        else:
              is_ok= messagebox.askokcancel(title=web_entry.get(),message=f"These are the details entered: \nEmail: {mail_entry.get()} \nPassword: {pass_entry.get()} \nIs it okay to save?")
              if is_ok:
                with open("data.txt",mode="a") as file:
                    file.write(f"{web_entry.get()} | {mail_entry.get()} | {pass_entry.get()}\n")
                    web_entry.delete(0,END)
                    pass_entry.delete(0,END)
                    web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas= Canvas(height=200,width=200,highlightthickness=0)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)

#website
web_entry=Entry(width=40)
web_entry.focus()  #focues the cursor to this box (in the beginning)
web_entry.grid(column=1,row=1,columnspan=2)

#username
mail_entry=Entry(width=40)
mail_entry.insert(0,"sharma@gmail.com")
mail_entry.grid(column=1,row=2,columnspan=2)

#password
pass_entry=Entry(width=21)
pass_entry.grid(column=1,row=3)

#generate password button
generate=Button(text="Generate Password",width=15,command=generate_password)
generate.grid(column=2,row=3)

# add button
add=Button(text="Add",height=1,width=34,command=save)
add.grid(column=1,row=4,columnspan=2)

#website text label
web_text=Label(text="Website: ")
web_text.grid(column=0,row=1)

# username text label
username= Label(text="Email/Username: ")
username.grid(column=0,row=2)

# password text label
password= Label(text="Password: ")
password.grid(column=0,row=3)

window.mainloop()