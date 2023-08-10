from tkinter import *
import tkinter as tk
import customtkinter
import time

root = tk.Tk()
root.geometry("200x150")

label = tk.Label(root, text = "Hello World")
label.pack(padx = 5, pady = 5)

def change(value):
    label.config(font=(12*value))
    print(value)

def scale(value):
    if value >= 1 and value <= 1.2:
        value = 1.1
        change(value)
    if value >= 1.2 and value <= 1.3:
        value = 1.2
        change(value)
    if value >= 1.3 and value <= 1.4:
        value = 1.3
        change(value)
        
def slider_event(value):
    time.sleep(1)
    scale(value)

slider = customtkinter.CTkSlider(root, from_=1, to=1.5, command=slider_event).place(x=50, y=50)


root.mainloop()