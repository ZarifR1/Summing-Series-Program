import tkinter as tk
from tkinter import *                                                                        #   Importing essential packages for the program
import googletrans
import textblob
from tkinter import ttk, messagebox 
import customtkinter
import time

def summing_series():
    def clear():                                                                            #   Function to clear inputs and outputs
        sequence.configure(state="normal")
        sequence.delete(1.0,END)
        sequence.configure(state="disabled")
        space=customtkinter.CTkLabel(root,text="                                                                      ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)
        entry1.delete(0,END)                                                                
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END) 
        radio1.deselect()
        radio2.deselect()                                                                  #   Making the program into a recallable function for increased stability and performance
        

    def switch():                                                                           #   Switches themes
        global theme, current_theme, theme_accent, bg_colour, fg_colour, text_colour        #   Allows these variables to be used anywhere                   
        current_theme = root.cget("background")                                             #   Recieves the colour of the background
        if current_theme == "gray14":                                                       #   Checks which theme the progam is running
            theme = "light"                                                                 #   Switches to the theme it isn't running
            theme_accent = "gray92"                                                         #   The colour palette of the different themes
            bg_colour = "grey86"                                                            #   Number next to colour is the darkness, lower is darker
            fg_colour = "grey70"
            text_colour = "black"
            
        else:
            theme = "dark"
            theme_accent = "gray14"
            bg_colour = "grey17"
            fg_colour = "grey35"
            text_colour = "white"

        root.config(bg=theme_accent)
        customtkinter.set_appearance_mode(theme)                                            #    Updating all GUI text, this includes the colour scheme
        label1.configure(bg_color=bg_colour, fg_color=fg_colour)
        label2.configure(bg_color=bg_colour, fg_color=fg_colour)
        label3.configure(bg_color=bg_colour, fg_color=fg_colour)
        label4.configure(bg_color=bg_colour, fg_color=fg_colour)    
        label5.configure(bg_color=bg_colour, fg_color=fg_colour)
        radio1.configure(bg_color=bg_colour, fg_color=fg_colour)
        radio2.configure(bg_color=bg_colour, fg_color=fg_colour)
        clear_button.configure(bg_color=bg_colour)
        entry1.configure(bg_color=bg_colour, fg_color=fg_colour)
        entry2.configure(bg_color=bg_colour, fg_color=fg_colour)
        entry3.configure(bg_color=bg_colour, fg_color=fg_colour)
        entry4.configure(bg_color=bg_colour, fg_color=fg_colour)
        sequence.configure(bg_color=bg_colour, fg_color=fg_colour)
        label6.configure(bg_color=bg_colour, fg_color=fg_colour)
        space=customtkinter.CTkLabel(root,text="                                                                      ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)
        key_1.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_2.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_3.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_4.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_5.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_6.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_7.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_8.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_9.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_0.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_delete.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        key_clear.configure(bg_color=bg_colour, fg_color=fg_colour, text_color=text_colour)
        label7.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        label8.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        radio_First_term.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        radio_Increment.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        radio_Num_Terms.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        switch_button.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        expand_button.configure(bg_color=bg_colour,fg_color=fg_colour, text_color=text_colour)
        translate_GUI.configure(bg_color=bg_colour)
        res_slider.configure(bg_color=bg_colour, fg_color=fg_colour)
        frame1.configure(bg_color=theme_accent)
        translated_combo.configure(bg_color=bg_colour, fg_color=fg_colour)
        
        clear()                                                                            #   Unsure why this fixes the code
    
    def expand(state_gui):                                                                 #    Expands the GUI to show the keypad, translator and theme changer
        if state_gui == 0:
            root.geometry("1000x620")
            root.maxsize(width=1000, height=620)
            root.minsize(width=1000, height=620)
            expand_button.configure(text="\u2190",command=lambda: expand(1))
        else:
            root.geometry("550x620")
            root.maxsize(width=550, height=620)
            root.minsize(width=550, height=620)
            expand_button.configure(text="\u2192",command=lambda:expand(0))
            
    def scale(value):
        global new_scale
        time.sleep(1)
        new_scale = round(value,1)
        customtkinter.set_window_scaling(new_scale)
        customtkinter.set_widget_scaling(new_scale)
        text = Res_mod+" "+str(new_scale)+"x"
        label8.configure(text=text)
        

    root=customtkinter.CTk()                                                                               #   creating GUI window
    root.title("Summing Series")
    root.geometry("550x620") 
    root.maxsize(width=550, height=620)
    root.minsize(width=550, height=620)                                                               #   Assigns the resolution of this window
    root.config(bg=theme_accent)                                                            #   Sets the background colour
    frame1 = customtkinter.CTkFrame(master=root, bg_color=theme_accent, corner_radius=30)
    frame1.pack(pady=20, padx=50, fill="both", expand=True)                                 #   Adds a frame to the program
    customtkinter.set_appearance_mode(theme)                                                #   Sets the theme, predefined themes can be set at the bottom of the code
    root.resizable(0,0)

    global label1, label2, label3, label4, label5                                                                            #   Makes variable accessible from anywhere
    label1=customtkinter.CTkLabel(root,text=First_term, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6, width=150)             #   Creating Labels to inform user
    label2=customtkinter.CTkLabel(root,text=Increment, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6, width=150)              #   fg_colour = colour of the background of the button
    label3=customtkinter.CTkLabel(root,text=Num_of_terms, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6, width=150)           #   bg_colour = the background colour of the rounded edges
    label4=customtkinter.CTkLabel(root,text=Series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6, width=80)                 #   corner_radius = roundness of the corners
    label5=customtkinter.CTkLabel(root,text=Sum_of_series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6, width=80)
    
    sequence=customtkinter.CTkTextbox(root, width=290, height=250, corner_radius=15, fg_color=fg_colour, bg_color=bg_colour)                                                  #   Creating series and sum of series
    sequence.place(x=x6+15,y=y5)
    sequence.configure(state="disabled")

    label1.place(x=x1,y=y1)                                                                 #   Placing labels on window
    label2.place(x=x1,y=y2)
    label3.place(x=x1,y=y3)
    label4.place(x=x5,y=y5)
    label5.place(x=x5,y=y8)

 
    entry1=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)                #   Creating entries for user to enter values
    entry2=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)
    entry3=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)

    entry1.place(x=x2,y=y1)                                                                 #   Placing entries on window
    entry2.place(x=x2,y=y2)
    entry3.place(x=x2,y=y3)
    
    
    def clear_entry():
        entry4.delete(0,  END)
        
    def choose_first_term():
        entry1.delete(0,END)
        entry1.insert(0, entry4.get())
        clear_entry()
        radio_Increment.deselect()
        radio_Num_Terms.deselect()

    def choose_increment():
        entry2.delete(0,END)
        entry2.insert(0, entry4.get())
        clear_entry()
        radio_First_term.deselect()
        radio_Num_Terms.deselect()

    def choose_num_terms():
        entry3.delete(0,END)
        entry3.insert(0, entry4.get())
        clear_entry()
        radio_First_term.deselect()
        radio_Increment.deselect()

    def insert_entry(number):
        current=entry4.get()
        entry4.delete(0,END)
        entry4.insert(0,str(current)+str(number))
        
    def delete_entry():
        i = len(entry4.get())
        entry4.delete(i-1)
        
    
    
    entry4=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)                                                                            # Entry for the key pad written term
    entry4.place(x=675-15, y =145)
    
    label7=customtkinter.CTkLabel(root,text=Choose_entry_text,bg_color=bg_colour,fg_color=fg_colour,corner_radius=6)                         #   Entry box selection label
    label7.place(x=650+10,y=50)
    
    label8 = customtkinter.CTkLabel(root, text="Resolution Modifier: 1x", fg_color=fg_colour , corner_radius=6, bg_color=bg_colour, width=150)
    label8.place(x=750,y=430)

    radio_First_term=customtkinter.CTkRadioButton(root,text=First_term,command=choose_first_term,bg_color=bg_colour,fg_color=fg_colour,corner_radius=15)                  #    Entry box selection radiobuttons
    radio_First_term.place(x=550,y=100)

    radio_Increment=customtkinter.CTkRadioButton(root,text=Increment,command=choose_increment,bg_color=bg_colour,fg_color=fg_colour,corner_radius=15)
    radio_Increment.place(x=670,y=100)

    radio_Num_Terms=customtkinter.CTkRadioButton(root,text=Num_of_terms,command=choose_num_terms,bg_color=bg_colour,fg_color=fg_colour,corner_radius=15)
    radio_Num_Terms.place(x=780,y=100)

    key_1=customtkinter.CTkButton(root,text="1",width=100, height=40, font=("ariel", 18), bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(1) )                                                #   Keypad numbers
    key_1.place(x=570,y=150+40)

    key_2=customtkinter.CTkButton(root,text="2",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(2) )
    key_2.place(x=675,y=150+40)

    key_3=customtkinter.CTkButton(root,text="3",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(3) )
    key_3.place(x=780,y=150+40)

    key_4=customtkinter.CTkButton(root,text="4",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(4) )
    key_4.place(x=570,y=183+53)

    key_5=customtkinter.CTkButton(root,text="5",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(5) )
    key_5.place(x=675,y=183+53)

    key_6=customtkinter.CTkButton(root,text="6",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(6) )
    key_6.place(x=780,y=183+53)

    key_7=customtkinter.CTkButton(root,text="7",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(7) )
    key_7.place(x=570,y=216+66)

    key_8=customtkinter.CTkButton(root,text="8",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(8) )
    key_8.place(x=675,y=216+66)

    key_9=customtkinter.CTkButton(root,text="9",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(9) )
    key_9.place(x=780,y=216+66)

    key_0=customtkinter.CTkButton(root,text="0",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=lambda:insert_entry(0) )
    key_0.place(x=675,y=249+79)

    key_delete=customtkinter.CTkButton(root,text="DEL",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=delete_entry )
    key_delete.place(x=780,y=249+79)
    
    key_clear=customtkinter.CTkButton(root,text="AC",width=100,height=40,font=("ariel", 18),bg_color=bg_colour,fg_color=fg_colour, command=clear_entry )
    key_clear.place(x=570,y=249+79)

    def validation(Msg,check):                                                                       #   Checks if the entry input is valid
        global conitnue, a, n, d
        sequence.configure(state="normal")
        sequence.delete(1.0, END)
        if check == 0:
            try:
                a, d, n = float(entry1.get()), float(entry2.get()), int(entry3.get())
                if n <= 0:
                    sequence.insert(1.0, text=Msg)
                    sequence.configure(text_color= "red", state="disabled", font=("REM",17))
                    conitnue=1
                if n >= 30000:
                    sequence.delete(1.0, END)
                    sequence.insert(1.0, text=Math_Error)
                    sequence.configure(text_color= "red", state="disabled", font=("REM",17))
                    conitnue=1
                else: 
                    conitnue = 0
            except ValueError:
                sequence.insert(1.0, text=Msg)
                sequence.configure(text_color= "red", state="disabled", font=("REM",17))
                conitnue = 1
        else:
            pass
    
    def translate():
        global Error_msg, Res_mod, Math_Error                                               #   Function to translate languages
        try:                                                                                #   Get the languages from Dictionary Keys
            for key, value in languages.items():                                            #   Get the From Language key
                if (value == original_combo.get()):
                    from_language_key=key
            for key,value in languages.items():                                             #   Get the To Language key
                if (value ==translated_combo.get()):
                    to_language_key=key
            
            if translated_combo.get() == "english":                                         #   English can't be translated to english
                label1.configure(text = "First term")                                   #   so english is the only language that was
                label2.configure(text = "Increment")                                    #   manually written
                label3.configure(text = "Number of terms")
                label4.configure(text = "Series")                                       #   The text is changed instead of replaced
                label5.configure(text = "Sum")                                          #   which gives the program increased performance
                radio1.configure(text = "Arithmetic Progression", font=("ariel",13))   
                radio2.configure(text = "Geometric Progression")
                clear_button.configure(text = "Clear")
                root.title("Summing Series")
                Error_msg="Please check entries and try again"
                validation(Error_msg,1)
                translate_GUI.configure(text="Translate text")
                switch_button.configure(text= "Switch theme")
                label6.configure(text="Translated Language")
                radio_First_term.configure(text="First term", font=("ariel", 13))
                radio_Increment.configure(text="Increment")
                radio_Num_Terms.configure(text="Number of terms")
                label7.configure(text="Choose the entry box")
                Res_mod = "Resolution Modifier:"
                try:
                    label8.configure(text=Res_mod+" "+str(new_scale)+"x", font=("ariel",13))
                except:
                    label8.configure(text=Res_mod+"1x", font=("ariel", 13))
                
                
            if translated_combo.get() != "english":                                         #   Checks what language is picked, this one runs if it isn't english
                if to_language_key == "no": to_language_key = "da"
                First_term=(textblob.TextBlob("First term").translate(from_lang=from_language_key,to=to_language_key))                          #   Translates all the variables
                Increment=(textblob.TextBlob("Increment").translate(from_lang=from_language_key,to=to_language_key))
                Num_of_terms=(textblob.TextBlob("Number of terms").translate(from_lang=from_language_key,to=to_language_key))
                Series=(textblob.TextBlob("Series").translate(from_lang=from_language_key,to=to_language_key))
                if to_language_key !="da":
                    Sum_of_series=(textblob.TextBlob("Sum").translate(from_lang=from_language_key,to=to_language_key))
                else:
                    Sum_of_series="Sum"
                Clear=(textblob.TextBlob("Clear").translate(from_lang=from_language_key,to=to_language_key))
                Arithmetic_Progression=(textblob.TextBlob("Arithmetic Progression").translate(from_lang=from_language_key,to=to_language_key))
                Geometric_Progression=(textblob.TextBlob("Geometric Progression").translate(from_lang=from_language_key,to=to_language_key))
                GUI_Title=(textblob.TextBlob("Summing Series").translate(from_lang=from_language_key, to=to_language_key))
                Error_msg=(textblob.TextBlob("Please check entries and try again").translate(from_lang=from_language_key, to=to_language_key))
                Translate_text=(textblob.TextBlob("Translate").translate(from_lang=from_language_key, to=to_language_key))
                Switch_text=(textblob.TextBlob("Switch").translate(from_lang=from_language_key, to=to_language_key))
                Translated_Language=(textblob.TextBlob("Translated Language").translate(from_lang=from_language_key, to=to_language_key))
                Choose_entry_text=(textblob.TextBlob("Choose the entry box").translate(from_lang=from_language_key, to=to_language_key))
                Res_mod=(textblob.TextBlob("Resolution Modifier:").translate(from_lang=from_language_key, to=to_language_key))
                Math_Error = (textblob.TextBlob("Math Error").translate(from_lang=from_language_key, to=to_language_key))
                
                label1.configure(text = First_term)                                                                                                 #   Changes the text on labels
                label2.configure(text = Increment)                                                                                                  #   radiobuttons and buttons
                label3.configure(text = Num_of_terms)
                label4.configure(text = Series)    
                label5.configure(text=Sum_of_series)
                if translated_combo.get() == "xhosa":radio1.configure(text = Arithmetic_Progression, font=("ariel", 9))
                else: radio1.configure(text = Arithmetic_Progression, font=("ariel", 13))
                radio2.configure(text = Geometric_Progression)
                clear_button.configure(text = Clear)
                root.title(GUI_Title)
                validation(Error_msg,1)
                translate_GUI.configure(text=Translate_text)
                switch_button.configure(text= Switch_text)
                label6.configure(text=Translated_Language)
                if translated_combo.get() == "finnish" or translated_combo.get() == "zulu" or translated_combo.get() == "georgian":
                    radio_First_term.configure(text=First_term, font=("ariel", 10))
                else: radio_First_term.configure(text=First_term, font=("ariel", 13))
                radio_Increment.configure(text=Increment)
                radio_Num_Terms.configure(text=Num_of_terms)
                label7.configure(text=Choose_entry_text)
                try:
                    if translated_combo.get() == "georgian" or translated_combo.get() == "xhosa":
                        label8.configure(text=Res_mod+" "+str(new_scale)+"x", font=("ariel", 10))
                    else: 
                        label8.configure(text=Res_mod+" "+str(new_scale)+"x", font=("ariel", 13))
                except:
                    if translated_combo.get() == "georgian" or translated_combo.get() == "xhosa":
                        label8.configure(text=Res_mod+"1x", font=("ariel", 10))
                    else:
                        label8.configure(text=Res_mod+"1x", font=("ariel", 13))
                
            
            for j in range(0,int(len(languages.values()))):                                 #   Changing original language to new translated language
                if language_list[j]==translated_combo.get():
                    original_combo.current(j)
            
        except Exception as e:
            messagebox.showerror("Translator",e)
        clear()
    
    def ap():                                                                                       #   Function to calculate the sum and series of an ap
        global sum_of_terms, space
        sequence.configure(state="normal", text_color="white" , font=("ariel",12))
        sequence.delete(1.0,END)                                                                #   Clearing the series
        space=customtkinter.CTkLabel(root,text="                                                          ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#  Clearing the sum of series
        validation(Error_msg,0)
        if conitnue == 0:
            f=0                                                                                     #   "f"th term in the series 
            a=float(entry1.get())                                                                   #   "a"=first term
            d=float(entry2.get())                                                                   #   "d"=increment
            n=int(entry3.get())                                                                    #   "n"=number of terms               
            decimal1=len(str(a).split(".")[1])                                                      #   Decimal places of first term
            decimal2=len(str(d).split(".")[1])                                                   #   Decimal places of increment
            if decimal1 >= decimal2:                                                                #   Choosing the larger decimal place
                Increment_decimal=decimal1
            else:
                Increment_decimal=decimal2
            progression=[]                                                                          #   Empty series
            progression.append(a+f*d)                                                               #   First term
            while (f+1) != n:                                                                       #   Goes through the terms
                f=f+1                                                                               #   Increments the terms
                progression.append(",")                                                             #   Separates the terms
                progression.append(round(a+f*d,Increment_decimal))                                                           #term inputted in the series
            try: sum=(n/2)*(2*a+(n-1)*d)                                                                 #   Sum of all terms
            except:
                sequence.delete(1.0, END)
                sequence.insert(1.0, text=Math_Error)
                sequence.configure(text_color= "red", state="disabled", font=("REM",17))
            sum=round(sum,Increment_decimal)                                                                  #   Round the sum of terms
            sequence.insert(1.0,progression)                                                        #   Inserting the series
            sequence.configure(state="disabled")
            sum_of_terms=customtkinter.CTkLabel(root,text=sum,bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#     Placing the sum of series

        radio2.deselect()

     
    def gp():                                                                                       #   Function to calculate the sum and series of an gp
        global sum_of_terms, space, conitnue
        sequence.configure(state="normal", text_color="white" , font=("ariel",12))
        sequence.delete(1.0,END)                                                                #   Clearing the series
        space=customtkinter.CTkLabel(root,text="                                                          ",bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#   Clearing the sum of series
        validation(Error_msg,0)
        if conitnue == 0:
            f=0
            a=float(entry1.get())                                                                   #   "a"=first term
            d=float(entry2.get())                                                                   #   "d"=increment
            n=int(entry3.get())                                                                     #   "n"=number of terms
            decimal1=len(str(a).split(".")[1])                                                      #   Decimal places of first term
            decimal2=len(str(d).split(".")[1])                                                      #   Decimal places of increment        
            if decimal1 >= decimal2:                                                                #   Choosing the larger decimal place
                Increment_decimal=decimal1
            else:
                Increment_decimal=decimal2                                                                    #   The 'fth' term in the series
            progression=[]                                                                          #   Empty series
            progression.append(a*(d**f))                                                            #   First term                                                     
            while (f+1) != n:                                                                       #   Goes through the terms
                f=f+1                                                                               #   Increments through the terms
                progression.append(",")                                                             #   Separates the terms
                try: 
                    progression.append(round(a*(d**f),Increment_decimal))
                    Increment_decimal=Increment_decimal*2                               #   Term inputted in the series
                except:
                    sequence.delete(1.0, END)
                    sequence.insert(1.0, text=Math_Error)
                    sequence.configure(text_color= "red", state="disabled", font=("REM",17))
                    conitnue = 1
                    f = n-1
            if conitnue == 0:
                Increment_decimal=Increment_decimal*2                                               #   Incrementing decimal
                try:
                    sum=(a*((d**n)-1))/(d-1)                                                            #   Sum of series
                    sum=round(sum,Increment_decimal)                                                    #   Round the sum of terms                                                            
                except Exception as e:                                                                 #   Distincts error from calculation
                    messagebox.showerror("Sum of Series",e)
                    sum=a*n                                                                            #   Shows error when increment is 1     #   Sum of all terms
                sequence.insert(1.0,progression)                                                        #   Inserting the series
                sum_of_terms=customtkinter.CTkLabel(root,text=sum,bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#     Placing the sum of series
                sequence.configure(state="disabled")
        radio1.deselect()
    
    expand_button=customtkinter.CTkButton(root,text="\u2192",width=50,bg_color=bg_colour,fg_color=fg_colour,command=lambda:expand(0))       #   Button which expands the GUI
    expand_button.place(x=420,y=530)

    label6=customtkinter.CTkLabel(root, text="Translated Language", fg_color=fg_colour , corner_radius=6, bg_color=bg_colour, width=150)
    label6.place(x=570,y=430)

    languages=googletrans.LANGUAGES                                                     #   Grabbing languages from googletrans
    language_list=list(languages.values())

    original_combo=ttk.Combobox(root,width=20,value=language_list)                    #   Comboboxes
    original_combo.current(21)
    
    translated_combo=customtkinter.CTkComboBox(root, width=150, values=language_list, bg_color=bg_colour)
    translated_combo.set("english")                                                     #   Options and placements
    translated_combo.place(x=570,y=480)

    translate_GUI=customtkinter.CTkButton(root,text="Translate", command=translate , bg_color=bg_colour, corner_radius=15, width=150 )
    translate_GUI.place(x=570,y=530)

    switch_button=customtkinter.CTkSwitch(root,text="Switch Theme", command=switch,bg_color=bg_colour,fg_color=fg_colour)
    switch_button.place(x=750,y=530)

    radio1=customtkinter.CTkRadioButton(root,text=Arithmetic_Progression,command=ap, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15,value=1)#   Creating radiobuttons for user to 
    radio2=customtkinter.CTkRadioButton(root,text=Geometric_Progression,command=gp, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)#    choose between ap and gp

    clear_button=customtkinter.CTkButton(root,text=Clear,command=clear,width=80, bg_color=bg_colour, corner_radius=15)#   Creating and placing clear button
    clear_button.place(x=x7-7,y=y7)
    
    res_slider = customtkinter.CTkSlider(root, from_=0.5, to=3, command=scale, number_of_steps=25, width=150, bg_color=bg_colour)
    res_slider.set(1)
    res_slider.place(x=750, y=485) 

    radio1.place(x=x3-5,y=y4)                                                                         #   Placing radiobuttons on window
    radio2.place(x=x4+5,y=y4)

    
    translate()
    root.mainloop()
                                                                                                    #   Predefined settings for program
First_term="  First term  "                                                                         #   Predefined language
Increment="  Increment  "
Num_of_terms="  Number of terms  "
Series="  Series  "
Sum_of_series="  Sum  "
Clear="  Clear  "
Arithmetic_Progression="Arithmetic Progression"
Geometric_Progression="Geometric Progression"
Choose_entry_text = "Chose the entry box"
Res_mod = "Resolution Modifier"
Math_Error = "Math Error"

x1=100
y1=50
y2=100
y3=150
x2=250+20
x3=100
y4=200                                                                                              #   Coordinates of Labels
x4=280
x5=70
y5=250
x6=140+20
x7=75
y7=350
x8=80
y8=530

theme = "dark"                                                                                      #   Predefined theme out of the standard 

if theme == "light":
    theme_accent = "gray92"                                                                         #   Colour palette of predefined themes
    bg_colour = "grey86"
    fg_colour = "grey70"
    text_colour = "black"
if theme == "dark":
    theme_accent = "gray14"
    bg_colour = "grey17"
    fg_colour = "grey35"
    text_colour = "white"

summing_series()                                                                                    #   Runs the program (which is in a function)