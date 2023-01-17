from tkinter import *
root = Tk()
root.geometry('600x400')
root.configure(bg = '#F5CBA7')

lb1 = Label(root, bg="#F5CBA7", text='By Ohm Com')
lb1.grid(row=0,column=0, columnspan=2, sticky = "we",  padx = 250, pady = 5)

lb4 = Label(root, bg="#F5CBA7", font = '20', fg = 'blue', text='Number1:')
lb5 = Label(root, bg="#F5CBA7", font = '20', fg = 'blue', text='Number2:')
lb4.grid(row=1,column=0, sticky = "e",padx=10, pady=5)
lb5.grid(row=2,column=0, sticky = "e",padx=10, pady=5)

lb6 = Entry(root, width = 25, font = '20', bg="white")
lb7 = Entry(root, width = 25, font = '20', bg="white")
lb6.grid(row=1,column=1, sticky = "w",padx=10, pady=5)
lb7.grid(row=2,column=1, sticky = "w",padx=10, pady=5)

btn1 = Button(root, text="Test1", width = 20, height = 2, font = '20', bg = 'white')
btn2 = Button(root, text="Test2", width = 20, height = 2, font = '20', bg = 'white')
btn1.grid(row = 3, column = 0, sticky = "e", padx = 5,pady = 5)
btn2.grid(row = 3, column = 1, sticky = "w", pady = 5)

root.mainloop()