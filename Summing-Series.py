#importing essential packages for the program
from tkinter import*
import googletrans
import textblob
from tkinter import ttk, messagebox 

#creating GUI window
root=Tk()
root.title("Summing Series")
root.geometry("550x800")

#Creating Labels to inform user
label1=Label(root,text="First term: ")
label2=Label(root,text="Increment: ")
label3=Label(root,text="Number of terms: ")
label4=Label(root,text="Series: ")
label5=Label(root,text="Sum of series: ")

#Creating series and sum of series
sequence=Text(root,height=15,width=40)
sequence.place(x=100,y=250)

#Placing labels on window
label1.place(x=50,y=50)
label2.place(x=50,y=100)
label3.place(x=50,y=150)
label4.place(x=50,y=250)
label5.place(x=50,y=500)

#Creating entries for user to enter values
entry1=Entry(root,borderwidth=5)
entry2=Entry(root,borderwidth=5)
entry3=Entry(root,borderwidth=5)

#Placing entries on window
entry1.place(x=200,y=50)
entry2.place(x=200,y=100)
entry3.place(x=200,y=150)

#Function to clear inputs and outputs
def clear():
    sequence.delete(1.0,END)
    space=Label(root,text="                                        ")
    space.place(x=150,y=500)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

#Function to calculate the sum and series of an ap
def ap():
    sequence.delete(1.0,END)                                                                #clearing the series
    space=Label(root,text="                                        ").place(x=150,y=500)    #clearing the sum of series
    a=float(entry1.get())                                                                   #a=first term
    d=float(entry2.get())                                                                   #d=increment
    n=int(entry3.get())                                                                   #n=number of terms
    f=0                                                                                     #the 'fth' term in the series
    series=[]                                                                               #empty series
    series.append(a+f*d)                                                                    #first term
    while (f+1) != n:                                                                       #goes through the terms
        f=f+1                                                                               #increments the terms
        series.append(",")                                                                  #separates the terms
        series.append(a+f*d)                                                                #term inputted in the series
    sum=(n/2)*(2*a+(n-1)*d)                                                                 #sum of all terms
    sequence.insert(1.0,series)                                                             #inserting the series
    sum_of_terms=Label(root,text=sum).place(x=150,y=500)                                    #placing the sum of series

#Function to calculate the sum and series of an gp 
def gp():
    sequence.delete(1.0,END)                                                                #clearing the series
    space=Label(root,text="                                        ").place(x=150,y=500)    #clearing the sum of series
    a=float(entry1.get())                                                                   #a=first term
    d=float(entry2.get())                                                                   #d=increment
    n=int(entry3.get())                                                                   #n=number of terms
    f=0                                                                                     #the 'fth' term in the series
    series=[]                                                                               #empty series
    series.append(a*(d**f))                                                                 #first term
    while (f+1) != n:                                                                       #goes through the terms
        f=f+1                                                                               #increments through the terms
        series.append(",")                                                                  #separates the terms
        series.append(a*(d**f))                                                             #term inputted in the series
    try:
        sum=(a*((d**n)-1))/(d-1)                                                            #sum of series                                                            
    except Exception as e:                                                                  #distincts error from calculation
        messagebox.showerror("Sum of Series",e)                                             #shows error when increment is 1                                                                #sum of all terms
    sequence.insert(1.0,series)                                                             #inserting the series
    sum_of_terms=Label(root,text=sum).place(x=150,y=500)                                    #placing the sum of series
    
#Creating radiobuttons for user to choose between ap and gp
radio1=Radiobutton(root,text="Arithmetic Progression",command=ap)
radio2=Radiobutton(root,text="Geometric Progression",command=gp)

#Creating and placing clear button
clear=Button(root,text="Clear",command=clear)
clear.place(x=50,y=200)

#Placing radiobuttons on window
radio1.place(x=50,y=550)
radio2.place(x=200,y=550)

root.mainloop()