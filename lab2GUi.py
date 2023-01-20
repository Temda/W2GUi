from tkinter import *
root = Tk()
root.geometry('456x565')
root.configure(bg = '#F5CBA7')

# background_image=PhotoImage(file="image/mars.png") 
# background_label = Label(root, image=background_image) 
# background_label.place(x=0, y=0, relwidth=1, relheight=1) 

lb1 = Label(root, fg="blue", font=('Tahoma', 15, 'bold'), text='Registration Form', bg = '#F5CBA7')
lb1.grid(row=0,column=0, columnspan=2, sticky = "w",  padx = 120, pady = 5)

from1 = Label(root, font = ('Tahoma', 13), text='Name :', bg = '#F5CBA7')
from2 = Label(root, font = ('Tahoma', 13), text='Email :', bg = '#F5CBA7')
form3 = Label(root, font = ('Tahoma', 13), text='Gender :', bg = '#F5CBA7')


from1.grid(row=1,column=0, sticky = "w",padx=40, pady=5)
from2.grid(row=2,column=0, sticky = "w",padx=40, pady=5)
form3.grid(row=3,column=0, sticky = "w",padx=40, pady=5)

form4 = Label(root, font = ('Tahoma', 13), text='Phone Number :', bg = '#F5CBA7')
form4.grid(row=6,column=0, sticky = "w",padx=40, pady=5)

form5 = Label(root, font = ('Tahoma', 13), text='User name :', bg = '#F5CBA7')
form5.grid(row=7,column=0, sticky = "w",padx=40, pady=5)

form6 = Label(root, font = ('Tahoma', 13), text='Password :', bg = '#F5CBA7')
form6.grid(row=8,column=0, sticky = "w",padx=40, pady=5)

form7 = Label(root, font = ('Tahoma', 13), text='Security Question :', bg = '#F5CBA7')
form7.grid(row=9,column=0, sticky = "w",padx=40, pady=5)

form8 = Label(root, font = ('Tahoma', 13), text='Answer :', bg = '#F5CBA7')
form8.grid(row=10,column=0, sticky = "w",padx=40, pady=5)


lb6 = Entry(root, width = 18, font = '20', bg="yellow")
lb7 = Entry(root, width = 18, font = '20', bg="yellow")
op1= Radiobutton(root, text="Male", value=1, bg = '#F5CBA7')
op2= Radiobutton(root, text="Female", value=2, bg = '#F5CBA7')
op3= Radiobutton(root, text="Other", value=3, bg = '#F5CBA7')
input4 = Entry(root, width = 18, font = '20', bg="yellow")
input5 = Entry(root, width = 18, font = '20', bg="yellow")
input6 = Entry(root, width = 18, font = '20', bg="yellow")
input7 = Entry(root, width = 18, font = '20', bg="yellow")
input8 = Entry(root, width = 18, font = '20', bg="yellow")





lb6.grid(row=1,column=1, sticky = "e",padx=40, pady=5)
lb7.grid(row=2,column=1, sticky = "e",padx=40, pady=5)
op1.grid(row=3,column=1, sticky = "w",padx=40, pady=5)
op2.grid(row=4,column=1, sticky = "w",padx=40, pady=5)
op3.grid(row=5,column=1, sticky = "w",padx=40, pady=5)
input4.grid(row=6,column=1, sticky = "e",padx=40, pady=5)
input5.grid(row=7,column=1, sticky = "e",padx=40, pady=5)
input6.grid(row=8,column=1, sticky = "e",padx=40, pady=5)
input7.grid(row=9,column=1, sticky = "e",padx=40, pady=5)
input8.grid(row=10,column=1, sticky = "e",padx=40, pady=5)

photo = PhotoImage(file='image/button.png')
 
photo = photo.subsample(3, 3)

btn1 = Button(root, text="Cancel", font = 'Tahoma 10 bold', width=150, borderwidth=0, border=0, image=photo, compound=CENTER, bg = '#F5CBA7')
btn2 = Button(root, text="Register", font = 'Tahoma 10 bold', width=150, borderwidth=0, border=0,image=photo, compound=CENTER, bg = '#F5CBA7')
btn1.grid(row = 11, column = 0, sticky = "e", padx = 12,pady = 30)
btn2.grid(row = 11, column = 1, sticky = "w", padx = 12,pady = 30)



root.mainloop()

# background image python