from tkinter import *
import customtkinter
import time

def change_scale(value):
    time.sleep(1)
    new_scale = float(value)
    customtkinter.set_window_scaling(new_scale)

window = customtkinter.CTk()
window.geometry("300x300")

scale_label = customtkinter.CTkLabel(window, text="Scale:")
scale_label.pack()

scale_slider =customtkinter.CTkSlider(window, from_=0.5, to=3, command=change_scale, number_of_steps=25, width=150)
scale_slider.set(1)
scale_slider.pack()

window.mainloop()