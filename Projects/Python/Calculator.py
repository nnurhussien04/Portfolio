import ctypes# this allows you to add a message box
import sys #This allows you to run a built-in module from tkinterr
from tkinter import *#This allows you to run a built-in module from tkinter
#ctypes.windll.user32.MessageBoxW(0, 'Extra measures has taken place in order to protect the calculator', "Info", 0)# this shows a message box with the information inside it coming first then the title then the style
#Name = input('Enter Name') # Asks the user for the name
#Password = input('Enter Password')#This is the variable asking for the password
##while Password != 'Nebil':# This is the while loop and if the user do not get the password it will keep on asking them till they get the code 
##          Password = input('Enter Password')
##PIN = int(input('Enter Pin')) # This is the variable asking for the pin
##for x in range(0,1):# This is the for loop if the user does not get it in 2 goes the program closes
##    if PIN == 1234:
##        break
##    else:
##        PIN = int(input('Enter Pin'))
##        sys.exit() # This is a variable that closes the whole program,
root = Tk() #This allows you to open the window for the GUI for tkinter   
root.title('Nebil Calculator')# This gives you a title for the window in tkinter
e = Entry(root,width=35,borderwidth=5) # This makes a screen to add your calcualtions
e.grid(row=0, column=0, columnspan = 3, padx=10, pady=10) # This allows you to display the screen and postion the size
def button_click(number): # This allows you to click the button on the calculator and stops you from repeating the same number twice 
    current = 0# e.get() #returns whatever button they clicked
    e.delete(0,END)# Deletes the charcaters after the number is written
    e.insert(0,str(current) + str(number))# Allows a string to display at the screen
def button_clear():
    e.delete(0,END)
def button_add():
    first_number = e.get()#This allows you to store a value from the button you clicked and returns it.  
    global f_num # this is a global variable that convert what ever you click into an integer
    global math # this is a global variable that works out the sum for you depending on the operator you choose 
    math = 'addition'
    f_num = int(first_number)
    e.delete(0,END)
def button_equal():
    second_number = e.get() # this variable does the same thing as the first number but the only difference is that the value its storing which is different
    e.delete(0,END)
    if math == 'addition': # once the user clicks the equal button depending on which operator the user clicked the program would see which one it is and add it up
        e.insert(0,f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0,f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0,f_num * int(second_number))
    if math == 'division':
        e.insert(0,f_num / int(second_number))
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0,END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0,END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0,END)



button_1 = Button(root,text='1', padx=40, pady=20, command = lambda: button_click(1)) # These variables define the button 
button_2 = Button(root,text='2', padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(root,text='3', padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(root,text='4', padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(root,text='5', padx=40, pady=20, command = lambda: button_click(5))
button_6 = Button(root,text='6', padx=40, pady=20, command = lambda: button_click(6))
button_7 = Button(root,text='7', padx=40, pady=20, command = lambda: button_click(7))
button_8 = Button(root,text='8', padx=40, pady=20, command = lambda: button_click(8))
button_9 = Button(root,text='9', padx=40, pady=20, command = lambda: button_click(9))
button_0 = Button(root,text='0', padx=40, pady=20, command = lambda: button_click(0))
button_add = Button(root,text='+', padx=39, pady=20, command = button_add)
button_equal = Button(root,text='=', padx=91, pady=20, command = button_equal)
button_clear = Button(root,text='Clear', padx=79, pady=20, command = button_clear)
button_subtract = Button(root,text='-', padx=41, pady=20, command = button_subtract)
button_multiply = Button(root,text='*', padx=40, pady=20, command = button_multiply)
button_divide = Button(root,text='/', padx=41, pady=20, command = button_divide) 

button_1.grid(row=3, column =0)# Here they display the button and postion it on screen
button_2.grid(row=3, column =1)
button_3.grid(row=3, column =2)
button_4.grid(row=2, column =0)
button_5.grid(row=2, column =1)
button_6.grid(row=2, column =2)
button_7.grid(row=1, column =0)
button_8.grid(row=1, column =1)
button_9.grid(row=1, column =2)
button_0.grid(row=4, column =0)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)



root.mainloop() # This is an event loop in python

