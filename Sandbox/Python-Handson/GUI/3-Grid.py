import tkinter

window = tkinter.Tk()
window.title("GUI")

# creating 2 text labels and input labels

tkinter.Label(window, text = "Username").grid(row = 0) # this is placed in 0 0
# 'Entry' is used to display the input-field
tkinter.Entry(window).grid(row = 0, column = 1) # this is placed in 0 1

tkinter.Label(window, text = "Password").grid(row = 1) # this is placed in 1 0
tkinter.Entry(window).grid(row = 1, column = 1) # this is placed in 1 1

# 'Checkbutton' is used to create the check buttons
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(row=2,columnspan = 2) # 'columnspan' tells to take the width of 2 columns
                                                                             # you can also use 'rowspan' in the similar manner

# creating a function called say_hi()
def say_hi():
    tkinter.Label(window, text = "Hi").grid(row = 4)

tkinter.Button(window, text = "Click Me!", command = say_hi).grid(row = 3) # 'command' is executed when you click the button

                                            
window.mainloop()
