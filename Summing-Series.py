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







root.mainloop()