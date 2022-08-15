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


def dble_bets_add_1():
    global dble_bets_1
    dble_bet_add_1 = dble_bet_add_sub_var.get()
    dble_bets_1 += dble_bet_add_1
    dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
    dble_bet_add_sub_var.set(5)

def dble_bets_sub_1():
    global dble_bets_1
    dble_bet_add_1 = dble_bet_add_sub_var.get()
    dble_bets_1 -= dble_bet_add_1
    dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
    dble_bet_add_sub_var.set(5)


def dble_bets_add_2():
    global dble_bets_2
    dble_bet_add_2 = dble_bet_add_sub_var.get()
    dble_bets_2 += dble_bet_add_2
    dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
    dble_bet_add_sub_var.set(5)

def dble_bets_sub_2():
    global dble_bets_2
    dble_bet_sub_2 = dble_bet_add_sub_var.get()
    dble_bets_2 -= dble_bet_sub_2
    dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
    dble_bet_add_sub_var.set(5)


dble_creds_1_counter = StringVar()  # Sets variable as a string variable
dble_creds_1_counter.set("Credits: $500.00")
dble_creds_1_display = Label(dble_frame,
                             textvariable=dble_creds_1_counter,
                             bg="orange",
                             font="Times 10")
dble_creds_1_display.place(x=25, y=70)

dble_bets_1_counter = StringVar()
dble_bets_1_counter.set("Bets: $0.00")
dble_bets_1_display = Label(dble_frame,
                            textvariable=dble_bets_1_counter,
                            bg="orange",
                            font="Times 10")
dble_bets_1_display.place(x=25, y=100)

dble_creds_2_counter = StringVar()
dble_creds_2_counter.set("Credits: $500.00")
dble_creds_2_display = Label(dble_frame,
                             textvariable=dble_creds_2_counter,
                             bg="orange",
                             font="Times 10")
dble_creds_2_display.place(x=555, y=70)

dble_bets_2_counter = StringVar()
dble_bets_2_counter.set("Bets: $0.00")
dble_bets_2_display = Label(dble_frame,
                            textvariable=dble_bets_2_counter,
                            bg="orange",
                            font="Times 10")
dble_bets_2_display.place(x=592, y=100)

dble_bet_add_sub_var = IntVar()
dble_bet_add_sub_var.set(5)
dble_bet_add_but_1 = Button(dble_frame,
                            text="Add bets",
                            bg="gold",
                            bd=1,
                            command=dble_bets_add_1)
dble_bet_add_but_1.place(x=20, y=150)
dble_bet_sub_but_1 = Button(dble_frame,
                            text="Remove bets",
                            bg="gold",
                            bd=1,
                            command=dble_bets_sub_1)
dble_bet_sub_but_1.place(x=20, y=180)

dble_bet_add_but_2 = Button(dble_frame, 
                            text="Add bets", 
                            bg="gold", 
                            bd=1, 
                            command=dble_bets_add_2)
dble_bet_add_but_2.place(x=604, y=150)
dble_bet_sub_but_2 = Button(dble_frame,
                            text="Remove bets", 
                            bg="gold", 
                            bd=1, 
                            command=dble_bets_sub_2)
dble_bet_sub_but_2.place(x=580, y=180)

root.mainloop()  # Loops the program until stopped/exited
