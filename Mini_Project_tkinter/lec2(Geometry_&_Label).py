# Pack -place widget blockwise 
# place - places widgets/buttons specific position
# grid -  places widgets/Buttons in grids like in excel sheet 

# label - widget (which is Non Interactive means fixed )

from tkinter import *
root = Tk()
# Gui logic here.
root.geometry("500x100") # Specifies height and width ("Width x Height")
root.minsize(200,100) # Specifies minimum geometry of window (width,Height)
root.maxsize(1200,500) # Specifies maximum geometry of window (width,Height)

Create_Label = Label(text = "First GUI Experience ..")
# This is how we create a label
# It did not show because we didn't packed it
# we have to pack it
Create_Label.pack()


# mainloop() keeps us in interactive window
root.mainloop()