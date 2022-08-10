from tkinter import *
from functools import partial


root = Tk()
root.title("Multiplayer Mode") # Window title

double_frame = Frame(root, width=700, height=500, bg="green") # Window frame
double_frame.grid()

dealer_side = Label(double_frame, text="Dealer", font="Times 14 bold",  # Dealer's Side, 
                    bg="#733f19", fg="white", padx=330, pady=12)  # of the table
dealer_side.place(x=-10, y=0)


root.mainloop() # Loops the program until stopped/exited