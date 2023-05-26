 email = email_entered.get()
     password = password_entred.get()

     with open("user_data.txt", "r") as file:
        for line in file:
            stored_email, stored_password = line.strip().split(",")
            if email == stored_email and password == stored_password:
                root.destroy()
                import Program_Home_page
                return
            

def login():
    email = email_entered.get()
    password = password_entred.get()

    with open("user_data.txt", "r") as file:
        for line in file:
            stored_email, stored_password = line.strip().split(",")
            if email == stored_email and password == stored_password:
                root.destroy()
                import Program_Home_page
                return
            








            ####### Imports #######
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import sv_ttk

####### Class Code #######

class User:
   def __init__(self, username, password, name, dob):
        self.username = username
        self.password = password
        self.name = name
        self.dob = dob
   
   def save_to_file(self):
      with open("user_data.txt", "a") as file:
         file.write(f"{self.username},{self.password},{self.name},{self.dob}\n")
   

####### Functions and Setup #######
###doesn't work###
def login(self, username, password):
    email = email_entered.get()
    password = password_entred.get()

    with open("user_data.txt", "r") as file:
     for line in file:
            stored_email, stored_password = line.strip().split(",")
            if email == stored_email and password == stored_password:
                root.destroy()
                import Program_Home_page


def sign_up():
    username = email_entry_signup.get()
    password = password_entry_signup.get()
    name = name_entered_signup.get()
    dob = dob_entered_signup.get()

    user = User(username, password, name, dob)
    user.save_to_file()
    root.destroy()
    import Program_Home_page




####### GUI code #######

root = Tk()
root.geometry("640x960")
root.title("Login/Sign-up page")
sv_ttk.set_theme("dark")

logo_image = PhotoImage(file="DDT Wireframe Homepage.png")
logo_label = ttk.Label(root, image=logo_image)
logo_label.grid(row=0, column= 1, columnspan=2, pady = 50, padx = "220")


top_frame = ttk.LabelFrame(root, text="Login")
top_frame.grid(row=7, column=1, padx=10, pady=10, sticky="N",columnspan=4)

email_label = ttk.Label(top_frame, text = "Email:", wraplength=250)
email_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
email_entered = StringVar()

email_entry = ttk.Entry(top_frame, textvariable = email_entered)
email_entry.grid(row=3, column=0, columnspan=2,padx=5, pady=5, ipadx = 45)

password_label = ttk.Label(top_frame, text = "Password:",wraplength=250)
password_label.grid(row=4, column=0, columnspan =2, padx=5, pady=5, rowspan=1)
password_entred = StringVar()

password_entry = ttk.Entry(top_frame, textvariable = password_entred, show="*")
password_entry.grid(row=5, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

#command 
login_radio_button = ttk.Button(top_frame, text="Login", command=login)
login_radio_button.grid(row=6, column=0 ,pady=10, columnspan=2 )

bottom_frame = ttk.LabelFrame(root, text="Sign-Up")
bottom_frame.grid(row=10, column=1, pady=10, sticky="N", padx=220)

email_label_signup = ttk.Label(bottom_frame, text = "Email:", wraplength=250)
email_label_signup.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
email_entered_signup = StringVar()

email_entry_signup = ttk.Entry(bottom_frame, textvariable = email_entered_signup)
email_entry_signup.grid(row=1, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

password_label_signup = ttk.Label(bottom_frame, text = "Password:", wraplength=250)
password_label_signup.grid(row=2, column=0, columnspan =2, padx=5, pady=5)
password_entred_signup = StringVar()

password_entry_signup = ttk.Entry(bottom_frame, textvariable = password_entred_signup, show="*")
password_entry_signup.grid(row=3, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

name_label_signup = ttk.Label(bottom_frame,text="Name:", wraplength=250)
name_label_signup.grid(row=4 ,column=0, columnspan =2, padx=5, pady = 5)
name_entered_signup = StringVar()

name_entry_signup = ttk.Entry(bottom_frame, textvariable=name_entered_signup)
name_entry_signup.grid(row=5, column=0, padx= 5, pady =5 , ipadx = 45)

dob_label_signup = ttk.Label(bottom_frame,text="Date of birth:", wraplength=250)
dob_label_signup.grid(row=6 ,column=0, columnspan =2, padx=5, pady = 5)
label_under_dob = ttk.Label(bottom_frame, text="Day/Month/Year", font=("Helvetica", 12))
label_under_dob.grid(row = 7, pady=4)

# Change the font size of the label's text
label_under_dob.config(font=("Helvetica",8))
dob_entered_signup = StringVar()

dob_entry_signup = ttk.Entry(bottom_frame, textvariable=dob_entered_signup)
dob_entry_signup.grid(row=8, column=0, padx= 5, pady =5 , ipadx = 45)

#command 
signup_button = ttk.Button(bottom_frame, text="Sign-Up", command=sign_up)
signup_button.grid(row=9, column=0 ,pady=10, columnspan=2 )

root.mainloop()

