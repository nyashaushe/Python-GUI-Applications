#first import module

from tkinter import *

#creatimg a root window

root = Tk()

#root window title
root.title("Welcome to My first GUI")
#SEETING DIMENSION OF WINDOW BY USING GEOMETRY(width by height)
root.geometry("700x400")

#all functionality is put here

#7. To add a menu bar, you can use Menu class. 
# First, we create a menu, 
# then we add our first label, 
# and finally, we assign the menu to our window. 
# We can add menu items under any menu by using add_cascade().


menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)



#adding label in root window 
lbl = Label(root, text ="Are you okay?")

#4. Adding grid() function is a geometry manager which keeps the label in the desired location inside the window. 
# If no parameters are mentioned by default it will place it in the empty cell; that is 0,0 as that is the first location.  

lbl.grid()


#5. Now add a button to the root window.
#def clicked():
    #lbl.configure(text="i am clicked")

#button widget with red color text inside

def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text = res)

#btn = Button(root, text = "click me",
             #fg = "red", command=clicked)
# set Button grid
#btn.grid(column=1, row=0)


#6. Using the Entry() class for user input
# adding Entry Field
txt = Entry(root, width=10, bd ="6")
txt.grid(column =1, row =0)

btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked, bd="6", bg="green")

# Set Button Grid
btn.grid(column=2, row=0)
#To display the user input text, we’ll make changes to the function clicked() at step 5. 
# We can get the user entered text using the get() function. When the Button after entering of the text, a default text concatenated with the user text.
# Also change button grid location to column 2 as Entry() will be column 1.




































#running program
root.mainloop()