import tkinter as tk
from random import sample
from tkinter import messagebox


def startLottery():
    inputs = [int(entry.get()) for entry in [number1, number2, number3, number4, number5, number6]]

    if all(1 <= num <= 49 for num in inputs) and len(set(inputs)) == 6:
        winning_numbers = sample(range(1, 50), 6)
        if inputs == winning_numbers:
            messagebox.showinfo("Congratulations!", "You won! The winning numbers are: {}".format(winning_numbers))
        else:
            messagebox.showwarning("Sorry, you lost.", "The winning numbers are: {}".format(winning_numbers))
    else:
        messagebox.showwarning("Invalid Input", "Please enter six unique numbers between 1 and 49.")


root = tk.Tk()
root.title("Lottery")
root.geometry("400x400")

welcome_label = tk.Label(root, text="Welcome to the Lottery!\nEnter six numbers between 1 and 49.\n", foreground="red",
                         font=("Times New Roman", 20))
welcome_label.pack()

number1 = tk.Spinbox(root, from_=1, to=49, width=59)
number1.pack()

number2 = tk.Spinbox(root, from_=1, to=49, width=59)
number2.pack()

number3 = tk.Spinbox(root, from_=1, to=49, width=59)
number3.pack()

number4 = tk.Spinbox(root, from_=1, to=49, width=59)
number4.pack()

number5 = tk.Spinbox(root, from_=1, to=49, width=59)
number5.pack()

number6 = tk.Spinbox(root, from_=1, to=49, width=59)
number6.pack()

start_button = tk.Button(root, text="START", command=startLottery)
start_button.pack()

tk.mainloop()
