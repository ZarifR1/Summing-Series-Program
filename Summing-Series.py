#importing essential packages for the program
from tkinter import*
import googletrans
import textblob
from tkinter import ttk, messagebox 

#creating GUI window
root=Tk()
root.title("Summing Series")
root.geometry("550x800")

#Translatable labels
global First_term, Increment, Num_of_terms, Series, Sum_of_series, Clear, Arithmetic_Progression, Geometric_Progression
First_term="First term: "
Increment="Increment: "
Num_of_terms="Number of terms:"
Series="Series: "
Sum_of_series="Sum: "
Clear="Clear"
Arithmetic_Progression="Arithmetic Progression"
Geometric_Progression="Geometric Progression"

#Creating Labels to inform user
label1=Label(root,text=First_term)
label2=Label(root,text=Increment)
label3=Label(root,text=Num_of_terms)
label4=Label(root,text=Series)
label5=Label(root,text=Sum_of_series)

#Creating series and sum of series
sequence=Text(root,height=15,width=40)
sequence.place(x=100,y=250)

translated_label=Label(root,text=" ")
translated_gp=Label(root,text=" ")
translated_ap=Label(root,text=" ")
translated_clear=Label(root,text=" ")

#Co ordinates of Labels
x1=50
y1=50
y2=100
y3=150
y4=250
y5=500
x2=200
y6=350

#Placing labels on window
label1.place(x=x1,y=y1)
label2.place(x=x1,y=y2)
label3.place(x=x1,y=y3)
label4.place(x=x1,y=y4)
label5.place(x=x1,y=y5)

#Creating entries for user to enter values
entry1=Entry(root,borderwidth=5)
entry2=Entry(root,borderwidth=5)
entry3=Entry(root,borderwidth=5)

#Placing entries on window
entry1.place(x=200,y=50)
entry2.place(x=200,y=100)
entry3.place(x=200,y=150)

#Function to translate languages
def translate():
    #Delete previous GUI labels
    global translated_ap, translated_gp, translated_clear, translated_label
    translated_label.destroy()
    translated_gp.destroy()
    translated_ap.destroy()
    translated_clear.destroy()
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    clear_button.destroy()
    radio1.destroy()
    radio2.destroy()
    Label_names=[First_term,Increment,Num_of_terms,Arithmetic_Progression,Geometric_Progression,Series,Clear,Sum_of_series]
    Label_cords=[x1,x1,x1,x1,x2,x1,x1,x1,y5,y6,y4,x2,x2,y3,y2,y1]

    '''for i in range(0,int(len(Label_names))):
        space=Label(root,text="             ").place(x=Label_cords[i],y=Label_cords[(len(Label_cords)-1)-i])'''

    try:  #Get the languages from Dictionary Keys
          #Get the From Language key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key=key

        #Get the To Language key
        for key,value in languages.items():
            if (value ==translated_combo.get()):
                to_language_key=key
        
        #Translating the terms
        for i in range(0,int(len(Label_names))):
            translation=textblob.TextBlob(Label_names[i])
            translation=translation.translate(from_lang=from_language_key, to=to_language_key)
        
            #Placing translated text on GUI
            if Label_names[i] != Arithmetic_Progression or Geometric_Progression or Clear:
                translated_label=Label(root,text=translation).place(x=Label_cords[i],y=Label_cords[(len(Label_cords)-1)-i])

            if Label_names[i]==Arithmetic_Progression:
                translated_ap=Radiobutton(root,text=translation,command=ap).place(x=Label_cords[i],y=Label_cords[(len(Label_cords)-1)-i])

            if Label_names[i]==Geometric_Progression:
                translated_gp=Radiobutton(root,text=translation,command=gp).place(x=Label_cords[i],y=Label_cords[(len(Label_cords)-1)-i])
            
            if Label_names[i]==Clear:
                translated_clear=Button(root,text=translation,command=clear).place(x=Label_cords[i],y=Label_cords[(len(Label_cords)-1)-i])

    except Exception as e:
        messagebox.showerror("Translator",e)




