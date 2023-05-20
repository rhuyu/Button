# Importing tkinter class library and renaming it as tk for ease of access 
import tkinter as tk

# Defining a function that prints "Button Clicked" when triggered
def button_click():
    print("Button Clicked!")
    
# Declaring variables root with the tk library and giving it a name    
root = tk.Tk()
root.title("Button Example")

# Creating widget object that takes in 3 parameters: destination, text displayed, and event
button  = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

# Keeps the window open and visible
root.mainloop()