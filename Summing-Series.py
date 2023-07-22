#importing essential packages for the program
from tkinter import*
import googletrans
import textblob
from tkinter import ttk, messagebox 
import customtkinter


    

#making the program into a recallable function for increased stability and performance
def summing_series():
    # themes
    def switch():
        global theme, current_theme, theme_accent, bg_colour, fg_colour
        current_theme = root.cget("background")
        if current_theme == "grey19":
            theme = "light"
            theme_accent = "grey60"
            bg_colour = "grey86"
            fg_colour = "grey70"
        else:
            theme = "dark"
            theme_accent = "grey19"
            bg_colour = "grey17"
            fg_colour = "grey35"
        root.config(bg=theme_accent)
        customtkinter.set_appearance_mode(theme)                                            # Updating all GUI text
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
        if ibte == 1:
            label1trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            label2trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            label3trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            label4trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            label5trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            radio1trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            radio2trans.configure(bg_color=bg_colour, fg_color=fg_colour)
            cleartrans.configure(bg_color=bg_colour)
        if ibte == 2:
            ap()
        if ibte == 3:
            gp()
            

    #creating GUI window
    root=Tk()
    root.title("Summing Series")
    root.geometry("550x800")
    root.config(bg=theme_accent)
    frame1 = customtkinter.CTkFrame(master=root, corner_radius=30)
    frame1.pack(pady=20, padx=60, fill="both", expand=True)                     # adds a frame in the program
    customtkinter.set_appearance_mode(theme)                                    #sets theme

    #Translatable labels
    global First_term, Increment, Num_of_terms, Series, Sum_of_series, Clear, Arithmetic_Progression, Geometric_Progression
    First_term="  First term  "
    Increment="  Increment  "
    Num_of_terms="  Number of terms  "
    Series="  Series  "
    Sum_of_series="  Sum  "
    Clear="  Clear  "
    Arithmetic_Progression="Arithmetic Progression"
    Geometric_Progression="Geometric Progression"


    global label1, label2, label3, label4, label5                                                                                   # makes variable accessible from anywhere

    #Creating Labels to inform user
    label1=customtkinter.CTkLabel(root,text=First_term, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)                    #fg_colour = colour of the background of the button
    label2=customtkinter.CTkLabel(root,text=Increment, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)                     #bg_colour = the background colour of the rounded edges
    label3=customtkinter.CTkLabel(root,text=Num_of_terms, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)                  #corner_radius = roundness of the corners
    label4=customtkinter.CTkLabel(root,text=Series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
    label5=customtkinter.CTkLabel(root,text=Sum_of_series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
    

    #Creating series and sum of series
    sequence=Text(root,height=15,width=40)
    sequence.place(x=x6,y=y5)

    #Placing labels on window
    label1.place(x=x1,y=y1)
    label2.place(x=x1,y=y2)
    label3.place(x=x1,y=y3)
    label4.place(x=x5,y=y5)
    label5.place(x=x8,y=y8)

    #Creating entries for user to enter values
    entry1=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)
    entry2=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)
    entry3=customtkinter.CTkEntry(root, corner_radius=6, bg_color=bg_colour)

    #Placing entries on window
    entry1.place(x=x2,y=y1)
    entry2.place(x=x2,y=y2)
    entry3.place(x=x2,y=y3)


    def delete():
        #Delete previous GUI label
        translate_GUI.destroy()
        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        label5.destroy()
        clear_button.destroy()
        radio1.destroy()
        radio2.destroy()
    
    #Function to translate languages
    def translate():
        delete()
        global label1trans, label2trans, label3trans,label4trans, label5trans, radio1trans, radio2trans, cleartrans, ibte
        
        try:  #Get the languages from Dictionary Keys
            #Get the From Language key
            for key, value in languages.items():
                if (value == original_combo.get()):
                    from_language_key=key

            #Get the To Language key
            for key,value in languages.items():
                if (value ==translated_combo.get()):
                    to_language_key=key
            
            if translated_combo.get() == "english":
                
                label1trans=customtkinter.CTkLabel(root,text=First_term, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label1trans.place(x=x1,y=y1)

                label2trans=customtkinter.CTkLabel(root,text=Increment, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label2trans.place(x=x1,y=y2)

                label3trans=customtkinter.CTkLabel(root,text=Num_of_terms, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label3trans.place(x=x1,y=y3)

                label4trans=customtkinter.CTkLabel(root,text=Series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label4trans.place(x=x5,y=y5)

                label5trans=customtkinter.CTkLabel(root,text=Sum_of_series, fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label5trans.place(x=x8,y=y8)

                radio1trans=customtkinter.CTkRadioButton(root,text=Arithmetic_Progression,command=ap, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)
                radio1trans.place(x=x3,y=y4)

                radio2trans=customtkinter.CTkRadioButton(root,text=Geometric_Progression,command=gp, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)
                radio2trans.place(x=x4,y=y4)

                cleartrans=customtkinter.CTkButton(root,text=Clear,command=clear,width=15, bg_color=bg_colour, corner_radius=6)
                cleartrans.place(x=x7,y=y7)

                ibte=1

            if translated_combo.get() != "english": 
            #Translating the terms and placing them on GUI
                label1trans=customtkinter.CTkLabel(root,text=textblob.TextBlob(First_term).translate(from_lang=from_language_key,to=to_language_key), fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label1trans.place(x=x1,y=y1)

                label2trans=customtkinter.CTkLabel(root,text=textblob.TextBlob(Increment).translate(from_lang=from_language_key,to=to_language_key), fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label2trans.place(x=x1,y=y2)

                label3trans=customtkinter.CTkLabel(root,text=textblob.TextBlob(Num_of_terms).translate(from_lang=from_language_key,to=to_language_key), fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label3trans.place(x=x1,y=y3)

                label4trans=customtkinter.CTkLabel(root,text=textblob.TextBlob(Series).translate(from_lang=from_language_key,to=to_language_key), fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label4trans.place(x=x5,y=y5)

                label5trans=customtkinter.CTkLabel(root,text=textblob.TextBlob(Sum_of_series).translate(from_lang=from_language_key,to=to_language_key), fg_color=fg_colour, bg_color=bg_colour, corner_radius=6)
                label5trans.place(x=x8,y=y8)

                radio1trans=customtkinter.CTkRadioButton(root,text=textblob.TextBlob(Arithmetic_Progression).translate(from_lang=from_language_key,to=to_language_key),command=ap, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)
                radio1trans.place(x=x3,y=y4)
                
                radio2trans=customtkinter.CTkRadioButton(root,text=textblob.TextBlob(Geometric_Progression).translate(from_lang=from_language_key,to=to_language_key),command=gp, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)
                radio2trans.place(x=x4,y=y4)

                cleartrans=customtkinter.CTkButton(root,text=textblob.TextBlob(Clear).translate(from_lang=from_language_key,to=to_language_key),command=clear,width=15, bg_color=bg_colour, corner_radius=6)
                cleartrans.place(x=x7,y=y7)

                ibte = 1
           
            #Changing original language to new translated language
            for j in range(0,int(len(languages.values()))):
                if language_list[j]==translated_combo.get():
                    original_combo.current(j)
            
        
        except Exception as e:
            messagebox.showerror("Translator",e)
        window.destroy()     #closes the tanslate GUI so user knows it worked




    #Function to open translated langauges
    def open_translate():
        global language_list, languages, original_combo, translated_combo, window, translate_GUI
        #Creating window for translator
        window=Tk()
        window.title("Translator")
        window.geometry("250x200")                                                                   # restricts the size of the window
        window.maxsize(width=250, height=200)
        window.minsize(width=250, height=200)
        window.config(bg=theme_accent)
        frame1 = customtkinter.CTkFrame(master=window, width=250, height=200, border_width=5, border_color=theme_accent, corner_radius=15)
        frame1.place(x =0,y=0)                                                                       #creates a padding from the border and within it is a rounded edged frame
        customtkinter.set_appearance_mode(theme)                                                    #sets theme


        #Grabbing languages from googletrans
        languages=googletrans.LANGUAGES
        language_list=list(languages.values())

        #Comboboxes and Layout of GUI

        original_combo=ttk.Combobox(window,width=20,value=language_list)
        original_combo.current(21)
        label7=customtkinter.CTkLabel(window, text="Translated Language", fg_color=fg_colour , corner_radius=6, bg_color=bg_colour)
        label7.grid(row=3,column=0,pady=10,padx=50)

        translated_combo=ttk.Combobox(window, width=20, values=language_list)
        translated_combo.current(15)
        translated_combo.grid(row=4,column=0,pady=10,padx=50)

        translate_GUI=customtkinter.CTkButton(window,text="Translate", command=translate , bg_color=bg_colour, corner_radius=15 )
        translate_GUI.grid(row=5,column=0,pady=10,padx=50)

        window.mainloop()

    #error window
    def error():
        reinput=Tk()
        reinput.title("Error Message")
        reinput.geometry("400x100")                                                                   # restricts the size of the window
        reinput.maxsize(width=400, height=100)
        reinput.minsize(width=400, height=100)
        Error_message = Label(reinput, text="Please check input fields and try again", fg="red", font=30).pack(padx=20, pady=30)
       
    #checks if the entry input is valid
    def validation():
        global conitnue
        conitnue = 0                                                                            #"continue" is like a ticket for the program to run
        a=(entry1.get())
        if a.isalpha() == True or len(a) == 0:                                                  # checks if the fields are letters or blank
            conitnue = conitnue + 1                                                             # any misinput denies the ticket
        d=(entry2.get())
        if d.isalpha() == True or len(d) == 0:
            conitnue = conitnue + 1
        n=(entry3.get())
        if n.isalpha() == True or len(n) ==0:
            conitnue = conitnue + 1
        if conitnue >= 1:
            error()                                                                             # opens an error window


    #Function to clear inputs and outputs
    def clear():
        sequence.delete(1.0,END)
        space=customtkinter.CTkLabel(root,text="                                                                      ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)

    #Function to calculate the sum and series of an ap
    def ap():
        radio1.deselect()
        validation()                                                                            #sends inputs to validate
        global sum_of_terms, space, ibte
        if conitnue == 0:
            sequence.delete(1.0,END)                                                                #clearing the series
            space=customtkinter.CTkLabel(root,text="                                                          ", bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)    #clearing the sum of series
            a=float(entry1.get())                                                                   #a=first term
            d=float(entry2.get())                                                                   #d=increment
            n=int(entry3.get())                                                                     #n=number of terms
            f=0                                                                                     #fth term in the series                
            decimal1=len(str(a).split(".")[1])                                                      #decimal places of first term
            decimal2=len(str(d).split(".")[1])                                                      #decimal places of increment
            if decimal1 >= decimal2:                                                                #choosing the larger decimal place
                decimal=decimal1
            else:
                decimal=decimal2
            progression=[]                                                                          #empty series
            progression.append(a+f*d)                                                               #first term
            while (f+1) != n:                                                                       #goes through the terms
                f=f+1                                                                               #increments the terms
                progression.append(",")                                                             #separates the terms
                progression.append(round(a+f*d,decimal))                                                           #term inputted in the series
            sum=(n/2)*(2*a+(n-1)*d)                                                                 #sum of all terms
            sum=round(sum,decimal)                                                                  #round the sum of terms
            sequence.insert(1.0,progression)                                                        #inserting the series
            sum_of_terms=customtkinter.CTkLabel(root,text=sum,bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)                                    #placing the sum of series
            ibte = 2
        else:
            pass

    #Function to calculate the sum and series of an gp 
    def gp():
        radio2.deselect()
        validation()
        global sum_of_terms, space, ibte
        if conitnue == 0:
            sequence.delete(1.0,END)                                                                #clearing the series
            space=customtkinter.CTkLabel(root,text="                                                          ",bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)                  #clearing the sum of series
            a=float(entry1.get())                                                                   #a=first term
            d=float(entry2.get())                                                                   #d=increment
            n=int(entry3.get())                                                                     #n=number of terms
            f=0
            decimal1=len(str(a).split(".")[1])                                                      #decimal places of first term
            decimal2=len(str(d).split(".")[1])                                                      #decimal places of increment        
            if decimal1 >= decimal2:                                                                #choosing the larger decimal place
                decimal=decimal1
            else:
                decimal=decimal2                                                                    #the 'fth' term in the series
            progression=[]                                                                          #empty series
            progression.append(a*(d**f))                                                            #first term
            Increment_decimal=decimal                                                               #Decimal to round off terms                                                      
            while (f+1) != n:                                                                       #goes through the terms
                f=f+1                                                                               #increments through the terms
                progression.append(",")                                                             #separates the terms
                progression.append(round(a*(d**f),Increment_decimal))                               #term inputted in the series
                Increment_decimal=Increment_decimal*2                                               #Incrementing decimal
            try:
                sum=(a*((d**n)-1))/(d-1)                                                            #sum of series
                sum=round(sum,Increment_decimal)                                                              #round the sum of terms                                                            
            except Exception as e:                                                                  #distincts error from calculation
                messagebox.showerror("Sum of Series",e)                                             #shows error when increment is 1                                                                #sum of all terms
            sequence.insert(1.0,progression)                                                        #inserting the series
            sum_of_terms=customtkinter.CTkLabel(root,text=sum,bg_color=bg_colour, fg_color=bg_colour).place(x=x6,y=y8)                                    #placing the sum of series
            ibte = 3
        else:
            pass
        
        
    #Creating radiobuttons for user to choose between ap and gp
    radio1=customtkinter.CTkRadioButton(root,text=Arithmetic_Progression,command=ap, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)
    radio2=customtkinter.CTkRadioButton(root,text=Geometric_Progression,command=gp, bg_color=bg_colour, fg_color=fg_colour, corner_radius=15)

    #Creating and placing clear button
    clear_button=customtkinter.CTkButton(root,text=Clear,command=clear,width=15, bg_color=bg_colour, corner_radius=6)
    clear_button.place(x=x7,y=y7)

    #Placing radiobuttons on window
    radio1.place(x=x3,y=y4)
    radio2.place(x=x4,y=y4)

    #Creating menubar for menu options
    menubar=Menu(root)
    root.config(menu=menubar)
    file_menu=Menu(menubar,tearoff=False)
    file_menu.add_command(label="Language",command=open_translate)
    file_menu.add_command(label="Customise", command=switch)
    menubar.add_cascade(label="Settings", menu=file_menu)

    root.mainloop()




#predefined settings for program

#Co ordinates of Labels
x1=100
y1=50
y2=100
y3=150
x2=250
x3=100
y4=200
x4=280
x5=70
y5=250
x6=140
x7=75
y7=350
x8=80
y8=500

#coordinates of entry
x1_1 = 200
y1 = 50

#other coordinates
x1_2 = 150

#adds theme
theme = "dark"

if theme == "light":
    theme_accent = "grey60"
    bg_colour = "grey86"
    fg_colour = "grey70"
if theme == "dark":
    theme_accent = "grey19"
    bg_colour = "grey17"
    fg_colour = "grey35"

#ibte is required to run the code
ibte = 0

summing_series()