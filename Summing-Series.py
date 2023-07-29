from tkinter import*                                                                        #   Importing essential packages for the program
import googletrans
import textblob
from tkinter import ttk, messagebox 
import customtkinter

def summing_series():                                                                       #   Making the program into a recallable function for increased stability and performance

    def switch():                                                                           #   Switches themes
        global theme, current_theme, theme_accent, bg_colour, fg_colour, text_colour                     #   Allows these variables to be used anywhere
        current_theme = root.cget("background")                                             #   Recieves the colour of the background
        if current_theme == "grey19":                                                       #   Checks which theme the progam is running
            theme = "light"                                                                 #   Switches to the theme it isn't running
            theme_accent = "grey60"                                                         #   The colour palette of the different themes
            bg_colour = "grey86"                                                            #   Number next to colour is the darkness, lower is darker
            fg_colour = "grey70"
            text_colour = "black"
        else:
            theme = "dark"
            theme_accent = "grey19"
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
        sequence.configure(bg_color=bg_colour, fg_color=fg_colour)
        space=customtkinter.CTkLabel(root,text="                                                                      ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)
        
        if ibte == 2:
            ap()
        if ibte == 3:
            gp()
            

    root=Tk()                                                                               #   creating GUI window
    root.title("Summing Series")
    root.geometry("550x800")                                                                #   Assigns the resolution of this window
    root.config(bg=theme_accent)                                                            #   Sets the background colour
    frame1 = customtkinter.CTkFrame(master=root, corner_radius=30)
    frame1.pack(pady=20, padx=60, fill="both", expand=True)                                 #   Adds a frame to the program
    customtkinter.set_appearance_mode(theme)                                                #   Sets the theme, predefined themes can be set at the bottom of the code


    global label1, label2, label3, label4, label5                                                                            #   Makes variable accessible from anywhere
    label1=customtkinter.CTkLabel(root,text=First_term, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)             #   Creating Labels to inform user
    label2=customtkinter.CTkLabel(root,text=Increment, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)              #   fg_colour = colour of the background of the button
    label3=customtkinter.CTkLabel(root,text=Num_of_terms, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)           #   bg_colour = the background colour of the rounded edges
    label4=customtkinter.CTkLabel(root,text=Series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)                 #   corner_radius = roundness of the corners
    label5=customtkinter.CTkLabel(root,text=Sum_of_series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
    
    sequence=customtkinter.CTkTextbox(root, width=330, height=250, corner_radius=15, fg_color=fg_colour, bg_color=bg_colour)                                                  #   Creating series and sum of series
    sequence.place(x=x6,y=y5)

    label1.place(x=x1,y=y1)                                                                 #   Placing labels on window
    label2.place(x=x1,y=y2)
    label3.place(x=x1,y=y3)
    label4.place(x=x5,y=y5)
    label5.place(x=x8,y=y8)

 
    entry1=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)                #   Creating entries for user to enter values
    entry2=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)
    entry3=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)

    entry1.place(x=x2,y=y1)                                                                 #   Placing entries on window
    entry2.place(x=x2,y=y2)
    entry3.place(x=x2,y=y3)

    
    def translate():                                                                        #   Function to translate languages
        try:                                                                                #   Get the languages from Dictionary Keys
            for key, value in languages.items():                                            #   Get the From Language key
                if (value == original_combo.get()):
                    from_language_key=key

            for key,value in languages.items():                                             #   Get the To Language key
                if (value ==translated_combo.get()):
                    to_language_key=key
            
            if translated_combo.get() == "english":                                         #   English can't be translated to english
                label1.configure(text = "  First term  ")                                   #   so english is the only language that was
                label2.configure(text = "  Increment  ")                                    #   manually written
                label3.configure(text = "  Number of terms  ")
                label4.configure(text = "  Series  ")                                       #   The text is changed instead of replaced
                label5.configure(text = "  Sum  ")                                          #   which gives the program increased performance
                radio1.configure(text = "Arithmetic Progression")   
                radio2.configure(text = "Geometric Progression")
                clear_button.configure(text = "  Clear ")
                
            if translated_combo.get() != "english":                                         #   Checks what language is picked, this one runs if it isn't english

                First_term=(textblob.TextBlob("  First term  ").translate(from_lang=from_language_key,to=to_language_key))                          #   Translates all the variables
                Increment=(textblob.TextBlob("  Increment  ").translate(from_lang=from_language_key,to=to_language_key))
                Num_of_terms=(textblob.TextBlob("  Number of terms  ").translate(from_lang=from_language_key,to=to_language_key))
                Series=(textblob.TextBlob("  Series  ").translate(from_lang=from_language_key,to=to_language_key))
                Sum_of_series=(textblob.TextBlob("  Sum  ").translate(from_lang=from_language_key,to=to_language_key))
                Clear=(textblob.TextBlob("  Clear  ").translate(from_lang=from_language_key,to=to_language_key))
                Arithmetic_Progression=(textblob.TextBlob("Arithmetic Progression").translate(from_lang=from_language_key,to=to_language_key))
                Geometric_Progression=(textblob.TextBlob("Geometric Progression").translate(from_lang=from_language_key,to=to_language_key))

                label1.configure(text = First_term)                                                                                                 #   Changes the text on labels
                label2.configure(text = Increment)                                                                                                  #   radiobuttons and buttons
                label3.configure(text = Num_of_terms)
                label4.configure(text = Series)    
                label5.configure(text = Sum_of_series)
                radio1.configure(text = Arithmetic_Progression)
                radio2.configure(text = Geometric_Progression)
                clear_button.configure(text = Clear)
            
            for j in range(0,int(len(languages.values()))):                                 #   Changing original language to new translated language
                if language_list[j]==translated_combo.get():
                    original_combo.current(j)
            
        except Exception as e:
            messagebox.showerror("Translator",e)
        window.destroy()                                                                    #   Closes the tanslator GUI so user knows it worked

    
    def open_translate():                                                                   #   Function to open translated langauges
        global language_list, languages, original_combo, translated_combo, window, translate_GUI
        
        window=Tk()                                                                         #   Creating window for translator
        window.title("Translator")
        window.geometry("250x200")                                                          #   Restricts the size of the window
        window.maxsize(width=250, height=200)
        window.minsize(width=250, height=200)
        window.config(bg=theme_accent)
        frame1 = customtkinter.CTkFrame(master=window, width=250, height=200, border_width=5, border_color=theme_accent, corner_radius=15)
        frame1.place(x =0,y=0)                                                              #   Creates a padding from the border and within it is a rounded edged frame
        customtkinter.set_appearance_mode(theme)                                            #   sets theme


        languages=googletrans.LANGUAGES                                                     #   Grabbing languages from googletrans
        language_list=list(languages.values())


        original_combo=ttk.Combobox(window,width=20,value=language_list)                    #   Comboboxes and Layout of GUI and placements
        original_combo.current(21)
        label7=customtkinter.CTkLabel(window, text="Translated Language", fg_color=fg_colour , corner_radius=6, bg_color=bg_colour)
        label7.grid(row=3,column=0,pady=10,padx=50)

        translated_combo=ttk.Combobox(window, width=20, values=language_list)               #   Options and placements
        translated_combo.current(15)
        translated_combo.grid(row=4,column=0,pady=10,padx=50)

        translate_GUI=customtkinter.CTkButton(window,text="Translate", command=translate , bg_color=bg_colour, corner_radius=15 )
        translate_GUI.grid(row=5,column=0,pady=10,padx=50)

        window.mainloop()

    def validation():                                                                       #   Checks if the entry input is valid
        global conitnue, a, n, d
        sequence.configure(state="normal")
        sequence.delete(1.0, END)
        try:
            a, d, n = float(entry1.get()), float(entry2.get()), float(entry3.get())
            conitnue = 0
        except ValueError:
            conitnue = 1
            sequence.insert(1.0, text="Please check entries and try again")
            sequence.configure(text_color= "red", state="disabled", font=("REM",18))


    def clear():                                                                            #   Function to clear inputs and outputs
        sequence.configure(state="normal")
        sequence.delete(1.0,END)
        sequence.configure(state="disabled")
        space=customtkinter.CTkLabel(root,text="                                                                      ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)
        entry1.delete(0,END)                                                                
        entry2.delete(0,END)
        entry3.delete(0,END)

    
    def ap():                                                                                       #   Function to calculate the sum and series of an ap
        global sum_of_terms, space, ibte
        sequence.configure(state="normal", text_color="white" , font=("ariel",12))
        sequence.delete(1.0,END)                                                                #   Clearing the series
        space=customtkinter.CTkLabel(root,text="                                                          ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#  Clearing the sum of series
        validation()
        print(conitnue)
        if conitnue == 0:
            f=0                                                                                     #   "f"th term in the series 
            a=float(entry1.get())                                                                   #   "a"=first term
            d=float(entry2.get())                                                                   #   "d"=increment
            n=round(float(entry3.get())+0.1,0)                                                                    #   "n"=number of terms               
            decimal1=len(str(a).split(".")[1])                                                      #   Decimal places of first term
            decimal2=len(str(d).split(".")[1])                                                      #   Decimal places of increment
            if decimal1 >= decimal2:                                                                #   Choosing the larger decimal place
                decimal=decimal1
            else:
                decimal=decimal2
            progression=[]                                                                          #   Empty series
            progression.append(a+f*d)                                                               #   First term
            while (f+1) != n:                                                                       #   Goes through the terms
                f=f+1                                                                               #   Increments the terms
                progression.append(",")                                                             #   Separates the terms
                progression.append(round(a+f*d,decimal))                                                           #term inputted in the series
            sum=(n/2)*(2*a+(n-1)*d)                                                                 #   Sum of all terms
            sum=round(sum,decimal)                                                                  #   Round the sum of terms
            sequence.insert(1.0,progression)                                                        #   Inserting the series
            sequence.configure(state="disabled")
            sum_of_terms=customtkinter.CTkLabel(root,text=sum,bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#     Placing the sum of series
            ibte = 2                                                                                #   Placeholder term --> used like memory 
        else:                                                                                       #   used to make sure changing theme works
            pass                                                                                    #   while calculations are happening and keeps answers

     
    def gp():                                                                                       #   Function to calculate the sum and series of an gp
        global sum_of_terms, space, ibte
        sequence.configure(state="normal", text_color="white" , font=("ariel",12))
        sequence.delete(1.0,END)                                                                #   Clearing the series
        space=customtkinter.CTkLabel(root,text="                                                          ",bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#   Clearing the sum of series
        validation()
        print(conitnue)
        if conitnue == 0:
            f=0
            a=float(entry1.get())                                                                   #   "a"=first term
            d=float(entry2.get())                                                                   #   "d"=increment
            n=round(float(entry3.get())+0.1,0)                                                                     #   "n"=number of terms
            decimal1=len(str(a).split(".")[1])                                                      #   Decimal places of first term
            decimal2=len(str(d).split(".")[1])                                                      #   Decimal places of increment        
            if decimal1 >= decimal2:                                                                #   Choosing the larger decimal place
                decimal=decimal1
            else:
                decimal=decimal2                                                                    #   The 'fth' term in the series
            progression=[]                                                                          #   Empty series
            progression.append(a*(d**f))                                                            #   First term
            Increment_decimal=decimal                                                               #   Decimal to round off terms                                                      
            while (f+1) != n:                                                                       #   Goes through the terms
                f=f+1                                                                               #   Increments through the terms
                progression.append(",")                                                             #   Separates the terms
                progression.append(round(a*(d**f),Increment_decimal))                               #   Term inputted in the series
                Increment_decimal=Increment_decimal*2                                               #   Incrementing decimal
            try:
                sum=(a*((d**n)-1))/(d-1)                                                            #   Sum of series
                sum=round(sum,Increment_decimal)                                                    #   Round the sum of terms                                                            
            except Exception as e:                                                                  #   Distincts error from calculation
                messagebox.showerror("Sum of Series",e)                                             #   Shows error when increment is 1     #   Sum of all terms
            sequence.insert(1.0,progression)                                                        #   Inserting the series
            sum_of_terms=customtkinter.CTkLabel(root,text=sum,bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)#     Placing the sum of series
            sequence.configure(state="disabled")
            ibte = 3                                                                                #   Placeholder term --> used like memory
        else:
            pass
        

    radio1=customtkinter.CTkRadioButton(root,text=Arithmetic_Progression,command=ap, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)#   Creating radiobuttons for user to 
    radio2=customtkinter.CTkRadioButton(root,text=Geometric_Progression,command=gp, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)#    choose between ap and gp

    clear_button=customtkinter.CTkButton(root,text=Clear,command=clear,width=15, bg_color=bg_colour, corner_radius=6)#   Creating and placing clear button
    clear_button.place(x=x7,y=y7)

    radio1.place(x=x3,y=y4)                                                                         #   Placing radiobuttons on window
    radio2.place(x=x4,y=y4)

    menubar=Menu(root)                                                                              #   Creating menubar for menu options
    root.config(menu=menubar)
    file_menu=Menu(menubar,tearoff=False)
    file_menu.add_command(label="Language",command=open_translate)
    file_menu.add_command(label="Customise", command=switch)
    menubar.add_cascade(label="Settings", menu=file_menu)

    root.mainloop()
#                                                                                                       Predefined settings for program
First_term="  First term  "                                                                         #   Predefined language
Increment="  Increment  "
Num_of_terms="  Number of terms  "
Series="  Series  "
Sum_of_series="  Sum  "
Clear="  Clear  "
Arithmetic_Progression="Arithmetic Progression"
Geometric_Progression="Geometric Progression"

x1=100
y1=50
y2=100
y3=150
x2=250
x3=100
y4=200                                                                                              #   Coordinates of Labels
x4=280
x5=70
y5=250
x6=140
x7=75
y7=350
x8=80
y8=500

x1_1 = 200                                                                                          #   Coordinates of entry
y1 = 50

x1_2 = 150                                                                                          #   Other coordinates

theme = "dark"                                                                                      #   Predefined theme out of the standard 

if theme == "light":
    theme_accent = "grey60"                                                                         #   Colour palette of predefined themes
    bg_colour = "grey86"
    fg_colour = "grey70"
if theme == "dark":
    theme_accent = "grey19"
    bg_colour = "grey17"
    fg_colour = "grey35"

ibte = 0                                                                                            #   Ibte is required to run the code as it acts like memory
summing_series()                                                                                    #   Runs the program (which is in a function)