from tkinter import *
from functools import partial

root = Tk()
root.title("Multiplayer Mode")  # Window title

dble_frame = Frame(root, width=700, height=500, bg="green")  # Window frame
dble_frame.grid()

dealer_side = Label(
    dble_frame,
    text="Dealer",
    font="Times 14 bold",  # Dealer's Side, 
    bg="#733f19",
    fg="white",
    padx=330,
    pady=12)  # of the table
dealer_side.place(x=-10, y=0)


dble_creds_1 = 500  # Intial value of credits for player one
dble_bets_1 = 0  # and their bets

dble_creds_2 = 500  # Intial value for credits for player two
dble_bets_2 = 0  # and their bets

dble_creds_1_counter = StringVar()  # Sets variable as a string variable
dble_creds_1_counter.set("Credits: $500")
dble_creds_1_display = Label(dble_frame,
                             textvariable=dble_creds_1_counter,
                             bg="orange",
                             font="Times 10")
dble_creds_1_display.place(x=30, y=70)

dble_bets_1_counter = StringVar()
dble_bets_1_counter.set("Bets: $0")
dble_bets_1_display = Label(dble_frame, textvariable=dble_bets_1_counter, bg="orange", font="Times 10")
dble_bets_1_display.place(x=30, y=100)

dble_creds_2_counter = StringVar()
dble_creds_2_counter.set("Credits: $500")
dble_creds_2_display = Label(dble_frame, textvariable=dble_creds_2_counter, bg="orange", font="Times 10")
dble_creds_2_display.place(x=580, y=70)

dble_bets_2_counter = StringVar()
dble_bets_2_counter.set("Bets: $0")
dble_bets_2_display = Label(dble_frame, textvariable=dble_bets_2_counter, bg="orange", font="Times 10")
dble_bets_2_display.place(x=617, y=100)



root.mainloop()  # Loops the program until stopped/exited