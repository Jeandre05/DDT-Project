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

#menu defs
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
root.title("Data page")


info_title = ttk.Label(root, text= "Information:", font=("Helvetica", 30)) #underline
info_title.grid(row=0, column=1, columnspan=3, padx=10, pady=20, sticky="N")

#Resize the image for logo 
#Open image
logo_pic = Image.open("DDT logo homepage.png")
#Resize image to 
resized = logo_pic.resize((50,50), Image.ANTIALIAS)
logo_final_pic = ImageTk.PhotoImage(resized)
#Paste image
logo_image_label = Label(root, image=logo_final_pic)
logo_image_label.grid(row=0,column=3,pady=7)


top_frame = ttk.LabelFrame(root)
top_frame.grid(row = 1, column=1, columnspan=3, sticky="NE", padx=70)

catagory_label = ttk.Label(top_frame,text="Catagory:", font=("Helvetica", 18))
catagory_label.grid(row=0, column=0 , padx=20, pady=5)

workout_label = ttk.Label(top_frame,text="Workout:", font=("Helvetica", 18))
workout_label.grid(row=0, column=2 , padx=20, pady=5)

generate_button = ttk.Button(top_frame,text="Generate")
generate_button.grid(row=2, column=1)

#create a drop down box for catagories
categories = ["Legs", "Arms", "Chest"]
category_combobox = ttk.Combobox(top_frame, values=categories)
category_combobox.grid(row=1, column=0, padx=10, pady=10)

#create a drop down box for catagories
#workouts set for now (objects later)
workouts = ["Legs", "Arms", "Chest"]
workouts_combobox = ttk.Combobox(top_frame, values=categories)
workouts_combobox.grid(row=1, column=2, padx=10, pady=10)

#menu
menu_frame = ttk.Frame(root)
menu_frame.grid(sticky="NE",column=1,row=8 ,pady = 60)

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

button2 = ttk.Button(menu_frame, image=home_photo2,command=go_to_homepage)
button2.grid(column=1, row=0)

button3 = ttk.Button(menu_frame, image=information_photo3, command=go_to_informationpage)
button3.grid(column=2, row=0)

root.mainloop()

