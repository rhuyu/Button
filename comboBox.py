#imporing tkinter library and renaming as tk
import tkinter as tk
#From the library we want to import ttk(manipulate the object style)
from tkinter import ttk

#Defining a function that allows for display when item is selected
def on_select(event):
  
  #Create an item objectt that obtains the value of the selected item.
  selected_item = event.widget.get()
  print("Selected Item:", selected_item)

#Creating and naming the root window so we can place our widget
root = tk.Tk()
root.title("Dropbox Example")

#Create an array that populates the itembox
items = ["Ice Cream", "Bubble Tea","Bingsoo", "Taiyaki", "Strawberry Shortcake"]

#Create the combo box object put the object in the root window adn populate values
combo_box = ttk.Combobox(root, values=items)

#Binding function will tie the selected item to the on_selectde function
combo_box.bind("<<ComboboxSelected>>", on_select)

# Pack the object to the screen wuth the Geometry manager
combo_box.pack()

#mainloop keeps the root parent window visible
root.mainloop()