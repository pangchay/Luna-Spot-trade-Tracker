import tkinter as tk

# from core import total_spent
# from core import total_spent_sum
# from core import profits
# from core import portfolio_profit
# from core import portfolio_balance
# from core import purchases
# from core import luna_quantity
# from core import luna_held


frame = tk.Tk()
frame.title("Luna Spot Trader")
frame.geometry('800x800')


def buy_input():
    inp = inputtxt.get(1.0, "end-1c")


# textbox creation
inputtxt = tk.Text(frame, height=1, width=20)
inputtxt.pack()

# button creation
submit_button = tk.Button(frame, text="Submit", command=buy_input)
submit_button.pack()

frame.mainloop()