#Function to open translated langauges
def open_translate():
    global language_list, languages, original_combo, translated_combo
    #Creating window for translator
    window=Tk()
    window.title("Translator")
    window.geometry("250x300")

    #Grabbing languages from googletrans
    languages=googletrans.LANGUAGES
    language_list=list(languages.values())

    #Comboboxes and Layout of GUI
    label6=Label(window,text="Original Language:")
    label6.grid(row=1,column=0,pady=10,padx=50)

    original_combo=ttk.Combobox(window,width=20,value=language_list)
    original_combo.current(21)
    original_combo.grid(row=2,column=0,pady=10,padx=50)

    label7=Label(window,text="Translated Language:")
    label7.grid(row=3,column=0,pady=10,padx=50)

    translated_combo=ttk.Combobox(window,width=20,value=language_list)
    translated_combo.current(15)
    translated_combo.grid(row=4,column=0,pady=10,padx=50)

    translate_GUI=Button(window,text="Translate", command=translate)
    translate_GUI.grid(row=5,column=0,pady=10,padx=50)

    window.mainloop()


#Function to clear inputs and outputs
def clear():
    sequence.delete(1.0,END)
    space=Label(root,text="                                        ").place(x=150,y=500)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

#Function to calculate the sum and series of an ap
def ap():
    sequence.delete(1.0,END)                                                                #clearing the series
    space=Label(root,text="                                        ").place(x=150,y=500)    #clearing the sum of series
    a=float(entry1.get())                                                                   #a=first term
    d=float(entry2.get())                                                                   #d=increment
    n=int(entry3.get())                                                                     #n=number of terms
    f=0                                                                                     #the 'fth' term in the series
    progression=[]                                                                               #empty series
    progression.append(a+f*d)                                                                    #first term
    while (f+1) != n:                                                                       #goes through the terms
        f=f+1                                                                               #increments the terms
        progression.append(",")                                                                  #separates the terms
        progression.append(a+f*d)                                                                #term inputted in the series
    sum=(n/2)*(2*a+(n-1)*d)                                                                 #sum of all terms
    sequence.insert(1.0,progression)                                                             #inserting the series
    sum_of_terms=Label(root,text=sum).place(x=150,y=500)                                    #placing the sum of series

#Function to calculate the sum and series of an gp 
def gp():
    sequence.delete(1.0,END)                                                                #clearing the series
    space=Label(root,text="                                        ").place(x=150,y=500)    #clearing the sum of series
    a=float(entry1.get())                                                                   #a=first term
    d=float(entry2.get())                                                                   #d=increment
    n=int(entry3.get())                                                                     #n=number of terms
    f=0                                                                                     #the 'fth' term in the series
    progression=[]                                                                          #empty series
    progression.append(a*(d**f))                                                            #first term
    while (f+1) != n:                                                                       #goes through the terms
        f=f+1                                                                               #increments through the terms
        progression.append(",")                                                             #separates the terms
        progression.append(a*(d**f))                                                        #term inputted in the series
    try:
        sum=(a*((d**n)-1))/(d-1)                                                            #sum of series                                                            
    except Exception as e:                                                                  #distincts error from calculation
        messagebox.showerror("Sum of Series",e)                                             #shows error when increment is 1                                                                #sum of all terms
    sequence.insert(1.0,progression)                                                        #inserting the series
    sum_of_terms=Label(root,text=sum).place(x=150,y=500)                                    #placing the sum of series
    
#Creating radiobuttons for user to choose between ap and gp
radio1=Radiobutton(root,text=Arithmetic_Progression,command=ap)
radio2=Radiobutton(root,text=Geometric_Progression,command=gp)

#Creating and placing clear button
clear_button=Button(root,text=Clear,command=clear)
clear_button.place(x=x1,y=y6)

#Placing radiobuttons on window
radio1.place(x=x1,y=x2)
radio2.place(x=x2,y=x2)

#Creating menubar for menu options
menubar=Menu(root)
root.config(menu=menubar)
file_menu=Menu(menubar,tearoff=False)
file_menu.add_command(label="Translate",command=open_translate)
menubar.add_cascade(label="Options", menu=file_menu)

root.mainloop()