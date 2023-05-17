####### Imports #######
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import sv_ttk

####### Class Code #######

class Details:
   pass



####### Functions and Setup #######

def login():
   pass

def sign_up():
   pass
####### GUI code #######

root = Tk()
root.geometry("640x960")
root.title("Login/Sign-up page")
sv_ttk.set_theme("dark")


##bg = PhotoImage(file = "")
##background_label = ttk.Label(root, image=bg)
##background_label.place(x=0, y=-20, relwidth=1, relheight=1)


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

password_entry = ttk.Entry(top_frame, textvariable = password_entred)
password_entry.grid(row=5, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

#command 
login_radio_button = ttk.Button(top_frame, text="Login", command=login)
login_radio_button.grid(row=6, column=0 ,pady=10, columnspan=2 )



#Resize the image for Return photo (possible function)
#Open image
#retrun_pic = Image.open("Place Holder Image.png")

#Resize image to 
#resized = retrun_pic.resize((250,170), Image.ANTIALIAS)
#return_final_pic = ImageTk.PhotoImage(resized)

#Paste image
#return_image_label = Label(root, image=return_final_pic)
#return_image_label.grid(row=7,column=2, pady= 5, columnspan=2, padx = 20)



###Split###



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

password_entry_signup = ttk.Entry(bottom_frame, textvariable = password_entred_signup)
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


#Resize the image for Return photo (possible function)
#Open image
#welcome_pic = Image.open("Place Holder Image.png")

#Resize image to 
#resized = welcome_pic.resize((250,170), Image.ANTIALIAS)
#welcome_final_pic = ImageTk.PhotoImage(resized)

#Paste image
#welcome_image_label = Label(root, image=welcome_final_pic)
#welcome_image_label.grid(row=10,column=2, pady= 5, columnspan=2, padx= 20)

root.mainloop()

