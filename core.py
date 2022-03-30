import tkinter as tk
from tkinter import *
from luna_price import price

# import pickle - learn this for saving states could also save in SQL database
# Add option to choose token at start of app (meh)
# Add GUI
# Use pyinstaller to make it a standalone application
# GG

total_spent = []
total_spent_sum = []
profits = []
portfolio_profit = 0
portfolio_balance = 0
purchases = []
luna_quantity = []
luna_held = 0

enter_orders = "y"
while enter_orders == "y":
    purchase = {}
    purchase["Amount"] = input("Luna amount bought: ")
    purchase["Cost"] = input("Luna price in Dollars at the time of purchase: ")
    purchases.append(purchase)

    profit = (float(price) * float(purchase["Amount"]) - (float(purchase["Amount"]) * float(purchase["Cost"])))
    profits.append(profit)
    portfolio_profit = sum(profits)

    total_spent.append(float(purchase["Cost"]) * float(purchase["Amount"]))
    total_spent_sum = sum(total_spent)
    enter_orders = input("do you have more orders to input? (y or n): ")

    portfolio_balance = total_spent_sum + portfolio_profit
    luna_quantity.append(float(purchase["Amount"]))
    luna_held = sum(luna_quantity)

else:
    print(f"Current Luna price: \n${price}")
    print(f"Total spent: \n${total_spent_sum}")
    print("Here are your purchases: \n" + str(purchases))
    print("Here are your profits per purchase: \n" + str(profits))
    print(f"Luna held: \n{luna_held}")
    print(f"Total  portfolio profit: \n${portfolio_profit}")
    print(f"Portfolio balance: \n${portfolio_balance}")
