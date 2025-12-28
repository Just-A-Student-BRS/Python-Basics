from tkinter import *
root = Tk()
# Gui logic here.
root.geometry("400x200")
photo = PhotoImage(file = r"C:\Users\Subhash Buchade\OneDrive\Pictures\RSCOE_logo_latest-removebg-preview.png")
label_To_Show = Label(image = photo)
label_To_Show.pack()

# mainloop() keeps us in interactive window
root.mainloop()