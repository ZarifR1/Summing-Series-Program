from tkinter import* #importing Tkinter

#creating GUI window
root=Tk()
root.title("APs and GPs")
root.geometry("500x500")

#Creating Labels to inform user
label1=Label(root,text="First term: ")
label2=Label(root,text="Increment: ")
label3=Label(root,text="Number of terms: ")
label4=Label(root,text="Series: ")
label5=Label(root,text="Sum of series: ")

#Placing labels on window
label1.place(x=50,y=50)
label2.place(x=50,y=100)
label3.place(x=50,y=150)
label4.place(x=50,y=250)
label5.place(x=50,y=300)

#Creating entries for user to enter values
entry1=Entry(root,borderwidth=5)
entry2=Entry(root,borderwidth=5)
entry3=Entry(root,borderwidth=5)

#Placing entries on window
entry1.place(x=200,y=50)
entry2.place(x=200,y=100)
entry3.place(x=200,y=150)

#Function to calculate the sum and series of an ap
def ap():
    a=float(entry1.get())                                       #a=first term
    d=float(entry2.get())                                       #d=increment
    n=float(entry3.get())                                       #n=number of terms
    f=0                                                         #the 'fth' term in the series
    series=[]                                                   #empty series
    series.append(a+f*d)                                        #first term
    while (f+1) != n:                                           #goes through the terms
        f=f+1                                                   #increments the terms
        series.append(",")                                      #separates the terms
        series.append(a+f*d)                                    #term inputted in the series
    sum=(n/2)*(2*a+(n-1)*d)                                     #sum of all terms
    Progression=Label(root, text=series).place(x=100,y=250)     #placing the series
    sum_of_terms=Label(root,text=sum).place(x=150,y=300)        #placing the sum of series
#Function to calculate the sum and series of an gp 
def gp():
    a=float(entry1.get())                                       #a=first term
    d=float(entry2.get())                                       #d=increment
    n=float(entry3.get())                                       #n=number of terms
    f=0                                                         #the 'fth' term in the series
    series=[]                                                   #empty series
    series.append(a*(d**f))                                     #first term
    while (f+1) != n:                                           #goes through the terms
        f=f+1                                                   #increments through the terms
        series.append(",")                                      #separates the terms
        series.append(a*(d**f))                                 #term inputted in the series
    sum=(a*((d**n)-1))/(d-1)                                    #sum of all terms
    Progression=Label(root, text=series).place(x=100,y=250)     #placing the series
    sum_of_terms=Label(root,text=sum).place(x=150,y=300)        #placing the sum of series
    
#Creating radiobuttons for user to choose between ap and gp
radio1=Radiobutton(root,text="Arithmetic Progression",command=ap)
radio2=Radiobutton(root,text="Geometric Progression",command=gp)

#Creating and placing clear button
Clear=Button(root,text="Clear",width=20).place(x=50,y=350)

#Placing radiobuttons on window
radio1.place(x=50,y=200)
radio2.place(x=200,y=200)

root.mainloop()