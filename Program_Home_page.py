####### Imports #######
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
from PIL import Image, ImageDraw
import sv_ttk


####### Class Code #######

class Details:
   pass



####### Functions and Setup #######

def generate_legs():
   pass

def generate_arms():
   pass

def generate_chest():
   pass

#def menu defs
def go_to_homepage():
  root.destroy()
  import Program_Home_page

def go_to_datapage():
   root.destroy()
   import Program_Data_page

def go_to_informationpage():
   root.destroy()
   import Program_Information_page

####### GUI code #######

root = Tk()
root.geometry("640x960")
root.title("Home page")


title_frame = ttk.LabelFrame(root)
title_frame.grid(row = 0, column=1, pady= 10, padx = 10, sticky="N")

app_title = ttk.Label(title_frame,text="iGym", font=("Arial", 20))
app_title.grid(row= 1 ,column = 2 , sticky="NESW", pady= 5, padx = 20)

#Resize the image for logo 
#Open image
logo_pic = Image.open("DDT logo homepage.png")

#Resize image to 
resized = logo_pic.resize((50,50), Image.ANTIALIAS)
logo_final_pic = ImageTk.PhotoImage(resized)

#Paste image
logo_image_label = Label(title_frame, image=logo_final_pic)
logo_image_label.grid(row=1,column=1,padx=10,pady=7)


name = StringVar()
name = "John"
welcome_label_text = "Lets get started " + name + "!"

welcome_message = ttk.Label(root,text=welcome_label_text, font=("Arial", 24))
welcome_message.grid(row= 3 ,column = 1, sticky="NW", pady= 30, padx = 10)



legs_frame = ttk.LabelFrame(root)
legs_frame.grid(row=4, column=1)

legs_label_home = ttk.Label(legs_frame, text="Workout for Legs", wraplength=250)
legs_label_home.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Resize the image for legs (possible function)
#Open image
legs_pic = Image.open("Legs Image homepage.jpg")

#Resize image to 
resized = legs_pic.resize((250,170), Image.ANTIALIAS)
legs_final_pic = ImageTk.PhotoImage(resized)

#Paste image
legs_image_label = Label(root, image=legs_final_pic)
legs_image_label.grid(row=4,column=0, padx=10, pady= 5)


generate_button_legs = ttk.Button(legs_frame, text="Generate", command=generate_legs)
generate_button_legs.grid(row=2, column=1, columnspan=1)



arms_frame = ttk.LabelFrame(root)
arms_frame.grid(row=6, column=1)

arms_label_home = ttk.Label(arms_frame, text="Workout for Arms", wraplength=250)
arms_label_home.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#Resize the image for arms (possible function)
#Open image
arms_pic = Image.open("Arms Image homepage.jpg")

#Resize image to 
resized = arms_pic.resize((250,170), Image.ANTIALIAS)
arms_final_pic = ImageTk.PhotoImage(resized)

#Paste image
arms_image_label = Label(root, image=arms_final_pic)
arms_image_label.grid(row=6,column=0,padx=10, pady= 5)


generate_button_arms = ttk.Button(arms_frame, text="Generate", command=generate_arms)
generate_button_arms.grid(row=2, column=1, columnspan=1)



chest_frame = ttk.LabelFrame(root)
chest_frame.grid(row=7, column=1)

chest_label_home = ttk.Label(chest_frame, text="Workout for Chest", wraplength=250)
chest_label_home.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#Resize the image for chest (possible function)
#Open image
chest_pic = Image.open("Chest Image homepage.jpg")

#Resize image to 
resized = chest_pic.resize((250,170), Image.ANTIALIAS)
chest_final_pic = ImageTk.PhotoImage(resized)

#Paste image
chest_image_label = Label(root, image=chest_final_pic)
chest_image_label.grid(row=7,column=0, padx=10, pady= 5)


generate_button_arms = ttk.Button(chest_frame, text="Generate", command=generate_arms)
generate_button_arms.grid(row=2, column=1, columnspan=1)

#menu
menu_frame = ttk.Frame(root)
menu_frame.grid(sticky="NSEW", columnspan=1,column=1,row=8 ,pady = 60)

# Load the images for the menu items
data_image1 = Image.open("Data logo menu.png")
data_image1 = data_image1.resize((40, 40))
data_photo1 = ImageTk.PhotoImage(data_image1)

home_image2 = Image.open("DDT logo homepage.png")
home_image2 = home_image2.resize((40, 40))
home_photo2 = ImageTk.PhotoImage(home_image2)

information_image3 = Image.open("Information logo menu.png")
information_image3 = information_image3.resize((40, 40))
information_photo3 = ImageTk.PhotoImage(information_image3)

 # Create menu buttons with images
button1 = ttk.Button(menu_frame, image=data_photo1, command=go_to_datapage)
button1.grid(column=0,row=0)

button2 = ttk.Button(menu_frame, image=home_photo2, command=go_to_homepage)
button2.grid(column=1, row=0)

button3 = ttk.Button(menu_frame, image=information_photo3,command=go_to_informationpage)
button3.grid(column=2, row=0)

root.mainloop()


