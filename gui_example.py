from tkinter import *

root = Tk()

# # Creating Frames
# topFrame = Frame(root) # Create top frame
# topFrame.pack()
#
# bottomFrame = Frame(root) # Create bottom frame
# bottomFrame.pack(side=BOTTOM)
#
#
# # Creates buttons
# button1 = Button(topFrame, text="Button 1", fg="red") #fg = 'foreground' or text color
# button2 = Button(topFrame, text="Button 2", fg="blue") #fg = 'foreground' or text color
# button3 = Button(topFrame, text="Button 3", fg="green") #fg = 'foreground' or text color
# button4 = Button(bottomFrame, text="Button 4", fg="purple") #fg = 'foreground' or text color
#
# button1.pack(side=LEFT) # Displays button on GUI
# button2.pack(side=LEFT) # Displays button on GUI
# button3.pack(side=RIGHT) # Displays button on GUI
# button4.pack(side=RIGHT) # Displays button on GUI
#
# # Creating widgets
# one = Label(root, text="One", bg="red",fg="white")
# two = Label(root, text="Two", bg="green", fg="black")
# three = Label(root, text="Three", bg="blue", fg="white")
#
# one.pack()
# two.pack(fill=X) # Fill-x responsive horizontally
# three.pack(side=LEFT, fill=Y) # Fill-y responsive vertically

# Creating Grid Layout

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0)
label2.grid(row=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()
